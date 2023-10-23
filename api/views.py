from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import UserSerializer, userProfileSerializer, ResumeSerializer, skillSerializer
from app.models import User, Personal_Details, Skills


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'get current user':'/current-user/',
        'update current user profile': '/update-account/',
        'delete current account': '/delete-account/',
        'create resume': '/create-resume/',
        'get a resume': 'get-resume/<pk:pk>/',
        'delete a resume': 'delete-resume/<int:pk>/',
        'get a resume skil': 'get-skill/<int:pk>/',
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
@permission_classes([IsAuthenticated])
def deleteAccount(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return Response('User Deleted Successfully')

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def createResume(request):
#     user = User.objects.get(id=request.user.id)
#     serializer = ResumeSerializer(data=request.data)
#     print(serializer.Meta.model.full_name)
#     print(request.data['full_name'])
#     if user:
#         if serializer.is_valid():
#             serializer.Meta.model.full_name = request.data['full_name']
#             serializer.Meta.model.email = user.email
#             serializer.save()
#             return Response(serializer.data)
  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getResume(request, pk):
    user = User.objects.get(id=request.user.id)
    resume = Personal_Details.objects.get(id=pk, user=user)
    if user and resume:
        if user == request.user:
            serializer = ResumeSerializer(resume, many = False)
            return Response(serializer.data)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteResume(request, pk):
    user = User.objects.get(id=request.user.id)
    resume = Personal_Details.objects.get(id=pk, user=user)
    if user and resume:
        if user == request.user:
            resume.delete()
            return Response('Resume Deleted Successfully')
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSkill(request, pk):
    user = User.objects.get(id=request.user.id)
    skill = Skills.objects.get(id=pk)
    if user and skill:
        if user == skill.personal_detail.user:
            serializer = skillSerializer(skill, many = False)
            return Response(serializer.data)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateSkill(request, pk):
    user = User.objects.get(id=request.user.id)
    skill = Skills.objects.get(id=pk)
    if user and skill:
        if user == skill.personal_detail.user:
            serializer = skillSerializer(skill, many = False)
            return Response(serializer.data)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
