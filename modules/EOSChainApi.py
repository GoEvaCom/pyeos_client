#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: EOSChainApi
   :synopsis: A basic wrapper around the EOS Chain API..
.. moduleauthor:: Merouane Benthameur <merouane.benth@gmail.com>
"""


class ChainAPI:
    """ wrapper for EOS Chain API"""
    def __init__(self, connection_session):
        self.session = connection_session

    def get_info(self):
        """
        Get latest information related to a node.
        :return: response object
        """
        path = '/v1/chain/get_info'
        return self.session.get(path=path)

    def get_block(self, block_id):
        """
        Get information related to a block.
        :param block_id: str: the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_block'
        return self.session.get(path=path, data=block_id)

    def get_account(self, account_name):
        """
        Get information related to an account.
        :param account_name: str: the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_account'
        return self.session.get(path=path, data=account_name)

    def get_code(self, account_name):
        """
        Fetch smart contract code.
        :param account_name: str: the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_code'
        return self.session.get(path=path, data=account_name)

    def get_table_rows(self, account_details):
        """
        Fetch smart contract data from an account.
        :param account_details: str: account details, the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_table_rows'
        return self.session.get(path=path, data=account_details)

    def abi_json_to_bin(self, data):
        """
        Serialize json to binary hex. The resulting binary hex is usually used for the data field in push_transaction.
        :param data: str: the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/abi_json_to_bin'
        return self.session.get(path=path, data=data)

    def abi_bin_to_json(self, data):
        """
        Serialize back binary hex to json.
        :param data:
        :return:
        """
        path = '/v1/chain/abi_bin_to_json'
        return self.session.get(path=path, data=data)

    def push_transaction(self, transaction):
        """
        This method expects a transaction in JSON format and will attempt to apply it to the blockchain,
        :param transaction: str: transaction, the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.session.get(path=path, data=transaction)

    def push_transactions(self, transactions):
        """
        This method push multiple transactions at once.
        :param transactions: str: list of transactions, the format must be a string of a list
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.session.get(path=path, data=transactions)

    def get_required_keys(self, transaction_data):
        """
        Get required keys to sign a transaction from list of your keys.
        :param transaction_data: str: transaction data with a list of keys, the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_required_keys'
        return self.session.get(path=path, data=transaction_data)
