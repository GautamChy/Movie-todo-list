from django.urls import path
from .views import todo_list
from .views import todo_list_detail


from .views import index,contact_us,about_us,home,list,create,mark,edit,delete,todo_list,todo_list_detail   # * ekai choti sabb 
urlpatterns = [
    path('index/',index),
    path('contact/',contact_us),
    path('about/',about_us),
    path('my home/',home),
    path('task/',list),
    path('task/create',create),
    path('task/<pk>/',mark),
    path('task/<pk>/edit',edit),
    path('task/<pk>/delete/', delete),
    path('todolist/',todo_list),
    path('todolist/<id>/',todo_list_detail)
    
   
    
   
     
]


