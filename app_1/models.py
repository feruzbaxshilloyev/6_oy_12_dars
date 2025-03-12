from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    short_info = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='user_images/')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Users'

    def __str__(self):
        return self.name
