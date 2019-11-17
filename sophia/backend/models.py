from django.db.models.fields import IntegerField, CharField, DateTimeField
from django.db import models


class Sample(models.Model):
    """
    Represents a table of samples
    """
    name = CharField(max_length=30, unique=True)
    origin = CharField(max_length=30)
    date = DateTimeField()

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'


class Organism(models.Model):
    """
    Represents a table of organisms
    """
    name = CharField(max_length=50, unique=True)
    type = CharField(max_length=30)
    danger = IntegerField()

    def __str__(self):
        return f'{self.name}'


class DetectedOrganism(models.Model):
    """
    Represents a table of organisms detected in a sample
    """
    name = CharField(max_length=50)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    type = models.ForeignKey(Organism, on_delete=models.CASCADE)
    confidence = IntegerField()

    def __str__(self):
        return f'{self.name}'
