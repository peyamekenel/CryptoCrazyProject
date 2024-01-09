import requests

def getCryptoData():
    response= requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code==200:
        return response.json()

crypto_response=getCryptoData()
user_input=input("enter your crypto currency: ")
for crypto in crypto_response:
    if crypto["currency"]==user_input:
        print(crypto["price"])
        break