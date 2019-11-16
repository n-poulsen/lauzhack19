from .models import DetectedOrganism


def parse_samples(samples):
    """
    Parses samples into a dict of the following shape:

        {'samples': [
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
