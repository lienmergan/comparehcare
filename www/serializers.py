from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, City, PostalCode, Address, HealthInsurance, Category, \
    HealthInsuranceContribution, HealthInsuranceBenefit, HouseholdType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class PostalCodeSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = PostalCode
        fields = ('id', 'code', 'city')


class HouseholdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdType
        fields = ('id', 'household_type')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    household_type = HouseholdTypeSerializer()

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'household_type')


class AddressSerializer(serializers.ModelSerializer):
    postal_code = PostalCodeSerializer()
    city = CitySerializer()

    class Meta:
        model = Address
        fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'street', 'street_number', 'postal_code', 'city')


class HealthInsuranceSerializer(serializers.ModelSerializer):
    postal_code = PostalCodeSerializer()
    address = AddressSerializer()

    class Meta:
        model = HealthInsurance
        fields = ('id', 'name', 'url', 'postal_code', 'address')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class HealthInsuranceContributionSerializer(serializers.ModelSerializer):
    health_insurance = HealthInsuranceSerializer()

    class Meta:
        model = HealthInsuranceContribution
        fields = ('id', 'contribution', 'created_at', 'updated_at', 'deleted_at', 'health_insurance')


class HealthInsuranceBenefitSerializer(serializers.ModelSerializer):
    health_insurance = HealthInsuranceSerializer()
    category = CategorySerializer()

    class Meta:
        model = HealthInsuranceBenefit
        fields = ('description', 'single', 'couples', 'family_little_children', 'family_teenagers', 'seniors', 'created_at', 'updated_at', 'deleted_at', 'health_insurance', 'category')
