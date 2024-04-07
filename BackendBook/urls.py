
from django.contrib import admin
from django.urls import path,include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='name'),
    path("recommend/<slug:id>/",views.recomand,name='recommend-more'),
    path("login/",views.logine,name='login'),
    path("logout/",views.user_logout,name='logout'),
    path("singin/",views.singup,name='singin'),
    path("update/",views.update,name='update'),
    path("app/",include('app.urls'))
]
