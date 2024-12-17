from django.urls import path
from .views import UserLogoutView, user_home, search, ReadBlogsView
from .views import  UserLoginView, UserRegisterView
from .views import  view_lawyer_details
from .views import  blog_detail
urlpatterns = [
    path('user_register/', UserRegisterView.as_view(), name='user_register'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),


    path('search_lawyer/', search, name='search'),
path('lawyer_detail/<int:id>/', view_lawyer_details, name='view_lawyer_details'),
    path('read_blog/', ReadBlogsView.as_view(), name='read_blogs'),
    path('blog_detail/<int:pk>',blog_detail, name='blog_detail'),




    path('', user_home,name='user_home'),
]
