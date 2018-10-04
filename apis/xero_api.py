# -*- coding: utf-8 -*-
"""This is a wrapper class for PyXero API.

PyXero itself is a wrapper for the Xero accounting platform API.

Examples:
    Using xero api for a public app
    ``
    from apis.XeroAPI import XeroAPI
    app = XeroAPI("public" ,"0L67EMJGHO5TPNV9ECR7KLZ4RY2GLY", consumer_secret="3ZPJSGGFKHXULYXTRVJE8OYUCORX4B")
    app.start_session()
    ``
Attributes:
    ...

Todo:
    * ...

"""

# standard library imports
import webbrowser

# third party imports
from xero import Xero
from xero.auth import PublicCredentials, PrivateCredentials


# local imports
from apis.base_api import BaseAPI


class XeroAPI(BaseAPI):
    """The wrapper for PyXero API which connects with the Xero accounting platform API.
    """

    def __init__(self, app_type, consumer_key, *args, consumer_secret=None, rsa_key=None, **kwargs):
        """Create a session using the provided Xero app (key, secret).

        Args:
            consumer_key (str): Consumer key for HMAC-SHA1 based three-legged OAuth 1.0a.
            consumer_secret (str): Consumer key for HMAC-SHA1 based three-legged OAuth 1.0a.
            rsa_key: file handle to the rsa_key for RSA-SHA1 based two-legged OAuth 1.0a
            *arg: non-keyworded arguemnts passed to the parent BaseAPI initializer.
            **kwargs: keyworded arguemnts passed to the parent BaseAPI initializer.
        """
        self.session = None
        self.app_type = app_type
        if app_type == "public":
            if consumer_secret is None:
                raise TypeError(
                    "Xero API applications of type Public require a consumer secret code.")
            else:
                self.session_credentials = PublicCredentials(
                    consumer_key, consumer_secret)
        elif app_type == "private":
            if rsa_key is None:
                raise TypeError(
                    "Xero API applications of type Private require an RSA key.")
            else:
                self.session_credentials = PrivateCredentials(
                    consumer_key, rsa_key)
        elif app_type == "partner":
            raise TypeError(
                "Xero API applications of type Partner are not yet supported.")
        else:
            raise TypeError(
                "Unexpected Xero API application type: " + app_type)

        super().__init__(*args, **kwargs)

    def start_session(self):
        """Start a session using the provided public Xero app (key, secret) pair.
        """
        # Validate session
        if self.app_type == "public":
            try:
                webbrowser.open(self.session_credentials.url)
                verification_code = input(
                    "Please enter the verification code: ")
                self.session_credentials.verify(verification_code)
            except Exception as ex:
                print(
                    "\nError : XeroAPI : Token Authentication with Xero Account Failed.")
                print("Raising exception...\n")
                raise ex
        # Initiate session
        self.session = Xero(self.session_credentials)

    def get_accounts(self):
        """Get list of all accounts (where to pay from).
        """
        return self.session.accounts.all()

    def get_vendors(self):
        """Get list of all vendors (who to pay).

        Note:
            The vendor data is called a "contact" in Xero terminology with the IsSupplier flag set.

        """
        return self.session.contacts.filter(IsSupplier=True)
