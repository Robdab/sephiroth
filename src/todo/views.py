from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from todo.models import List  


def index(request):
    pass_to_template = 'this string was passed from views.py to the template.'
    return render_to_response('index.html', {'pass_to_template': pass_to_template})

def status_report(request):
    todo_listing = []

    for todo_list in List.objects.all():
        todo_dict = {}
        todo_dict['list_object'] = todo_list  
        todo_dict['item_count'] = todo_list.item_set.count()  
        todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()  
        todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)  
        todo_listing.append(todo_dict)

    return render_to_response('todo/status_report.html', { 'todo_listing': todo_listing })