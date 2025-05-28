import uuid
from dotenv import load_dotenv
import requests, os
import base64

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
auth = os.getenv('AUTH')

# just to see if it converts good (another way for get a base64 auth key)
# not using here now
id_secret = f'{client_id}:{client_secret}'
encoded_auth = base64.b64encode(id_secret.encode('utf-8')).decode('utf-8')
# just to see if it converts good
print(encoded_auth == auth)
rq_uid = str(uuid.uuid4())

# start
url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload = 'scope=GIGACHAT_API_PERS'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': rq_uid,
    'Authorization': f'Basic {auth} '
}

# chain.pem - path to mincifra root cert
response = requests.request('POST', url, headers=headers, data=payload, verify='chain.pem')

print(response.json().get('access_token'))
