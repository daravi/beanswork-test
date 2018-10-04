
from apis.xero_api import XeroAPI
from converters import *
import json

# TODO grab keys and rsa file from definitions

# BeanworksTest-Public
# Create a session
public_app = XeroAPI("public", "0L67EMJGHO5TPNV9ECR7KLZ4RY2GLY",
                     consumer_secret="3ZPJSGGFKHXULYXTRVJE8OYUCORX4B")
public_app.start_session()
# GET list of accounts and vendors
accounts = from_xero_accounts(public_app.get_accounts())
vendors = from_xero_vendors(public_app.get_vendors())

# Write accounts and vendors to disk
with open('accountspub.json', 'w') as outfile:
    json.dump(accounts, outfile, indent=2, default=str)
with open('vendorspub.json', 'w') as outfile:
    json.dump(vendors, outfile, indent=2, default=str)

# BeanworksTest-Private (Demo Company)
with open("/Users/puya/.certs/privatekey.pem") as keyfile:
    rsa_key = keyfile.read()
private_app = XeroAPI("private", "OMCDOHODSLRIO00QXHQQFIG9PPCWMG",
                      rsa_key=rsa_key)
private_app.start_session()
# GET list of accounts and vendors
accounts = from_xero_accounts(private_app.get_accounts())
vendors = from_xero_vendors(private_app.get_vendors())

# Write accounts and vendors to disk
with open('accountspri.json', 'w') as outfile:
    json.dump(accounts, outfile, indent=2, default=str)
with open('vendorspri.json', 'w') as outfile:
    json.dump(vendors, outfile, indent=2, default=str)
