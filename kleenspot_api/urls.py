"""kleenspot_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="KLEENSPOT API",
        default_version='VERSION 1',
        description="The KleenSpot API provides a robust platform for connecting cleaning service providers with customers in need of cleaning services. Our API is designed to be fast, secure, and easy to integrate, allowing cleaning companies to easily manage their bookings, dispatch cleaners, and track progress through our user-friendly interface. Our API includes endpoints for creating and managing customer accounts, booking and canceling cleaning appointments, managing cleaning schedules and service offerings, and processing payments securely through our integrated payment gateway.We use the latest security protocols to protect user data and ensure privacy, including user authentication and authorization, SSL encryption, and secure storage of sensitive information.Developers can easily integrate with our API using RESTful web services and a clear and concise API documentation that outlines each endpoint and required parameters. Our API is designed to scale and can handle a large volume of requests without compromising on performance or reliability. With the KleenSpot API, cleaning companies can streamline their operations and provide a seamless experience for their customers.",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="kemoeverlyne@gmail.com"),
        license=openapi.License(name="Proprietory License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
    path('expenses/', include('expenses.urls')),
    path('income/', include('income.urls')),
    path('services/', include('services.urls')),

    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
