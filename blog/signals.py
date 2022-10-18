from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception

"""
    Basics of signals:
    - While using "@receiver decorator", not need to use custom "signal.connet()" method. It will be automatic
    
    ## If "@receiver decorator" is not used then we can use "signal.connet()" to establish the connection
    # to connect a signal
        - syntax: signal.connet(receiver_func, sender) # we are connecting to the reciever function
"""
############################ Signals for log in - log out - log in failed ############################
# receiver function for logged_in signal
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    # we can show all kinds of details of the user here
    # email, password (hash format), email etc...
    print("-----------------------------")
    print("logged in signal... Run Intro....")
    print("sender--->", sender)
    print("Request--->", request)
    print("User--->", user)
    print("User--->", user.password)
    print(f"kwargs: {kwargs}")
# user_logged_in.connect(login_success, sender=User) # when not using "@receiver decorator"


# receiver function for logged_out signal
@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    # we can show all kinds of details of the user here
    # email, password (hash format), email etc...
    print("-----------------------------")
    print("Logged out signal... Run Outro....")
    print("sender--->", sender)
    print("Request--->cvcvv", request)
    print("User--->", user)
    print(f"kwargs: {kwargs}")
# user_logged_out.connect(logout_success, sender=User) # when not using "@receiver decorator"

# receiver function for logged_out signal
@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    # we can show all kinds of details of the user here
    # email, password (hash format), email etc...
    print("-----------------------------")
    print("Login failed signal... Failed Run Intro....")
    print("credentials--->", credentials)
    print("Request--->", request)
    print(f"kwargs: {kwargs}")
# user_login_failed.connect(login_failed) # when not using "@receiver decorator"

############################ Signals for pre-save, post-save ############################
@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print('--------------------------')
    print('pre save signals...')
    print('sender--->', sender)
    print('Instance-->', instance)
    print(f'kwargs: {kwargs}')
# pre_save.connect(at_beginning_save, sender=User)

@receiver(post_save, sender=User)
def at_ending_request(sender, instance, created, **kwargs):
    if created:
        print('--------------------------')
        print('post save signal...')
        print('New record')
        print('sender--->', sender)
        print(' Instance--->', instance)
        print(' created--->', created)
        print(f'kwargs: {kwargs}')
    else:
        print('--------------------------')
        print('post save signal...')
        print('Updated record')
        print('sender--->', sender)
        print(' Instance--->', instance)
        print(' created--->', created)
        print(f'kwargs: {kwargs}')
# post_save.connect(at_ending_request)

############################ Signals for pre-delete, post-delete ############################
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print('--------------------------')
    print('Pre delete signals...')
    print('sender--->', sender)
    print('Instance-->', instance)
    print(f'kwargs: {kwargs}')
# pre_delete.connect(at_beginning_delete, sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print('--------------------------')
    print('Post delete signals...')
    print('sender--->', sender)
    print('Instance-->', instance)
    print(f'kwargs: {kwargs}')
# post_delete.connect(at_ending_delete, sender=User)

############################ Signals for pre-init, post-inint ############################
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print('--------------------------')
    print('pre Init...')
    print('sender--->', sender)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
# pre_init.connect(at_beginning_init, sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print('--------------------------')
    print('post Init...')
    print('sender--->', sender)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
# post_init.connect(at_ending_init, sender=User)

############################ Signals for request-started, request-finished, get-request-exception ############################
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('--------------------------')
    print('At beginning Request...')
    print('sender--->', sender)
    print('Environ--->', environ)
    print(f'kwargs: {kwargs}')
# request_started.connect(at_beginning_request)

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('--------------------------')
    print('At ending Request...')
    print('sender--->', sender)
    print(f'kwargs: {kwargs}')
# request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_req_exception(sender, **kwargs):
    print('--------------------------')
    print('at request exception...')
    print('sender--->', sender)
    print(f'kwargs: {kwargs}')
# got_request_exception.connect(at_req_exception)

############################ Signals for pre-migrate, post-migrate ############################
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('--------------------------')
    print('Before install app...')
    print('sender--->', sender)
    print('app_config--->', app_config)
    print('verbosity--->', verbosity)
    print('interactive--->', interactive)
    print('using--->', using)
    print('plan--->', plan)
    print('plan--->', plan)
    print('apps--->', apps)
    print('sender--->', sender)
    print(f'kwargs: {kwargs}')
# pre_migrate.connect(before_install_app)

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('--------------------------')
    print('at_end_migrate_flush...')
    print('sender--->', sender)
    print('app_config--->', app_config)
    print('verbosity--->', verbosity)
    print('interactive--->', interactive)
    print('using--->', using)
    print('plan--->', plan)
    print('plan--->', plan)
    print('apps--->', apps)
    print('sender--->', sender)
    print(f'kwargs: {kwargs}')
# post_migrate.connect(at_end_migrate_flush)