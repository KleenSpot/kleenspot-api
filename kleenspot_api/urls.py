"""kleenspot_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



schema_view = get_schema_view(
    openapi.Info(
        title="KLEENSPOT API",
        default_version='V2',
        description="The KleenSpot API provides endpoints for connecting cleaning service providers with customers in need of cleaning services. Our API is designed to be fast, secure, and easy to integrate, allowing cleaning companies to easily manage their bookings, dispatch cleaners, and track progress through our user-friendly interface. Our API includes endpoints for creating and managing customers accounts, bookings and canceling cleaning appointments, managing cleaning schedules and service offerings, and processing payments securely through our integrated payment gateway.We use the latest security protocols to protect user data and ensure privacy, including user authentication and authorization, SSL encryption, and secure storage of sensitive information.Developers can easily integrate with our API using RESTful web services and a clear and concise API documentation that outlines each endpoint and required parameters. Our API is designed to scale and can handle a large volume of requests without compromising on performance or reliability. With the KleenSpot API, cleaning companies can streamline their operations and provide a seamless experience for their customers.",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="kemoeverlyne@gmail.com"),
        license=openapi.License(name="Proprietory License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('dj_rest_auth.urls')),  
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('workers/', include('workers.urls')),
    

    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
