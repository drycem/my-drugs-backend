from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from mydrugs.models import Drug
from mydrugs.serializers import UserSerializer, GroupSerializer, DrugSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewes or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DrugViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows drugs to be viewed.
    """
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'code'
