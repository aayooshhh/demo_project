from rest_framework.views import APIView
from rest_framework.response import Response

class FirstAPI(APIView):
    def get(self, request):
        return Response(data={'detail':'This is modified GET method 1'})
