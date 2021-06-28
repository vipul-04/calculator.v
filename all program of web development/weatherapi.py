import tkinter as tk
import requests
import time

def getWeather(canvas):
    city=textfeild.get()
    api="http://api.openweathermap.org/data/2.5/weather?q="+city+"appid=54b39e53b84b2c9f65970e7c2c503043"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273)
    min_temp=int(json_data['main']['temp_min']-273)
    max_temp=int(json_data['main']['temp_max']-273)
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']))
    sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']))

    final_info= condition + "\n" + str(temp) +"*C"
    final_data = "\n" + "Max Temp:" + str(max_temp) +"\n" + "Min Temp:" + str(min_temp) +"\n" +"humidity:" + str(humidity) +"\n" + "Wind Speed:" +  str(Wind)+ "\n" + "Sunreise:" + sunrise + "\n" + "Sunset:"+ sunset 
    label1.config(text= final_info)
    label2.config(text= final_data)


canvas= tk.Tk()
canvas.geomtery("600*500")
canvas.title("Weather App")

f=("poppins", 15, "bold")
t=("poppins",35,"bold")

textfield= tk.Entry(canvas,font=t)
textfield.pack(pady=20 )
textfield.focus()
textfield.bind('Return', getweather)

lable1 =tk.Label(canvas,font=t)
lable1.pack()
lable2 =tk.Label(canvas,font=f)
lable2.pack()
canvas.mainloop()
