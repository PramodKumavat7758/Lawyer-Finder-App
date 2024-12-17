from django.shortcuts import render, get_object_or_404, redirect

from admin_dashboard.models import CustomUser
from lawyer.models import Lawyer
from django.contrib import messages

# Admin dashboard view
def admin_dashboard(request):
    lawyer_count = Lawyer.objects.count()
    user_count = CustomUser.objects.count()
    context = {
        'lawyer_count': lawyer_count,
        'user_count': user_count,
    }
    return render(request, 'admin/dashboard.html', context)

# List of all lawyers
def lawyer_list(request):
    lawyers = Lawyer.objects.all()
    return render(request, 'admin/lawyer_list.html', {'lawyers': lawyers})

# Approve or reject a lawyer
def approve_lawyer(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, id=lawyer_id)
    lawyer.is_approved = not lawyer.is_approved
    lawyer.save()
    messages.success(request, f"Lawyer {'approved' if lawyer.is_approved else 'rejected'}.")
    return redirect('admin:lawyer_list')

# Update lawyer
def update_lawyer(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, id=lawyer_id)
    if request.method == 'POST':
        lawyer.full_name = request.POST.get('full_name', lawyer.full_name)
        lawyer.mobile = request.POST.get('mobile', lawyer.mobile)
        lawyer.email = request.POST.get('email', lawyer.email)
        lawyer.save()
        messages.success(request, "Lawyer details updated successfully.")
        return redirect('admin:lawyer_list')
    return render(request, 'admin/update_lawyer.html', {'lawyer': lawyer})

# Delete lawyer
def delete_lawyer(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, id=lawyer_id)
    lawyer.delete()
    messages.success(request, "Lawyer deleted successfully.")
    return redirect('admin:lawyer_list')

# List of all users
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'admin/user_list.html', {'users': users})

# Update user
def update_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, "User details updated successfully.")
        return redirect('admin:user_list')
    return render(request, 'admin/update_user.html', {'user': user})

# Delete user
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('admin:user_list')
