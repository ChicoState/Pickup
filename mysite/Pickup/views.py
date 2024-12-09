from django.shortcuts import render, redirect
from . import models
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . import forms

def index(request):
    current_user = request.user
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            postF = form.save(commit=False)
            postF.author = request.user
            postF.date_time = form.cleaned_data['date_time']
            postF.post_loc = form.cleaned_data['post_loc']  # Save the location
            postF.save()
            postF.rsvp_list.add(request.user)
            return redirect('/')
    else:
        form = forms.PostForm()
    
    posts = models.Post.objects.all()

    context = {
        'current_user': current_user,
        'form': form,
        'title': 'Pickup',
        'posts': posts,
        'google_maps_api_key': 'AIzaSyATgY252mj0kipD4snpGnc9Hdrj4UlLFVA'
    }
    return render(request, 'index.html', context=context)

def postJson(request):
    rsvp = []
    if request.user.is_authenticated:
        tmpposts = request.user.rsvp.all()
        for p in tmpposts:
            rsvp.append(p.pk)
    p_objects = models.Post.objects.all()
    p_dictionary = {}
    p_dictionary['posts'] = []
    for p in p_objects[::-1]:
        tempp = {}
        if p.pk in rsvp:
            tempp["rsvp"] = True
        else:
            tempp["rsvp"] = False
        tempp["author"] = p.author.username
        tempp["post_date"] = p.post_date
        tempp["postID"] = p.pk
        tempp["post_title"] = p.post_title
        tempp["post_text"] = p.post_text
        tempp["post_loc"] = p.post_loc
        tempp["date_time"] = p.date_time  # Include date and time
        p_dictionary['posts'] += [tempp]
    return JsonResponse(p_dictionary)

def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("/login/")
        else:
            return redirect('/register/')
    else:
        form = forms.RegistrationForm(request.POST)
        context = {"form": form}
        return render(request,"registration/register.html",context=context)

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required
def upload(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            postF = form.save(commit=False)
            postF.author = request.user
            postF.save()
            postF.rsvp_list.add(request.user)
            return redirect('/')