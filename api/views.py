from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import UserSerializer, userProfileSerializer
from app.models import User 

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'get current user':'/current-user/',
        'update current user profile': '/update-account/',
        'delete current account': '/delete-account/',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def userProfileUpdate(request):
    user = User.objects.get(id=request.user.id)
    serializer = userProfileSerializer(user,  data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteAccount(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return Response('User Deleted Successfully')


