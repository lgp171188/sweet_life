from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Reading(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    label = models.ForeignKey(Label, related_name='readings')
    comments = models.TextField(blank=True, null=True)

    def label_name(self):
        return self.label.name
