from django.shortcuts import render

# Everything regarding the first thing user will se when they enter Social Frames
def render_home(request):
    return render(request, 'storyboard/home_page.html')


def render_sign_in(request):
    return render(request, 'storyboard/sign_in.html')


def render_sign_out(request):
    return render(request, 'storyboard/sign_out.html')


def render_sign_up(request):
    return render(request, 'storyboard/sign_up.html')
