# 🌦️ Iran Weather Forecast

**A simple, interactive, and terminal-based weather forecasting application built with Python.**

Explore the weather across Iran with a clean command-line interface. Choose a city from a predefined list, enter its ID, and get a **7-day weather forecast** directly in your terminal.

Whether you're practicing Python, learning to work with weather APIs, or building your next command-line project, this application is a practical step toward mastering real-world development.

> **Explore Iran's weather, one city at a time.** 🇮🇷

---

## ✨ Features

- 🌍 **Iranian Cities:** Browse a predefined list of Iranian cities, each with a unique ID.
- 🔎 **Interactive City Selection:** Select a city by entering its corresponding ID.
- 📅 **7-Day Forecast:** Retrieve weather predictions for the selected city.
- 🌡️ **Weather Details:** Display available information such as temperature, daily conditions, and precipitation.
- 🔄 **Continuous Exploration:** Return to the city list and check another city's forecast without restarting the application.
- 🧹 **Clean Terminal Interface:** Clear the terminal between forecasts for a more organized experience.
- ⚡ **Lightweight & Beginner-Friendly:** Practice Python fundamentals through a useful real-world project.

## 🖥️ Sample Output

The following is an **illustrative example** of how the application could look in the terminal. Weather values are fictional and do not represent a live forecast.

```text
==================================================
          🇮🇷 IRAN WEATHER FORECAST
==================================================

Select a city to view its 7-day forecast:

  ID    CITY
  ---   ----------------
   1    Tehran
   2    Mashhad
   3    Isfahan
   4    Shiraz
   5    Tabriz
   6    Rasht
   7    Ahvaz
   8    Kerman
   9    Yazd
  10    Bandar Abbas

--------------------------------------------------
Enter city ID: 1

Fetching weather forecast for Tehran...

==================================================
             🌤️ TEHRAN FORECAST
==================================================

Date         Condition       Min °C    Max °C
--------------------------------------------------
2026-10-14   Sunny             18        29
2026-10-15   Partly Cloudy     17        27
2026-10-16   Cloudy            16        25
2026-10-17   Light Rain        15        22
2026-10-18   Sunny             17        28
2026-10-19   Clear             18        30
2026-10-20   Partly Cloudy     17        26

==================================================

Press Enter to continue...
```

After pressing Enter, the terminal clears and the city list appears again, allowing you to select another destination.

## 🛠️ Technologies Used

- **Python 3** — Application logic and data processing.
- **Weather API** — Retrieves forecast data for Iranian cities.
- **Requests** *(if used)* — Sends HTTP requests to the weather service.
- **Standard Python Libraries** — Terminal interaction and screen clearing.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ali2mar81/iran-weather-forecast.git
```

### 2. Navigate to the project directory

```bash
cd iran-weather-forecast
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

If the project uses the `requests` library:

```bash
pip install requests
```

If a `requirements.txt` file is available, install all dependencies with:

```bash
pip install -r requirements.txt
```

### 5. Run the application

Use the entry-point filename in your project. For example, if it is `main.py`:

```bash
python main.py
```


## 🎯 Learning Objectives

This project offers practical experience with:

- Python functions and modular programming.
- Lists, dictionaries, and data organization.
- HTTP requests and REST APIs.
- JSON parsing and error handling.
- User input validation.
- Exception handling for network failures.
- Working with dates and weather forecast data.
- Terminal manipulation and command-line interfaces.
- Environment variables and API key management.

## 🔮 Future Improvements

Possible enhancements include:

- [ ] Add more Iranian cities.
- [ ] Display humidity, wind speed, and precipitation probability.
- [ ] Add weather icons and colorized terminal output.
- [ ] Support city search by name.
- [ ] Handle invalid IDs, API errors, and internet connection failures gracefully.
- [ ] Cache recent forecasts to reduce unnecessary API requests.
- [ ] Add Celsius/Fahrenheit conversion.
- [ ] Write automated tests using `pytest`.
- [ ] Add a configuration system for multiple weather providers.


## 🤝 Contributing

Suggestions, bug reports, and improvements are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Submit a pull request.

## 📄 License

This project is available for learning and personal development.

---

**Built with Python 🐍 | Powered by weather data ☁️ | Made for learning 🚀**
