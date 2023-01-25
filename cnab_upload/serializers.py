from rest_framework import serializers
from .models import CNABMovimentation


class CNABMovimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNABMovimentation
        fields = "__all__"


class ListMovimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNABMovimentation
        fields = "__all__"
