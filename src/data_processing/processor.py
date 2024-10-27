class WeatherProcessor:
    def process(self, data):
        return {
            'city': data['name'],
            'main': data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'dt': data['dt']
        }
