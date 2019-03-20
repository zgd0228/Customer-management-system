# Generated by Django 2.1.5 on 2019-03-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='权限名称')),
                ('urls', models.CharField(max_length=64, verbose_name='权限路径')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='角色名称')),
                ('permissions', models.ManyToManyField(to='rbac.Permission', verbose_name='角色权限')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('age', models.IntegerField(verbose_name='用户年龄')),
                ('tel', models.IntegerField(verbose_name='用户电话')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('roles', models.ManyToManyField(to='rbac.Role', verbose_name='用户角色')),
            ],
        ),
    ]
