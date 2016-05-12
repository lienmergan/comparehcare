from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from www import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
# The API URLs are now determined automatically by the router.
router = DefaultRouter(trailing_slash=False)
router.register(r'postalcodes', views.PostalCodeViewSet)
router.register(r'cities', views.CityCodeViewSet)
router.register(r'userprofiles', views.UserProfileViewSet)


# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

"""
# API endpoints
urlpatterns = patterns('',
                       url(r'^$', views.api_root),
                       url(r'^postalcodes/$', views.PostalCodeList.as_view(),
                           name='postalcode-list'),
                       url(r'^postalcodes/(?P<pk>[0-9]+)/$', views.PostalCodeDetail.as_view(),
                           name='postalcode-detail')
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
"""