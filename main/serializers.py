from rest_framework import serializers
from .models import * 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']




# class FamilySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Family
#         fields = '__all__'

# class CareerContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CareerContact
#         fields = '__all__'

# class PriorCareerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PriorCareer
#         fields = '__all__'

# class AwardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Award
#         fields = '__all__'

# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = '__all__'

# class LanguageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Language
#         fields = '__all__'

# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = '__all__'


# class CandidateDetailSerializer(serializers.ModelSerializer):
#     families = FamilySerializer(many=True, read_only=True)
#     career_contacts = CareerContactSerializer(many=True, read_only=True)
#     prior_careers = PriorCareerSerializer(many=True, read_only=True)
#     awards = AwardSerializer(many=True, read_only=True)
#     educations = EducationSerializer(many=True, read_only=True)
#     languages = LanguageSerializer(many=True, read_only=True)
#     skills = SkillSerializer(many=True, read_only=True)
#     image_url = serializers.SerializerMethodField()


#     class Meta:
#         model = Anket
#         fields = '__all__'

#     def get_image_url(self, obj):
#         if obj.image and obj.image.photo:
#             return obj.image.photo.url 
#         return None 

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         # Add any custom processing if necessary.
#         return representation

# class InterviewGetSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username') 
#     department = serializers.CharField(source='user.profile.department') 
#     title = serializers.CharField(source='user.profile.title') 
#     first_name = serializers.CharField(source='user.profile.first_name') 
#     last_name = serializers.CharField(source='user.profile.last_name') 

#     class Meta:
#         model = Interview
#         fields = ['id', 'username', 'department', 'title', 'first_name', 'last_name', 'level', 'status', 'interviewed_date', 'main_overall', 'is_completed', 'is_scheduled', 'is_final', 'conclution_points']


