from tkinter import *
import time
from datetime import datetime
import api as a
import api2 as a2
import os

# Current Dir 
c_dir = os.getcwd()



# Window 
window = Tk()
window.geometry("684x392")
window.title('Weather')
#window.configure(bg = "#ffffff")

#pngs
icon = PhotoImage(file=fr'{c_dir}\elements\weather_app.png')
sun_rain = PhotoImage(file=fr"{c_dir}\elements\Sun cloud mid rain.png")
rain_img = PhotoImage(file=fr"{c_dir}\elements\Moon cloud mid rain.png")
thunder = PhotoImage(file=fr"{c_dir}\elements\lightning.png")
sunny = PhotoImage(file=fr"{c_dir}\elements\sunny.png")
cloud_night = PhotoImage(file=fr'{c_dir}\elements\Moon cloud fast wind.png')
cloud_sun = PhotoImage(file=fr"{c_dir}\elements\sun-clouds.png")
showers = PhotoImage(file=fr"{c_dir}\elements\showers.png")
misty_ = PhotoImage(file=fr"{c_dir}\elements\mostly-cloudy.png")
background_img = PhotoImage(file = fr"{c_dir}\elements\background.png")
high_smbl_img= PhotoImage(file= fr"{c_dir}\elements\High.png")
low_smbl_img = PhotoImage(file= fr"{c_dir}\elements\Low.png")
weather_img = PhotoImage(file=fr"{c_dir}\elements\clouds.png")
img0 = PhotoImage(file = fr"{c_dir}\elements\img0.png")

# Icon 
window.iconphoto(False,icon)
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 392,
    width = 684,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
# functions
def window_png():
    al = a2.now1
    am_pm =a2.am_pm
    if  "Rain" in al :
        if am_pm =="PM":
            canvas.itemconfig(weather, image=rain_img)
            canvas.moveto(weather,515,0)
        else :
            canvas.itemconfig(weather, image=sun_rain)
            canvas.moveto(weather, 490, 0)
    elif "cloudy" in al:
        if am_pm == "PM":
            canvas.itemconfig(weather, image=cloud_night)
        else:
            canvas.itemconfig(weather,image=cloud_sun)
    elif "sunny" in al:
        canvas.itemconfig(weather, image=sunny)
    elif "mist" in al:
        canvas.itemconfig(weather,image=misty_)
    elif  "shovers" in al:
        canvas.itemconfig(weather,image=showers)
    else:
        pass

def clock():
   hh= time.strftime("%I")
   mm= time.strftime("%M")
   ss= time.strftime("%S")
   day=time.strftime("%A")
   ap=time.strftime("%p")
   time_zone= time.strftime("%Z")
   canvas.itemconfig(time_,text= hh + ":" + mm +":" + ss)
   window.after(1000,clock)

def  min_1 ():
    a.api_re_load()
    canvas.itemconfig(humdity_val, text=a.humidity)
    canvas.itemconfig(uv_val, text=a.uv)
    canvas.itemconfig(temp_val,text =a.temp)
    canvas.itemconfig(wind_spped,text= a.w_speed)
    canvas.itemconfig(pressure_val,text= a.w_pressure)
    rain = str(a.rain_hr) + " mm "
    canvas.itemconfig(rain_hr,text =rain)
    canvas.itemconfig(day_condition,text=a2.now1)
    canvas.itemconfig(Low_temp_val,text=a2.min_temp)
    canvas.itemconfig(Max_temp_val,text=a2.max_temp)
    canvas.itemconfig(location,text= a.location)
    window_png()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y ")
    canvas.itemconfig(date, text=dt_string)
    window.after(10000,min_1)

# Labels,Buttons
background = canvas.create_image(
    342.0, 196.0,
    image=background_img)

high_bl = canvas.create_image(
    50,163,
    image= high_smbl_img)

low_bl = canvas.create_image(
    125,163,
    image=low_smbl_img)

weather = canvas.create_image( 555+20, 90,image=weather_img)

day_condition=canvas.create_text(
    564.0, 151.5 - 5,
    text = "Showers",
    fill = "#ffffff",
    font = ("Radley-Regular", int(16.0)))

date=canvas.create_text(
    85.0+5, 292.5,
    text = "Day-month",
    fill = "#ffffff",
    font = ("Radley-Regular", int(16.0)))

time_=canvas.create_text(
    58.5+15, 261.5,
    text = "Time",
    fill = "#ffffff",
    font = ("Radley-Regular", int(16.0)))

canvas.create_text(
    465.0, 227.0,
    text = "UV Index",
    fill = "#d9dbdb",
    font = ("RobotoRoman-Regular", int(14.0)))

canvas.create_text(
    460.0, 288.0,
    text = "Humidity",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(14.0)))

canvas.create_text(
    477.0, 316.0+4,
    text = "Wind Speed",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(14.0)))

canvas.create_text(
    477.0, 353.0,
    text = "Rain in last hr",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(14.0)))

canvas.create_text(
    462.0, 254.0+6,
    text = "Pressure",
    fill = "#ffffff",
    font = ("RobotoRoman-Regular", int(14.0)))

uv_val=canvas.create_text(
    579.0, 228.0,
    text = "1.0",
    fill = "#ffffff",
    font = ("RobotoRoman-SemiBold", int(14.0)))

humdity_val = canvas.create_text(
    579.0, 289.0,
    text = "55",
    fill = "#ffffff",
    font = ("RobotoRoman-SemiBold", int(14.0)))

wind_spped = canvas.create_text(
    579.0+ 8, 321.0,
    text = "5.00 mph",
    fill = "#ffffff",
    font = ("RobotoRoman-SemiBold", int(14.0)))

rain_hr =canvas.create_text(
    605, 350.0,
    text = "30%",
    fill = "#ffffff",
    font = ("RobotoRoman-SemiBold", int(14.0)))

pressure_val= canvas.create_text(
    597.5, 257.0,
    text = "1023.1 pa",
    fill = "#ffffff",
    font = ("RobotoRoman-SemiBold", int(14.0)))

Low_temp_val = canvas.create_text(
    139.0+20, 160.0,
    text = "10",
    fill = "#ffffff",
    font = ("ArchivoRoman-Regular", int(20.0)))

Max_temp_val = canvas.create_text(
    80.5+5, 162.0,
    text = "15 ",
    fill = "#ffffff",
    font = ("ArchivoRoman-Regular", int(20.0)))

temp_val = canvas.create_text(
    68.5 + 10, 97.5,
    text = "13",
    fill = "#ffffff",
    font = ("ComicSansMS", int(60.0)))

location = canvas.create_text(
    180.0-25, 197.0,
    text = "Tirupur,Tamil Nadu , India",
    fill = "#ffffff",
    font = ("Radley-Regular", int(20.0)))


clock()
min_1()

window.resizable(False, False)
window.mainloop()
