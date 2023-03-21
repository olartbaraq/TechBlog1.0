from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post'] = Post.objects.latest("date_posted")
        context['all_posts'] = Post.objects.all()
        context['programming_posts'] = Post.objects.filter(section='Programming').order_by('-date_posted')[:3]
        context['gaming_posts'] = Post.objects.filter(section='Gaming').order_by('-date_posted')[:3]
        context['anime_posts'] = Post.objects.filter(section='Anime').order_by('-date_posted')[:3]
        context['title'] = 'HomePage'
        return context
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/ind_post.html'
    

class AnimePostView(ListView):
    model  = Post
    template_name = 'blog/anime.html'
    ordering = ['-date_posted']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_anime_posts'] = Post.objects.filter(section='Anime').order_by('-date_posted')
        context['title'] = 'Anime Page'
        return context
    

class ProgrammingPostView(ListView):
    model  = Post
    template_name = 'blog/programming.html'
    ordering = ['-date_posted']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_prog_posts'] = Post.objects.filter(section='Programming').order_by('-date_posted')
        context['title'] = 'Programming Page'
        return context
       

class GamingPostView(ListView):
    model  = Post
    template_name = 'blog/gaming.html'
    ordering = ['-date_posted']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_gaming_posts'] = Post.objects.filter(section='Gaming').order_by('-date_posted')
        context['title'] = 'Gaming Page'
        return context
    
    
def AboutPage(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})

def ContactPage(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName  = request.POST.get('LastName')
        Email = request.POST.get('Email')
        message =  request.POST.get('message')
        confirmation = 'Your message was sent successfully'
        
        send_mail(
            'Message from' + FirstName + LastName, # subject
            message, # message
            Email, # from email
            ['akanbi.ges201@gmail.com'], # to email
        )
        
        return render(request, 'blog/contact.html', {'title': 'Contact Page', 'confirmation': confirmation, 'FirstName': FirstName})
    else:
        return render(request, 'blog/contact.html', {'title': 'Contact Page'})




