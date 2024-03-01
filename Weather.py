import pyowm
from pyowm  import OWM 
owm =pyowm.OWM('da62e83a3d465abede859b7b16df1395')
mgr = owm.weather_manager()

place =input("which city or country")

# Search for weather in place and get details
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]   

print("in city " + place + " Now " + (w.detailed_status))
print(" in city temperature is " +  str(temp))

if temp < 10:
	print("Now wear it very cold like a tank")
elif temp < 20:
	print("Now put on the cold to keep warm")
elif temp < 30:
	print("Now put on very short shorts")
else:
	print("The temperature is normal Put on whatever you want")
	
input()