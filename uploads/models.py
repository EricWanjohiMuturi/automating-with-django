from django.db import models

# Create your models here.
class Uploads(models.Model):
    file = models.FileField(upload_to='uploads/')
    model_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Upload"
        verbose_name_plural = "Uploads"

    def __str__(self):
        return self.model_name