# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Category'


class Post(models.Model):
    title = models.CharField()
    content = models.CharField()
    user = models.ForeignKey('User', models.DO_NOTHING,related_name='post') 
    category = models.ForeignKey('Category', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Post'


class User(models.Model):
    name = models.CharField()
    empno = models.CharField()
    create_dt = models.DateTimeField()
    update_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'
