import requests

url="https://restcountries.com/v3.1/all"

response=requests.get(url)



if response.status_code==200:
    response=response.json()
    datacountries=''
    
    for title in response:
        name=title['name']['official']
        region=title['region']
        population=title['population']
        population=str(population)
        datacountries+="\n"+"Nombre oficial: "+name+"\n"+"Region: "+region+"\n" +"Poblacion: "+population+"\n"
    print(datacountries)
    f = open ('countries.txt','w')
    f.write(datacountries)
    f.close()
        
        
        
    
    
        
        