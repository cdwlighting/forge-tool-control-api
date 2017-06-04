"""
    This test case is for the tool access view.  It contains 3 profiles,
    2 machines and the access level fields.  The cases test are such:
        1- Valid membership & FULL access on the Machine
        2- Invalid memberchip & FULL access on the Machine
        3 - Valid membership & NONE access on the Machine
"""
from django.test import TestCase
import mock
from access.models import Profile


class testtoolaccess(TestCase):
    def testToolAccessOk(self):
        mock_render_response = mock.MagicMock()
