from django.shortcuts import render

# Crea le tue views qui.

def post_list(request):
    return render(request, 'blog/post_list.html', {})