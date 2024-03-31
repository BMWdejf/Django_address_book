from django.contrib.auth.models import Group, User
from rest_framework import serializers
# TODO: import Address_Book

# Serializers for User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'group']

# Serializers for Group
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# Serializers for Address_Book
class AddressBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressBook
        fields = ['fb_id', 'kod', 'nazev']
