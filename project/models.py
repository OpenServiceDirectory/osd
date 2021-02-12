from django.db import models
from django.contrib.gis.db import models
from django.db.models.deletion import CASCADE
from accounts.models import Account
from django.core.validators import MinValueValidator, MaxValueValidator
from django.templatetags.static import static
from spatialdata.models import Limits

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    location = models.PointField()
    image = models.ImageField(default="static/images/default-service.jpg", blank=True, upload_to='advertisements')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    location = models.PointField()
    image = models.ImageField(blank=True, upload_to='services')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return static("images/default-service.jpg")
    
    def get_location(self):
        limits = Limit

        return "nice"


class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    msg = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review de {self.user.username}: \n{self.msg}"
