"""Test the Ruckus Unleashed config flow."""
from datetime import timedelta
from unittest.mock import AsyncMock, patch

from aioruckus.const import (
    ERROR_CONNECT_TEMPORARY,
    ERROR_CONNECT_TIMEOUT,
    ERROR_LOGIN_INCORRECT,
)
from aioruckus.exceptions import AuthenticationError

from homeassistant import config_entries, data_entry_flow
from homeassistant.components.ruckus_unleashed.const import DOMAIN
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.util import utcnow

from . import CONFIG, DEFAULT_TITLE, RuckusAjaxApiPatchContext, mock_config_entry

from tests.common import async_fire_time_changed


async def test_form(hass: HomeAssistant) -> None:
    """Test we get the form."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}

    with RuckusAjaxApiPatchContext(), patch(
        "homeassistant.components.ruckus_unleashed.async_setup_entry",
        return_value=True,
    ) as mock_setup_entry:
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            CONFIG,
        )
        await hass.async_block_till_done()

        assert result2["type"] == "create_entry"
        assert result2["title"] == DEFAULT_TITLE
        assert result2["data"] == CONFIG
        assert len(mock_setup_entry.mock_calls) == 1


async def test_form_invalid_auth(hass: HomeAssistant) -> None:
    """Test we handle invalid auth."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with RuckusAjaxApiPatchContext(
        login_mock=AsyncMock(side_effect=AuthenticationError(ERROR_LOGIN_INCORRECT))
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            CONFIG,
        )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "invalid_auth"}


async def test_form_user_reauth(hass: HomeAssistant) -> None:
    """Test reauth."""
    entry = mock_config_entry()
    entry.add_to_hass(hass)

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_REAUTH}
    )

    flows = hass.config_entries.flow.async_progress()
    assert len(flows) == 1
    assert "flow_id" in flows[0]

    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "reauth_confirm"

    result2 = await hass.config_entries.flow.async_configure(
        flows[0]["flow_id"],
        user_input={
            CONF_HOST: "1.2.3.4",
            CONF_USERNAME: "new_name",
            CONF_PASSWORD: "new_pass",
        },
    )

    await hass.async_block_till_done()
    assert result2["type"] == data_entry_flow.FlowResultType.FORM
    assert result2["step_id"] == "user"


async def test_form_cannot_connect(hass: HomeAssistant) -> None:
    """Test we handle cannot connect error."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with RuckusAjaxApiPatchContext(
        login_mock=AsyncMock(side_effect=ConnectionError(ERROR_CONNECT_TIMEOUT))
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            CONFIG,
        )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "cannot_connect"}


async def test_form_unexpected_response(hass: HomeAssistant) -> None:
    """Test we handle unknown error."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with RuckusAjaxApiPatchContext(
        login_mock=AsyncMock(
            side_effect=ConnectionRefusedError(ERROR_CONNECT_TEMPORARY)
        )
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            CONFIG,
        )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "cannot_connect"}


async def test_form_cannot_connect_unknown_serial(hass: HomeAssistant) -> None:
    """Test we handle cannot connect error on invalid serial number."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}

    with RuckusAjaxApiPatchContext(system_info={}):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            CONFIG,
        )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "cannot_connect"}


async def test_form_duplicate_error(hass: HomeAssistant) -> None:
    """Test we handle duplicate error."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with RuckusAjaxApiPatchContext():
        await hass.config_entries.flow.async_configure(
            result["flow_id"],
            CONFIG,
        )

        future = utcnow() + timedelta(minutes=60)
        async_fire_time_changed(hass, future)
        await hass.async_block_till_done()

        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )
        assert result["type"] == "form"
        assert result["errors"] == {}

        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            CONFIG,
        )

    assert result2["type"] == "abort"
    assert result2["reason"] == "already_configured"
