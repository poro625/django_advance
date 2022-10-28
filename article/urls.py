
from django.urls import path
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, 
    TokenRefreshView, 
)



urlpatterns = [
    # path()
    path('api/token/', TokenObtainPairView.as_view(), name='aaa'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='bbb'),
    
]