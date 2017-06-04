from access.models import AccessLevelResponse
from  rest_framework import serializers

class AccessResponseSerializer(serializers.ModelSerializer):
		class _Meta:
			Model: AccessLevelResponse
			