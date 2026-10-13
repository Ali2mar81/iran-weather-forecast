import os
import sys

import requests

# Iranian cities with stable IDs and coordinates.
CITIES = {
    1: {"name": "Tehran", "latitude": 35.6892, "longitude": 51.3890},
    2: {"name": "Mashhad", "latitude": 36.2605, "longitude": 59.6168},
    3: {"name": "Isfahan", "latitude": 32.6546, "longitude": 51.6680},
    4: {"name": "Karaj", "latitude": 35.8400, "longitude": 50.9391},
    5: {"name": "Shiraz", "latitude": 29.5918, "longitude": 52.5837},
    6: {"name": "Tabriz", "latitude": 38.0962, "longitude": 46.2738},
    7: {"name": "Qom", "latitude": 34.6416, "longitude": 50.8746},
    8: {"name": "Ahvaz", "latitude": 31.3183, "longitude": 48.6706},
    9: {"name": "Kermanshah", "latitude": 34.3142, "longitude": 47.0650},
    10: {"name": "Urmia", "latitude": 37.5527, "longitude": 45.0761},
    11: {"name": "Rasht", "latitude": 37.2808, "longitude": 49.5832},
    12: {"name": "Kerman", "latitude": 30.2839, "longitude": 57.0834},
    13: {"name": "Yazd", "latitude": 31.8974, "longitude": 54.3569},
    14: {"name": "Bandar Abbas", "latitude": 27.1832, "longitude": 56.2666},
    15: {"name": "Arak", "latitude": 34.0917, "longitude": 49.6892},
    16: {"name": "Zahedan", "latitude": 29.4963, "longitude": 60.8629},
    17: {"name": "Sanandaj", "latitude": 35.3149, "longitude": 46.9988},
    18: {"name": "Sari", "latitude": 36.5633, "longitude": 53.0601},
    19: {"name": "Gorgan", "latitude": 36.8456, "longitude": 54.4393},
    20: {"name": "Bushehr", "latitude": 28.9234, "longitude": 50.8203},
}

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def clear_terminal():
    """Clear the terminal on Windows, macOS, and Linux."""
    os.system("cls" if os.name == "nt" else "clear")


def show_city_menu():
    print("=" * 46)
    print("       IRAN WEATHER FORECAST")
    print("=" * 46)
    print("Select a city by entering its ID:\n")

    for city_id, city in CITIES.items():
        print(f"{city_id:>2}. {city['name']}")

    print("\n 0. Exit")
    print("-" * 46)


def get_forecast(city):
    """Request a seven-day daily forecast from Open-Meteo."""
    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "daily": (
            "weather_code,temperature_2m_max,temperature_2m_min,"
            "precipitation_probability_max"
        ),
        "forecast_days": 7,
        "timezone": "Asia/Tehran",
    }

    response = requests.get(FORECAST_URL, params=params, timeout=15)
    response.raise_for_status()
    return response.json()["daily"]


def describe_weather_code(code):
    """Convert a WMO weather code to a readable description."""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return descriptions.get(code, "Unknown conditions")


def display_forecast(city, forecast):
    print("=" * 76)
    print(f"  7-DAY FORECAST: {city['name'].upper()}, IRAN")
    print("=" * 76)
    print(
        f"{'Date':<13} {'Min':>7} {'Max':>7} "
        f"{'Rain chance':>13}   Weather"
    )
    print("-" * 76)

    for index, date in enumerate(forecast["time"]):
        minimum = forecast["temperature_2m_min"][index]
        maximum = forecast["temperature_2m_max"][index]
        rain_chance = forecast["precipitation_probability_max"][index]
        weather = describe_weather_code(forecast["weather_code"][index])

        minimum_text = f"{minimum}°C" if minimum is not None else "N/A"
        maximum_text = f"{maximum}°C" if maximum is not None else "N/A"
        rain_text = f"{rain_chance}%" if rain_chance is not None else "N/A"

        print(
            f"{date:<13} {minimum_text:>7} {maximum_text:>7} "
            f"{rain_text:>13}   {weather}"
        )

    print("=" * 76)


def wait_to_continue():
    """Wait for Enter, or any key where the optional keyboard library is installed."""
    try:
        import msvcrt  # Available on Windows
        print("\nPress any key to return to the city list...")
        msvcrt.getch()
    except ImportError:
        try:
            import termios
            import tty

            print("\nPress any key to return to the city list...")
            file_descriptor = sys.stdin.fileno()
            old_settings = termios.tcgetattr(file_descriptor)
            try:
                tty.setraw(file_descriptor)
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
        except (ImportError, OSError, AttributeError):
            input("\nPress Enter to return to the city list...")


def main():
    while True:
        clear_terminal()
        show_city_menu()

        choice = input("Enter city ID: ").strip()

        if choice == "0":
            print("\nThanks for using Iran Weather Forecast. Goodbye!")
            break

        if not choice.isdigit() or int(choice) not in CITIES:
            input("\nInvalid city ID. Press Enter to try again...")
            continue

        city = CITIES[int(choice)]
        clear_terminal()
        print(f"Fetching the 7-day forecast for {city['name']}...\n")

        try:
            forecast = get_forecast(city)
            display_forecast(city, forecast)
        except requests.Timeout:
            print("The request timed out. Please check your connection and try again.")
        except requests.RequestException as error:
            print(f"Could not retrieve weather data: {error}")
        except (KeyError, ValueError, TypeError):
            print("The weather service returned unexpected data. Please try again.")

        wait_to_continue()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nApplication closed.")
