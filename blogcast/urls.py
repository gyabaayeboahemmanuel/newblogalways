from django.contrib import admin
from django.urls import path,include
from article import views
from account.views import signup,login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = (
    [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('articles/', include('article.urls')),
    path("signup", signup, name="signup"), 
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    #path("accounts/login", login, name="login"), 
    path('', views.index, name = "index" ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
   # path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('blog/', include('blog.urls')),
    #path('api/v1/', include('blog.api.v1.routers.routers')), 
    #path("podcast/", include('podcast.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)