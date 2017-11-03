import requests
import sys

def main():
    cities=[ "Tokyo", "Paris" , "London"]
    api_key="&APPID=875ecd6cd3b9cbef96b941d8a0a0ed57"
    url ="http://api.openweathermap.org/data/2.5/weather?q="
    units="&units=imperial"
    li =[]

    for city in cities:
        #print (url + city + api_key)
        dic={}
        response = requests.get(url+city+ units+ api_key)
        weather =response.json()
        print ("The temperature in {} is {}f and the conditions are {}"\
               .format(weather['name'],weather['main']['temp'],\
                       weather['weather'][0]['description']))
        dic['city']=weather['name']
        dic['temp']=weather['main']['temp']
        dic['conditions'] = weather['weather'][0]['description']
        li.append(dic)




    #print (li)
    return li

if __name__=='__main__':
    main()
