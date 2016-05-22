from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from .models import User, UserProfile, City, PostalCode, Address, HealthInsurance, Category, HealthInsuranceContribution, HealthInsuranceBenefit, HouseholdType
from .serializers import UserSerializer, PostalCodeSerializer, CitySerializer, UserProfileSerializer, AddressSerializer, \
    HealthInsuranceSerializer, CategorySerializer, HealthInsuranceContributionSerializer, HealthInsuranceBenefitSerializer, HouseholdTypeSerializer

# Create your views here.

"""
def home(request):
    return render(request, "www/home.html")
"""

"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'postalcodes': reverse('postalcode-list', request=request, format=format)
    })
"""


class PostalCodeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['post'])
    def set_user(self, request):
        user = self.get_object()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user.set_user(serializer.data['username', 'password'])
            user.save()
            return Response({'status': 'user set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class HouseholdTypeViewSet(viewsets.ModelViewSet):
    queryset = HouseholdType.objects.all()
    serializer_class = HouseholdTypeSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class HealthInsuranceViewSet(viewsets.ModelViewSet):
    queryset = HealthInsurance.objects.all()
    serializer_class = HealthInsuranceSerializer


class HealthInsuranceContributionViewSet(viewsets.ModelViewSet):
    queryset = HealthInsuranceContribution.objects.all()
    serializer_class = HealthInsuranceContributionSerializer


class HealthInsuranceBenefitViewSet(viewsets.ModelViewSet):
    queryset = HealthInsuranceBenefit.objects.all()
    serializer_class = HealthInsuranceBenefitSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



"""
class PostalCodeList(generics.ListCreateAPIView):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer


class PostalCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer
"""