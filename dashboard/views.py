# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required


from .models import RequestForm, TicketForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.shortcuts import render
from .models import Project
from django.contrib.auth.models import User
from .models import UniversityRequestForm
from django.forms import formset_factory
from .models import Ticket, UniversityRequest

import datetime


@login_required(login_url='/login/')
def dashboard(request):
    ticket_form = TicketForm()
#   today = datetime.datetime.now().date()
    return render(request, "dashboard/dashboard.html", {'ticket_form': ticket_form})

@login_required(login_url='/login/')
def user(request):
#   today = datetime.datetime.now().date()
    return render(request, "dashboard/user.html")

@login_required(login_url='/login/')
def thanks(request):
#   today = datetime.datetime.now().date()
    return render(request, "dashboard/thanks.html")

@login_required(login_url='/login/')
def cloudprovider(request):
    uname = request.user.get_username()
    if uname == 'admin':
#   today = datetime.datetime.now().date()
        return render(request, "dashboard/cloud-provider.html")
    else:
        return render(request, "dashboard/noauth.html")

@login_required(login_url='/login/')
def userdata(request):
    uname = request.user.get_username()
    posts = Project.objects.all().filter(requester='admin')

    return render(request, 'dashboard/post_list.html', {'posts': posts })



@login_required(login_url='/login/')
def javaform(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            #pass
            return HttpResponseRedirect('/dashboard/thanks/')  # does nothing, just trigger the validation
    else:
        form = RequestForm()
    return render(request, 'dashboard/java-home.html', {'form': form})
# Create your views here.

@login_required(login_url='/login/')
def drupalform(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            #pass
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
    else:
        form = RequestForm()
    return render(request, 'dashboard/drupal-home.html', {'form': form})
# Create your views here.


@login_required(login_url='/login/')
def nodeform(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            #pass
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
    else:
        form = RequestForm()
    return render(request, 'dashboard/node-home.html', {'form': form})

# Form for raising a ticket (Project request and ticket form)
@login_required(login_url='/login/')
def raise_ticket(request):
    if request.method == 'POST':
        print("Form submission started...")  
        print("Request POST Data:", request.POST)

        ticket_form = TicketForm(request.POST, request.FILES)

        if ticket_form.is_valid():
            print("Forms are valid... saving data")

            ticket = ticket_form.save(commit=False)
            ticket.user = request.user  

            # Print ticket_em_cc field value before saving
            email_list = request.POST.getlist('ticket_em_cc')  
            print("Raw Emails from POST request:", email_list)

            # Join emails into a string and save
            ticket.ticket_em_cc = ', '.join(email_list)  
            print("Final email string:", ticket.ticket_em_cc)

            ticket.save()
            print("Ticket successfully saved! Emails CC:", ticket.ticket_em_cc)

            return redirect('thanks')  
        else:
            print("Ticket Form Errors:", ticket_form.errors)

    else:
        ticket_form = TicketForm()

    return render(request, 'dashboard/ticket-home.html', {'ticket_form': ticket_form})


@login_required(login_url='/login/')
def university_request(request):
    UniversityRequestFormSet = formset_factory(UniversityRequestForm, extra=1)  # Start with 1 form

    if request.method == 'POST':
        formset = UniversityRequestFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:  # Only save if the form has data
                    university_request = form.save(commit=False)
                    university_request.user = request.user
                    university_request.save()
            return redirect('thanks')  # Redirect to dashboard after submission
    else:
        formset = UniversityRequestFormSet()

    return render(request, 'dashboard/university_request.html', {'formset': formset})

def raised_requests(request):
    if request.user.is_superuser:
        shark_tickets = Ticket.objects.all()    # If the user is an admin, fetch all tickets
        db_scale_requests = UniversityRequest.objects.all()
    else:
        shark_tickets = Ticket.objects.filter(user=request.user)
        db_scale_requests = UniversityRequest.objects.filter(user=request.user)
    context = {
        'shark_tickets': shark_tickets,
        'db_scale_requests': db_scale_requests
    }
    
    return render(request, 'dashboard/raised_requests.html', context)

@login_required(login_url='/login/')
def update_ticket_status(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if not request.user.is_superuser:
        return redirect('raised_requests')  # Redirect if not a superuser
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Ticket.STATUS_CHOICES).keys():
            ticket.status = new_status
            ticket.save()
    return redirect('raised_requests')

@login_required(login_url='/login/')
def update_request_status(request, request_id):
    university_request = get_object_or_404(UniversityRequest, id=request_id)
    if not request.user.is_superuser:
        return redirect('raised_requests')  # Redirect if not a superuser
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(UniversityRequest.STATUS_CHOICES).keys():
            university_request.status = new_status
            university_request.save()
    return redirect('raised_requests')

