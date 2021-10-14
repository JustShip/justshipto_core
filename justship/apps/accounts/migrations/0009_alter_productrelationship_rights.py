# Generated by Django 3.2.7 on 2021-10-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_productrelationship_rights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrelationship',
            name='rights',
            field=models.CharField(blank=True, choices=[('owner', 'Is owner'), ('collaborator', 'Is collaborator')], max_length=30),
        ),
    ]
