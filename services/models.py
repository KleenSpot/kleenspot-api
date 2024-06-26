# '''
# cleaners models
# '''
# from django.db import models
# from django.conf import settings
# from django.utils import timezone


# class Cleaner(models.Model):
#     '''
#     Cleaner model
#     '''
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, blank=True)
#     address = models.CharField(max_length=200, blank=True)
#     city = models.CharField(max_length=200, blank=True)
#     created_date = models.DateTimeField(default=timezone.now)
#     updated_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.user.username}'s profile"


# class CleanerService(models.Model):
#     '''
#     CleanerService model
#     '''
#     cleaner = models.ForeignKey(
#         Cleaner, on_delete=models.CASCADE, related_name='services')
#     service = models.ForeignKey(
#         'Service', on_delete=models.CASCADE, related_name='cleaners')
#     created_date = models.DateTimeField(default=timezone.now)
#     updated_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.cleaner.user.username + ' - ' + self.service.name


# class Service(models.Model):
#     '''
#     Service Model
#     '''
#     name = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     created_date = models.DateTimeField(default=timezone.now)
#     updated_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name
