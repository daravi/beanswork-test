# -*- coding: utf-8 -*-
"""This is a tester file to be replaced by a service.

Examples:
    ``
    >> python data_grabber.py
    ``
Attributes:
    ...

Todo:
    * write to a postgresql database instead of text file
    * grab keys and rsa file from a configuration xml file
    * ...
"""
import json
from apis.xero_api import XeroAPI
from converters import from_xero_accounts, from_xero_vendors

# BeanworksTest-Public
# Create a session
PUBLIC_APP = XeroAPI("public", "0L67EMJGHO5TPNV9ECR7KLZ4RY2GLY",
                     consumer_secret="3ZPJSGGFKHXULYXTRVJE8OYUCORX4B")
PUBLIC_APP.start_session()
# GET list of accounts and vendors
ACCOUNTS = from_xero_accounts(PUBLIC_APP.get_accounts())
VENDORS = from_xero_vendors(PUBLIC_APP.get_vendors())

# Write accounts and vendors to disk
with open('accountspub.json', 'w') as outfile:
    json.dump(ACCOUNTS, outfile, indent=2, default=str)
with open('vendorspub.json', 'w') as outfile:
    json.dump(VENDORS, outfile, indent=2, default=str)

# # BeanworksTest-Private (Demo Company)
# with open("/Users/puya/.certs/privatekey.pem") as keyfile:
#     rsa_key = keyfile.read()
# private_app = XeroAPI("private", "OMCDOHODSLRIO00QXHQQFIG9PPCWMG",
#                       rsa_key=rsa_key)
# private_app.start_session()
# # GET list of accounts and vendors
# accounts = from_xero_accounts(private_app.get_accounts())
# vendors = from_xero_vendors(private_app.get_vendors())
