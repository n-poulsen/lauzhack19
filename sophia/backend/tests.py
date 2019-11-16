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
        org3 = Organism.objects.create(
            name='UltraDeath',
            type='Bacteria',
            danger=10,
        )
        org4 = Organism.objects.create(
            name='PetaDeath',
            type='Bacteria',
            danger=100,
        )
        DetectedOrganism.objects.create(
            name='SuperMegaDeath',
            sample=s2,
            type=org2,
            confidence=80,
        )
        DetectedOrganism.objects.create(
            name='UltraDeath',
            sample=s2,
            type=org3,
            confidence=40,
        )
        DetectedOrganism.objects.create(
            name='PetaDeath',
            sample=s2,
            type=org4,
            confidence=90,
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
        self.assertEquals(s2['danger'], 100)
        self.assertEquals(s2['origin'], 'room-6')
        self.assertEquals(s2['date'], '2019-10-04 04:45:00+00:00')

    def test_load_all_samples(self):
        c = Client()
        response = c.get('/api/loadAllSamples/')
        data = json.loads(response.content)
        samples = data['samples']
        s1 = samples[0]
        self.assertEquals(s1['sample_name'], 'sample2')
        self.assertEquals(s1['danger'], 100)
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
        self.assertEquals(s1['danger'], 100)
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
        self.assertEquals(s1['danger'], 100)
        self.assertEquals(s1['origin'], 'room-6')
        self.assertEquals(s1['date'], '2019-10-04 04:45:00+00:00')
        s2 = samples[1]
        self.assertEquals(s2['sample_name'], 'sample1')
        self.assertEquals(s2['danger'], 3)
        self.assertEquals(s2['origin'], 'room-4')
        self.assertEquals(s2['date'], '2019-10-11 18:14:00+00:00')

    def test_load_sample_1(self):
        c = Client()
        response = c.get('/api/loadSample/', data={'sample': 'sample1'})
        s = json.loads(response.content)
        self.assertEquals(s['sample_name'], 'sample1')
        self.assertEquals(s['danger'], 3)
        self.assertEquals(s['origin'], 'room-4')
        self.assertEquals(s['date'], '2019-10-11 18:14:00+00:00')
        self.assertEquals(len(s['organisms_found']), 1)
        b = s['organisms_found'][0]
        self.assertEquals(b['name'], 'SuperDeath')
        self.assertEquals(b['type'], 'Virus')
        self.assertEquals(b['confidence'], 50)
        self.assertEquals(b['danger'], 3)

    def test_load_sample_2(self):
        c = Client()
        response = c.get('/api/loadSample/', data={'sample': 'sample2'})
        s = json.loads(response.content)
        self.assertEquals(s['sample_name'], 'sample2')
        self.assertEquals(s['danger'], 100)
        self.assertEquals(s['origin'], 'room-6')
        self.assertEquals(s['date'], '2019-10-04 04:45:00+00:00')
        self.assertEquals(len(s['organisms_found']), 3)
        b = s['organisms_found'][0]
        self.assertEquals(b['name'], 'SuperMegaDeath')
        self.assertEquals(b['type'], 'Virus')
        self.assertEquals(b['confidence'], 80)
        self.assertEquals(b['danger'], 5)
        b = s['organisms_found'][1]
        self.assertEquals(b['name'], 'UltraDeath')
        self.assertEquals(b['type'], 'Bacteria')
        self.assertEquals(b['confidence'], 40)
        self.assertEquals(b['danger'], 10)
        b = s['organisms_found'][2]
        self.assertEquals(b['name'], 'PetaDeath')
        self.assertEquals(b['type'], 'Bacteria')
        self.assertEquals(b['confidence'], 90)
        self.assertEquals(b['danger'], 100)

    def test_load_origin_1(self):
        c = Client()
        response = c.get('/api/loadOrigin/', data={'origin': 'room-4'})
        s = json.loads(response.content)['samples']
        self.assertEquals(len(s), 1)
        s = s[0]
        self.assertEquals(s['sample_name'], 'sample1')
        self.assertEquals(s['danger'], 3)
        self.assertEquals(s['origin'], 'room-4')
        self.assertEquals(s['date'], '2019-10-11 18:14:00+00:00')
        self.assertEquals(len(s['organisms_found']), 1)
        b = s['organisms_found'][0]
        self.assertEquals(b['name'], 'SuperDeath')
        self.assertEquals(b['type'], 'Virus')
        self.assertEquals(b['confidence'], 50)
        self.assertEquals(b['danger'], 3)

    def test_load_origin_2(self):
        s = Sample.objects.create(
            name='sample1',
            origin='room-4',
            date=datetime.datetime(2019, 10, 12, 18, 14, tzinfo=self.tzone),
        )
        org = Organism.objects.create(
            name='NiceBacteria',
            type='Bacteria',
            danger=0,
        )
        DetectedOrganism.objects.create(
            name='NiceBacteria',
            sample=s,
            type=org,
            confidence=99,
        )
        c = Client()
        response = c.get('/api/loadOrigin/', data={'origin': 'room-4'})
        samples = json.loads(response.content)['samples']
        self.assertEquals(len(samples), 2)
        s = samples[0]
        self.assertEquals(s['sample_name'], 'sample1')
        self.assertEquals(s['danger'], 3)
        self.assertEquals(s['origin'], 'room-4')
        self.assertEquals(s['date'], '2019-10-11 18:14:00+00:00')
        self.assertEquals(len(s['organisms_found']), 1)
        b = s['organisms_found'][0]
        self.assertEquals(b['name'], 'SuperDeath')
        self.assertEquals(b['type'], 'Virus')
        self.assertEquals(b['confidence'], 50)
        self.assertEquals(b['danger'], 3)
        s = samples[1]
        self.assertEquals(s['sample_name'], 'sample1')
        self.assertEquals(s['danger'], 0)
        self.assertEquals(s['origin'], 'room-4')
        self.assertEquals(s['date'], '2019-10-12 18:14:00+00:00')
        self.assertEquals(len(s['organisms_found']), 1)
        b = s['organisms_found'][0]
        self.assertEquals(b['name'], 'NiceBacteria')
        self.assertEquals(b['type'], 'Bacteria')
        self.assertEquals(b['confidence'], 99)
        self.assertEquals(b['danger'], 0)

    def test_add_sample_1(self):
        c = Client()
        response = c.get('/api/addSample/', data={'url': 'sample3.file'})
        s = json.loads(response.content)
        self.assertEquals(s['sample_name'], 'sample3')
