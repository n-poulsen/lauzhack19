from django.http import JsonResponse, HttpResponse
from .models import Sample
from .helper import parse_samples


def load_all_samples(request):
    """
    Returns all samples that are in the dataset, ordered by descending date, in the following format:
        {'samples': [
            'sample_name': string,
            'danger': int,
            'origin': string,
            'date': string,
        ]}

    :param request: the user request
    :return: JsonResponse. A JSON Response containing all samples.
    """
    return JsonResponse(parse_samples(Sample.objects.order_by('date')))


def load_n_samples(request):
    """
    Returns all samples that are in the dataset, ordered by descending date, in the following format:
        {'samples': [
            'sample_name': string,
            'danger': int,
            'origin': string,
            'date': string,
        ]}

    :param request: the user request
    :return: JsonResponse. A JSON Response containing all samples.
    """
    try:
        # Get user tags
        n = int(request.GET.get('n'))
        return JsonResponse(parse_samples(Sample.objects.order_by('date')[:n]))
    except KeyError:
        print('error')
        return HttpResponse('Failure. JSON parse failed.')


def load_sample(request):
    return JsonResponse({
        'hello': 'YEAH!'
    })


def load_type(request):
    return JsonResponse({
        'hello': 'YEAH!'
    })


def add_sample(request):
    return JsonResponse({
        'hello': 'YEAH!'
    })
