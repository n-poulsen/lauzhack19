from django.urls import path
from .views import load_all_samples, load_n_samples, load_sample, load_origin, add_sample

urlpatterns = [
    path('loadAllSamples/', load_all_samples),
    path('loadNSamples/', load_n_samples),
    path('loadSample/', load_sample),
    path('loadOrigin/', load_origin),
    path('addSample/', add_sample),
]
