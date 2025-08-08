
from django.contrib import admin
from django.urls import path, include
import two_factor.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),

]
