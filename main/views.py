from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Clement Samuel Marly',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
