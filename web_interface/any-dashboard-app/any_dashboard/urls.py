from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

admin.site.site_header = 'Camsecuro'

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('cameras/', include('camsecuro.urls')),
    path('exit', lambda request: redirect('/accounts/logout/', permanent=True)),
    path('admin/', admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path('', lambda request: redirect('cameras/', permanent=True))
]
