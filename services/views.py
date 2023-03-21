from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CleanerSerializer, CleanerServiceSerializer, ServiceSerializer
from .models import Cleaner, CleanerService, Service
from rest_framework import permissions
from .permissions import IsOwner


class CleanerListAPIView(ListCreateAPIView):
    serializer_class = CleanerSerializer
    queryset = Cleaner.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CleanerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CleanerSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Cleaner.objects.all()
    lookup_field = "user"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CleanerServiceListAPIView(ListCreateAPIView):
    serializer_class = CleanerServiceSerializer
    queryset = CleanerService.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CleanerServiceDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CleanerServiceSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = CleanerService.objects.all()
    lookup_field = "service"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ServiceListAPIView(ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ServiceDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Service.objects.all()
    lookup_field = "name"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
