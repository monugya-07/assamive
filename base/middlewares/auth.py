from django.shortcuts import redirect
from django.urls import reverse


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # if not request.session.get("customer"):
        # returnUrl = request.META["PATH_INFO"]
        # return redirect("login")
        # if not request.session.get("customer"):
        #     return redirect(f"login?return_url={returnUrl}")

        if not request.session.get("customer"):
            returnUrl = request.get_full_path()
            login_url = reverse("login") + f"?return_url={returnUrl}"
            return redirect(login_url)

        response = get_response(request)

        return response

    return middleware
