# Generated by Django 3.1.5 on 2021-01-10 21:54

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, null=True, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='')),
                ('biography', models.TextField(blank=True)),
                ('website', models.CharField(blank=True, max_length=50)),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('account_type',
                 models.CharField(choices=[('PES', 'Pessoal'), ('PRO', 'Profissional')], default='PES', max_length=3)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]