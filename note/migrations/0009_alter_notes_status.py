# Generated by Django 5.0 on 2023-12-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_alter_notes_filetype_alter_notes_notesfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
