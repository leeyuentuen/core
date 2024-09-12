"""Constants for the Renault integration tests."""

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.renault.const import (
    CONF_KAMEREON_ACCOUNT_ID,
    CONF_LOCALE,
    DOMAIN,
)
from homeassistant.components.select import ATTR_OPTIONS
from homeassistant.components.sensor import (
    ATTR_STATE_CLASS,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    ATTR_DEVICE_CLASS,
    ATTR_ENTITY_ID,
    ATTR_ICON,
    ATTR_IDENTIFIERS,
    ATTR_MANUFACTURER,
    ATTR_MODEL,
    ATTR_MODEL_ID,
    ATTR_NAME,
    ATTR_STATE,
    ATTR_UNIT_OF_MEASUREMENT,
    CONF_PASSWORD,
    CONF_USERNAME,
    PERCENTAGE,
    STATE_NOT_HOME,
    STATE_OFF,
    STATE_ON,
    STATE_UNKNOWN,
    Platform,
    UnitOfEnergy,
    UnitOfLength,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfTime,
    UnitOfVolume,
)

ATTR_DEFAULT_DISABLED = "default_disabled"
ATTR_UNIQUE_ID = "unique_id"

FIXED_ATTRIBUTES = (
    ATTR_DEVICE_CLASS,
    ATTR_OPTIONS,
    ATTR_STATE_CLASS,
    ATTR_UNIT_OF_MEASUREMENT,
)
DYNAMIC_ATTRIBUTES = (ATTR_ICON,)

ICON_FOR_EMPTY_VALUES = {
    "binary_sensor.reg_number_hvac": "mdi:fan-off",
    "select.reg_number_charge_mode": "mdi:calendar-remove",
    "sensor.reg_number_charge_state": "mdi:flash-off",
    "sensor.reg_number_plug_state": "mdi:power-plug-off",
}

MOCK_ACCOUNT_ID = "account_id_1"

# Mock config data to be used across multiple tests
MOCK_CONFIG = {
    CONF_USERNAME: "email@test.com",
    CONF_PASSWORD: "test",
    CONF_KAMEREON_ACCOUNT_ID: "account_id_1",
    CONF_LOCALE: "fr_FR",
}

MOCK_VEHICLES = {
    "zoe_40": {
        "expected_device": {
            ATTR_IDENTIFIERS: {(DOMAIN, "VF1AAAAA555777999")},
            ATTR_MANUFACTURER: "Renault",
            ATTR_MODEL: "Zoe",
            ATTR_NAME: "REG-NUMBER",
            ATTR_MODEL_ID: "X101VE",
        },
        "endpoints": {
            "battery_status": "battery_status_charging.json",
            "charge_mode": "charge_mode_always.json",
            "cockpit": "cockpit_ev.json",
            "hvac_status": "hvac_status.1.json",
        },
        Platform.BINARY_SENSOR: [
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.PLUG,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_plug",
                ATTR_STATE: STATE_ON,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_plugged_in",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.BATTERY_CHARGING,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_charging",
                ATTR_STATE: STATE_ON,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charging",
            },
            {
                ATTR_ENTITY_ID: "binary_sensor.reg_number_hvac",
                ATTR_ICON: "mdi:fan-off",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_hvac_status",
            },
        ],
        Platform.BUTTON: [
            {
                ATTR_ENTITY_ID: "button.reg_number_start_air_conditioner",
                ATTR_ICON: "mdi:air-conditioner",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_start_air_conditioner",
            },
            {
                ATTR_ENTITY_ID: "button.reg_number_start_charge",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_start_charge",
            },
            {
                ATTR_ENTITY_ID: "button.reg_number_stop_charge",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_stop_charge",
            },
        ],
        Platform.DEVICE_TRACKER: [],
        Platform.SELECT: [
            {
                ATTR_ENTITY_ID: "select.reg_number_charge_mode",
                ATTR_ICON: "mdi:calendar-remove",
                ATTR_OPTIONS: [
                    "always",
                    "always_charging",
                    "schedule_mode",
                    "scheduled",
                ],
                ATTR_STATE: "always",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charge_mode",
            },
        ],
        Platform.SENSOR: [
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_autonomy",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: "141",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_autonomy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENERGY,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_available_energy",
                ATTR_STATE: "31",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_available_energy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfEnergy.KILO_WATT_HOUR,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.BATTERY,
                ATTR_ENTITY_ID: "sensor.reg_number_battery",
                ATTR_STATE: "60",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_level",
                ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_battery_activity",
                ATTR_STATE: "2020-01-12T21:40:16+00:00",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_last_activity",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_temperature",
                ATTR_STATE: "20",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_temperature",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTemperature.CELSIUS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENUM,
                ATTR_ENTITY_ID: "sensor.reg_number_charge_state",
                ATTR_ICON: "mdi:flash",
                ATTR_OPTIONS: [
                    "not_in_charge",
                    "waiting_for_a_planned_charge",
                    "charge_ended",
                    "waiting_for_current_charge",
                    "energy_flap_opened",
                    "charge_in_progress",
                    "charge_error",
                    "unavailable",
                ],
                ATTR_STATE: "charge_in_progress",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charge_state",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.POWER,
                ATTR_ENTITY_ID: "sensor.reg_number_charging_power",
                ATTR_STATE: "0.027",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charging_power",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfPower.KILO_WATT,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DURATION,
                ATTR_ENTITY_ID: "sensor.reg_number_charging_remaining_time",
                ATTR_ICON: "mdi:timer",
                ATTR_STATE: "145",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charging_remaining_time",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTime.MINUTES,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_mileage",
                ATTR_ICON: "mdi:sign-direction",
                ATTR_STATE: "49114",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_mileage",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
                ATTR_ENTITY_ID: "sensor.reg_number_outside_temperature",
                ATTR_STATE: "8.0",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_outside_temperature",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTemperature.CELSIUS,
            },
            {
                ATTR_ENTITY_ID: "sensor.reg_number_hvac_soc_threshold",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_hvac_soc_threshold",
                ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_hvac_activity",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_hvac_last_activity",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENUM,
                ATTR_ENTITY_ID: "sensor.reg_number_plug_state",
                ATTR_ICON: "mdi:power-plug",
                ATTR_OPTIONS: [
                    "unplugged",
                    "plugged",
                    "plugged_waiting_for_charge",
                    "plug_error",
                    "plug_unknown",
                ],
                ATTR_STATE: "plugged",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_plug_state",
            },
            {
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_res_state",
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start_code",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_res_state_code",
            },
        ],
    },
    "zoe_50": {
        "expected_device": {
            ATTR_IDENTIFIERS: {(DOMAIN, "VF1AAAAA555777999")},
            ATTR_MANUFACTURER: "Renault",
            ATTR_MODEL: "Zoe",
            ATTR_NAME: "REG-NUMBER",
            ATTR_MODEL_ID: "X102VE",
        },
        "endpoints": {
            "battery_status": "battery_status_not_charging.json",
            "charge_mode": "charge_mode_schedule.json",
            "cockpit": "cockpit_ev.json",
            "hvac_status": "hvac_status.2.json",
            "location": "location.json",
            "lock_status": "lock_status.1.json",
            "res_state": "res_state.1.json",
        },
        Platform.BINARY_SENSOR: [
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.PLUG,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_plug",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_plugged_in",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.BATTERY_CHARGING,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_charging",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charging",
            },
            {
                ATTR_ENTITY_ID: "binary_sensor.reg_number_hvac",
                ATTR_ICON: "mdi:fan-off",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_hvac_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.LOCK,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_lock",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_lock_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_rear_left_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_rear_left_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_rear_right_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_rear_right_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_driver_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_driver_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_passenger_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_passenger_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_hatch",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_hatch_status",
            },
        ],
        Platform.BUTTON: [
            {
                ATTR_ENTITY_ID: "button.reg_number_start_air_conditioner",
                ATTR_ICON: "mdi:air-conditioner",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_start_air_conditioner",
            },
            {
                ATTR_ENTITY_ID: "button.reg_number_start_charge",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_start_charge",
            },
            {
                ATTR_ENTITY_ID: "button.reg_number_stop_charge",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_stop_charge",
            },
        ],
        Platform.DEVICE_TRACKER: [
            {
                ATTR_ENTITY_ID: "device_tracker.reg_number_location",
                ATTR_ICON: "mdi:car",
                ATTR_STATE: STATE_NOT_HOME,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_location",
            }
        ],
        Platform.SELECT: [
            {
                ATTR_ENTITY_ID: "select.reg_number_charge_mode",
                ATTR_ICON: "mdi:calendar-clock",
                ATTR_OPTIONS: [
                    "always",
                    "always_charging",
                    "schedule_mode",
                    "scheduled",
                ],
                ATTR_STATE: "schedule_mode",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charge_mode",
            },
        ],
        Platform.SENSOR: [
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_autonomy",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: "128",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_autonomy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENERGY,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_available_energy",
                ATTR_STATE: "0",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_available_energy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfEnergy.KILO_WATT_HOUR,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.BATTERY,
                ATTR_ENTITY_ID: "sensor.reg_number_battery",
                ATTR_STATE: "50",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_level",
                ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_battery_activity",
                ATTR_STATE: "2020-11-17T08:06:48+00:00",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_last_activity",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_temperature",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_battery_temperature",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTemperature.CELSIUS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENUM,
                ATTR_ENTITY_ID: "sensor.reg_number_charge_state",
                ATTR_ICON: "mdi:flash-off",
                ATTR_OPTIONS: [
                    "not_in_charge",
                    "waiting_for_a_planned_charge",
                    "charge_ended",
                    "waiting_for_current_charge",
                    "energy_flap_opened",
                    "charge_in_progress",
                    "charge_error",
                    "unavailable",
                ],
                ATTR_STATE: "charge_error",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charge_state",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.POWER,
                ATTR_ENTITY_ID: "sensor.reg_number_admissible_charging_power",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charging_power",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfPower.KILO_WATT,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DURATION,
                ATTR_ENTITY_ID: "sensor.reg_number_charging_remaining_time",
                ATTR_ICON: "mdi:timer",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_charging_remaining_time",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTime.MINUTES,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_mileage",
                ATTR_ICON: "mdi:sign-direction",
                ATTR_STATE: "49114",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_mileage",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
                ATTR_ENTITY_ID: "sensor.reg_number_outside_temperature",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_outside_temperature",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTemperature.CELSIUS,
            },
            {
                ATTR_ENTITY_ID: "sensor.reg_number_hvac_soc_threshold",
                ATTR_STATE: "30.0",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_hvac_soc_threshold",
                ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_hvac_activity",
                ATTR_STATE: "2020-12-03T00:00:00+00:00",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_hvac_last_activity",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENUM,
                ATTR_ENTITY_ID: "sensor.reg_number_plug_state",
                ATTR_ICON: "mdi:power-plug-off",
                ATTR_OPTIONS: [
                    "unplugged",
                    "plugged",
                    "plugged_waiting_for_charge",
                    "plug_error",
                    "plug_unknown",
                ],
                ATTR_STATE: "unplugged",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_plug_state",
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_location_activity",
                ATTR_STATE: "2020-02-18T16:58:38+00:00",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_location_last_activity",
            },
            {
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start",
                ATTR_STATE: "Stopped, ready for RES",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_res_state",
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start_code",
                ATTR_STATE: "10",
                ATTR_UNIQUE_ID: "vf1aaaaa555777999_res_state_code",
            },
        ],
    },
    "captur_phev": {
        "expected_device": {
            ATTR_IDENTIFIERS: {(DOMAIN, "VF1AAAAA555777123")},
            ATTR_MANUFACTURER: "Renault",
            ATTR_MODEL: "Captur ii",
            ATTR_NAME: "REG-NUMBER",
            ATTR_MODEL_ID: "XJB1SU",
        },
        "endpoints": {
            "battery_status": "battery_status_charging.json",
            "charge_mode": "charge_mode_always.json",
            "cockpit": "cockpit_fuel.json",
            "location": "location.json",
            "lock_status": "lock_status.1.json",
            "res_state": "res_state.1.json",
        },
        Platform.BINARY_SENSOR: [
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.PLUG,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_plug",
                ATTR_STATE: STATE_ON,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_plugged_in",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.BATTERY_CHARGING,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_charging",
                ATTR_STATE: STATE_ON,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_charging",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.LOCK,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_lock",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_lock_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_rear_left_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_rear_left_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_rear_right_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_rear_right_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_driver_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_driver_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_passenger_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_passenger_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_hatch",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_hatch_status",
            },
        ],
        Platform.BUTTON: [
            {
                ATTR_ENTITY_ID: "button.reg_number_start_air_conditioner",
                ATTR_ICON: "mdi:air-conditioner",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_start_air_conditioner",
            },
            {
                ATTR_ENTITY_ID: "button.reg_number_start_charge",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_start_charge",
            },
            {
                ATTR_ENTITY_ID: "button.reg_number_stop_charge",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_stop_charge",
            },
        ],
        Platform.DEVICE_TRACKER: [
            {
                ATTR_ENTITY_ID: "device_tracker.reg_number_location",
                ATTR_ICON: "mdi:car",
                ATTR_STATE: STATE_NOT_HOME,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_location",
            }
        ],
        Platform.SELECT: [
            {
                ATTR_ENTITY_ID: "select.reg_number_charge_mode",
                ATTR_ICON: "mdi:calendar-remove",
                ATTR_OPTIONS: [
                    "always",
                    "always_charging",
                    "schedule_mode",
                    "scheduled",
                ],
                ATTR_STATE: "always",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_charge_mode",
            },
        ],
        Platform.SENSOR: [
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_autonomy",
                ATTR_ICON: "mdi:ev-station",
                ATTR_STATE: "141",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_battery_autonomy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENERGY,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_available_energy",
                ATTR_STATE: "31",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_battery_available_energy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfEnergy.KILO_WATT_HOUR,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.BATTERY,
                ATTR_ENTITY_ID: "sensor.reg_number_battery",
                ATTR_STATE: "60",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_battery_level",
                ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_battery_activity",
                ATTR_STATE: "2020-01-12T21:40:16+00:00",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_battery_last_activity",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
                ATTR_ENTITY_ID: "sensor.reg_number_battery_temperature",
                ATTR_STATE: "20",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_battery_temperature",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTemperature.CELSIUS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENUM,
                ATTR_ENTITY_ID: "sensor.reg_number_charge_state",
                ATTR_ICON: "mdi:flash",
                ATTR_OPTIONS: [
                    "not_in_charge",
                    "waiting_for_a_planned_charge",
                    "charge_ended",
                    "waiting_for_current_charge",
                    "energy_flap_opened",
                    "charge_in_progress",
                    "charge_error",
                    "unavailable",
                ],
                ATTR_STATE: "charge_in_progress",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_charge_state",
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.POWER,
                ATTR_ENTITY_ID: "sensor.reg_number_admissible_charging_power",
                ATTR_STATE: "27.0",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_charging_power",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfPower.KILO_WATT,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DURATION,
                ATTR_ENTITY_ID: "sensor.reg_number_charging_remaining_time",
                ATTR_ICON: "mdi:timer",
                ATTR_STATE: "145",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_charging_remaining_time",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfTime.MINUTES,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_fuel_autonomy",
                ATTR_ICON: "mdi:gas-station",
                ATTR_STATE: "35",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_fuel_autonomy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.VOLUME,
                ATTR_ENTITY_ID: "sensor.reg_number_fuel_quantity",
                ATTR_ICON: "mdi:fuel",
                ATTR_STATE: "3",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_fuel_quantity",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfVolume.LITERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_mileage",
                ATTR_ICON: "mdi:sign-direction",
                ATTR_STATE: "5567",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_mileage",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.ENUM,
                ATTR_ENTITY_ID: "sensor.reg_number_plug_state",
                ATTR_ICON: "mdi:power-plug",
                ATTR_OPTIONS: [
                    "unplugged",
                    "plugged",
                    "plugged_waiting_for_charge",
                    "plug_error",
                    "plug_unknown",
                ],
                ATTR_STATE: "plugged",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_plug_state",
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_location_activity",
                ATTR_STATE: "2020-02-18T16:58:38+00:00",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_location_last_activity",
            },
            {
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start",
                ATTR_STATE: "Stopped, ready for RES",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_res_state",
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start_code",
                ATTR_STATE: "10",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_res_state_code",
            },
        ],
    },
    "captur_fuel": {
        "expected_device": {
            ATTR_IDENTIFIERS: {(DOMAIN, "VF1AAAAA555777123")},
            ATTR_MANUFACTURER: "Renault",
            ATTR_MODEL: "Captur ii",
            ATTR_NAME: "REG-NUMBER",
            ATTR_MODEL_ID: "XJB1SU",
        },
        "endpoints": {
            "cockpit": "cockpit_fuel.json",
            "location": "location.json",
            "lock_status": "lock_status.1.json",
            "res_state": "res_state.1.json",
        },
        Platform.BINARY_SENSOR: [
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.LOCK,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_lock",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_lock_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_rear_left_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_rear_left_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_rear_right_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_rear_right_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_driver_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_driver_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_passenger_door",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_passenger_door_status",
            },
            {
                ATTR_DEVICE_CLASS: BinarySensorDeviceClass.DOOR,
                ATTR_ENTITY_ID: "binary_sensor.reg_number_hatch",
                ATTR_STATE: STATE_OFF,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_hatch_status",
            },
        ],
        Platform.BUTTON: [
            {
                ATTR_ENTITY_ID: "button.reg_number_start_air_conditioner",
                ATTR_ICON: "mdi:air-conditioner",
                ATTR_STATE: STATE_UNKNOWN,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_start_air_conditioner",
            },
        ],
        Platform.DEVICE_TRACKER: [
            {
                ATTR_ENTITY_ID: "device_tracker.reg_number_location",
                ATTR_ICON: "mdi:car",
                ATTR_STATE: STATE_NOT_HOME,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_location",
            }
        ],
        Platform.SELECT: [],
        Platform.SENSOR: [
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_fuel_autonomy",
                ATTR_ICON: "mdi:gas-station",
                ATTR_STATE: "35",
                ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_fuel_autonomy",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.VOLUME,
                ATTR_ENTITY_ID: "sensor.reg_number_fuel_quantity",
                ATTR_ICON: "mdi:fuel",
                ATTR_STATE: "3",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_fuel_quantity",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfVolume.LITERS,
            },
            {
                ATTR_DEVICE_CLASS: SensorDeviceClass.DISTANCE,
                ATTR_ENTITY_ID: "sensor.reg_number_mileage",
                ATTR_ICON: "mdi:sign-direction",
                ATTR_STATE: "5567",
                ATTR_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_mileage",
                ATTR_UNIT_OF_MEASUREMENT: UnitOfLength.KILOMETERS,
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_DEVICE_CLASS: SensorDeviceClass.TIMESTAMP,
                ATTR_ENTITY_ID: "sensor.reg_number_last_location_activity",
                ATTR_STATE: "2020-02-18T16:58:38+00:00",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_location_last_activity",
            },
            {
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start",
                ATTR_STATE: "Stopped, ready for RES",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_res_state",
            },
            {
                ATTR_DEFAULT_DISABLED: True,
                ATTR_ENTITY_ID: "sensor.reg_number_remote_engine_start_code",
                ATTR_STATE: "10",
                ATTR_UNIQUE_ID: "vf1aaaaa555777123_res_state_code",
            },
        ],
    },
}
