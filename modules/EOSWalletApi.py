#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: EOSWalletApi
   :synopsis: A basic wrapper around the EOS Wallet API..
.. author:: Merouane Benthameur <merouane.benth@gmail.com>
"""


class WalletAPI:
    """wrapper for EOS Wallet API"""
    def __init__(self, connection_session):
        self.session = connection_session

    def wallet_create(self, wallet_name):
        """
        Create a new wallet with the given name
        :param wallet_name: str: name of the wallet to be created
        :return: response object
        """
        path = '/v1/wallet/create'
        return self.session.post(path=path, data=wallet_name)

    def wallet_open(self, wallet_name):
        """
        Open an existing wallet of the given name
        :param wallet_name: str: name of the wallet to be opened
        :return: response object
        """
        path = '/v1/wallet/open'
        return self.session.post(path=path, data=wallet_name)

    def wallet_lock(self, wallet_name):
        """
        Lock a wallet of the given name
        :param wallet_name: str: name of the wallet to be opened
        :return: response object
        """
        path = '/v1/wallet/lock'
        return self.session.post(path=path, data=wallet_name)

    def wallet_lock_all(self):
        """
        Lock all wallets
        :return: response object
        """
        path = '/v1/wallet/lock_all'
        return self.session.get(path=path)

    def wallet_unlock(self, wallet_name_passord):
        """
        Unlock a wallet with the given name and password
        :param wallet_name_passord: str: list with name and passord of the given wallet
        :return: response object
        """
        path = '/v1/wallet/unlock'
        return self.session.post(path=path, data=wallet_name_passord)

    def wallet_import_key(self, wallet_name_privKey):
        """
        Import a private key to the wallet of the given name
        :param wallet_name_privKey: str: list that contains the wallet name and private key
        :return: response object
        """
        path = '/v1/wallet/import_key'
        return self.session.post(path=path, data=wallet_name_privKey)

    def wallet_list(self):
        """
        List all wallets
        :return: response object
        """
        path = '/v1/wallet/list_wallets'
        return self.session.get(path=path)

    def wallet_list_keys(self):
        """
        List all key pairs across all wallets
        :return:
        """
        path = '/v1/wallet/list_keys'
        return self.session.get(path=path)

    def wallet_get_public_keys(self):
        """
        List all public keys across all wallets
        :return: reponse object
        """
        path = '/v1/wallet/get_public_keys'
        return self.session.get(path=path)

    def wallet_set_timeout(self, timeout):
        """
        Set wallet auto lock timeout (in seconds)
        :param timeout: str: timeout in seconds
        :return: response object
        """
        path = 'v1/wallet/set_timeout'
        return self.session.post(path=path, data=timeout)

    def wallet_sign_trx(self, transaction_data):
        """
        Sign transaction given an array of transaction, require public keys, and chain id
        :param transaction_data: str: list of transaction json and  public key
        :return: response key
        """
        path = '/v1/wallet/sign_transaction'
        return self.session.post(path=path, data=transaction_data)
