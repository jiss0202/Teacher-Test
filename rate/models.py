from django.db import models
from django.conf import settings 

# Create your models here.
class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="rate_user", on_delete=models.CASCADE)
    subject = models.CharField(max_length=60)
    professor = models.CharField(max_length=45)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    title = models.TextField()
    content = models.TextField()
