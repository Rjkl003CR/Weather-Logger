import datetime
import urllib.request


def log_weather():
  # You can change "London" to your own city name
  city = "London"
  url = f"https://wttr.in/{city}?format=3"

  try:
    # Fetch weather data from wttr.in
    req = urllib.request.Request(url, headers={"User-Agent": "curl"})
    with urllib.request.urlopen(req) as response:
      weather_data = response.read().decode("utf-8").strip()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"- **{timestamp}**: {weather_data}\n"

    # Append to log file (saves in a 'log' folder if you prefer, or the root folder)
    # If your log folder is named 'log', change this to 'log/weather_log.md'
    with open("weather_log.md", "a") as f:
      f.write(log_entry)

    print("Weather logged successfully!")

  except Exception as e:
    print(f"Error fetching weather: {e}")


if __name__ == "__main__":
  log_weather()