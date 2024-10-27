class AlertManager:
    def _init_(self):
        self.thresholds = {
            'high_temp': 35,
            'consecutive_high_temp': 2
        }
        self.high_temp_count = 0

    def check_thresholds(self, data):
        if data['temp'] > self.thresholds['high_temp']:
            self.high_temp_count += 1
            if self.high_temp_count >= self.thresholds['consecutive_high_temp']:
                self._trigger_alert(f"High temperature alert: {data['temp']}°C in {data['city']}")
        else:
            self.high_temp_count = 0

    def _trigger_alert(self, message):
        print(f"ALERT: {message}")
        # Here you could implement email notifications or other alert mechanisms
