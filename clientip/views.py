from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    # get the stored ip address from session
    ip = request.session.get('ip', 0) # return 'ip' if found else return 0
    user = User.objects.get(username=request.user.username) # currently logged in user
    context = {
        'ip': ip,
        'user': user
    }
    return render(request, 'clientip/home.html', context=context)