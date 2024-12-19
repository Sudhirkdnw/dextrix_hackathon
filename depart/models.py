from django.db import models 
#from depart.models import AppUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    member_id = models.AutoField
    member_name = models.CharField(max_length=80, default="User")
    member_type = models.CharField(max_length=50, default="Team Member")
    member_course = models.CharField(max_length=50, default=None)
    member_phone = models.CharField(max_length=10, default=None)
    member_instagram_ID = models.CharField(max_length=200, default=None)
    member_linkedin_link = models.CharField(max_length=200, default="https://www.linkedin.com/feed/")
    member_facebook_link = models.CharField(max_length=200, default="https://www.facebook.com/home.php")
    member_twitter_link = models.CharField(max_length=200, default=None)
    join_date = models.DateField(timezone.now())
    update_date = models.DateField(timezone.now())
    image = models.ImageField(upload_to="member/images" , default='default.jpg')
    
    
    def __str__(self):
        return self.member_name
    
class student(models.Model):
    student_id = models.AutoField
    student_name = models.CharField(max_length=50, default='Enter Name')
    student_branch = models.CharField(max_length=100, default=None)
    student_section = models.IntegerField( default=None)
    student_admission_id = models.CharField(max_length=20,default=None)
    student_phone = models.CharField(max_length=10, default=None)
    student_club = models.CharField(max_length=50 , default=None)
    student_instagram_ID = models.CharField(max_length=200, default="https://www.instagram.com/")
    student_linkedin_link = models.CharField(max_length=200, default="https://www.linkedin.com/feed/")
    student_facebook_link = models.CharField(max_length=200, default="https://www.facebook.com/home.php")
    student_image = models.ImageField(upload_to="student/images" , default='default.jpg')
    
    def __str__(self):
        return self.student_name
    
class hero(models.Model):
    hero_id = models.AutoField
    join_date = models.DateField(timezone.now())
    update_date = models.DateField(timezone.now())
    image = models.ImageField(upload_to="Hero/images" , default='default.jpg')
    
    
class club(models.Model):
    club_id = models.AutoField
    club_name = models.CharField(max_length=30, default="GU Club")
    club_logo = models.ImageField(upload_to="clublogo" , default="default.jpg" )
    
    def __str__(self):
        return self.club_name
    
class aboutpage(models.Model):
    about_id =models.AutoField
    about_image = models.ImageField(upload_to="about" , default="/media/default.jpg")
    about_heading = models.CharField(max_length=64 , default=None)
    about_p1 = models.TextField(max_length=500)
    about_p2 = models.TextField(max_length=500)
    
    
    
class event(models.Model):
    model_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=80 ,default=None)
    event_hoste_name = models.CharField(max_length=20 , default=None)
    event_date = models.DateTimeField(timezone.now())
    event_para = models.TextField(max_length=1000)
    event_image = models.ImageField(upload_to="event", default="default.png") 
    event_host_image = models.ImageField(upload_to="event/host" , default= "default_user.png")    
    
    def __str__(self):
        return self.event_title  
    
class registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    registration_name = models.CharField(max_length=50)
    registration_phone = models.CharField(max_length=50, default=None)
    registration_email = models.CharField(max_length=50, default=None)
    registration_course = models.CharField(max_length=50, default=None)
    registration_admission_no = models.CharField(max_length=50, default=None)
    registration_section = models.CharField(max_length=50, default=None)
    registration_course_year = models.CharField(max_length=50, default=None)   
    registration_dob = models.CharField(max_length=50, default=None)
    registration_skill = models.CharField(max_length=50, default=None)
    registration_gender = models.CharField(max_length=50, default=None)    
    registration_profile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    registration_payment_image = models.CharField(max_length=50, default=None)
    # registration_amount = models.CharField(max_length=50, default=0)
    
    def __str__(self):
        return self.registration_name  
    

    
    
    