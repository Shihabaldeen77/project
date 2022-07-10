from .models import Job
from .serilaizers import Jobserilazer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def joblistapi(request):
    all_job=Job.objects.all()
    date=Jobserilazer(all_job,many=True).data
    return Response({'data':date})





@api_view(['GET'])
def joplistapiid(request,id):
    jobl=Job.objects.get(id=id)
    date=Jobserilazer(jobl).data
    return Response({'data':date})