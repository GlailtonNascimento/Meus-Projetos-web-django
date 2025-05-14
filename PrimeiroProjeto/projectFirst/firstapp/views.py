from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# View baseada em função
def hello_world(request):
    return HttpResponse("Hello, world!")

# View baseada em classe
class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse("Hello, Ethiopia!")