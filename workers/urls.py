from django.urls import path
from . import views


urlpatterns = [
    path('cleaners/', views. CleanerListAPIView.as_view(), name="cleaner"),
    path('cleaners/<int:id>', views.CleanerDetailAPIView.as_view(), name="cleaner"),
    path('services/', views. ServiceListAPIView.as_view(), name="service"),
    path('services/<int:id>', views.ServiceDetailAPIView.as_view(), name="service"),
    
]
