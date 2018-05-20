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
        """
        constructor  of the WalletAPI
        :param connection_session: session request object
        """
        self.session = connection_session

    def wallet_create(self, wallet_name):
        """
        Create a new wallet with the given name.

        :param wallet_name: (str) name of the wallet to be created
        :return: response object

        :Example:

        >>> WalletAPI.wallet_create(wallet_name='"default"')
        PW5KFWYKqvt63d4iNvedfDEPVZL227D3RQ1zpVFzuUwhMAJmRAYyX

        This command will return the password that can be used to
        unlock the wallet in the future

        """
        path = '/v1/wallet/create'
        return self.session.post(path=path, data=wallet_name)

    def wallet_open(self, wallet_name):
        """
        Open an existing wallet of the given name.

        :param wallet_name: (str) name of the wallet to be opened
        :return: response object

        :Example:

        >>> WalletAPI.wallet_open(wallet_name='"default"')
        {}

        """
        path = '/v1/wallet/open'
        return self.session.post(path=path, data=wallet_name)

    def wallet_lock(self, wallet_name):
        """
        Lock a wallet of the given name

        :param wallet_name: (str) name of the wallet to be opened
        :return: response object

        :Example:

        >>> WalletAPI.wallet_lock(wallet_name='"default"')
        {}

        """
        path = '/v1/wallet/lock'
        return self.session.post(path=path, data=wallet_name)

    def wallet_lock_all(self):
        """
        Lock all wallets.

        :return: response object

        :Example:

        >>> WalletAPI.wallet_lock_all()
        {}

        """
        path = '/v1/wallet/lock_all'
        return self.session.get(path=path)

    def wallet_unlock(self, wallet_name_passord):
        """
        Unlock a wallet with the given name and password

        :param wallet_name_passord: (str) list with name and password
        of the given wallet
        :return: response object

        :Example:

        >>> WalletAPI.wallet_unlock(wallet_name_passord='["default",
               "PW5KFWYKqvt63d4iNvedfDEPVZL227D3RQ1zpVFzuUwhMAJmRAYyX"]')
        {}

        """
        path = '/v1/wallet/unlock'
        return self.session.post(path=path, data=wallet_name_passord)

    def wallet_import_key(self, wallet_name_privKey):
        """
        Import a private key to the wallet of the given name

        :param wallet_name_privKey: (str) list that contains the wallet
        name and private key
        :return: response object

        :Example:

        >>> WalletAPI.wallet_import_key(wallet_name_privKey='["default",
               "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"]')

        """
        path = '/v1/wallet/import_key'
        return self.session.post(path=path, data=wallet_name_privKey)

    def wallet_list(self):
        """
        List all wallets

        :return: response object

        :Example:

        >>> WalletAPI.wallet_list()
        ["default *"]

        """
        path = '/v1/wallet/list_wallets'
        return self.session.get(path=path)

    def wallet_list_keys(self):
        """
        List all key pairs across all wallets

        :return: response object

        :Example:

        >>> WalletAPI.wallet_list_keys()
        [["EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV","5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"]]

        """
        path = '/v1/wallet/list_keys'
        return self.session.get(path=path)

    def wallet_get_public_keys(self):
        """
        List all public keys across all wallets

        :return: response object

        :Example:

        >>> WalletAPI.wallet_get_public_keys()
        ["EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"]

        """
        path = '/v1/wallet/get_public_keys'
        return self.session.get(path=path)

    def wallet_set_timeout(self, timeout):
        """
        Set wallet auto lock timeout (in seconds)

        :param timeout: (str) timeout in seconds
        :return: response object

        :Example:

        >>> WalletAPI.wallet_set_timeout(timeout='10')
        {}

        """
        path = '/v1/wallet/set_timeout'
        return self.session.post(path=path, data=timeout)

    def wallet_sign_trx(self, transaction_data):
        """
        Sign transaction given an array of transaction, require
        public keys, and chain id

        :param transaction_data: (str) list of transaction json and  public key
        :return: response key

        :Example:

        >>> WalletAPI.wallet_sign_trx(transaction_data='[{"ref_block_num":21453,"ref_block_prefix":3165644999,"expiration":"2017-12-08T10:28:49","scope":["initb","initc"],"read_scope":[],"messages":[{"code":"currency","type":"transfer","authorization":[{"account":"initb","permission":"active"}],"data":"000000008093dd74000000000094dd74e803000000000000"}],"signatures":[]},["EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"],""]')
        {
          "ref_block_num": 21453,
          "ref_block_prefix": 3165644999,
          "expiration": "2017-12-08T10:28:49",
          "scope": [
            "initb",
            "initc"
          ],
          "read_scope": [],
          "messages": [
            {
              "code": "currency",
              "type": "transfer",
              "authorization": [
                {
                  "account": "initb",
                  "permission": "active"
                }
              ],
              "data": "000000008093dd74000000000094dd74e803000000000000"
            }
          ],
          "signatures": [
            "1f393cc5ce6a6951fb53b11812345bcf14ffd978b07be386fd639eaf440bca7dca16b14833ec661ca0703d15e55a2a599a36d55ce78c4539433f6ce8bcee0158c3"
          ]
        }

        """
        path = '/v1/wallet/sign_transaction'
        return self.session.post(path=path, data=transaction_data)
