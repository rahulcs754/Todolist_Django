from django.shortcuts import render,redirect
from .models import TodoList, Category

def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] 
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
                
            try:
                checkedlist = request.POST["checkedbox"]    
                #checked todos to be deleted
                for todo_id in checkedlist:
                    todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                    todo.delete() #deleting todo    
            except:
                return render(request,'errors/error.html')
            
                 
       
             
    return render(request, "index.html", {"todos": todos, "categories":categories})


def handler404x(request, exception):
    return render(request, 'errors/404.html')

def handler500x(request):
    return render(request, 'errors/500.html')

