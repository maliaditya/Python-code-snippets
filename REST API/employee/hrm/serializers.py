from rest_framework import serializers
from .models import Users

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = Users
        #fields = ('name','employee_id')
        fields = '__all__'