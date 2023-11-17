import tkinter as tk
import requests

api_key = '44e3a58014ada440483ed460f8644c42'

def update_error_label(message):
    error_label.config(text=message, fg="red")

def get_weather():
    city_name = entry_search.get()
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        try:
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            pressure = weather_data['main']['pressure']
            # Update labels with weather information
            temp_label.config(text=f"Temperature: {temperature}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} km/h")
            pressure_label.config(text=f"Pressure: {pressure} Pa")
            update_error_label("")  # Clear error label if no error occurred
        except KeyError as e:
            update_error_label(f"Error: {e}. Please try again.")
    else:
        update_error_label("Failed to fetch weather data. Please check your connection.")

def weather_gui():
    global temp_label, humidity_label, wind_label, pressure_label, error_label, entry_search

    window = tk.Tk()
    window.title("Weather App")
    window.geometry("600x800")
    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)
  
    label_get_location = tk.Label(frame, text="Enter City:")
    label_get_location.grid(row=0, column=0)  
    entry_search = tk.Entry(frame)
    entry_search.grid(row=0, column=1, padx=5)
    search_btn = tk.Button(frame, text="Search", padx=3, command=get_weather)
    search_btn.grid(row=0, column=2)
    
    # Labels to display weather information
    temp_label = tk.Label(frame, text="Temperature:")
    temp_label.grid(row=3, column=0)
    humidity_label = tk.Label(frame, text="Humidity:")
    humidity_label.grid(row=4, column=0)
    wind_label = tk.Label(frame, text="Wind Speed:")
    wind_label.grid(row=5, column=0)
    pressure_label = tk.Label(frame, text="Pressure:")
    pressure_label.grid(row=6, column=0)

    error_label = tk.Label(frame, text="", fg="red")
    error_label.grid(row=7, column=0, columnspan=3)

    window.mainloop()

weather_gui()
