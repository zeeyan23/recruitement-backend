from django.contrib import admin

from recruitement.models import *
# Register your models here.

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_type_name','createdDate', 'modifiedDate')
    list_display_links = ('id', 'user_type_name') # adds links to id and name fields

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id','user_type_id','first_name','last_name','experience_level','resume','join_type','profile_photo','phone_number','email_address',
                'createdDate','modifiedDate')
    list_display_links = ('id', 'user_type_id') # adds links to id and name fields

class UserLogAdmin(admin.ModelAdmin):
    list_display = ('user_account_id','last_login_date','last_job_apply_date','createdDate','modifiedDate')
    list_display_links = ('user_account_id','last_login_date') # adds links to id and name fields

class BusinessStreamAdmin(admin.ModelAdmin):
    list_display = ('id','business_stream_name','createdDate','modifiedDate')
    list_display_links = ('id','business_stream_name') # adds links to id and name fields

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','profile_description','business_stream_id','establishment_date','company_website_url',
                    'createdDate','modifiedDate')
    list_display_links = ('id','company_name') # adds links to id and name fields


class CompanyImageAdmin(admin.ModelAdmin):
    list_display = ('id','company_id','company_image','createdDate','modifiedDate')
    list_display_links = ('id','company_id') # adds links to id and name fields

class UserEducationAdmin(admin.ModelAdmin):
    list_display = ('id','user_account_id','education','univesity','course','speclalization','course_type','course_duration','completion_date','grading_system',
                'marks','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields

class UserWorkStatusAdmin(admin.ModelAdmin):
    list_display = ('id','user_account_id','work_title','url','duration_from','duration_to','working_staus','description','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields

class UserPersonelInfoAdmin(admin.ModelAdmin):
    list_display = ('user_account_id','current_industry','preferred_shift','preferred_work_location','expected_salary','gender','date_of_birth'
                ,'differently_abled','career_break','reasonforbreak','work_permit_for_any_countries','permanent_address',
                'hometown','pincode','language','createdDate','modifiedDate')
    list_display_links = ('user_account_id','current_industry') # adds links to id and name fields

class SeekerSkillSetAdmin(admin.ModelAdmin):
    list_display = ('id','user_account_id','skill_set_id','skill_level','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields

class UserSkillsAdmin(admin.ModelAdmin):
    list_display = ('id','user_account_id','skill_name','software_version','last_used','experience','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields

class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id','posted_by_id','job_type_id','company_id','is_company_name_hidden','created_date',
                    'job_description','job_location_id','is_active','createdDate','modifiedDate')
    list_display_links = ('id','posted_by_id') # adds links to id and name fields

class JobPostActivityAdmin(admin.ModelAdmin):
    list_display = ('id','user_account_id','job_post_id','apply_date','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('id','job_type','createdDate','modifiedDate')
    list_display_links = ('id','job_type') # adds links to id and name fields

class JobLocationAdmin(admin.ModelAdmin):
    list_display = ('id','street_address','city','state','country','zip','createdDate','modifiedDate')
    list_display_links = ('id','street_address') # adds links to id and name fields

class JobPostSkillSet(admin.ModelAdmin):
    list_display = ('id','skill_set_id','job_post_id','skill_level','createdDate','modifiedDate')
    list_display_links = ('id','skill_set_id') # adds links to id and name fields

class UserSocialProfileAdmin(admin.ModelAdmin):
    list_display = ('id','social_profile','url','description',
                'user_account_id','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields

class UserCertificationAdmin(admin.ModelAdmin):
    list_display = ('id','user_account_id','certification_name','certification_completion_id','certification_url',
                'certification_validity','certification_will_expire','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields

class UserProjectAdmin(admin.ModelAdmin):
    list_display = ('id','user_account_id','project_title','tag_this_project_with_your_Education','client_name',
                'project_staus','workd_from','project_details','createdDate','modifiedDate')
    list_display_links = ('id','user_account_id') # adds links to id and name fields


admin.site.register(user_type,UserTypeAdmin)
admin.site.register(user_account, UserAccountAdmin)
admin.site.register(user_log, UserLogAdmin)
admin.site.register(business_stream, BusinessStreamAdmin)
admin.site.register(company, CompanyAdmin)
admin.site.register(company_image, CompanyImageAdmin)
admin.site.register(user_education, UserEducationAdmin)
admin.site.register(user_workstatus, UserWorkStatusAdmin)
admin.site.register(user_personalinfo, UserPersonelInfoAdmin)
admin.site.register(seeker_skill_set, SeekerSkillSetAdmin)
admin.site.register(user_skills, UserSkillsAdmin)
admin.site.register(job_post, JobPostAdmin)
admin.site.register(job_post_activity, JobPostActivityAdmin)
admin.site.register(job_type, JobTypeAdmin)
admin.site.register(job_location, JobLocationAdmin)
admin.site.register(job_post_skill_set, JobPostSkillSet)
admin.site.register(user_socialprofile, UserSocialProfileAdmin)
admin.site.register(user_certification, UserCertificationAdmin)
admin.site.register(user_projects, UserProjectAdmin)