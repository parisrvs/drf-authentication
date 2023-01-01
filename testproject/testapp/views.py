from django.shortcuts import render


def homepage(request):
    return render(
        request,
        "testapp/homepage.html"
    )
