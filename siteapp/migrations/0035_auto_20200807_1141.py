# Generated by Django 3.0.7 on 2020-08-07 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0034_support'),
    ]

    operations = [
        migrations.RenameField(
            model_name='support',
            old_name='support_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='support',
            old_name='support_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='support',
            old_name='support_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='support',
            old_name='support_url',
            new_name='url',
        ),
    ]