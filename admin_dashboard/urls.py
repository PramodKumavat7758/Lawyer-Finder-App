from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('lawyers/', views.lawyer_list, name='lawyer_list'),
    path('lawyer/approve/<int:lawyer_id>/', views.approve_lawyer, name='approve_lawyer'),
    path('lawyer/update/<int:lawyer_id>/', views.update_lawyer, name='update_lawyer'),
    path('lawyer/delete/<int:lawyer_id>/', views.delete_lawyer, name='delete_lawyer'),
    path('users/', views.user_list, name='user_list'),
    path('user/update/<int:user_id>/', views.update_user, name='update_user'),
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
