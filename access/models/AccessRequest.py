"""
    This model is the expected format of the access reqeust.
"""


class AccessRequest:
	def __init__(self, membership_card_id, machine_mac_id):
		self.membeship_card_id = membership_card_id
		self.machine_mac_id = machine_mac_id
