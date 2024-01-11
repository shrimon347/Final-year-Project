from django.db import models
from base.models import User
# Create your models here.


BRANCH_CHOICES = ( 
    ("CSE", "CSE"), 
    ("EEE", "EEE"), 
    ("CIVIL", "CIVIL"), 
    ("MECHANICAL", "MECHANICAL"), 
    ("IT", "IT"), 
    ("NETWORKING", "NETWORKING"), 
    ("ECE", "ECE"), 
    ("OTHER", "OTHER"), 
) 

FILETYPE_CHOICES = (
    ("pdf", "PDF"), 
    ("doc", "DOC/DOCX"), 
    ("CIVIL", "CIVIL"), 
    ("ppt", "PPT/WORD"), 
    ("zip", "ZIP"), 
    ("image", "IMAGE"),  
    ("OTHER", "OTHER"), 
)

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.DateField()
    branch = models.CharField(max_length=30,  choices = BRANCH_CHOICES, default = 'CSE')
    subject = models.CharField(max_length=30)
    notesfile = models.FileField(null=True,upload_to='note')
    filetype = models.CharField(max_length=30, choices = FILETYPE_CHOICES, default = 'pdf')
    description = models.CharField(max_length=200, null=True)
    status = models.BooleanField('Approved', default = False)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.subject