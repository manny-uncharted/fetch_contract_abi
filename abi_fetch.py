import argparse
from urllib import response # for command line arguments
import requests # for http requests
import json # for json parsing


# Function to fetch the ABI of a contract
contract_address = input("Enter the contract address: ")

# ABI_ENDPOINT = f'https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey=YourApiKeyToken'

ABI_ENDPOINT = f'https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}'


def __main__():

    response = requests.get(ABI_ENDPOINT)
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    result = json.dumps(abi_json, indent=4, sort_keys=True)

    with open("abi.json", 'w') as file1:
        file1.write(result)

if __name__ == '__main__':
    __main__()