from .models import Sample, Organism, DetectedOrganism
import random
import datetime

RANDOM_VIRUSES = ['TastyVirus', 'CoolVirus', 'DeathVirus', 'DarthVirus']
DANGER_VIRUS = [0, 0, 1, 100]
RANDOM_BACTERIAS = ['Nice Bacteria', 'SuperDeath', 'MegaDeath', 'GigaDeath']
DANGER_BACTERIA = [0, 1, 5, 10]


def parse_samples(samples):
    """
    Parses samples into a dict of the following shape:

        {   'samples': [
            'sample_name': string,
            'danger': int,
            'origin': string,
            'date': string,
        ]}

    :param samples: QuerySet. The QuerySet of samples that need to be parsed.
    :return: dict. The parsed samples
    """
    parsed = []
    for sample in samples:
        sample_organisms = DetectedOrganism.objects.filter(sample=sample)
        max_danger = 0
        for sample_org in sample_organisms:
            org = sample_org.type
            if org.danger > max_danger:
                max_danger = org.danger
        parsed.append({
            'sample_name': sample.name,
            'danger': max_danger,
            'origin': sample.origin,
            'date': str(sample.date),
        })
    return {'samples': parsed}


def parse_full_sample(sample):
    """
    Parses samples into a dict of the following shape:

        {   'sample_name': string,
            'danger': int,
            'origin': string,
            'date': string,
            organisms_found: [{
                'name': string
                'type': string virus, bacteria, ...
                'confidence': int (between 0 and 100)
                'danger': int
            }]
        }

    :param sample: Sample. The Sample instance to parse.
    :return: dict. The parsed samples
    """
    sample_organisms = DetectedOrganism.objects.filter(sample=sample)
    organisms_found = []
    max_danger = 0
    for sample_org in sample_organisms:
        org = sample_org.type
        if org.danger > max_danger:
            max_danger = org.danger
        organisms_found.append({
            'name': org.name,
            'type': org.type,
            'confidence': sample_org.confidence,
            'danger': org.danger,
        })
    return {
        'sample_name': sample.name,
        'danger': max_danger,
        'origin': sample.origin,
        'date': str(sample.date),
        'organisms_found': organisms_found,
    }


def add_sample(name, origin, date):
    return Sample.objects.create(
        name=name,
        origin=origin,
        date=date,
    )


def add_organism(name, org_type, danger):
    return Organism.objects.create(
        name=name,
        type=org_type,
        danger=danger,
    )


def add_detected(name, sample, organism, confidence):
    return DetectedOrganism.objects.create(
        name=name,
        sample=sample,
        type=organism,
        confidence=confidence,
    )


def generate_sample(name):
    origin = 'room' + str(random.randint(1, 31))
    s = add_sample(name, origin, datetime.datetime.now())
    num_virus = random.randint(0, 4)
    num_bacteria = random.randint(0, 4)
    viruses = random.sample(range(4), num_virus)
    bacteria = random.sample(range(4), num_bacteria)
    for v in viruses:
        org_name = RANDOM_VIRUSES[v]
        danger = DANGER_VIRUS[v]
        if Organism.objects.filter(name=org_name).count() == 0:
            org = add_organism(org_name, 'Virus', danger)
        else:
            org = Organism.objects.get(name=org_name)
        add_detected(org_name, s, org, random.randint(80, 100))
    for b in bacteria:
        org_name = RANDOM_BACTERIAS[b]
        danger = DANGER_BACTERIA[b]
        if Organism.objects.filter(name=org_name).count() == 0:
            org = add_organism(org_name, 'Bacteria', danger)
        else:
            org = Organism.objects.get(name=org_name)
        add_detected(org_name, s, org, random.randint(80, 100))
    return s


def process_sample(url):
    sample_name = url.split('.')[0]
    if Sample.objects.filter(name=sample_name).count() == 1:
        return None
    else:
        return generate_sample(sample_name)
