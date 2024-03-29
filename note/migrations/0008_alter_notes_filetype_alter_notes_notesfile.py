# Generated by Django 5.0 on 2023-12-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_alter_notes_notesfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='filetype',
            field=models.CharField(choices=[('pdf', 'PDF'), ('doc', 'DOC/DOCX'), ('CIVIL', 'CIVIL'), ('ppt', 'PPT/WORD'), ('zip', 'ZIP'), ('image', 'IMAGE'), ('OTHER', 'OTHER')], default='pdf', max_length=30),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notesfile',
            field=models.FileField(null=True, upload_to='note'),
        ),
    ]
