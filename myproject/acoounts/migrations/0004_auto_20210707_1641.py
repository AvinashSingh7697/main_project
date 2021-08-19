# Generated by Django 3.2.4 on 2021-07-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoounts', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=100)),
                ('is_completen', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
