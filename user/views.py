from tempfile import template

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import FormView, ListView

from admin_dashboard.models import CustomUser
from lawyer.models import Lawyer, Blog
from user.forms import UserRegistrationForm




from django.shortcuts import render


def search(request):
    specialization = request.GET.get('specialization', '')
    location = request.GET.get('location', '')

    # Filter approved lawyers based on specialization and location
    lawyers = Lawyer.objects.filter(
       # is_approved=True,
        specializations__icontains=specialization,
        address__icontains=location
    )
    print(lawyers)

    return render(request, 'user/search.html', {'lawyers': lawyers})
 # Import your Lawyer model

def view_lawyer_details(request, id):
    # Fetch the lawyer by ID or return 404 if not found
    lawyer = get_object_or_404(Lawyer, id=id)
    return render(request, 'user/lawyer_details.html', {'lawyer': lawyer})


def user_home(request):
    return render(request, 'user/home.html')

class UserRegisterView(View):
    template_name = 'user/register.html'

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'user'
            user.save()
            login(request, user)
            return redirect('user_home')
        return render(request, self.template_name, {'form': form})

# User Login View
class UserLoginView(FormView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        if user.is_user():
            login(self.request, user)
            return redirect('user_home')
        else:
            form.add_error(None, "You are not authorized to log in as a user.")
            return self.form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('search')
        return super().dispatch(request,*args,**kwargs)

# User Logout View
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user_login')


class ReadBlogsView(ListView):
    model = Blog
    template_name = 'user/read_blogs.html'
    context_object_name = 'blogs'


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'user/blog_detail.html', {'blog': blog})