from django.db import models

class About(models.Model):
    topic = models.CharField(max_length=200)
    message = models.TextField(max_length=5000)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-post_date',)
        verbose_name = ('About')
        verbose_name_plural = ('About version')

class Cv(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField(max_length=50000)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-post_date',)
        verbose_name = ('CV')
        verbose_name_plural = ('CV version')



