"""remark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import redirect_admin

urlpatterns = [
    # path('', include('pages.urls')),
    path("", redirect_admin),
    path("admin/", admin.site.urls),
    path("laudo_plaqueta/", include("laudo_plaqueta.urls")),
    path("laudo_etiqueta/", include("laudo_etiqueta.urls")),
    path("laudo_chassi/", include("laudo_chassi.urls")),
    path("laudo_motor/", include("laudo_motor.urls")),
    path("laudo_vidros/", include("laudo_vidros.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
