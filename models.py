from django.db import models


class Image(models.Model):
    public_id = models.CharField(max_length=2056, primary_key=True)
    image_url = models.CharField(max_length=20561)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)




