from django.http import JsonResponse


def load_all_samples(request):
    return JsonResponse({
        'hello': 'YEAH!'
    })


def load_n_samples(request):
    return JsonResponse({
        'hello': 'YEAH!'
    })


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
