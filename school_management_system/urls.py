"""school_management_system URL Configuration

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

from school_management_system import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('refresh/', views.refresh),
    path('teachers/', views.teachers),
    path('dashboard/', views.dashboard),
    path('tea_id/<str:id>', views.tea_id, name='tea_id'),
    path('std_id/<str:id>', views.std_id, name='std_id'),
    path('class_token/<str:token>', views.class_token, name='class_token'),


]
