from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib import messages
from accounts.models import Profile
from accounts.forms import UserRegisterForm

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


class UserListView(ListView):

    model = Profile
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return Profile.objects.all().order_by('-rating')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'users_nav': 'active'
        })
        return context
