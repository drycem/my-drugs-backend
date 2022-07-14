from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mydrugs import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DrugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Drug
        fields = ('url', 'name', 'code', 'atc', 'etken', 'firma', 'durum')
        extra_kwargs = {
            'url': {'view_name': 'drug-detail', 'lookup_field': 'code'}
        }

class SgkDrugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SgkDrug
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'sgkdrug-detail', 'lookup_field': 'BARKOD'}
        }
