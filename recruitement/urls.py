from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user_type/',views.usertype.as_view()),


    path('user_log/',views.userlog.as_view()),

    path('user_login/',views.userlogin.as_view()),
    path('forgot_password/<int:pk>/',views.forgotpassword.as_view()),

    path('business_stream/',views.businessstream.as_view()),

    path('company_save_details/',views.companyadddetails.as_view()),
    path('company_save_image/',views.companysaveimage.as_view()),
    path('company_save_details/<int:pk>/',views.companyprofile.as_view()),

    # path('seeker_profile/',views.seekerprofile.as_view()),
    # path('seeker_profile/<int:pk>/',views.editseekrprofile.as_view()),
    path('education_detail/',views.educationdetail.as_view()),
    path('experince_detail/',views.experincedetail.as_view()),

    path('seeker_skill_set/',views.seekerskillset.as_view()),

    path('post_job/',views.postjob.as_view()),
    path('post_job/<int:pk>/',views.editjob.as_view()),

    path('jobpostactivity/',views.jobpostactivity.as_view()),
    
    path('job_type/',views.jobtype.as_view()),
    path('jobskillset/',views.skillset.as_view()),

    path('skillset/',views.skills.as_view()),  

    path('job_location/',views.joblocation.as_view()),

    path('user_save_account/',views.usersaveaccount.as_view()),
    path('user_save_account/<int:pk>/',views.edituseraccount.as_view()),

    path('usereducation/',views.usereducation.as_view()),
    path('usereducation/<int:pk>/',views.editusereducation.as_view()),

    path('userskills/',views.userskills.as_view()),
    path('userskills/<int:pk>/',views.edituserskills.as_view()),

    path('usersocialprofile',views.usersocialprofile.as_view()),
    path('usersocialprofile/<int:pk>/',views.editusersocialprofile.as_view()),

    path('userworkstatus',views.userworkstatus.as_view()),
    path('userworkstatus/<int:pk>/',views.edituserworkstatus.as_view()),

    path('usercertification',views.usercertification.as_view()),
    path('usercertification/<int:pk>/',views.editusercertification.as_view()),

    path('userpersonalinfo',views.userpersonalinfo.as_view()),  
    path('userpersonalinfo/<int:pk>/',views.edituseruserpersonalinfo.as_view()), 

    path('userprojects',views.userprojects.as_view()),
    path('userprojects/<int:pk>/',views.edituserprojects.as_view()),

    path('employmentdetails',views.employmentdetails.as_view()),
    path('employmentdetails/<int:pk>/',views.editemploymentdetails.as_view()),

    path('publications',views.publications.as_view()),
    path('publications/<int:pk>/',views.editpublications.as_view()),

    path('presentation',views.presentation.as_view()),
    path('presentation/<int:pk>/',views.editpresentation.as_view()),

    path('patent',views.patent.as_view()),
    path('patent/<int:pk>/',views.editpatent.as_view()),
]