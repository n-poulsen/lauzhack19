from django.urls import path
from .views import load_all_samples, load_n_samples, load_sample, load_type, add_sample

urlpatterns = [
    path('loadAllSamples/', load_all_samples),
    path('loadNSamples/', load_n_samples),
    path('loadSample/', load_sample),
    path('loadType/', load_type),
    path('addSample/', add_sample),
]
