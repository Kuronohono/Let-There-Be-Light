from django.shortcuts import render

def light_view(request):
  return render(request, 'light_template.html')
