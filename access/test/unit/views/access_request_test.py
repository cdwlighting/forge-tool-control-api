"""
    Test case for the AccessRequest View.
"""
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from access.views import ToolAccess
from access.models import Machine, Profile, AccessLevel, Department

from mock import patch, MagicMock
import factory


class DepartmentFactory(factory.Factory):
	class Meta:
		model = Department

	name = 'Metal Shop'


class MachineFactory(factory.Factory):
	class Meta:
		model = Machine

	mac_address = 'FFFFFFFFFFFFFFFFFF'
	machine_name = 'Milling Machine'
	department = DepartmentFactory()


class UserFactory(factory.Factory):
	class Meta:
		model = User


class ProfileFactory(factory.Factory):
	class Meta:
		model = Profile

	user = UserFactory()
	department_head = None
	valid_membership = True
	member_card_id = 'DEADBEAD'


class AccessLevelFactory(factory.Factory):
	class Meta:
		model = AccessLevel

	access_level = 'FULL'
	profile = ProfileFactory()
	machine = MachineFactory()


class AccessRequestTest(TestCase):

    """
        This Class is the TestCase for ToolAccess
    """
    def setUp(self):
    	self.accesslevel = AccessLevelFactory()
    	self.factory = RequestFactory()

    def test_access_request(self):
			"""
			This function tests the view to verify that it will
			return a valid response with the given membership_id and machine_id.
			"""

			# this is a dictionary posted to the view.
			data = {
				'machine_id': 'FFFFFFFFFFFFFFFFFF',
				'member_id': 'DEADBEAD'
			}
			# we get a request from the Factory.
			request = self.factory.post(
				reverse('access_request'), 
				data
			)

			# use the View, and the request to get the response
			view = AccessRequestView.as_view()
			response = view(reqeust)

			# ensure we are getting a valid response
			self.assertEqual(response.status_code, 202)
