from access.models import AccessRequest
from  rest_framework import serializers


class AccessLevelRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRequest
        fields = ('membership_card_id', 'machine_mac_id')
