#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: NodeosConnect
   :synopsis: This Class creates connection to EOS nodeos API RPC and the Wallet API RPC.
              Only to methods are implemented GET and POST.
.. author: Merouane Benthameur <merouane.benth@gmail.com>
"""

import requests

__version: "0.1.0"


class RequestHandlerAPI:
    """ a class to handle the http connection with the EOS node."""

    def __init__(self, base_url,  verify=False, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        self.ssl_verify = verify

        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__set_session_attr(
                    getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    def get(self, path, **kwargs):
        """
        A GET Http method.

        :param path: str: path to  api endpoint
        :param kwargs: json: arguments auth, headers, data ..etc.

        :return: response object

        """
        try:
            return self.session.get(self.base_url + path, verify=self.ssl_verify, **kwargs)
        except requests.exceptions.RequestException as e:
            raise e

    def post(self, path, **kwargs):
        """
        A POST Http method.

        :param path: str: path to  api endpoint
        :param kwargs: json: arguments auth, headers, data ..etc.

        :return: response object

        """
        try:
            return self.session.post(self.base_url + path, verify=self.ssl_verify, **kwargs)
        except requests.exceptions.RequestException as e:
            raise e

    @staticmethod
    def __set_session_attr(source, destination):
        """
        set session attributes
        :param source: the default attributes when starting the session
        :param destination: json: target attributes to be set

        :return:json: session attributes

        """
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestHandlerAPI.__set_session_attr(value, node)
            else:
                destination[key] = value
        return destination
