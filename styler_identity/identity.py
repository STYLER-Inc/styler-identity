# -*- coding: utf-8 -*-

""" Identity class

    Encapsulates the logic to handle JWT tokens
"""

from jwt.exceptions import InvalidTokenError
import jwt


class Identity:
    """ Holds the identity of the logged user
    """
    def __init__(self, token):
        self.token = token
        try:
            self.decoded = jwt.decode(self.token, verify=False)
        except InvalidTokenError:
            raise ValueError('Invalid JWT token')

    def get_user_id(self):
        """ Returns the user_id provided by firebase
        """
        return self.decoded['user_id']

    def get_shops(self):
        """ Returns a list of shop_ids that the user has access to
        """
        return self.decoded['claims']['shop']

    def get_organizations(self):
        """ Returns a list of organization_ids that the user has access to
        """
        return self.decoded['claims']['organization']

    def get_token(self):
        """ Returns the original JWT token
        """
        return self.token
