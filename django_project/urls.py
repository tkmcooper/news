from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),  # Include the URLs from the pages app
    path("accounts/", include("django.contrib.auth.urls")),  # Add this line to include built-in auth URLs
    path("accounts/", include("accounts.urls")),

]
