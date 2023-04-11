from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, read_only='True')
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    email = serializers.CharField(
        style={'input_type': 'email'}, write_only=True
    )
    groups = serializers.CharField(
        style={'input_type': 'text'}, write_only=True
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'groups']
        
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password'])
        )
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'id', 'name']

#User Management
class user_type_serializer(serializers.ModelSerializer):
    class Meta:
        model=user_type
        fields=['id','user_type_name','createdDate','modifiedDate']

class user_account_serializer(serializers.ModelSerializer):
    
    user_type_id=serializers.ReadOnlyField(source='user_type_id.id')
    class Meta:
        model=user_account
        fields=['id','user_type_id','first_name','last_name','experience_level','resume','join_type','profile_photo','phone_number','email_address',
                'password','createdDate','modifiedDate']
        
class user_log_serializer(serializers.ModelSerializer):

    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_log
        fields=['user_account_id','last_login_date','last_job_apply_date','createdDate','modifiedDate']
        
#Company Porfile
class business_stream_serializer(serializers.ModelSerializer):
    class Meta:
        model=business_stream
        fields=['id','business_stream_name']

class company_serializer(serializers.ModelSerializer):
    
    business_stream_id=serializers.ReadOnlyField(source='business_stream_id.id')
    class Meta:
        model=company
        fields=['id','company_name','profile_description','business_stream_id','establishment_date','company_website_url','createdDate','modifiedDate']

class company_image_serializer(serializers.ModelSerializer):

    company_id=serializers.ReadOnlyField(source='company_id.id')
    class Meta:
        model=company_image
        fields=['id','company_id','company_image','createdDate','modifiedDate']

#Seeker Profile Builder
class user_education_serializer(serializers.ModelSerializer):
   
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_education
        fields=['id','user_account_id','education','univesity','course','speclalization','course_type','course_duration','completion_date','grading_system',
                'marks','createdDate','modifiedDate']
        
class user_socialprofile_serializer(serializers.ModelSerializer):
   
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_socialprofile
        fields=['id','social_profile','url','description',
                'user_account_id','createdDate','modifiedDate']

class user_certification_serializer(serializers.ModelSerializer):
   
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_certification
        fields=['id','user_account_id','certification_name','certification_completion_id','certification_url',
                'certification_validity_from_year','certification_validity_from_month','certification_validity_to_year','certification_validity_to_month'
                ,'certification_will_expire','createdDate','modifiedDate']
        
class user_projects_serializer(serializers.ModelSerializer):
   
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_projects
        fields=['id','user_account_id','project_title','tag_this_project_with_your_Education','client_name',
                'project_staus','worked_from_year','worked_from_month','project_details','createdDate','modifiedDate']
        
class user_workstatus_serializer(serializers.ModelSerializer):
   
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_workstatus
        fields=['id','user_account_id','work_title','url','duration_from_year','duration_from_month','duration_to_year','duration_to_month','working_staus','description','createdDate','modifiedDate']
        
class user_personalinfo_serializer(serializers.ModelSerializer):
    
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_personalinfo
        fields=['user_account_id','current_industry','preferred_shift','preferred_work_location','expected_salary','gender','date_of_birth'
                ,'differently_abled','career_break','reasonforbreak','work_permit_for_any_countries','permanent_address',
                'hometown','pincode','language','createdDate','modifiedDate']
        
class seeker_skill_set_serializer(serializers.ModelSerializer):
    
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    skill_set_id=serializers.ReadOnlyField(source='skill_set_id.id')
    class Meta:
        model=seeker_skill_set
        fields=['id','user_account_id','skill_set_id','skill_level','createdDate','modifiedDate']

class employment_serializer(serializers.ModelSerializer):
    
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=employment
        fields=['id','user_account_id','employment_type','is_current_employment','total_experince_year','total_experince_month','joining_date_month','joining_date_year',
                'current_company_name','current_designation','joining_date',
                'current_salary','skills_used','job_profile','notice_period','createdDate','modifiedDate']
        
class researchpublication_serializer(serializers.ModelSerializer):
    
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=researchpublication
        fields=['id','user_account_id','title','url','published_on_month','published_on_year','createdDate','modifiedDate']

class presentation_serializer(serializers.ModelSerializer):
    
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=presentation
        fields=['id','user_account_id','presentation_title','url','description','createdDate','modifiedDate']

class patent_serializer(serializers.ModelSerializer):
    
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=patent
        fields=['id','user_account_id','title','url','patent_office','status','application_number','issue_date_month','issue_date_year'
                    ,'description','createdDate','modifiedDate']

class user_skills_serializer(serializers.ModelSerializer):
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    class Meta:
        model=user_skills
        fields=['id','user_account_id','skill_name','software_version','last_used','experience_year','experience_month','createdDate','modifiedDate']

#Job Post Management
class job_post_activity_serializer(serializers.ModelSerializer):
    
    user_account_id=serializers.ReadOnlyField(source='user_account_id.id')
    job_post_id=serializers.ReadOnlyField(source='job_post.id')
    class Meta:
        model=job_post_activity
        fields=['id','job_post_id','user_account_id','apply_date','createdDate','modifiedDate']

class job_post_skill_set_serializer(serializers.ModelSerializer):
    
    skill_set_id=serializers.ReadOnlyField(source='skill_set_id.id')
    job_post_id=serializers.ReadOnlyField(source='job_post_id.id')
    class Meta:
        model=job_post_skill_set
        fields=['id','skill_set_id','job_post_id','skill_level','createdDate','modifiedDate']

class job_type_serializer(serializers.ModelSerializer):
    class Meta:
        model=job_type
        fields=['id','job_type','createdDate','modifiedDate']

class job_post_serializer(serializers.ModelSerializer):
    posted_by_id=serializers.ReadOnlyField(source='posted_by_id.id')
    job_type_id=serializers.ReadOnlyField(source='job_type_id.id')
    company_id=serializers.ReadOnlyField(source='company_id.id')
    class Meta:
        model=job_post
        fields=['id','posted_by_id','job_type_id','company_id','is_company_name_hidden','created_date',
                'job_description','is_active','job_location_id','createdDate','modifiedDate']

class job_location_serializer(serializers.ModelSerializer):
    class Meta:
        model=job_location
        fields=['id','street_address','city','state','country','zip','createdDate','modifiedDate']


