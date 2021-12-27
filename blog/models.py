from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.
class post(models.Model):
    aouthor=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DurationField(blank=True,null=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title
