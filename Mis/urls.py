
from django.contrib import admin
from django.urls import path,include

admin.site.site_header="MIS ADMIN"
admin.site.site_title="MIS Admin Portal"
admin.site.index_title="Welcome to MIS Admin Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('user/',include('account.urls'))
]
