from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import UserSerializer, userProfileSerializer, ResumeSerializer, skillSerializer, addSkillSerializer
from app.models import User, Personal_Details, Skills


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'get current user':'/current-user/',
        'update current user profile': '/update-account/',
        'delete current account': '/delete-account/',
        'create resume': '/create-resume/',
        'get a resume': '/get-resume/<pk:pk>/',
        'delete a resume': '/delete-resume/<int:pk>/',
        'create a skill': '/create-skill/<int:personal_detail_pk>/',
        'get a resume skil': '/get-skill/<int:pk>/',
        'update a resume skill': '/update-skill/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume skill': '/delete-skill/<int:pk>/<int:personal_detail_pk>/',
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createResume(request):
    user = User.objects.get(id=request.user.id)
    serializer = ResumeSerializer(data=request.data)
    if user:
        if serializer.is_valid():
            serializer_instance = serializer.save()
            serializer_instance.user = user
            serializer_instance.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

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
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_skill(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = addSkillSerializer(data=request.data, context={'request': request})
    if user and personal_detail:
        if request.user == personal_detail.user:        
            if serializer.is_valid():
                serializer_instance = serializer.save()
                serializer_instance.personal_detail = personal_detail
                serializer_instance.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

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
def updateSkill(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    skill = Skills.objects.get(id=pk, personal_detail=personal_detail)
    if user and skill and personal_detail:
            serializer = skillSerializer(skill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteSkill(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    skill = Skills.objects.get(id=pk, personal_detail=personal_detail)
    if user and skill and personal_detail:
        skill.delete()
        return Response('Skill Deleted Successfully')
        
{
    "skill_level": 1,
   "skill_name": "Django",
"personal_detail": 1
}
