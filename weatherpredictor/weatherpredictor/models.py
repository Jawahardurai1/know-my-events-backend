from django.db import models
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile

class data(models.Model):
    poster=models.ImageField(upload_to='uploads/') 
    eve=models.CharField(max_length=200)
    date=models.DateField(max_length=20)
    venue=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    link=models.CharField(max_length=700)

def save(self, *args, **kwargs):
        # Open the uploaded image
        img = PilImage.open(self.poster)

        # Convert to JPEG format (or any other format you need)
        if img.format != 'JPEG':
            img = img.convert('RGB')
            img_io = BytesIO()
            img.save(img_io, format='JPEG', quality=85)  # Set quality as needed
            img_file = ContentFile(img_io.getvalue(), name=self.poster.name.split('.')[0] + '.jpg')

            # Update the poster field with the new JPEG file
            self.poster.save(img_file.name, img_file, save=False)

        # Call the original save method
        super().save(*args, **kwargs)
