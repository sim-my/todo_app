from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.add, name="add"),
    path('add/items', views.add_items, name="add_items"),
    path('delete/items/<int:todo_id>', views.delete_items, name="delete_items"),

]
