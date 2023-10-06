import requests
import keys
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth

unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))


json_response = r.json()

my_access_token = json_response ['access_token']



data_to_encode = keys.business_shortcode + keys.lipa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
# print (encoded_string)

decoded_password = encoded_string.decode('utf-8')
print(decoded_password)

def Lipa():

  access_token = my_access_token
  api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
  headers = {"Authorization": "Bearer %s" % access_token}

  request =  {

      
    "BusinessShortCode": keys.business_shortcode,    
    "Password": decoded_password,    
    "Timestamp": formatted_time,    
    "TransactionType": "CustomerPayBillOnline",    
    "Amount": "1",    
    "PartyA": keys.phone_number,    
    "PartyB": keys.business_shortcode,    
    "PhoneNumber":keys.phone_number,    
    "CallBackURL": "https://mydomain.com/pat",    
    "AccountReference":"KENNEDY",    
    "TransactionDesc":"TESLA MODEL X"
  }


  response = requests.post(api_url, json=request, headers=headers)


  print(response.text)
  
Lipa()
  
  

  




