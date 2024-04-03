from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 

@api_view(['GET']) 
def health_check(request): 
    return Response({'msg': 'application is running!'}, status=status.HTTP_200_OK)

@api_view(['GET']) 
def fetch_fact(request): 
    return Response({'success': True}, status=status.HTTP_200_OK) 

@api_view(['GET']) 
def get_fact(request): 
    return Response({'error': 'no_task_has_been_queued_yet'})