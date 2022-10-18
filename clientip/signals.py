from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("---------------------")
    print('user logged in')
    print('user--->', user)
    ip = request.META.get('REMOTE_ADDR') # gives logged in user's IP address
    print('clientip--->', ip)

    # Here, we will save this user's IP to the session and then show it on the page from session
    request.session['ip'] = ip # stored in session

