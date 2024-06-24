
import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
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
        # Check if the user is the currently signed-in user
        if self.user != id.objects.get(pk=self.user.pk):
            raise ValidationError("You don't have permission to perform this action.")
