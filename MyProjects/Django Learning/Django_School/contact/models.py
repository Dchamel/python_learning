from django.db import models


class Contact(models.Model):
    """Email Subscribe"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
