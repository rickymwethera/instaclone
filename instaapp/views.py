from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Comment,Profile
from .forms import PostForm, CommentForm
from django.views.generic import DetailView


# Create your views here.

# @login_required(login_url='accounts/login/')

def welcome(request):
    posts=Image.objects.all()
    return render(request, 'index.html', {"images":posts})

def profile(request):
    return render(request, 'profile.html')

def create_post(request):
    current_user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            add=form.save(commit=False)
            current_user = Profile.objects.get(name=request.user)
            add.author = current_user
            add.save()
            return redirect('index')
    

    context = {'form':form}
    return render(request,'posts.html',context)

def follow_unfollow(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(name=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.name in my_profile.following.all():
            my_profile.following.remove(obj.name)
        else:
            my_profile.following.add(obj.name)
        return redirect(request.META.get('HTTP_REFERER')) 
    return redirect('explore')

def like_post(request, pk):
    post = get_object_or_404(Image, id=pk)
    liked= False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class ProfileDetailView(DetailView):
    model = Profile
    template = "profile.html"
    #get user profile
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    #get my profile
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(name=self.request.user)
        if view_profile.name in my_profile.following.all():
            follow = True
        else:
            follow =False
        context["follow"] = follow
        return context