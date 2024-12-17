from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, path, reverse
from django.views.generic import View, TemplateView, CreateView, FormView, ListView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from user.forms import UserRegistrationForm
from .forms import LawyerRegistrationForm, BlogForm, ProfileForm
from .models import Blog, Lawyer


# Dashboard for Lawyer
class LawyerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'lawyer/lawyer_dashboard.html'



class LawyerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lawyer
    template_name = 'lawyer/update_profile.html'
    fields = [
        'full_name', 'email', 'mobile', 'address',
        'specializations', 'qualifications',
        'years_of_experience', 'court_duty', 'profile_photo'
    ]

    def get_object(self, queryset=None):
        # Ensure we're updating the currently logged-in lawyer's profile
        try:
            return self.request.user.lawyer_profile
        except Lawyer.DoesNotExist:
            raise PermissionDenied("You do not have permission to update this profile.")

    def get_success_url(self):
        # Redirect to the lawyer dashboard after successful update
        return reverse_lazy('lawyer_dashboard')

    def test_func(self):
        # Ensure only logged-in lawyers can access this view
        return self.request.user.is_authenticated and self.request.user.is_lawyer()











# Lawyer Registration View
class LawyerRegisterView(View):
    template_name = 'lawyer/register.html'

    def get(self, request):
        lawyer_form = UserRegistrationForm()
        profile_form = ProfileForm()
        return render(request, self.template_name, {
            'lawyer_form': lawyer_form,
            'profile_form': profile_form,
        })

    def post(self, request):
        lawyer_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if lawyer_form.is_valid() and profile_form.is_valid():
            # Create lawyer user
            lawyer_user = lawyer_form.save(commit=False)
            lawyer_user.set_password(lawyer_form.cleaned_data['password'])
            lawyer_user.save()

            # Create lawyer profile
            profile = profile_form.save(commit=False)
            profile.user = lawyer_user
            profile.save()

            # Log in the user
            login(request, lawyer_user)
            return redirect('lawyer_dashboard')

        return render(request, self.template_name, {
            'lawyer_form': lawyer_form,
            'profile_form': profile_form,
        })
# Lawyer Login View
class LawyerLoginView(FormView):
    template_name = 'lawyer/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        if user.is_lawyer():
            login(self.request, user)
            return redirect('lawyer_dashboard')
        else:
            form.add_error(None, "You are not authorized to log in as a lawyer.")
            return self.form_invalid(form)

# Lawyer Logout View
class LawyerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('lawyer_login')







class AddBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/add_blog.html'
    success_url = reverse_lazy('view_blogs')  # Redirect to the page where blogs are displayed

    def form_valid(self, form):
        # Ensure the user is a lawyer
        if self.request.user.is_lawyer():
            # Retrieve the Lawyer profile of the logged-in user
            lawyer_profile = self.request.user.lawyer_profile  # Accessing the related Lawyer profile
            form.instance.author = lawyer_profile  # Assign the Lawyer instance to the Blog's author field
            return super().form_valid(form)
        else:
            # If the user is not a lawyer, handle appropriately (optional)
            return redirect('not_authorized')  # Example redirect if the user is not a lawyer

class UpdateBlogView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/update_blog.html'
    success_url = reverse_lazy('view_blogs')

    def get_queryset(self):
        if self.request.user.is_lawyer():
            return Blog.objects.filter(author=self.request.user.lawyer_profile)
        return Blog.objects.none()


class DeleteBlogView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/delete_blog.html'
    success_url = reverse_lazy('view_blogs')

    def get_queryset(self):
        if self.request.user.is_lawyer():
            return Blog.objects.filter(author=self.request.user.lawyer_profile)
        return Blog.objects.none()

# View Blogs
class ViewBlogsView(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'blogs/manage_blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        # Ensure the user is a lawyer
        if self.request.user.is_lawyer():  # Call the method to check the role
            # Filter blogs by the logged-in lawyer's profile
            return Blog.objects.filter(author=self.request.user.lawyer_profile)
        return Blog.objects.none()



