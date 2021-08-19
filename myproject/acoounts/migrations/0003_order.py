# Generated by Django 3.2.4 on 2021-06-23 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acoounts', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('dilivered', 'dilovered'), ('out of stocks', 'out of stocks')], max_length=200)),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acoounts.customer')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acoounts.product')),
            ],
        ),
    ]