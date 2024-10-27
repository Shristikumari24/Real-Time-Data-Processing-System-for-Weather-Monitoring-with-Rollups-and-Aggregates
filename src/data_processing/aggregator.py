from collections import defaultdict

class WeatherAggregator:
    def _init_(self, db):
        self.db = db
        self.daily_data = defaultdict(list)

    def update(self, data):
        day = data['dt'] // (24 * 3600)
        self.daily_data[day].append(data)
        self._update_daily_summary(day)

    def _update_daily_summary(self, day):
        data = self.daily_data[day]
        summary = {
            'date': day * 24 * 3600,
            'avg_temp': sum(d['temp'] for d in data) / len(data),
            'max_temp': max(d['temp'] for d in data),
            'min_temp': min(d['temp'] for d in data),
            'dominant_condition': max(set(d['main'] for d in data), key=lambda x: [d['main'] for d in data].count(x))
        }
        self.db.update_daily_summary(summary)

    def get_daily_summary(self):
        return self.db.get_daily_summaries()
