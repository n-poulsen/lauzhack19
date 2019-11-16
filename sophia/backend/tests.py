from django.test import TestCase
from .models import Sample, Organism, DetectedOrganism
from .helper import parse_samples
import datetime


class SampleTestCase(TestCase):

    def setUp(self):
        s1 = Sample.objects.create(
            name='sample1',
            origin='room-4',
            date=datetime.datetime.now(),
        )
        s2 = Sample.objects.create(
            name='sample2',
            origin='room-6',
            date=datetime.datetime.now(),
        )
        org1 = Organism.objects.create(
            name='SuperDeath',
            type='Virus',
            danger=3,
        )
        org2 = Organism.objects.create(
            name='SuperMegaDeath',
            type='Virus',
            danger=5,
        )
        DetectedOrganism.objects.create(
            name='SuperDeath',
            sample=s1,
            type=org1,
            confidence=50,
        )
        DetectedOrganism.objects.create(
            name='SuperMegaDeath',
            sample=s2,
            type=org2,
            confidence=80,
        )

    def test_easy(self):
        samples = Sample.objects.all()
        for s in parse_samples(samples):
            print(s)
