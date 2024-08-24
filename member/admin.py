from django.contrib import admin
from .models import Member
from django.contrib.sessions.models import Session

admin.site.register(Session)

class MemberAdmin(admin.ModelAdmin):
	list_display="username","password","phonenumber","realname"

admin.site.register(Member, MemberAdmin)

