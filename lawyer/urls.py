from django.urls import path
from lawyer.views import AddBlogView, ViewBlogsView, LawyerDashboardView, LawyerRegisterView, LawyerLoginView, \
    LawyerLogoutView, LawyerUpdateView, UpdateBlogView, DeleteBlogView

urlpatterns = [

    #Lawyer Profile Management

    path('lawyer_register/', LawyerRegisterView.as_view(), name='lawyer_register'),
    path('dashboard/', LawyerDashboardView.as_view(), name='lawyer_dashboard'),
    path('update/',LawyerUpdateView.as_view(), name='lawyer_update'),
    path('lawyer_login/', LawyerLoginView.as_view(), name='lawyer_login'),
    path('logout/', LawyerLogoutView.as_view(), name='lawyer_logout'),

    #Blogs Managements
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('manage_blogs/', ViewBlogsView.as_view(), name='view_blogs'),
    path('update_blog/<int:pk>/', UpdateBlogView.as_view(), name='update_blogs'),
    path('delete_blog/<int:pk>/', DeleteBlogView.as_view(), name='delete_blogs'),



]






