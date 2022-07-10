from cgitb import lookup
import django_filters
from .models import Job

class Jopfilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    description=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude=['image','slug','owner','puplishat']
