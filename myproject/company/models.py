from django.db import models


class Member(models.Model):
    image = models.ImageField(upload_to="images/", default="about.jpg")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


class AboutManager(models.Manager):
    def get_or_create_singleton(self):
        obj, created = self.get_or_create(pk=1)
        return obj


class About(models.Model):
    about_img = models.ImageField(upload_to="images/", default="about.jpg")
    header = models.CharField(max_length=255)
    body = models.TextField()

    objects = AboutManager()

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "About"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
