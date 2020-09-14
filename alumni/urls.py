from django.urls import include, path
from rest_framework import routers
from alumni.views import *

router = routers.DefaultRouter()
router.register('alumni', AlumniViewSet)
router.register('user', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
