"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import HomeView, ArticleView, AddPostView, EditView, Deletion,AboutPageView

urlpatterns = [
    # path('', views.home,name="home"),
    path ( '', HomeView.as_view (), name="home" ),
    path ( 'article/<int:pk>', ArticleView.as_view (), name='article-detail' ),
    path ( 'add_post/', AddPostView.as_view (), name='add_post' ),
    path ( 'article1/<int:pk>', EditView.as_view (), name='edit_post1' ),
    path ( 'delete/<int:pk>', Deletion.as_view (), name='deletion_post' ),
    path('about/',AboutPageView.as_view(),name='about')

]
