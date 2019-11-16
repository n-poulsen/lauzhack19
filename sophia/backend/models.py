from django.db.models.fields import TextField, IntegerField
from django.db import models


class Sample(models.Model):
    """
    Represents a table of samples
    """

    def __str__(self):
        return f'Article id: {self.id}'


class Organism(models.Model):
    """
    Represents a table of organisms
    """

    def __str__(self):
        return f'Article id: {self.id}'


class DetectedOrganism(models.Model):
    """
    Represents a table of organisms detected in a sample
    """

    def __str__(self):
        return f'Article id: {self.id}'
