from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from api.serializers import UserSerializer, userProfileSerializer, ResumeSerializer, skillSerializer, addSkillSerializer, feedbackSerializer
from app.models import User, Personal_Details, Skills, Feedback


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
        'register': '/register/',
        'login': '/login/',
        'logout': '/logout',
        'create a resume': '/create-resume/<int:pk>/',
        'create a resume feeback': 'create-feeback/<int:pk>/',
        'resume feedbacks': 'resume/<int:pk>/feedbacks/',
    }
    return Response(api_urls)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = None
        if email:
            try:
                user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def userProfileUpdate(request):
    user = User.objects.get(id=request.user.id)
    serializer = userProfileSerializer(user,  data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAccount(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return Response('User Deleted Successfully', status=status.HTTP_200_OK)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getResume(request, pk):
    user = User.objects.get(id=request.user.id)
    resume = Personal_Details.objects.get(id=pk, user=user)
    if user and resume:
        if user == request.user:
            serializer = ResumeSerializer(resume, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteResume(request, pk):
    user = User.objects.get(id=request.user.id)
    resume = Personal_Details.objects.get(id=pk, user=user)
    if user and resume:
        if user == request.user:
            resume.delete()
            return Response('Resume Deleted Successfully', status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def createFeedback(request, pk):
    personal_detail = Personal_Details.objects.get(id=pk)
    serializer = feedbackSerializer(data=request.data, context={'personal_detail': personal_detail})
    if personal_detail:
        if serializer.is_valid():
            serializer_instance = serializer.save()
            serializer_instance.personal_detail = personal_detail
            serializer_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def resumeFeedbacks(request, pk):
    personal_detail = Personal_Details.objects.get(id=pk)
    if personal_detail:
        feedbacks = Feedback.objects.filter(personal_detail=personal_detail)
        serializer = feedbackSerializer(feedbacks, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSkill(request, pk):
    user = User.objects.get(id=request.user.id)
    skill = Skills.objects.get(id=pk)
    if user and skill:
        if user == skill.personal_detail.user:
            serializer = skillSerializer(skill, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
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
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteSkill(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    skill = Skills.objects.get(id=pk, personal_detail=personal_detail)
    if user and skill and personal_detail:
        skill.delete()
        return Response('Skill Deleted Successfully', status=status.HTTP_200_OK)