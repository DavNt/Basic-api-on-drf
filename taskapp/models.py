from django.db import models


# Create your models here.
class Picture(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    author = models.CharField(max_length=294)
    width = models.IntegerField()
    height = models.IntegerField()
    url = models.URLField(unique=True)
    download_url = models.URLField(unique=True)

    def __int__(self):
        return self.id


class PicId(models.Model):
    id = models.ForeignKey(Picture, on_delete=models.CASCADE, primary_key=True)
    url = models.URLField(unique=True)

    def save(self, *args, **kwargs):
        self.url = self.id.download_url
        super(PicId, self).save(*args, **kwargs)
