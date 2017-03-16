"""
    This Serializer is for the Profile Model.
"""

from __future__ import unicode_literals

from rest_framework import serializers
from access.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile Serializer serializes the Profile Model.
    """
    user = serializers.HyperlinkedRelatedField(many=False, read_only=True,
                                               view_name='users')
    department = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                     view_name='departments')
    access_levels = serializers.HyperlinkedRelatedField(many=True,
                                                        read_only=True,
                                                        view_name='accesslevels')

    class Meta:
        model = Profile
        fields = (
            "user",
            "department",
            "access_levels",
            "valid_membership",
            "member_card_id",
        )
