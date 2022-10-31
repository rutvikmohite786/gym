from django.db import models

class SliderHome(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    img_path = models.CharField(max_length=200)
