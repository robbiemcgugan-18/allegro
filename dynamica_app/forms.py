from django import forms

from dynamica_app.models import Music, Request, PartFormat, UserProfile
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm

class AddMusicForm(forms.ModelForm):
    name = forms.TextInput()

    class Meta:
        model = Music
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class RequestForm(forms.ModelForm):
    name = forms.TextInput()
    part = forms.ChoiceField()
    user = forms.TextInput()

    class Meta:
        model = Request
        fields = ("name", "part")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'name' in self.data:
            piece_name = self.data.get('name')
            part_list = (Music.objects.get(name=piece_name).part_format.part_data).split(",")

            part_list_formatted = []
            for part in part_list:
                part_list_formatted.append((part, part))

            self.fields['part'].choices = part_list_formatted

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'groups',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['groups'].help_text = 'Hold down "Ctrl" (Windows) or "Cmd" (Mac) to select more than one group for the user.'
        self.fields['password'].widget = forms.PasswordInput()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ""



class UserProfileForm(forms.ModelForm):
    instrument = forms.TextInput()

    class Meta:
        model = UserProfile
        fields = ('DOB', 'instrument')

        widgets = {
            'DOB': forms.TextInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ""


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'groups',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['groups'].help_text = 'Hold down "Ctrl" (Windows) or "Cmd" (Mac) to select more than one group for the user.'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ""

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
