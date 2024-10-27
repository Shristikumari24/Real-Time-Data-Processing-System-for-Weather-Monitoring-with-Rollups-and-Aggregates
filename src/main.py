import asyncio
from api.weather_api import WeatherAPI
from data_processing.processor import WeatherProcessor
from data_processing.aggregator import WeatherAggregator
from storage.database import Database
from alerts.alert_manager import AlertManager
from visualization.visualizer import Visualizer

async def main():
    db = Database()
    weather_api = WeatherAPI()
    processor = WeatherProcessor()
    aggregator = WeatherAggregator(db)
    alert_manager = AlertManager()
    visualizer = Visualizer()

    while True:
        for city in ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']:
            data = await weather_api.get_weather(city)
            processed_data = processor.process(data)
            aggregator.update(processed_data)
            alert_manager.check_thresholds(processed_data)
        
        visualizer.update_visualizations(aggregator.get_daily_summary())
        await asyncio.sleep(300)  # 5 minutes

if __name__ == "_main_":
    asyncio.run(main())
