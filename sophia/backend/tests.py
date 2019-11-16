from django.test import TestCase, Client
from .models import Sample, Organism, DetectedOrganism
from .helper import parse_samples
import datetime
import json
import pytz


class SampleTestCase(TestCase):
    tzone = pytz.UTC

    def setUp(self):
        s1 = Sample.objects.create(
            name='sample1',
            origin='room-4',
            date=datetime.datetime(2019, 10, 11, 18, 14, tzinfo=self.tzone),
        )
        org1 = Organism.objects.create(
            name='SuperDeath',
            type='Virus',
            danger=3,
        )
        DetectedOrganism.objects.create(
            name='SuperDeath',
            sample=s1,
            type=org1,
            confidence=50,
        )
        s2 = Sample.objects.create(
            name='sample2',
            origin='room-6',
            date=datetime.datetime(2019, 10, 4, 4, 45, tzinfo=self.tzone),
        )
        org2 = Organism.objects.create(
            name='SuperMegaDeath',
            type='Virus',
            danger=5,
        )
        DetectedOrganism.objects.create(
            name='SuperMegaDeath',
            sample=s2,
            type=org2,
            confidence=80,
        )

    def test_easy(self):
        samples = parse_samples(Sample.objects.all())['samples']
        s1 = samples[0]
        self.assertEquals(s1['sample_name'], 'sample1')
        self.assertEquals(s1['danger'], 3)
        self.assertEquals(s1['origin'], 'room-4')
        self.assertEquals(s1['date'], '2019-10-11 18:14:00+00:00')
        s2 = samples[1]
        self.assertEquals(s2['sample_name'], 'sample2')
        self.assertEquals(s2['danger'], 5)
        self.assertEquals(s2['origin'], 'room-6')
        self.assertEquals(s2['date'], '2019-10-04 04:45:00+00:00')

    def test_load_all_samples(self):
        c = Client()
        response = c.get('/api/loadAllSamples/')
        data = json.loads(response.content)
        samples = data['samples']
        s1 = samples[0]
        self.assertEquals(s1['sample_name'], 'sample2')
        self.assertEquals(s1['danger'], 5)
        self.assertEquals(s1['origin'], 'room-6')
        self.assertEquals(s1['date'], '2019-10-04 04:45:00+00:00')
        s2 = samples[1]
        self.assertEquals(s2['sample_name'], 'sample1')
        self.assertEquals(s2['danger'], 3)
        self.assertEquals(s2['origin'], 'room-4')
        self.assertEquals(s2['date'], '2019-10-11 18:14:00+00:00')

    def test_load_0_samples(self):
        c = Client()
        response = c.get('/api/loadNSamples/', data={'n': 0})
        data = json.loads(response.content)
        samples = data['samples']
        self.assertEquals(len(samples), 0)

    def test_load_1_samples(self):
        c = Client()
        response = c.get('/api/loadNSamples/', data={'n': 1})
        data = json.loads(response.content)
        samples = data['samples']
        self.assertEquals(len(samples), 1)
        s1 = samples[0]
        self.assertEquals(s1['sample_name'], 'sample2')
        self.assertEquals(s1['danger'], 5)
        self.assertEquals(s1['origin'], 'room-6')
        self.assertEquals(s1['date'], '2019-10-04 04:45:00+00:00')

    def test_load_2_samples(self):
        c = Client()
        response = c.get('/api/loadNSamples/', data={'n': 2})
        data = json.loads(response.content)
        samples = data['samples']
        self.assertEquals(len(samples), 2)
        s1 = samples[0]
        self.assertEquals(s1['sample_name'], 'sample2')
        self.assertEquals(s1['danger'], 5)
        self.assertEquals(s1['origin'], 'room-6')
        self.assertEquals(s1['date'], '2019-10-04 04:45:00+00:00')
        s2 = samples[1]
        self.assertEquals(s2['sample_name'], 'sample1')
        self.assertEquals(s2['danger'], 3)
        self.assertEquals(s2['origin'], 'room-4')
        self.assertEquals(s2['date'], '2019-10-11 18:14:00+00:00')
