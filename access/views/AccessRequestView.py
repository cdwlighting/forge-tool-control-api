from access.models import Profile, Machine, AccessLevel, AccessRequest
from access.serializers.AccessLevelRequest import AccessLevelRequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AccessRequestView(APIView):
  def post(self, request, format=None):
		accessLevel = AccessLevel.objects.filter(profile__member_card_id = '', machine__mac_address='')

		accessRequest = AccessRequest('','')

		serializer = AccessLevelRequestSerializer(accessRequest, many=False )

		return Response(serializer.data)
