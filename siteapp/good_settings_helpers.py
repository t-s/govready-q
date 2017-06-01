from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class AllauthAccountAdapter(DefaultAccountAdapter):
    def authenticate(self, request, **credentials):
        ret = super(AllauthAccountAdapter, self).authenticate(request, **credentials)

        # Log login attempts.
        import logging
        logger = logging.getLogger(__name__)
        logger.error("login ip={ip} username={username} result={result}".format(
                ip=request.META.get("REMOTE_ADDR"),
                username=credentials.get("username"),
                result=("user:%d" % ret.id) if ret else "fail"
            ))

        return ret

    def send_mail(self, template_prefix, email, context):
        from htmlemailer import send_mail
        send_mail(
            template_prefix,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            context
        )


def signup_wrapper(request, *args, **kwargs):
    from allauth.account.views import signup
    ret = signup(request, *args, **kwargs)

    # Log login attempts.
    if request.method == "POST":
        import django.http.response
        import django.template.response

        result = "?"
        if isinstance(ret, django.template.response.TemplateResponse):
            try:
                result = "error:" + repr(ret.context_data['form'].errors)
            except:
                result = "error:" + type(ret)
        elif isinstance(ret, django.http.response.HttpResponseRedirect):
            result = "success"

        import logging
        logger = logging.getLogger(__name__)
        logger.error("signup ip={ip} username={username} result={result}".format(
                ip=request.META.get("REMOTE_ADDR"),
                username=request.POST.get("username"),
                result=result
            ))

    return ret

if settings.ALLAUTH_FORM_RENDERER:
    # Monkey-patch allauth to return forms that render with django-bootstrap3.
    import allauth.account.views
    allauth_get_form_class_original = allauth.account.views.get_form_class
    def allauth_get_form_class_patch(*args, **kwargs):
        form = allauth_get_form_class_original(*args, **kwargs)
        class F(form):
            def as_p(self):
                return settings.ALLAUTH_FORM_RENDERER(self)
        return F
    allauth.account.views.get_form_class = allauth_get_form_class_patch
