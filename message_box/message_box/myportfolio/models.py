from django.db import models
from django.contrib.auth.models import User
from django.template import RequestContext
from datetime import datetime
from django.urls import reverse
from django.contrib import auth


class departments(models.Model):
    department_name=models.CharField(max_length=100)
    def __str__(self):
        return self.department_name

class typeofuser(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    #declare a foreign key object of the User
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #profile_pic = models.ImageField(blank=True,upload_to='profile_pics')
    user_type=models.ForeignKey(typeofuser,on_delete=models.CASCADE)
    department=models.ForeignKey(departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    Name=models.CharField(max_length=200, null=True)
    Aadhar=models.PositiveIntegerField(null=True)
    Contact_Number=models.CharField(max_length=200,null=True)
    Email_id=models.CharField(max_length=200,null=True)
    Address=models.CharField(max_length=200,null=True)
    City=models.CharField(max_length=200,null=True)
    State=models.CharField(max_length=200,null=True)
    PIN_Code=models.PositiveIntegerField(null=True)
    from_user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='fromuser')
    to_user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='touser')
    title=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=1000,null=True)
    comments=models.CharField(max_length=1000, null=True)
    comments_aig=models.CharField(max_length=1000,null=True)
    up_files=models.FileField(verbose_name='file',upload_to='documents/')
    release_date = models.DateTimeField(default=datetime.now(), null=True)
    action_taken=models.CharField(max_length=1000, null=True)
    is_archived=models.BooleanField(default=False)
    is_approved_aig=models.BooleanField(default=False)
    is_approved_dgp=models.BooleanField(default=False)
    is_actiontaken=models.BooleanField(default=False)
    complaint_id = models.AutoField(primary_key=True)
    is_reconsider_aig=models.BooleanField(default=False)
    is_reconsider_dgp=models.BooleanField(default=False)
    reconsider_dgp=models.CharField(max_length=1000,null=True)
    reconsider_aig=models.CharField(max_length=1000,null=True)


    def get_absolute_url(self):
        return reverse('mess:detail', kwargs={'pk': self.pk})

    #store model in orer of release date
    class Meta:
       ordering = ['-release_date']

    def __str__(self):
        return self.to_user.username
