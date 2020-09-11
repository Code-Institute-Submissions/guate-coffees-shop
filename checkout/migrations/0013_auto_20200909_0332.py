# Generated by Django 3.0.8 on 2020-09-09 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200909_0332'),
        ('checkout', '0012_auto_20200901_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.UserInfo'),
        ),
    ]