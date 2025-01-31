from django.shortcuts import render
from django.http import JsonResponse
import redis
from django.conf import settings

# Connect to Redis
cache = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

def index(request):
    try:
        visits = cache.get('visits')
        if visits is None:
            visits = 0
            cache.set('visits', visits)
        visits = int(visits) + 1
        cache.set('visits', visits)
        return JsonResponse({'message': f'Hello, you have visited {visits} times!'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
