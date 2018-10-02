from xero import Xero
from xero.auth import PublicCredentials
import webbrowser
import json

# Credentials for BeanworksTest-Public
credentials = PublicCredentials(
    "0L67EMJGHO5TPNV9ECR7KLZ4RY2GLY", "3ZPJSGGFKHXULYXTRVJE8OYUCORX4B")
# Validate session
webbrowser.open(credentials.url)
verification_code = input("Please enter the verification code: ")
credentials.verify(verification_code)
xero = Xero(credentials)
# GET list of accounts and vendors
accounts = xero.accounts.all()
vendors = xero.contacts.filter(IsSupplier=True)
# Write accounts and vendors to disk
with open('accounts.json', 'w') as outfile:
    json.dump(accounts, outfile, indent=2, default=str)
with open('vendors.json', 'w') as outfile:
    json.dump(vendors, outfile, indent=2, default=str)
