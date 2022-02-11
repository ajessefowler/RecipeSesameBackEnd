from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elasticsearch import Elasticsearch
from django.http import JsonResponse
from .recipeSearch import search
from .nlp import get_keywords

class MessageView(APIView):
    def post(self, request):
        return Response(search(get_keywords(request.data['message'])))
        