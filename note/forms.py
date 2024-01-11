from django.forms import ModelForm


from .models import Notes


class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['branch', 'subject', 'notesfile', 'filetype' ,'description']
