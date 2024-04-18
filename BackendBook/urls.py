
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404

from app import views


handler404 = 'app.views.custom_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.landing,name='landing'),
    path("book/",views.book,name='book'),
    path("bookChange/",views.bookChange,name='bookChange'),
    path("bookChange/<int:id>/",views.delete_book,name='Delbook'),
    path("contect/",views.contect,name='contect'),
    path("book/recommend/<slug:id>/",views.recomand,name='recommend-more'),
    path("login/",views.logine,name='login'),
    path("logout/",views.user_logout,name='logout'),
    path("singin/",views.singup,name='singin'),
    path("update/",views.update,name='update'),
    path("app/",include('app.urls'))
]

