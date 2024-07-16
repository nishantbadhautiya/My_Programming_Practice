import tkinter as tk 
import requests 
import json 

root = tk.Tk() 
root.title('Weaterh App') 
root.geometry('600x200') 

def get_weather():
    zip_code = zip.get() 
    if not zip_code:
        print("Please enter a Zip Code") 
        return 
    api_key = '73D95FDB-D735-4503-B1FC-E35B5C85203F'
    url = f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={api_key}'
    response = requests.get(url).json()[0] 

    area = response['ReportingArea'] 
    aqi = response['AQI'] 
    category = response['Category']['Name'] 

    color = ''
    if category == 'Good':
        color = 'green' 
    elif category == 'Moderate':
        color = 'yellow' 
    elif category == 'Unhealthy for Sensitive Groups':
        color = 'blue' 
    elif category == 'Unhealthy':
        color = 'orange' 
    elif category == 'Very Unhealthy':
        color = 'purple' 
    elif category == 'Hazardous':
        color = 'red' 
    elif category == 'Unavailable':
        color = 'purple' 

    root.config(background=color) 
    root.geometry('1000x200')
    label = tk.Label(root, text=area + " " + str(aqi) + " " + category, bg=color, font=('Arial', 30)) 
    label.grid(row=1, column=0) 



zip = tk.Entry(root, width=30) 
zip.grid(row=0, column=0) 

lookup_button = tk.Button(root, text='Weater Lookup', padx=20, pady=5, bg='purple', command=get_weather) 
lookup_button.grid(row=0, column=1) 


root.mainloop() 
