from django.views.generic.list import ListView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from MovieRecommenderBackend.apps.URLDispatcher.models import Movie, RatingData, MyUser
from MovieRecommenderBackend.apps.URLDispatcher.admin import UserCreationForm
from MovieRecommenderBackend.libs.CFEngine.cfengine import get_recommendations_list


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
            username = form.cleaned_data.get('email')
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
    context_object_name = 'movie_list'
    paginate_by = 20


class RecommendationsView(ListView):
    model = Movie
    template_name = 'recommendations.html'
    context_object_name = 'movie_list'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(RecommendationsView, self).get_context_data(**kwargs)
        username = self.request.user.get_username()
        context['recommendations_list'] = get_recommendations_list(MyUser(email=username).ratingUser_id,
                                                                   Movie.objects.all().values(),
                                                                   RatingData.objects.all().values())
        return context

# Create your views here.
