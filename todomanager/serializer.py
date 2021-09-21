from django.db.models import fields
from rest_framework import serializers
from todomanager.models import Todo

# create serializer
class TodoSerializer(serializers.ModelSerializer):
    # create a meta class
    class Meta:
        model = Todo
        fields = '__all__'