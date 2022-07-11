from django.urls import include, path
from rest_framework import routers
from mydrugs import views

router = routers.DefaultRouter()
router.register(r'users', viewset=views.UserViewSet)
router.register(r'groups', viewset=views.GroupViewSet)
router.register(r'drugs', viewset=views.DrugViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
