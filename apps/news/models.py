from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    main_image = models.ImageField(upload_to='news', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    new = models.ForeignKey('New', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news')

    def __str__(self):
        return self.image.name