#__author:  Administrator
#date:  2017/3/8
from rest_framework import viewsets
from asset.rest_serialize import  AssetSerializer,IDCSerializer,UserProfileSerializer
from  asset import models

class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = AssetSerializer


class IDCViewSet(viewsets.ModelViewSet):
    queryset = models.IDC.objects.all()
    serializer_class = IDCSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = UserProfileSerializer