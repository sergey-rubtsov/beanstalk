from django.db import models

class Enquiry(models.Model):
    created = models.DateField('Date', auto_now_add=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    message = models.CharField(max_length=10000)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __unicode__(self):
        return "%s" % self.name
