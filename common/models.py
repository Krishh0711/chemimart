from django.db import models

class AbstractTimeStampModel(models.Model):
    """
    Abstract model class with timestamp fields for creation and update times.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True