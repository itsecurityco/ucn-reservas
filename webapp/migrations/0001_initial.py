# Generated by Django 4.0.3 on 2022-03-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('condition', models.CharField(choices=[('EX', 'Excelente'), ('GO', 'Buena'), ('BA', 'Mala')], default='EX', max_length=2)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
