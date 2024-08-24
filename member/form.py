from django import forms
from .models import Member

class MemberForm(forms.ModelForm): # chuyển form sang model tương ứng
    class Meta:
        model = Member
        fields = ['userName', 'password','phonenumber', 'realname']