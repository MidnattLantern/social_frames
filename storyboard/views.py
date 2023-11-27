from django.shortcuts import render

# Everything regarding the first thing user will se when they enter Social Frames
def render_home(request):
    return render(request, 'storyboard/home_page.html')
