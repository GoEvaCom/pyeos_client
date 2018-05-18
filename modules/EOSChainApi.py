#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
some doc
"""


class ChainAPI:
    """ warapper for EOS chain API"""
    def __init__(self, connection_session):
        self.session = connection_session

    def get_info(self):
        """
        Get latest information related to a node.
        :return:json: information about the node.
        """
        path = '/v1/chain/get_info'
        return self.session.get(path=path)

