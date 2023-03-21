from django.urls import path
from . import views


urlpatterns = [
    path('', views. CleanerListAPIView.as_view(), name="cleaner"),
    path('<int:id>', views.CleanerDetailAPIView.as_view(), name="cleaner"),
    path('', views. CleanerServiceListAPIView.as_view(), name="cleanerservice"),
    path('<int:id>', views.CleanerServiceDetailAPIView.as_view(), name="cleanerservice"),
    path('', views. ServiceListAPIView.as_view(), name="service"),
    path('<int:id>', views.ServiceDetailAPIView.as_view(), name="service"),
    
]
