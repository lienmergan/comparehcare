from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from .models import UserProfile, City, PostalCode, Address, HealthInsurance, Category, HealthInsuranceContribution, HealthInsuranceBenefit
from .serializers import UserSerializer, PostalCodeSerializer, CitySerializer, UserProfileSerializer, AddressSerializer, HealthInsuranceSerializer, CategorySerializer, HealthInsuranceContributionSerializer, HealthInsuranceBenefitSerializer

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


class CityCodeViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



"""
class PostalCodeList(generics.ListCreateAPIView):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer


class PostalCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer
"""