from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    # path('api/items/', views.get_items, name='get_items'),
    # # path('api/token/', views.login_view, name='login_view'),
    # path('api/test_access/', views.test_access, name='test_access'),
    # path('api/anket/', views.createAnket, name='createAnket'),
    # path('send_test_email', views.send_test_email, name='send_test_email'),


    # path('api/token/', obtain_auth_token, name='api_token_auth'),
    # path('api/profile_data/', views.profile_data, name='profile_data'),


    # path('api/candidates_data/', views.candidates_data, name='candidates_data'),
    # path('api/job_application/<int:pk>/', views.job_application, name='job_application'),
    # path('api/interview_history/<int:pk>/', views.interview_history, name='interview_history'),

    # path('api/create_interview_plan/', views.create_interview_plan, name='create_interview_plan'),
    # path('api/conduct_interview/', views.conduct_interview, name='conduct_interview'),
    # path('api/create_schedule/', views.create_schedule, name='create_schedule'),
    # path('api/schedule_list/', views.schedule_list, name='schedule_list'),
    # path('api/profile_list/', views.profile_list, name='profile_list'),

    # path('api/interview_detail/<int:pk>/', views.interview_detail, name='interview_detail'),


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