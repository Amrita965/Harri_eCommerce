from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        print("Self::", self)
        print("Args::", args)
        print("Kwargs::", kwargs)
        # Save the model first to ensure the image is available at self.image.path
        super().save(*args, **kwargs)

        #Perform image conversion
        if self.image:
            pass

    def __str__(self):
        return self.name