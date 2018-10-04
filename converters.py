# -*- coding: utf-8 -*-
"""A collection of translators for converting third-party data to beanworks objects.

This will ensure that the data being sent to the database have correct type.

Example:
    ``
    from converters import *
    session = XeroAPI("0L67EMJGHO5TPNV9ECR7KLZ4RY2GLY", "3ZPJSGGFKHXULYXTRVJE8OYUCORX4B")
    ``
Attributes:
    ...

Todo:
    * ...

"""


def from_xero_accounts(xero_accounts):
    """
        BeanWorks Accounts and Xero Accounts are identical JSONs
    """
    return xero_accounts


def to_xero_accounts(accounts):
    """
        BeanWorks Accounts and Xero Accounts are identical JSONs
    """
    return accounts


def from_xero_vendors(xero_vendors):
    """
        BeanWorks Vendors and Xero Vendors are identical JSONs
    """
    return xero_vendors


def to_xero_vendors(vendors):
    """
        BeanWorks Vendors and Xero Vendors are identical JSONs
    """
    return vendors
