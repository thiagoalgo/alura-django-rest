# Generated by Django 4.2.2 on 2023-06-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='periodo',
            field=models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1),
        ),
    ]
