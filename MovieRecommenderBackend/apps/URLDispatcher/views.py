from django.views.generic.list import ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from MovieRecommenderBackend.apps.URLDispatcher.models import Movie


def home(request):
    if request.user.is_authenticated:
        return redirect('/recommendations')
    else:
        return redirect('/movies')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/recommendations')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    paginate_by = 20

# Create your views here.
