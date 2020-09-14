from rest_framework import serializers

from alumni.models import *

class AlumniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)

        alumnus, created = Alumni.objects.update_or_create(user=user,
                            rollno=validated_data.pop('rollno'))
        return alumnus

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
