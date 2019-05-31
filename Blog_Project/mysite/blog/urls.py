from django.conf.urls import url
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
   url(r'^$',views.PostListView.as_view(),name='post_list'),
   url(r'^about/$',views.AboutView.as_view(),name='about'),
   url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
   url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
   url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
   url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
   url(r'^myposts/$',views.my_posts_list,name='my_posts'),
   url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
   url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
   url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
   url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
   url(r'^post/(?P<pk>\d+)/like/$',views.post_like,name='post_like'),
   url(r'^comment/(?P<pk>\d+)/like/$',views.comment_like,name='comment_like'),
   url(r"^login/$", auth_views.LoginView.as_view(template_name="login.html"),name='userlogin'),
   url(r"^logout/$", auth_views.LogoutView.as_view(), name="userlogout"),
   url(r"^signup/$", views.SignUp.as_view(), name="signup"),
]