from django.db import models

# Create your models here.

#User Management
class user_type(models.Model):
    user_type_name=models.CharField(max_length=20)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class user_account(models.Model):
    user_type_id = models.ForeignKey('user_type',related_name='usertype', on_delete=models.CASCADE,default=None)
    first_name=models.CharField(max_length=122)  
    last_name=models.CharField(max_length=122) 
    experience_level=models.CharField(max_length=122) 
    resume=models.FileField()
    join_type=models.CharField(max_length=122) 
    profile_photo=models.ImageField(max_length=200,null=True)
    phone_number=models.IntegerField()
    email_address=models.CharField(max_length=100) 
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class user_log(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id', on_delete=models.CASCADE,default=None,primary_key=True)
    last_login_date = models.DateTimeField(auto_now=True)
    last_job_apply_date = models.DateTimeField(blank=True,null=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

#Company Porfile
class business_stream(models.Model):
    business_stream_name=models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class company(models.Model):
    company_name=models.CharField(max_length=100)    
    profile_description=models.CharField(max_length=1000)
    business_stream_id = models.ForeignKey('business_stream',related_name='business_stream_id', on_delete=models.CASCADE,default=None,null=True)
    establishment_date=models.DateField()
    company_website_url=models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class company_image(models.Model):
    company_id = models.ForeignKey('company',related_name='company_id_company_image', on_delete=models.CASCADE,default=None,null=True)
    company_image=models.ImageField(max_length=200, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

#Seeker Profile Builder
class user_education(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id_user_education', on_delete=models.CASCADE,default=None)
    education=models.CharField(max_length=100)
    univesity=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    speclalization=models.CharField(max_length=100)
    course_type=models.CharField(max_length=50)
    course_duration=models.DateTimeField()
    completion_date=models.DateTimeField(blank=True)
    grading_system = models.CharField(max_length=100)
    marks = models.IntegerField(blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    # primary_key = ('user_account_id','certificate_degree_name', 'major')

class user_workstatus(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id_user_workstatus', on_delete=models.CASCADE,default=None)
    work_title=models.CharField(max_length=50)
    url=models.CharField(max_length=100)
    duration_from=models.DateField()
    duration_to=models.BooleanField()
    working_staus=models.BooleanField()
    description=models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class user_personalinfo(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id_user_personalinfo', on_delete=models.CASCADE,default=None)
    current_industry=models.CharField(max_length=120)
    preferred_shift=models.CharField(max_length=50)
    preferred_work_location=models.CharField(max_length=122)
    expected_salary=models.IntegerField()
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    differently_abled=models.BooleanField()
    career_break=models.BooleanField()
    reasonforbreak=models.CharField(max_length=150)
    work_permit_for_any_countries=models.CharField(max_length=50)
    permanent_address=models.CharField(max_length=200)
    hometown=models.CharField(max_length=50)
    pincode=models.IntegerField()
    language=models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)


class seeker_skill_set(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_idsss', on_delete=models.CASCADE,default=None)
    skill_set_id=models.ForeignKey('user_skills',related_name='skill_set_id_seeker', on_delete=models.CASCADE,default=None)# i need to add here forenkhkey from below table
    skill_level=models.IntegerField()
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    # primary_key = ('user_account_id', 'skill_set_id')

class user_skills(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id_user_skills', on_delete=models.CASCADE,default=None)
    skill_name=models.CharField(max_length=50)
    software_version=models.IntegerField()
    last_used=models.DateField()
    experience=models.DateField()
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

#Job Post Management

class job_post(models.Model):
    posted_by_id = models.ForeignKey('job_post_activity',related_name='posted_by_id', on_delete=models.CASCADE,default=None,null=True,blank=True)
    job_type_id = models.ForeignKey('job_type',related_name='job_type_id', on_delete=models.CASCADE,default=None)
    company_id = models.ForeignKey('company',related_name='company_id', on_delete=models.CASCADE,default=None)
    is_company_name_hidden=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    job_description=models.CharField(max_length=500)
    job_location_id = models.ForeignKey('job_location',related_name='job_location_id', on_delete=models.CASCADE,default=None)
    is_active=models.BooleanField()
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    # primary_key = ('posted_by_id', 'job_type_id','company_id','job_location_id')

class job_post_activity(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_idssss', on_delete=models.CASCADE,default=None)
    job_post_id = models.ForeignKey('job_post',related_name='job_post_id', on_delete=models.CASCADE,default=None)
    apply_date=models.DateTimeField(auto_now_add=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    # primary_key = ('user_account_id', 'job_post_id')


class job_type(models.Model):
    job_type=models.CharField(max_length=20)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class job_location(models.Model):
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class job_post_skill_set(models.Model):
    skill_set_id = models.ForeignKey('user_skills',related_name='skill_set_id', on_delete=models.CASCADE,default=None,null=True,blank=True)
    job_post_id = models.ForeignKey('job_post',related_name='job_post_id_job_post_skill_set', on_delete=models.CASCADE,default=None)
    skill_level=models.IntegerField()
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    # primary_key = ('skill_set_id', 'job_post_id')



class user_certification(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id_user_certification', on_delete=models.CASCADE,default=None)
    certification_name=models.CharField(max_length=120)
    certification_completion_id=models.IntegerField()
    certification_url=models.CharField(max_length=100)
    certification_validity=models.DateField()
    certification_will_expire=models.BooleanField()
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)


class user_socialprofile(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id_user_socialprofile', on_delete=models.CASCADE,default=None)
    social_profile=models.CharField(max_length=150)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class user_projects(models.Model):
    user_account_id = models.ForeignKey('user_account',related_name='user_account_id_user_projects', on_delete=models.CASCADE,default=None)
    project_title=models.CharField(max_length=150)
    tag_this_project_with_your_Education=models.BooleanField()
    client_name=models.CharField(max_length=20)
    project_staus=models.BooleanField()
    workd_from = models.DateField()
    project_details=models.CharField(max_length=300)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)
