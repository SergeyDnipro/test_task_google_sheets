# Generated by Django 4.0.7 on 2022-08-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_sheets_extraction_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='msg_status_text',
            field=models.CharField(default='In process...', max_length=20),
        ),
    ]
