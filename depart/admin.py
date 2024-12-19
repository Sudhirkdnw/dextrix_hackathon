from django.contrib import admin

# Register your models here.
from .models import Member , hero , club , aboutpage, student , event, registration


class AdminMember(admin.ModelAdmin):
    list_display = ('member_name', 'member_type','member_course','join_date')
admin.site.register(Member,AdminMember)
    

admin.site.register(hero)

admin.site.register(club)

admin.site.register(aboutpage)

class AdminStudent(admin.ModelAdmin):
    list_display = ('student_name','student_branch','student_admission_id','student_phone')
admin.site.register(student,AdminStudent)

class AdminEvent(admin.ModelAdmin):
    list_display = ('event_title', 'event_hoste_name','event_date')
    
admin.site.register(event,AdminEvent)


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('registration_name', 'registration_admission_no','registration_course','registration_phone','registration_skill')
admin.site.register(registration,RegisterAdmin)