from rest_framework.serializers import ModelSerializer
from app.models import *
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class userProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Personal_Details
        fields = '__all__'

class skillSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class experienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class projectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class educationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class languageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class referenceSerializer(ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'

class feedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ('time_created',)

class levelsSerializer(ModelSerializer):
    class Meta:
        model = Levels
        fields = '__all__'

class profileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


