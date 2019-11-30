import tkinter as tk
import requests
import os

HEIGHT = 700
WIDTH = 800
def test_function(entry):
    print(f'this is the entry:{entry}')

root = tk.Tk()

root.title('Queen_Weather')
# 227d764650f5005402e77a6204329aab
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def format_responses(weather):
    try:
        City = weather['city']['name']
        Country = weather['city']['country']
        day1 = weather['list'][0]['dt_txt']
        temerature1 = weather['list'][0]['main']['temp']
        desc1 = weather['list'][0]['weather'][0]['description']
        day2 = weather['list'][1]['dt_txt']
        temerature2 = weather['list'][1]['main']['temp']
        desc2 = weather['list'][1]['weather'][0]['description']
        day3 = weather['list'][2]['dt_txt']
        temerature3 = weather['list'][2]['main']['temp']
        desc3 = weather['list'][2]['weather'][0]['description']
        final_str = 'Country: %s\nCity: %s\n\nDate of: %s\nTemperature: %s\nDescription: %s\n\nDate of: %s\nTemperature: %s\nDescription: %s\n\nDate of: %s\nTemperature: %s\nDescription: %s'%(Country, City, day1, temerature1, desc1, day2, temerature2, desc2, day3, temerature3, desc3)
    except:
        final_str = 'City not found'
        
    return final_str


def get_weather(city):
    weather_key = os.environ.get('weather_key')
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    responses = requests.get(url, params = params)
    weather = responses.json()
    label['text'] = format_responses(weather)

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = ('Courier', 20))
entry.place(relwidth = 0.65, relheight = 1)
button = tk.Button(frame, text = 'Get weather', bg = 'gray', font = ('Courier', 15), 
command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font = ('Courier', 15), anchor = 'nw', justify = 'left', bd =4)
label.place(relwidth = 1, relheight = 1)



root.mainloop()
