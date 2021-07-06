from django.shortcuts import render, redirect

from .models import Team, Person

from django.http import HttpResponse

from django.forms import modelformset_factory, inlineformset_factory 


  
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import UserSerializer, TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

"""
def index(request, team_id):
    team = Team.objects.get(pk=team_id)
    userFormSet = inlineformset_factory(Team, User, fields=("name", ))

    if request.method == "POST":
        formset = userFormSet(request.POST, instance = team)

        if formset.is_valid():
            formset.save()

            return redirect("index",team_id=team.id)


    formset = userFormSet(instance = team)
    
    return render(request , "index.html", {"formset":formset})
"""






def index(request):

    users = list(Person.objects.all())


    b = Team(name='an2')
    b.save()
    if users:
        print("type", type(users), "usuarios:",users)
        for user in users:
            print(user)
            b.users.add(user)
    b.save()

    return HttpResponse('Hello, World!')
