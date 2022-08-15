from . import views
from django.urls import path, include
app_name='movieapp'
urlpatterns = [
    path('',views.fun1,name='fun1'),
    path('movie/<int:movie_id>',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('edit/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]
