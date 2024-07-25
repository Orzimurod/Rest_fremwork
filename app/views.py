from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def users_view(request):
    users = [{'name': 'Orzimurod', 'age': '20'}, {'name': 'Shahzod', 'age': '26'}]
    return Response(users)
