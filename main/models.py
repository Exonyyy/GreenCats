from django.db import models


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, db_index=True)
    surname = models.CharField(max_length=128, db_index=True)
    email = models.CharField(max_length=128, db_index=True)
    logo = models.ImageField(upload_to='static/media/user_logo')
    is_admin = models.BooleanField()
    is_moderator = models.BooleanField()
    is_activist = models.BooleanField()
    is_scientist = models.BooleanField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
