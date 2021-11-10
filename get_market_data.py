from dotenv import load_dotenv
import os
import cbpro


class Authenticate():
    
    def __init__(self, API_key, code, API_phrase):
        self.API_key = API_key
        self.code = code
        self.API_phrase = API_phrase

    def Client_Auth(self):
        url = "https://api-public.sandbox.pro.coinbase.com"
        #Authentication
        auth_client = cbpro.AuthenticatedClient(self.API_key, self.code, self.API_phrase,
                                  api_url=url)
        return auth_client
    
    def deposit(self):
        
        


#Testing
# Get API keys in env files 
API_key = os.getenv("API_key")
b64secret = os.getenv("code")
passphrase = os.getenv("API_phrase")
load_dotenv()

#creating a bot object
m= Authenticate(API_key, b64secret, passphrase)
m.Client_Auth()

#m = Authenticate()
