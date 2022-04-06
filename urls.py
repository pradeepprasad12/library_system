from django.urls import path,include
from bookaccount.api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView,TokenRefreshView,TokenObtainPairView

router = DefaultRouter()
router.register('crud',views.Userviewset,basename='user')


urlpatterns = [
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),


]