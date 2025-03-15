from django.db import models


class User(models.Model):
    author = models.CharField(max_length=100, null=True, blank=True)
    short_info = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='user_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Users'

    def __str__(self):
        return self.author
