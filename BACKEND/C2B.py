import requests
import keys
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token


def register_url():
    my_access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": keys.shortcode,
        "ResponseType": "Completed",  # Corrected parameter name
        "ConfirmationURL": "https://mydomain.com/confirmation",  # Corrected parameter name
        "ValidationURL": "https://mydomain.com/validation"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# register_url()



def C2B():
     my_access_token = generate_access_token()
  
     api_URL = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
     headers = {"Authorization": "Bearer %s" % my_access_token}
     request = {
       "ShortCode" : keys.shortcode,
       "CommandID" : "CustomerPayBillOnline",
       "Amount" : "1",
       "Msisdn" : keys.test_msisdn,
       "BillRefNumber" : "1234",
     }  
     
     response = requests.post(api_URL, json=request , headers=headers )
     
     
     print(response.text)
     
C2B()    




