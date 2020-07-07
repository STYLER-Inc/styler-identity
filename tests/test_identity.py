#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `styler_identity` package."""

import pytest


from styler_identity.identity import Identity


@pytest.fixture
def token():
    return (
        'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc2MjNlMTBhMDQ1MTQwZjFjZmQ0YmUwNDY2Y2'
        'Y4MDM1MmI1OWY4MWUiLCJ0eXAiOiJKV1QifQ.eyJyb2xlcyI6WyJzeXNhZG1pbiIsI'
        'nN0YWZmIiwiYWRtaW4iXSwiY2xhaW1zIjp7InNob3AiOlsiMTIzNDUiLCIzMzQ0MiJ'
        'dLCJvcmdhbml6YXRpb24iOlsiMzMzMzMiXX0sImlzcyI6Imh0dHBzOi8vc2VjdXJld'
        'G9rZW4uZ29vZ2xlLmNvbS9mYWN5LWRldmVsb3BtZW50IiwiYXVkIjoiZmFjeS1kZXZ'
        'lbG9wbWVudCIsImF1dGhfdGltZSI6MTU5NDAwNjAxNiwidXNlcl9pZCI6IjZuYWY4M'
        'Gp0eWJWUnVQMjJlWWNJWUdYMktKSzIiLCJzdWIiOiI2bmFmODBqdHliVlJ1UDIyZVl'
        'jSVlHWDJLSksyIiwiaWF0IjoxNTk0MDA2MDE2LCJleHAiOjE1OTQwMDk2MTYsImVtY'
        'WlsIjoiYnJ1bm8uc3VnYW5vQHN0eWxlci5saW5rIiwiZW1haWxfdmVyaWZpZWQiOmZ'
        'hbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImJydW5vLnN1Z'
        '2Fub0BzdHlsZXIubGluayJdfSwic2lnbl9pbl9wcm92aWRlciI6ImN1c3RvbSJ9fQ.'
        'EkyieQPlrQ7kQ9nAaTMz7O_PCNXo_c77Apx2aIes1CKfkeD1kXwLCd6V_Vy8NfNebL'
        '-aOymuCpssHv6Eew3qaIJ1qCrPWcLQ3xOvSYoStbk8dq4ZFHnKz68M7JPaUQg-wD0J'
        '5wnbkqHDtLwEG9QPdsFHK3pYNtgtz-5nP6P9RgDpmkmsz_Orf0el2etMzmPN_DZN0F'
        'zExd_4l2xcyk2Hs5Hrfz1OlZp6wuppoP4fNfgVzqdFS_uYugIgUR2Nn_dpD0qzh61T'
        '9MW8Rw5r68jBgaA04DUAY5EZtBIZotDFRMh-ZEMLD7HBDtE4ytawO-ADr_C5fAh4KP'
        'HS-mgPvZA0ag'
    )


class TestIdentity:
    """ Tests 
    """
    def test_invalid_token(self):
        with pytest.raises(ValueError) as expected:
            Identity('invalid token')

        assert str(expected.value) == 'Invalid JWT token'

    def test_valid_token(self, token):
        idem = Identity(token)

        assert isinstance(idem, Identity)

    def test_get_token(self, token):
        idem = Identity(token)

        tk = idem.get_token()

        assert token == tk

    def test_get_user_id(self, token):
        idem = Identity(token)

        user_id = idem.get_user_id()

        assert user_id == '6naf80jtybVRuP22eYcIYGX2KJK2'

    def test_get_shops(self, token):
        idem = Identity(token)

        shops = idem.get_shops()

        assert shops == ['12345', '33442']

    def test_get_organizations(self, token):
        idem = Identity(token)

        organizations = idem.get_organizations()

        assert organizations == ['33333']
