from django.http import HttpResponse, JsonResponse
from dict.models import Word
from django.core import serializers
import json

def search(request):
    keyword = request.GET['keyword']
    data = list(Word.objects.filter(esearch__startswith = keyword).values('esearch')[:10])
    return JsonResponse(data, safe=False)