import requests
try:
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Here you can directly use api key in quotes or use a text file to store you api and use open function to read it.

    api_key = open("api_key.txt", "r").read()

    city = "Mumbai"
    
    url = base_url + "appid=" + api_key + "&q=" + city
    
    response = requests.get(url).json() # You can print this variable for your data.

    #print(response)
    
    # I have used the following for loop to print the data in a formatted manner.
    for key, values in response.items():
        print(f'{key} : {values}') # Prints out all the key value pairs from the json file.
        
        '''if key == "name":
            print(values) #You can do this for individually print the value of a key. '''

except Exception as e:
    print(e)

# I have used Try except block to catch any exception and let the developer know the issue in the command prompt.