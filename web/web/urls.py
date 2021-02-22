"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import accounts.views # 수정할 것 !

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.index, name="index"), # 이부분(accounts/views.py) 수정할 것 ! 
    path('qna/', include('qna.urls')),
    path('accounts/', include('accounts.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('vote/', include('vote.urls')),
]
