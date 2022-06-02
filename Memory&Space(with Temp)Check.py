# Jevgeni Moskaljuk TA-21V
# TASK --------------------------------------------------------------------------------------------------------------- TASK #
#1. Palju on vaba RAMi ja kokku RAMi
#2. Palju on vaba salvestusruumi ja kokku 
#3. Kui RAM või Salvestusruum võtab üle 20%, siis kuvab hoiatusteadet (hoiatusteate täituvus % peab olema seadistatav)
#4. Ajalugu programmi käivitusest, vabast ruumist, hoiatuvusteatest peab olema salvestatud logisse (txt fail näiteks)
#5. Vaadata internetist mõnelt veebelehelt või APIst, mis on temperatuur Tallinnas ja see lisada tekstifaili.

import psutil as psu
import  requests

APIkey = "010cb4edccd749722ca7065d57f08363"
Url = "http://api.openweathermap.org/data/2.5/weather?"
City_name = "Tallinn"
APIUrl = Url + "appid=" + APIkey + "&q=" + City_name
Response = requests.get(APIUrl)
x = Response.json()
x1 = x["main"]
Temperature = round(x1["temp"] - 273.15)
Current_Temp = "Temperature in Tallinn: " + str(Temperature) + "C"
print(Current_Temp)


with open('readme.txt', 'w') as f:
    val = psu.virtual_memory()
val1 = getattr(val, "free")
val2 = getattr(val, "total")
print("Free memory you have (in MB):", val1*0.00000095367432)
MemoryResulFree = "Free Memory you have: "+str(round(val1*0.00000095367432,2))
print("Total memory you have (in MB):", val2*0.00000095367432)
MemoryResulTotal = "Free Memory you have: "+str(round(val2*0.00000095367432,2))

zas = psu.disk_usage("/")
zas1 = getattr(zas, "free")
zas2 = getattr(zas, "total")
print("Free space you have (in MB):", zas1*0.00000095367432)
SpaceResulFree = "Free Space you have: "+str(round(zas1*0.00000095367432,2))
print("Total space you have (in MB):", zas2*0.00000095367432)
SpaceResulTotal = "Free Space you have: "+str(round(zas2*0.00000095367432,2))

Get20per = zas1 / zas2 * 100
print("Free space you have is:",round(Get20per, 2),end='%')
if(Get20per <= 20):
    print("!!! YOU ARE LOW OF YOUR SPACE !!!")
    results = "!!! YOU ARE LOW OF YOUR SPACE !!!"
    
with open('readme.txt', 'w') as f:
    f.write(Current_Temp+"\n")
    f.write(MemoryResulFree+" MB" +"\n"+ MemoryResulTotal+" MB"+"\n"+SpaceResulFree+" MB"+"\n"+SpaceResulTotal+" MB")
    if(Get20per <=20):
        f.write("\n"+results)
