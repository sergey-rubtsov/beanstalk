from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_integer
from django.db import models

class Contact(models.Model):
    contact_name = models.CharField(max_length=25)
    contact_email = models.EmailField()
    telephone_number = models.CharField(max_length=20, validators=[MinLengthValidator(7)])
    message = models.TextField(max_length=5000)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-post_date',)
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')

    def __unicode__(self):
        return self.contact_email