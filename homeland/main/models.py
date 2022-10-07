from django.db import models
from django.urls import reverse


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name}"


class Gallery(models.Model):
    image = models.ImageField('Image', upload_to="gallery/%y/%m/%d/")

    def __str__(self):
        return f"Gallery {self.id}"


class AboutTour(models.Model):
    img = models.ImageField('Image', upload_to="about/")
    title = models.CharField('Title', max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Tour(models.Model):
    banner = models.ImageField('Banner', upload_to="banner/%y/%m/%d/")
    card = models.ImageField('Card', upload_to="card/%y/%m/%d/")
    title = models.CharField('Name of Tour', max_length=255)
    slug = models.SlugField(unique=True)
    cost = models.CharField('Cost', max_length=200)
    rating = models.IntegerField('Star', default=5)
    description = models.TextField()
    gallery = models.ManyToManyField(Gallery, blank=True)
    about = models.ManyToManyField(AboutTour, blank=True)

    def get_rating(self):
        string_rating = ''
        for i in range(0, self.rating + 1):
            string_rating += str(i)
        return string_rating

    def get_absolute_url(self):
        return reverse('main:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"
