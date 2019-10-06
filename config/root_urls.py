from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # API V1
    path('api/v1/user/', include('backend.user.urls.v1_urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
