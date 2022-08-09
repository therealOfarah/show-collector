from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Show, Genre

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def shows_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', {'shows':shows})

@login_required
def shows_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  show_genre_doesnt_have = Genre.objects.exclude(id__in = show.genre.all().values_list('id'))
  return render(request, 'shows/detail.html', {
    'show': show, 'genre': show_genre_doesnt_have
  })

class ShowCreate( CreateView):
  model = Show
  fields = ['show', 'description','start_date', 'final_date']
  success_url = '/shows/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ShowUpdate( UpdateView):
  model = Show
  fields = ['description', 'start_date','final_date']

class ShowDelete( DeleteView):
  model = Show
  success_url = '/shows/'

class GenreCreate( CreateView):
  model = Genre
  fields = '__all__'
  success_url = '/genre/'

class GenreList( ListView):
  model = Genre

class GenreDetail( DetailView):
  model = Genre

class GenreUpdate( UpdateView):
  model = Genre
  fields = ['name', 'color']
  success_url = '/genre/'

class GenreDelete(DeleteView):
  model = Genre
  success_url = '/genre/'

def signup(request):
  error_message = ""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('shows_index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
