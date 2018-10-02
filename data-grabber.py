from xero import Xero
from xero.auth import PrivateCredentials
from xero.auth import PublicCredentials
import webbrowser
import json

# BeanworksTest-Public
credentials = PublicCredentials(
    "0L67EMJGHO5TPNV9ECR7KLZ4RY2GLY", "3ZPJSGGFKHXULYXTRVJE8OYUCORX4B")
webbrowser.open(credentials.url)
verification_code = input("Please enter the verification code: ")
credentials.verify(verification_code)
xero = Xero(credentials)
accounts = xero.accounts.all()
vendors = xero.contacts.filter(IsSupplier=True)
# print(vendors, accounts)
with open('accounts.json', 'w') as outfile:
    json.dump(accounts, outfile, indent=2, default=str)
with open('vendors.json', 'w') as outfile:
    json.dump(vendors, outfile, indent=2, default=str)
