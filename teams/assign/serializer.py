
from django.contrib.auth.models import User
from .models import Team, Relation, Person
from rest_framework import serializers

from drf_writable_nested import WritableNestedModelSerializer

class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ("id", )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email" )

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id",)


class TeamSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    read_only=True
    users = PersonSerializer(many=True)#, required=True)    
    class Meta:
        model = Team
        fields = ('name', 'users',  )



"""def create(self, validated_data):
        tracks_data = validated_data.pop('users', "users")
        team = Team.objects.create(**validated_data)
        for track_data in tracks_data:
            User.objects.create(team=team, **track_data)
        return team"""