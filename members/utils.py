from django.conf import settings
from django.utils.encoding import smart_bytes
from django.utils.functional import allow_lazy
from django.utils.http import urlencode
from django.utils.six import text_type
from django.utils.text import Truncator

from hashlib import sha1, md5
import random, datetime
import warnings


def get_gravatar(email, size=80, default='identicon'):
    grav_url ='//www.gravatar.com/avatar/{}'
    ident = email.lower().encode('utf-8')
    grav_url = grav_url.format(md5(ident).hexdigest())

    grav_url += urlencode({
        's': str(size),
        'd': default
    })
    return grav_url

def signin_redirect(redirect=None, user=None):
    return settings.LOGIN_REDIRECT_URL

def generate_sha1(string, salt=None):
    if not isinstance(string, (str, text_type)):
        string = str(string)

    if not salt:
        salt = sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

    salted_bytes = (smart_bytes(salt) + smart_bytes(string))
    hash_ = sha1(salted_bytes).hexdigest()

    return salt, hash_

def get_profile_model():
    """
    Return the model class for the currently-active user profile
    model, as defined by the ``AUTH_PROFILE_MODULE`` setting.
    :return: The model that is used as profile.
    """
    if (not hasattr(settings, 'AUTH_PROFILE_MODULE')) or \
           (not settings.AUTH_PROFILE_MODULE):
        raise SiteProfileNotAvailable

    try:
        profile_mod = get_model(*settings.AUTH_PROFILE_MODULE.rsplit('.', 1))
    except LookupError:
        profile_mod = None

    if profile_mod is None:
        raise SiteProfileNotAvailable
    return profile_mod

def get_user_profile(user):
    profile_model = get_profile_model()
    try:
        profile = user.get_profile()
    except AttributeError:
        related_name = profile_model._meta.get_field('user')\
                                    .related_query_name()
        profile = getattr(user, related_name, None)
    except profile_model.DoesNotExist:
        profile = None
    if profile:
        return profile
    return profile_model.objects.create(user=user)

def get_protocol():
    """
    Returns a string with the current protocol.
    This can be either 'http' or 'https' depending on ``USERENA_USE_HTTPS``
    setting.
    """
    protocol = 'http'
    if getattr(settings, 'USERENA_USE_HTTPS', userena_settings.DEFAULT_USERENA_USE_HTTPS):
        protocol = 'https'
    return protocol

def get_datetime_now():
    """
    Returns datetime object with current point in time.
    In Django 1.4+ it uses Django's django.utils.timezone.now() which returns
    an aware or naive datetime that represents the current point in time
    when ``USE_TZ`` in project's settings is True or False respectively.
    In older versions of Django it uses datetime.datetime.now().
    """
    try:
        from django.utils import timezone
        return timezone.now() # pragma: no cover
    except ImportError: # pragma: no cover
        return datetime.datetime.now()

# Django 1.5 compatibility utilities, providing support for custom User models.
# Since get_user_model() causes a circular import if called when app models are
# being loaded, the user_model_label should be used when possible, with calls
# to get_user_model deferred to execution time

user_model_label = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


def get_user_model():
    warnings.warn("Use Django's django.contrib.auth.get_user_model directly. "
                  "This function will be removed in future versions of "
                  "django-userena.", DeprecationWarning)
    from django.contrib.auth import get_user_model
    return get_user_model()
