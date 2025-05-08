# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
from django.utils import timezone
from django import forms

@python_2_unicode_compatible  # only if you need to support Python 2
class Project(models.Model):
    #requester = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Requester")
    id = models.AutoField(primary_key=True)
    requester = models.CharField(max_length=30)
    project_name = models.CharField(max_length=30,unique=True)
    application_name = models.CharField(max_length=30)
    git_url = models.CharField(max_length=256)
    git_branch = models.CharField(max_length=30)
    platform_version = models.CharField(blank=True, max_length=30)
    cpu =  models.IntegerField(null=True, blank=True)
    memory = models.IntegerField(null=True, blank=True)
    build_tool = models.CharField(blank=True, max_length=30)
    mysql_password = models.CharField( blank=True, max_length=30)
    mongo_password = models.CharField(blank=True, max_length=30)
    env_key1 = models.CharField(blank=True,max_length=30)
    env_value1 = models.CharField(blank=True,max_length=500)
    env_key2 = models.CharField(blank=True,max_length=30)
    env_value2 = models.CharField( blank=True,max_length=500)
    env_key3 = models.CharField( blank=True,max_length=30)
    env_value3 = models.CharField( blank=True,max_length=500)
    env_key4 = models.CharField( blank=True,max_length=30)
    env_value4 = models.CharField( blank=True,max_length=500)
    env_key5 = models.CharField(blank=True,max_length=30)
    env_value5 = models.CharField( blank=True,max_length=500)
    env_key6 = models.CharField(blank=True,max_length=30)
    env_value6 = models.CharField( blank=True,max_length=500)
    env_key7 = models.CharField( blank=True,max_length=30)
    env_value7 = models.CharField( blank=True,max_length=500)
    env_key8 = models.CharField( blank=True,max_length=30)
    env_value8 = models.CharField( blank=True,max_length=500)
    env_key9 = models.CharField( blank=True,max_length=30)
    env_value9 = models.CharField( blank=True,max_length=500)
    env_key10 = models.CharField( blank=True,max_length=30)
    env_value10 = models.CharField( blank=True,max_length=500)
    project_flag = models.BooleanField( blank=True, default=False)
    mysql_status = models.CharField(default='Requested',max_length=256)
    mongo_status = models.CharField(default='Requested',max_length=256)
    jenkins_status = models.CharField(default='Requested',max_length=256)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    def __str__(self):
        return self.project_name

class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('P0', 'High'),
        ('P1', 'Medium'),
        ('P2', 'Normal'),
    ]

    # Category Choices
    CATEGORY_CHOICES = [
        ('Access Request-BitBucket', 'Access Request-BitBucket'),
        ('Access Request-VPN', 'Access Request-VPN'),
        ('Access Request-Mysql/Psql Database', 'Access Request-Mysql/Psql Database'),
        ('Access Request-Mongo Database', 'Access Request-Mongo Database'),
        ('Issue-CI/CD Jenkins/Spinnaker', 'Issue-CI/CD Jenkins/Spinnaker'),
        ('Issue-Grafana/Kibana', 'Issue-Grafana/Kibana'),
        ('Issue-NonProd', 'Issue-NonProd'),
        ('Issue-Production', 'Issue-Production'),
        ('New Service Setup', 'New Service Setup'),
        ('New-Task/Feature Request', 'New-Task/Feature Request'),
        ('General Guidance', 'General Guidance'),
    ]

    # Status Choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('OnHold', 'OnHold'),
        ('InProgress', 'InProgress'),
        ('Complete', 'Complete'),
    ]

    # Ticket fields
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    ticket_priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='P2')
    ticket_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    ticket_subject = models.CharField(max_length=256, null=True, blank=True)
    ticket_description = models.TextField(null=True, blank=True)
    ticket_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    ticket_em_cc = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return "Ticket {} - {}".format(self.id, self.ticket_category) 

class UniversityRequest(models.Model):
    UNIVERSITY_CHOICES = [
        ('andhra', 'Andhra'),
        ('bharathidasan', 'Bharathidasan'),
        ('chandigarh', 'Chandigarh'),
        ('centurion', 'Centurion'),
        ('drmgr', 'DrMGR'),
        ('dypatil', 'DYPatil'),
        ('jain', 'Jain'),
        ('kiit', 'KIIT'),
        ('kuk', 'KUK'),
        ('vgu', 'VGU'),
        ('niu', 'NIU'),
        ('jnu', 'JNU'),
        ('atlas', 'Atlas'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=255, choices=UNIVERSITY_CHOICES)
    size = models.CharField(max_length=50, choices=[
        ('t4g.small', 't4g.small'),
        ('t4g.medium', 't4g.medium'),
        ('t4g.large', 't4g.large'),
    ])
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    

    def __str__(self):  
        return self.university_name

class RequestForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['project_flag','pub_date','mysql_status','mongo_status','jenkins_status',]
        #fields = ['requester', 'project_name', 'application_name' , 'git_url','git_branch','platform_version','cpu' , 'memory','build_tool','mysql_password','mongo_password', 
        #'env_key1','env_value1']

class TicketForm(forms.ModelForm):
    TICKET_CC_CHOICES = [
        ('abhishek.aman@upgrad.com', 'abhishek.aman@upgrad.com'),
        ('alka.bahirat@upgrad.com', 'alka.bahirat@upgrad.com'),
        ('atul.yadav@upgrad.com', 'atul.yadav@upgrad.com'),
        ('balakrishna.ragala@upgrad.com', 'balakrishna.ragala@upgrad.com'),
        ('mukesh1.kumar@upgrad.com', 'mukesh1.kumar@upgrad.com'),
        ('ravi.kant@upgrad.com', 'ravi.kant@upgrad.com'),
        ('ravi.tatikonda@upgrad.com', 'ravi.tatikonda@upgrad.com'),
        ('vasista.reddy@upgrad.com', 'vasista.reddy@upgrad.com'),
    ]

    ticket_em_cc = forms.MultipleChoiceField(
        choices=TICKET_CC_CHOICES,
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    ) 
    class Meta:
        model = Ticket
        fields = ['ticket_priority', 'ticket_category', 'ticket_subject', 'ticket_description', 'ticket_attachment', 'ticket_em_cc']

class UniversityRequestForm(forms.ModelForm):
    class Meta:
        model = UniversityRequest
        fields = ['university_name', 'size', 'start_date', 'end_date']
        widgets = {
            'university_name': forms.Select(),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
# Create your models here.
