"""URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

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

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", view=include("authentication.urls"), name="auth"),
    path("users/", view=include("users.urls"), name="users"),
    path("posts/", view=include("posts.urls"), name="posts"),
    path("relations/", view=include("relations.urls"), name="relations"),
]

admin.sites.AdminSite.site_title = "Site Admin"
admin.sites.AdminSite.site_header = "Site Dashboard"
admin.sites.AdminSite.index_title = "Site Admin Panel"
