import requests
import json

VAULT_ADDR = 'http://127.0.0.1:8200'
VAULT_TOKEN = 'your-vault-token'

def read_secret(path):
    headers = {'X-Vault-Token': VAULT_TOKEN}
    url = f'{VAULT_ADDR}/v1/{path}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def write_secret(path, data):
    headers = {'X-Vault-Token': VAULT_TOKEN}
    url = f'{VAULT_ADDR}/v1/{path}'
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

# Usage
write_secret('secret/hello', {'value': 'world'})
print(read_secret('secret/hello'))
