# src/visualization/visualizer.py
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

class Visualizer:
    def update_visualizations(self, daily_summaries):
        dates = [summary[0] for summary in daily_summaries]
        avg_temps = [summary[1] for summary in daily_summaries]
        max_temps = [summary[2] for summary in daily_summaries]
        min_temps = [summary[3] for summary in daily_summaries]
        
        fig = make_subplots(rows=1, cols=1)

        fig.add_trace(
            go.Scatter(x=dates, y=avg_temps, mode='lines+markers', name='Average Temperature'),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=dates, y=max_temps, mode='lines+markers', name='Max Temperature'),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=dates, y=min_temps, mode='lines+markers', name='Min Temperature'),
            row=1, col=1
        )

        fig.update_layout(
            title='Daily Temperatures',
            xaxis_title='Date',
            yaxis_title='Temperature (°C)',
            legend_title='Temperature Type'
        )

        pio.write_html(fig, file='daily_temperatures.html', auto_open=True)