
from django.conf.urls import url,include
from asset import views
from asset import rest_views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'assets', rest_views.AssetViewSet)
router.register(r'idcs', rest_views.IDCViewSet)
router.register(r'users', rest_views.UserProfileViewSet)



urlpatterns = [
    url(r'', include(router.urls)),
    url(r'report/$', views.asset_report, name='asset_report'),
    url(r'report/asset_with_no_asset_id/$', views.asset_with_no_asset_id),
    url(r'^new_assets/approval/$', views.new_assets_approval, name="new_assets_approval"),

]
