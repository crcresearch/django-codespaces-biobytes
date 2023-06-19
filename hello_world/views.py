from django.shortcuts import render

def test_view(request):
    return render(request, "test.html", {})
from django.shortcuts import render

def map_view(request):
    return render(request, "map.html", {})