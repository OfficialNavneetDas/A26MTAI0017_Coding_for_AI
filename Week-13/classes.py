class SmartThermostat:
    # TODO: Define class attributes here:
    supported_brands = ["EcoBee", "Nest", "Honeywell"]
    max_temperature = 35.0
    min_temperature = 10.0
    
    def __init__(self, device_id: str, brand: str):
        # TODO: Initialize instance attributes:
        # device_id, brand (validate or fallback to "Generic"),
        self.device_id = device_id
        self.brand = brand if brand in SmartThermostat.supported_brands else "generic"
        
        # current_temp (20.0), target_temp (22.0), is_on (False)
        self.current_temp = 20.0
        self.target_temp = 22.0
        self.is_on = False

    def power_toggle(self):
        # TODO: Toggle is_on status (True <-> False) and print status
        self.is_on = not self.is_on

    def set_target_temperature(self, temp: float):
        # TODO: Check if device is ON. If yes, check if temp is between
        # min_temperature and max_temperature. Update target_temp if valid.
        if self.is_on:
            if SmartThermostat.min_temperature<temp<SmartThermostat.max_temperature:
                self.target_temp = temp

    def get_status(self) -> str:
        # TODO: Return formatted status string
        stat = "ON" if self.is_on else "OFF"
        return (f"Thermostat {self.device_id} ({self.brand}): Target {self.target_temp}°C | Status:{stat}")
