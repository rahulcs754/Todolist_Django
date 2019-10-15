from django.contrib import admin
from django.urls import path
from todolist.views import index, handler404x, handler500x
# for error
from django.conf.urls import handler400, handler403, handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="TodoList"),
] 


# for error
handler404 = 'todolist.views.handler404x'
handler500 = 'todolist.views.handler500x'
