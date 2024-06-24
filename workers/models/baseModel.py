import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_created", default=1)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_updated", default=1)
    is_approved = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def is_soft_deleted(self):
        return self.deleted_at is not None

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def undelete(self):
        self.deleted_at = None
        self.is_deleted = False
        self.save()

    def clean(self):
        if self.created_by != User.objects.get(pk=self.created_by.pk):
            raise ValidationError("You don't have permission to perform this action.")
