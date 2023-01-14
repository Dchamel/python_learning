from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main Page',
        'values': ['some', 'Hello', 123],
        'dict': {
            'car': 'Mercedes',
            'age': 5,
            'color': 'Silver'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
