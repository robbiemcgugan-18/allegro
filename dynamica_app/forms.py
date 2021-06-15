from django import forms

from dynamica_app.models import Music, Request, PartFormat

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
