# Generated by Django 2.2.4 on 2019-09-22 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0030_assign_projects_to_portfolios'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'permissions': [('can_grant_portfolio_owner_permission', 'Grant a user portfolio owner permission')]},
        ),
    ]
