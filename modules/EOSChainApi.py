#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: EOSChainApi
   :synopsis: A basic wrapper around the EOS Chain API..
.. author:: Merouane Benthameur <merouane.benth@gmail.com>
"""


class ChainAPI:
    """ wrapper for EOS Chain API"""
    def __init__(self, connection_session):
        self.session = connection_session

    def get_info(self):
        """
        Get latest information related to a node.

        :Example:

        >>> ChainAPI.get_info()
        {
          "server_version": "b2eb1667",
          "head_block_num": 259590,
          "last_irreversible_block_num": 259573,
          "head_block_id": "0003f60677f3707f0704f16177bf5f007ebd45eb6efbb749fb1c468747f72046",
          "head_block_time": "2017-12-10T17:05:36",
          "head_block_producer": "initp",
          "recent_slots": "1111111111111111111111111111111111111111111111111111111111111111",
          "participation_rate": "1.00000000000000000"
        }

        :return: response object
        """
        path = '/v1/chain/get_info'
        return self.session.get(path=path)

    def get_block(self, block_id):
        """
        Get information related to a block.

        :Example:

        >>> ChainAPI.get_block(block_id='{"block_num_or_id":5}')
        {
          "previous": "0000000445a9f27898383fd7de32835d5d6a978cc14ce40d9f327b5329de796b",
          "timestamp": "2017-07-18T20:16:36",
          "transaction_merkle_root": "0000000000000000000000000000000000000000000000000000000000000000",
          "producer": "initf",
          "producer_changes": [ ],
          "producer_signature": "204cb94b3186c3b4a7f88be4e9db9f8af2ffdb7ef0f27a065c8177a5fcfacf876f684e59c39f",
          "cycles": [ ],
          "id":"000000050c0175cbf218a70131ddc3c3fab8b6e954edef77e0bfe7c36b599b1d",
          "block_num":5,
          "ref_block_prefix":27728114
        }

        :param block_id: (str) the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_block'
        return self.session.post(path=path, data=block_id)

    def get_account(self, account_name):
        """
        Get information related to an account.

        :Example:

        >>> ChainAPI.get_account(account_name='{"account_name":"inita"}')
        {
          "name": "inita",
          "eos_balance": "999998.9574 EOS",
          "staked_balance": "0.0000 EOS",
          "unstaking_balance": "0.0000 EOS",
          "last_unstaking_time": "2106-02-07T06:28:15",
          "permissions": [
            {
              "name": "active",
              "parent": "owner",
              "required_auth": {
                "threshold": 1,
                "keys": [
                  {
                    "key": "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
                    "weight": 1
                  }
                ],
                "accounts": []
              }
            },
            {
              "name": "owner",
              "parent": "owner",
              "required_auth": {
                "threshold": 1,
                "keys": [
                  {
                    "key": "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
                    "weight": 1
                  }
                ],
                "accounts": []
              }
            }
          ]
        }
        :param account_name: (str) the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_account'
        return self.session.post(path=path, data=account_name)

    def get_code(self, account_name):
        """
        Fetch smart contract code.

         :Example:

        >>> ChainAPI.get_code(account_name='{"account_name":"currency"}')
       {
          "name":"currency",
          "code_hash":"a1c8c84b4700c09c8edb83522237439e33cf011a4d7ace51075998bd002e04c9",
          "wast":"(module\n  (type $0 (func (param i64 i64 i32) (result i32)))\n ...truncated",
          "abi": {
          "types": [{
              "new_type_name": "account_name",
              "type": "name"
            }
          ],
          "structs": [{
              "name": "transfer",
              "base": "",
              "fields": [
                {"name":"from", "type":"account_name"},
                {"name":"to", "type":"account_name"},
                {"name":"quantity", "type":"uint64"}
              ]
            },{
              "name": "account",
              "base": "",
              "fields": [
                {"name":"key", "type":"name"},
                {"name":"balance", "type":"uint64"}
              ]
            }
          ],
          "actions": [{
              "name": "transfer",
              "type": "transfer"
            }
          ],
          "tables": [{
              "name": "account",
              "type": "account",
              "index_type": "i64",
              "key_names" : ["key"],
              "key_types" : ["name"]
            }
          ]
        }

        :param account_name: (str) the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_code'
        return self.session.post(path=path, data=account_name)

    def get_table_rows(self, account_details):
        """
        Fetch smart contract data from an account.

        :Example:

        >>> ChainAPI.get_table_rows(account_details='{"scope":"inita", "code":"currency", "table":"account","json": true}')
       {
          "rows": [
            {
              "account": "account",
              "balance": 1000
            }
          ],
          "more": false
        }

        :param account_details: (str) account details, the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_table_rows'
        return self.session.post(path=path, data=account_details)

    def abi_json_to_bin(self, data):
        """
        Serialize json to binary hex. The resulting binary hex is usually used for the data field in push_transaction.
        :param data: str: the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/abi_json_to_bin'
        return self.session.post(path=path, data=data)

    def abi_bin_to_json(self, data):
        """
        Serialize back binary hex to json.
        :param data:
        :return:
        """
        path = '/v1/chain/abi_bin_to_json'
        return self.session.post(path=path, data=data)

    def push_transaction(self, transaction):
        """
        This method expects a transaction in JSON format and will attempt to apply it to the blockchain,
        :param transaction: str: transaction, the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.session.post(path=path, data=transaction)

    def push_transactions(self, transactions):
        """
        This method push multiple transactions at once.
        :param transactions: str: list of transactions, the format must be a string of a list
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.session.post(path=path, data=transactions)

    def get_required_keys(self, transaction_data):
        """
        Get required keys to sign a transaction from list of your keys.
        :param transaction_data: str: transaction data with a list of keys, the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_required_keys'
        return self.session.post(path=path, data=transaction_data)
