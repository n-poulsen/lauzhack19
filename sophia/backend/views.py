from django.http import JsonResponse, HttpResponse
import json


def load_content(request):
    return JsonResponse({
                'hello': 'YEAH!'
            })
