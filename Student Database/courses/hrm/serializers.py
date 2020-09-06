from rest_framework import serializers
from hrm.models import Users

class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    subtitle = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    timestamp = serializers.IntegerField(required=False)
    created_by = serializers.CharField(required=False)

    class Meta:
        model = Users
        #fields = ('name','subtitle')
        fields = '__all__'

