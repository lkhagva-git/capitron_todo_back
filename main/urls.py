from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/test/', views.test_access, name='test_access'),
    
    path('api/signin/', views.signin, name='signin'),
    path('api/profile_data/', views.profile_data, name='profile_data'),
    path('api/add_task/', views.add_task, name='add_task'),
    path('api/get_task/', views.get_task, name='get_task'),
    path('api/delete_task/', views.delete_task, name='delete_task'),
    path('api/update_task/', views.update_task, name='update_task'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)