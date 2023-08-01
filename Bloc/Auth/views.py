from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['POST'])
def register(request):
    data = {'message': 'Hello, this is a sample API response using @api_view!'}
    return Response(data)
