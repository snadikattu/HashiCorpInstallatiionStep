import requests
import json

VAULT_ADDR = 'http://127.0.0.1:8200'

class VaultClient:
    def __init__(self, vault_addr):
        self.vault_addr = vault_addr
        self.token = None

    def login(self, username, password):
        url = f'{self.vault_addr}/v1/auth/userpass/login/{username}'
        response = requests.post(url, json={'password': password})
        response.raise_for_status()
        self.token = response.json()['auth']['client_token']

    def read_secret(self, path):
        headers = {'X-Vault-Token': self.token}
        url = f'{self.vault_addr}/v1/{path}'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def write_secret(self, path, data):
        headers = {'X-Vault-Token': self.token}
        url = f'{self.vault_addr}/v1/{path}'
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

# Usage
vault = VaultClient(VAULT_ADDR)
vault.login('username', 'password')
vault.write_secret('secret/hello', {'value': 'world'})
print(vault.read_secret('secret/hello'))
