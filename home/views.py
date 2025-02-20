from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView (APIView):
    
    def get(self, request, format=None):
        # print($request)
        home = "This is home API"
        return Response(home)
    
    def post(self, request, format=None):
        # print($request)
        home = "This is home POST API"
        return Response(home)
    