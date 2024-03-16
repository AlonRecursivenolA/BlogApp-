from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from django import forms
from theblog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url']
        widgets = {

            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),

        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attr['class'] = 'form-control'
        # self.fields['password1'].widget.attr['class'] = 'form-control'
        # self.fields['password2'].widget.attr['class'] = 'form-control'


class UpdateFormView(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('email','first_name','last_name','last_login','is_superuser','is_staff','is_active','date_joined','password')
