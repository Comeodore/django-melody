from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/flats', views.FlatsViewSet)

urlpatterns = [
    path('', views.startpage),
    path('', include(router.urls)),
    path('buy/<int:id>', views.buy),
    path('success', views.success),
    path('cancel', views.cancel),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
