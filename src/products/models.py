from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to="static/products_img/", default="../static/image/default_img.png"
    )
    modelName = models.CharField(max_length=250, default="Doll")
    height = models.DecimalField(decimal_places=1, max_digits=20, default=5)
    color = models.CharField(max_length=50, default="Red")
    weight = models.DecimalField(decimal_places=0, max_digits=20, default=1)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.TextField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
