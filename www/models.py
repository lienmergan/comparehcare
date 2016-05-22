from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class HouseholdType(models.Model):
    household_type = models.CharField(max_length=55, default='alleenstaand')

    def __str__(self):
        # Returns the household type
        return self.household_type

    class Meta:
        verbose_name_plural = "HouseholdTypes"


# Create your models here

# Extending the User model
# https://docs.djangoproject.com/en/1.9/topics/auth/customizing/


class UserProfile(models.Model):
    # Define the family status by providing a choice list (enum)
    # ALLEENSTAAND = 'alleenstaand'
    # KOPPELS = 'koppels'
    # GEZIN_KLEINE_KINDEREN = 'gezin_kleinekinderen'
    # GEZIN_TIENERS = 'gezin_tieners'
    # SENIOREN = 'senioren'
    # HOUSEHOLD_TYPES_CHOICES = (
    #     (ALLEENSTAAND, 'alleenstaand'),
    #     (KOPPELS, 'koppels'),
    #     (GEZIN_KLEINE_KINDEREN, 'gezin met kleine kinderen'),
    #     (GEZIN_TIENERS, 'gezin met tieners'),
    #     (SENIOREN, 'senioren'),
    # )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    household_type = models.ForeignKey(HouseholdType, null=True, blank=True, on_delete=models.CASCADE)
    # household_type = models.CharField(max_length=15, choices=HOUSEHOLD_TYPES_CHOICES, default=ALLEENSTAAND)
    # owner = models.ForeignKey(User, related_name='profiles')

    def _get_household_type(self):
        # Returns the household type
        return self.household_type

    def __str__(self):
        # Returns the username of the user
        return self.user.username

    class Meta:
        verbose_name_plural = "UserProfiles"


class City(models.Model):
    name = models.CharField(max_length=90, blank=True)
    # postal_code = models.OneToOneField(PostalCode, on_delete=models.CASCADE, primary_key=True)
    pass

    def __str__(self):
        # Returns the city name
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class PostalCode(models.Model):
    code = models.CharField(max_length=10)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # Returns the postal code
        return self.code

    class Meta:
        verbose_name_plural = "Postalcodes"


class Address(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=5)
    postal_code = models.ForeignKey(PostalCode, null=True, blank=True, related_name='postal_code_id',
                                    on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True, related_name='city_id', on_delete=models.CASCADE)

    def _create_date(self):
        self.created_at = timezone.now()
        self.save()

    def _update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        # Returns the address
        return self.street + ' ' + self.street_number

    class Meta:
        verbose_name_plural = "Addresses"


class HealthInsurance(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    postal_code = models.ForeignKey(PostalCode, null=True, blank=True, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "HealthInsurances"

    def __str__(self):
        # Returns the name of the health insurance
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        # Returns the name of the health insurance
        return self.name


class HealthInsuranceContribution(models.Model):
    contribution = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)
    health_insurance = models.OneToOneField(HealthInsurance, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "HealthInsuranceContributions"

    def _create_date(self):
        self.created_at = timezone.now()
        self.save()

    def _update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        # Returns the yearly contribution
        return self.contribution


class HealthInsuranceBenefit(models.Model):
    description = models.TextField()
    single = models.BooleanField(default=True)
    couples = models.BooleanField(default=True)
    family_little_children = models.BooleanField(default=True)
    family_teenagers = models.BooleanField(default=True)
    seniors = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)
    health_insurance = models.ForeignKey(HealthInsurance, related_name='healthinsurance_id', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "HealthInsuranceBenefits"

    def __str__(self):
        # Returns the description of the healtcare benefit
        return self.health_insurance.name + ' ' + self.description