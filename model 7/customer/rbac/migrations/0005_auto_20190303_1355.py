# Generated by Django 2.1.5 on 2019-03-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_userinfo_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(default='', max_length=32, verbose_name='菜单图标'),
        ),
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=0, verbose_name='是否为菜单'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(null=True, verbose_name='用户年龄'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='用户邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.IntegerField(blank=True, null=True, verbose_name='用户电话'),
        ),
    ]