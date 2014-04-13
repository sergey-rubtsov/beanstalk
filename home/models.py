from django.db import models

class MainPageInfo(models.Model):
    topic = models.CharField(max_length=200)
    message = models.TextField(max_length=5000)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-post_date',)

    def __unicode__(self):
        return self.post_date
