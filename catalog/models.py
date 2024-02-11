from django.db import models


# def get_protection_types():
#     types = BankProtectionTypes.objects.all()
#     types_dict = dict()
#     for obj_type in types:
#         types_dict[obj_type[:5].upper()] = obj_type
#     return types_dict


class BankProtectionTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, db_index=True, unique=True)


class BankProtectionStructures(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True, db_index=True)
    short_description = models.CharField(max_length=1000)
    full_description = models.TextField()
    photo = models.ImageField(upload_to='stativ/media/protection_photo/from_scientists')
    mark = models.PositiveSmallIntegerField()
    prognosis = models.CharField(max_length=32, blank=True, null=True)
    # type = models.CharField(choices=get_protection_types)
    type = models.CharField(max_length=128)
    build_date = models.DateField(null=True, blank=True)
    last_repair_date = models.DateField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return self.name


class UserComments(models.Model):
    id = models.AutoField(primary_key=True)
    obj_id = models.ForeignKey(BankProtectionStructures, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    active = models.BooleanField()
    photo = models.ImageField(upload_to='static/media/protection_photos/from_comments')
    text = models.CharField(max_length=256)
    publish_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def update_comment_active(self):
        pass