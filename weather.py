import requests
key="2bdf5fc264f6364d85f65d9722d07435"
city=input("Enter your City name :  ")
weather=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}")
# print(weather.json()["main"]["temp"]-273.15)
ans =weather.json()
res=int(ans["main"]["temp"]-273.15)
print(res)
print("The Temperature in ",city,res,"°C")

