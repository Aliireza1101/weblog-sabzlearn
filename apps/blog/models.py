from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "PB", ("Published")
        REJECTED = "RJ", ("Rejected")
        DRAFT = "DF", ("Draft")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250)

    # Date
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Choice
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-publish",)
        indexes = [
            models.Index(fields=["-publish"]),
        ]
