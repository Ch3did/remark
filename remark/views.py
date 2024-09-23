from django.shortcuts import redirect


def redirect_admin(request):
    response = redirect("/admin/")
    return response
