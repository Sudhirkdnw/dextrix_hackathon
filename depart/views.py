from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import smtplib
# import stripe 
# import redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from .models import hero
from .models import aboutpage
from .models import club
from .models import student, event, registration

# stripe_api_key='pk_test_51Mm7CCSJNaTHzV0L7zNhZUPaDG3QcjUkQIUXFBjIjmjeJD5XAcBpsq4sxdxf0jPy2xvhuqnYog8Yk1XmN1LLfjd000WGoJtOL4'

def home(request):
    mydata = Member.objects.all()
    myhero = hero.objects.all().order_by("join_date")[:1]
    myhero1 = hero.objects.all().order_by("join_date")[1:2]
    myclub = club.objects.all()
    myabout = aboutpage.objects.all()
    myevent = event.objects.all()
    context = {'member': mydata,
               'hero':myhero,
               'hero1':myhero1,
               'club':myclub,
               'aboutus':myabout,
               'events':myevent,}
   
    return render(request,'index.html' , context )
    


def about(request):
    myabout = aboutpage.objects.all()
    context = {'aboutus':myabout}
    return render(request,'about.html', context)

def contact(request):
    if request.method == "POST":
        user = request.POST.get('user')
        email = request.POST.get('email') 
        receiver_email = 'chaudharydnw@gmail.com'
        subject = request.POST.get('subject')
        massage= request.POST.get('massage')

        text =f"subject:{subject}\n\n{massage}"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(email , "nrtkasqazktgqskv" )
        server.sendmail(email , receiver_email , text)

        print("Email Has been sent to: " + receiver_email)
    return render(request, 'contact.html' )

def project(request):
    myclub = club.objects.all()
    context = {'club':myclub}
    return render(request, 'project.html', context )

def service(request):
    return render(request, 'service.html' )

def team(request):
    mydata = Member.objects.all()
    context = {'member': mydata,}
    return render(request, 'team.html', context )

def card(request):
    mystudent = student.objects.all()
    data = {'student':mystudent}
    return render(request, 'card.html' , data)

def testimonial(request):
    return render(request, 'testimonial.html' )

def register(request):
    if request.method == 'POST':        
        registration_name = request.POST.get('registration_name')
        registration_email = request.POST.get('registration_email')
        registration_phone = request.POST.get('registration_phone')
        registration_dob = request.POST.get('registration_dob')
        registration_gender = request.POST.get('registration_gender')
        registration_course = request.POST.get('registration_course')
        registration_admission_no = request.POST.get('registration_admission_no')
        registration_section = request.POST.get('registration_section')
        registration_course_year = request.POST.get('registration_course_year')
        registration_skill = request.POST.get('registration_skill')
        registration_profile = request.POST.get('registration_profile')
        registration_payment_image= request.POST.get('registration_payment_image')
        
        data = registration(registration_name=registration_name ,registration_phone=registration_phone,registration_email=registration_email,registration_dob=registration_dob,registration_gender=registration_gender,registration_course=registration_course,
                        registration_admission_no=registration_admission_no,registration_section=registration_section ,registration_course_year=registration_course_year,registration_skill=registration_skill,registration_profile=registration_profile,
                        registration_payment_image=registration_payment_image)
        data.save()

       
    return render(request, 'register.html' )

def eventpage(request):
    myevent = event.objects.all()
    context = {'events': myevent } 
    return render(request, 'eventpage.html', context)

def guclub(request):
    myevent = event.objects.all()
    context = {'events': myevent } 
    return render(request, 'guclub.html', context)

def op(request):
    return render(request, 'op.html' )



