from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from api.serializers import *
from app.models import *


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
        'get resume profile': '/get-resume-profile/<int:pk>/',
        'create or update resume profile': '/resume-profile/<int:pk>/',
        'create a resume experience': '/create-experience/<int:personal_detail_pk>/',
        'get a resume experience': '/get-experience/<int:pk>/',
        'update a resume experience': '/update-experience/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume experience': '/delete-experience/<int:pk>/<int:personal_detail_pk>/',
        'create a resume project': '/create-project/<int:personal_detail_pk>/',
        'get a resume project': '/get-project/<int:pk>/',
        'update a resume project': '/update-project/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume project': '/delete-project/<int:pk>/<int:personal_detail_pk>/',
        'create a resume education': '/create-education/<int:personal_detail_pk>/',
        'get a resume education': '/get-education/<int:pk>/',
        'update a resume education': '/update-education/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume education': '/delete-education/<int:pk>/<int:personal_detail_pk>/',
        'create a resume language': '/create-language/<int:personal_detail_pk>/',
        'get a resume language': '/get-language/<int:pk>/',
        'update a resume language': '/update-language/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume language': '/delete-language/<int:pk>/<int:personal_detail_pk>/',
        'create a resume reference': '/create-reference/<int:personal_detail_pk>/',
        'get a resume reference': '/get-reference/<int:pk>/',
        'update a resume reference': '/update-reference/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume reference': '/delete-reference/<int:pk>/<int:personal_detail_pk>/',
        'create a resume award': '/create-award/<int:personal_detail_pk>/',
        'get a resume award': '/get-award/<int:pk>/',
        'update a resume award': '/update-award/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume award': '/delete-award/<int:pk>/<int:personal_detail_pk>/',
        'create a resume organisation': '/create-organisation/<int:personal_detail_pk>/',
        'get a resume organisation': '/get-organisation/<int:pk>/',
        'update a resume organisation': '/update-organisation/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume organisation': '/delete-organisation/<int:pk>/<int:personal_detail_pk>/',
        'create a resume certificate': '/create-certificate/<int:personal_detail_pk>/',
        'get a resume certificate': '/get-certificate/<int:pk>/',
        'update a resume certificate': '/update-certificate/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume certificate': '/delete-certificate/<int:pk>/<int:personal_detail_pk>/',
        'create a resume interest': '/create-interest/<int:personal_detail_pk>/',
        'get a resume interest': '/get-interest/<int:pk>/',
        'update a resume interest': '/update-interest/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume interest': '/delete-interest/<int:pk>/<int:personal_detail_pk>/',
        'create a resume publication': '/create-publication/<int:personal_detail_pk>/',
        'get a resume publication': '/get-publication/<int:pk>/',
        'update a resume publication': '/update-publication/<int:pk>/<int:personal_detail_pk>/',
        'delete a resume publication': '/delete-publication/<int:pk>/<int:personal_detail_pk>/'
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
    
@api_view(['GET'])
def levels(request):
    levels = Levels.objects.all()
    if levels:
        serializer = levelsSerializer(levels, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def getProfile(request, pk):
    personal_detail = Personal_Details.objects.get(id=pk)
    if personal_detail:
        profile = Profile.objects.get(personal_detail=personal_detail)
        if profile.personal_detail.user == request.user:
            serializer = profileSerializer(profile, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
        
        
@api_view(['POST'])
def createUpdateProfile(request, pk):
    personal_detail = Personal_Details.objects.get(id=pk)
    if personal_detail:
        if Profile.objects.filter(personal_detail=pk).exists():
            profile = Profile.objects.get(personal_detail=pk)
            if profile.personal_detail.user == request.user:
                serializer = profileSerializer(instance = profile,  data=request.data)
            else:
                return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer_instance = serializer.save()
            serializer_instance.personal_detail = personal_detail
            serializer_instance.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_skill(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = skillSerializer(data=request.data, context={'request': request})
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
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createExperience(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = experienceSerializer(data=request.data, context={'request': request})
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
def getExperience(request, pk):
    user = User.objects.get(id=request.user.id)
    experience = Experience.objects.get(id=pk)
    if user and experience:
        if user == experience.personal_detail.user:
            serializer = skillSerializer(experience, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateExperience(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    experience = Experience.objects.get(id=pk, personal_detail=personal_detail)
    if user and experience and personal_detail:
            serializer = skillSerializer(experience, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteExperience(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    experience = Experience.objects.get(id=pk, personal_detail=personal_detail)
    if user and experience and personal_detail:
        experience.delete()
        return Response('Experience Deleted Successfully', status=status.HTTP_200_OK)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProject(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = projectSerializer(data=request.data, context={'request': request})
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
def getProject(request, pk):
    user = User.objects.get(id=request.user.id)
    project = Project.objects.get(id=pk)
    if user and project:
        if user == project.personal_detail.user:
            serializer = projectSerializer(project, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProject(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    project = Project.objects.get(id=pk, personal_detail=personal_detail)
    if user and project and personal_detail:
            serializer = projectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProject(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    project = Project.objects.get(id=pk, personal_detail=personal_detail)
    if user and project and personal_detail:
        project.delete()
        return Response('Project Deleted Successfully', status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createEducation(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = educationSerializer(data=request.data, context={'request': request})
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
def getEducation(request, pk):
    user = User.objects.get(id=request.user.id)
    education = Education.objects.get(id=pk)
    if user and education:
        if user == education.personal_detail.user:
            serializer = educationSerializer(education, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateEducation(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    education = Education.objects.get(id=pk, personal_detail=personal_detail)
    if user and education and personal_detail:
            serializer = educationSerializer(education, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteEducation(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    education = Education.objects.get(id=pk, personal_detail=personal_detail)
    if user and education and personal_detail:
        education.delete()
        return Response('Education Deleted Successfully', status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createLanguage(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = languageSerializer(data=request.data, context={'request': request})
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
def getLanguage(request, pk):
    user = User.objects.get(id=request.user.id)
    language = Language.objects.get(id=pk)
    if user and language:
        if user == language.personal_detail.user:
            serializer = languageSerializer(language, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateLanguage(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    language = Language.objects.get(id=pk, personal_detail=personal_detail)
    if user and language and personal_detail:
            serializer = languageSerializer(language, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteLanguage(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    language = Language.objects.get(id=pk, personal_detail=personal_detail)
    if user and language and personal_detail:
        language.delete()
        return Response('Language Deleted Successfully', status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createReference(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = referenceSerializer(data=request.data, context={'request': request})
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
def getReference(request, pk):
    user = User.objects.get(id=request.user.id)
    reference = Reference.objects.get(id=pk)
    if user and reference:
        if user == reference.personal_detail.user:
            serializer = referenceSerializer(reference, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateReference(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    reference = Reference.objects.get(id=pk, personal_detail=personal_detail)
    if user and reference and personal_detail:
            serializer = referenceSerializer(reference, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteReference(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    reference = Reference.objects.get(id=pk, personal_detail=personal_detail)
    if user and reference and personal_detail:
        reference.delete()
        return Response('Reference Deleted Successfully', status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAward(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = awardSerializer(data=request.data, context={'request': request})
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
def getAward(request, pk):
    user = User.objects.get(id=request.user.id)
    award = Award.objects.get(id=pk)
    if user and award:
        if user == award.personal_detail.user:
            serializer = awardSerializer(award, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateAward(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    award = Award.objects.get(id=pk, personal_detail=personal_detail)
    if user and award and personal_detail:
            serializer = awardSerializer(award, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAward(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    award = Award.objects.get(id=pk, personal_detail=personal_detail)
    if user and award and personal_detail:
        award.delete()
        return Response('Reference Deleted Successfully', status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createOrganisation(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = organisationSerializer(data=request.data, context={'request': request})
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
def getOrganisation(request, pk):
    user = User.objects.get(id=request.user.id)
    organisation = Organisation.objects.get(id=pk)
    if user and organisation:
        if user == organisation.personal_detail.user:
            serializer = organisationSerializer(organisation, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrganisation(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    organisation = Organisation.objects.get(id=pk, personal_detail=personal_detail)
    if user and organisation and personal_detail:
            serializer = organisationSerializer(organisation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteOrganisation(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    organisation = Organisation.objects.get(id=pk, personal_detail=personal_detail)
    if user and organisation and personal_detail:
        organisation.delete()
        return Response('Reference Deleted Successfully', status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCertificate(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = certificateSerializer(data=request.data, context={'request': request})
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
def getCertificate(request, pk):
    user = User.objects.get(id=request.user.id)
    certificate = Certificate.objects.get(id=pk)
    if user and certificate:
        if user == certificate.personal_detail.user:
            serializer = certificateSerializer(certificate, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCertificate(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    certificate = Certificate.objects.get(id=pk, personal_detail=personal_detail)
    if user and certificate and personal_detail:
            serializer = certificateSerializer(certificate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCertificate(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    certificate = Certificate.objects.get(id=pk, personal_detail=personal_detail)
    if user and certificate and personal_detail:
        certificate.delete()
        return Response('Reference Deleted Successfully', status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createInterest(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = interestSerializer(data=request.data, context={'request': request})
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
def getInterest(request, pk):
    user = User.objects.get(id=request.user.id)
    interest = Interest.objects.get(id=pk)
    if user and interest:
        if user == interest.personal_detail.user:
            serializer = interestSerializer(interest, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateInterest(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    interest = Interest.objects.get(id=pk, personal_detail=personal_detail)
    if user and interest and personal_detail:
            serializer = interestSerializer(interest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteInterest(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    interest = Interest.objects.get(id=pk, personal_detail=personal_detail)
    if user and interest and personal_detail:
        interest.delete()
        return Response('Reference Deleted Successfully', status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPublication(request, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details.objects.get(user=user, id=personal_detail_pk)
    serializer = publicationSerializer(data=request.data, context={'request': request})
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
def getPublication(request, pk):
    user = User.objects.get(id=request.user.id)
    publication = Publication.objects.get(id=pk)
    if user and publication:
        if user == publication.personal_detail.user:
            serializer = publicationSerializer(publication, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePublication(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    publication = Publication.objects.get(id=pk, personal_detail=personal_detail)
    if user and publication and personal_detail:
            serializer = publicationSerializer(publication, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePublication(request, pk, personal_detail_pk):
    user = User.objects.get(id=request.user.id)
    personal_detail = Personal_Details(user=user, id=personal_detail_pk)
    publication = Publication.objects.get(id=pk, personal_detail=personal_detail)
    if user and publication and personal_detail:
        publication.delete()
        return Response('Reference Deleted Successfully', status=status.HTTP_200_OK)
