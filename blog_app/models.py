# blog/models.py
from django.db import models
from django.core.exceptions import ValidationError

def validate_image_format(image):
    if not image.name.endswith('.jpeg'):
        raise ValidationError('Only JPEG format is allowed.')

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', validators=[validate_image_format])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
