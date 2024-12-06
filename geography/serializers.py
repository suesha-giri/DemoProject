from rest_framework import serializers
from .models import City, Country
from django.db import transaction


class PlacesListSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='name')
    country = serializers.CharField(source='country.name')

    class Meta:
        model = City
        fields = ['id', 'city', 'country', 'population']


class PlacesCreateSerializer(PlacesListSerializer):
    class Meta(PlacesListSerializer.Meta):
        fields = PlacesListSerializer.Meta.fields

    def create(self, validated_data):
        country_name = validated_data['country']['name']
        city_name = validated_data['name']

        with transaction.atomic():
            country, created = Country.objects.get_or_create(name=country_name)
            if City.objects.filter(name=city_name, country=country).exists():
                raise serializers.ValidationError({"error": "This city already exists in the specified country."})

            city = City.objects.create(
                name=city_name,
                country=country,
                population=validated_data['population']
            )

        return city
    
