from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Sample
from .helper import parse_samples, parse_full_sample, process_sample


def load_all_samples(request):
    """
    Returns all samples that are in the dataset, ordered by descending date, in the following format:
        {'samples': [
            'sample_name': string,
            'danger': int,
            'origin': string,
            'date': string,
        ]}

    :param request: GET Request. The user request
    :return: JsonResponse. A JSON Response containing all samples.
    """
    return JsonResponse(parse_samples(Sample.objects.order_by('date')))


def load_n_samples(request):
    """
    Returns the N most recent samples in the dataset, where N is a parameter, in the following format:
        {'samples': [
            'sample_name': string,
            'danger': int,
            'origin': string,
            'date': string,
        ]}

    :param request: GET Request. The user request
    :return: JsonResponse. A JSON Response containing all samples.
    """
    try:
        # Get user tags
        n = int(request.GET.get('n'))
        return JsonResponse(parse_samples(Sample.objects.order_by('date')[:n]))
    except KeyError:
        return HttpResponse('Failure. Attribute parse failed.')


def load_sample(request):
    """
    Returns the sample with the name passed as a parameter, in the following format. Returns an empty dict if the sample
    could not be found.
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

    :param request: the user request
    :return: JsonResponse. A JSON Response containing all samples.
    """
    try:
        # Get user tags
        sample_name = request.GET.get('sample')
        try:
            sample = Sample.objects.get(name=sample_name)
            return JsonResponse(parse_full_sample(sample))
        except ObjectDoesNotExist:
            return JsonResponse({})
    except KeyError:
        return HttpResponse('Failure. Attribute parse failed.')


def load_origin(request):
    """
    Returns all samples with the origin passed as a parameter, in the following format. Returns an empty dict if the
    sample could not be found.
        {'samples': [
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
        ]}

    :param request: the user request
    :return: JsonResponse. A JSON Response containing all samples.
    """
    try:
        # Get user tags
        sample_name = request.GET.get('origin')
        samples = Sample.objects.filter(origin=sample_name)
        samples_found = []
        for sample in samples:
            samples_found.append(parse_full_sample(sample))
        return JsonResponse({'samples': samples_found})
    except KeyError:
        return HttpResponse('Failure. Attribute parse failed.')


def add_sample(request):
    """
    Adds a sample to the database, given the url to a sample file.

    :param request: the user request
    :return: JsonResponse. A JSON Response containing all samples.
    """
    try:
        # Get user tags
        url = request.GET.get('url')
        s = process_sample(url)
        if s is None:
            return HttpResponse('Failure. Sample Name already taken.')
        else:
            return JsonResponse(parse_full_sample(s))
    except KeyError:
        return HttpResponse('Failure. Attribute parse failed.')
