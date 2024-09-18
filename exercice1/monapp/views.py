from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def numbers(request):
    data = request.data.get('numbers', [])
    pairs = [num for num in data if num % 2 == 0]
    return Response({'pairs': pairs})

@api_view(['POST'])
def sum_numbers(request):
    num1 = request.data.get('num1')
    num2 = request.data.get('num2')
    total = num1 + num2
    return Response({'sum': total})
