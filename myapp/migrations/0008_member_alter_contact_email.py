# Generated by Django 5.0.2 on 2024-11-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
