from django.contrib import admin
from .models import Sample, Organism, DetectedOrganism

# Register your models here.
admin.site.register(Sample)
admin.site.register(Organism)
admin.site.register(DetectedOrganism)
