from django.contrib import admin

from .models import PostalCode, City, HealthInsurance, HealthInsuranceBenefit, HealthInsuranceContribution, Address, \
    Category, UserProfile, HouseholdType
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Create resources for use in admin; upload external files
class PostalCodeResource(resources.ModelResource):

    class Meta:
        model = PostalCode
        fields = ('id', 'code', 'city',)


class PostalCodeAdmin(ImportExportModelAdmin):
    ordering = ('code',)
    resource_class = PostalCodeResource
    pass


class CityResource(resources.ModelResource):

    class Meta:
        model = City
        fields = ('id', 'name',)


class CityAdmin(ImportExportModelAdmin):
    ordering = ('name',)
    resource_class = CityResource
    pass


class AddressResource(resources.ModelResource):

    class Meta:
        model = Address
        fields = ('id', 'street', 'street_number',)


class AddressAdmin(ImportExportModelAdmin):
    resource_class = AddressResource
    pass


class HealthInsuranceResource(resources.ModelResource):

    class Meta:
        model = HealthInsurance
        fields = ('id', 'name', 'url',)


class HealthInsuranceAdmin(ImportExportModelAdmin):
    ordering = ('name',)
    resource_class = HealthInsuranceResource
    pass


class HealthInsuranceContributionResource(resources.ModelResource):

    class Meta:
        model = HealthInsuranceContribution
        fields = ('id', 'contribution', 'health_insurance',)


class HealthInsuranceContributionAdmin(ImportExportModelAdmin):
    ordering = ('contribution',)
    resource_class = HealthInsuranceContributionResource
    pass


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class CategoryAdmin(ImportExportModelAdmin):
    ordering = ('name',)
    resource_class = CategoryResource
    pass


class HealthInsuranceBenefitResource(resources.ModelResource):
    class Meta:
        model = HealthInsuranceBenefit
        fields = ('id', 'description', 'health_insurance',)


class HealthInsuranceBenefitAdmin(ImportExportModelAdmin):
    resource_class = HealthInsuranceBenefitResource
    pass


class HouseholdTypeAdmin(admin.ModelAdmin):
    ordering = ('household_type',)


# Register your models here.
admin.site.register(PostalCode, PostalCodeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(HealthInsurance, HealthInsuranceAdmin)
admin.site.register(HealthInsuranceContribution, HealthInsuranceContributionAdmin)
admin.site.register(HealthInsuranceBenefit, HealthInsuranceBenefitAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.register(HouseholdType, HouseholdTypeAdmin)
