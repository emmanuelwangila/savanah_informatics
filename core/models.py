from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

class SoftDeleteModel(models.Model):
    is_active = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        """Soft delete"""
        self.is_active = False
        self.save()

    class Meta:
        abstract = True

class UserProfile(models.Model):
    user = models.OneToOneField(
        'auth.User',  # or 'customers.Customer' if using custom user model
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile for {self.user.email}"

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
    ]

    user = models.ForeignKey(
        'auth.User',  # or 'customers.Customer'
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)
    details = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = _('Audit Log')
        verbose_name_plural = _('Audit Logs')

    def __str__(self):
        return f"{self.get_action_display()} on {self.model_name} by {self.user}"

class Configuration(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.JSONField()
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.key