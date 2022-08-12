from rest_framework import viewsets
from rest_framework.response import Response


class HelloViewSet(viewsets.ViewSet):

    def list(self, request):
        data = { 'response': 200 }
        return Response(data)
