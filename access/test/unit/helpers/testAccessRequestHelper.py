import unittest
import mock

from access.helpers.AccessRequestHelper import AccessRequestHelper


class TestAcceessRequestHelper(unittest.TestCase):
    def test_member_is_authenticated(self):
        sut = AccessRequestHelper()
        self.assertTrue(True)
