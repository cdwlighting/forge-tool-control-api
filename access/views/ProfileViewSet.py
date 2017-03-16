from rest_framework import viewsets
from access.serializers import ProfileSerializer
from access.models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Model View set for the Profile model
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
