from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.models import Friend
from .forms import *


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, **kwargs):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
        except Friend.DoesNotExist:
            friend = None

        if friend:
            friends = friend.users.all()
        else:
            friends = []

        args = {'form': form, 'posts': posts,
                'users': users, 'friends': friends}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home:home')
        else:
            form = HomeForm()
            context = {'form': form}
        return render(request, self.template_name, context)


def change_friend_status(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')
