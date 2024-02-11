from django.db import models
from main.models import UserProfile


class ForumTopic(models.Model):
    id = models.AutoField(primary_key=True)
    from_person = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)
    took_park = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.topic_name


class TopicCallback(models.Model):
    id = models.AutoField(primary_key=True)
    topic_id = models.ForeignKey(ForumTopic, on_delete=models.CASCADE)
    email = models.CharField(max_length=128)
