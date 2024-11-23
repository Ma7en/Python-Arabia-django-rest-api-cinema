"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# tickets
from tickets import views as tickets_views

router = DefaultRouter()
router.register("guests", tickets_views.viewsets_guest)
router.register("movies", tickets_views.viewsets_movie)
router.register("reservations", tickets_views.viewsets_reservation)

urlpatterns = [
    path("admin/", admin.site.urls),
    # 1-
    path("django/jsonresponsenomodel/", tickets_views.no_rest_no_model),
    # =================================================================
    # 2-
    path("django/jsonresponsefrommodel/", tickets_views.no_rest_fram_model),
    # =================================================================
    # 3.1- get - post           -> from rest framework function based view @api_view
    path("rest/fbvlist/", tickets_views.FBV_List),
    # 3.2- get - put - delete   -> from rest framework function based view @api_view
    path(
        "rest/fbvlist/<int:pk>",
        tickets_views.FBV_pk,
    ),
    # =================================================================
    # 4.1- get - post           -> from rest framework class based view APIview
    path(
        "rest/cbvlist/",
        tickets_views.CBV_List.as_view(),
    ),
    # 4.2- get - put - delete   -> from rest framework class based view APIview
    path(
        "rest/cbvlist/<int:pk>",
        tickets_views.CBV_pk.as_view(),
    ),
    # =================================================================
    # 5.1- get - post           -> from rest framework class based view mixins
    path(
        "rest/mixinslist/",
        tickets_views.mixins_list.as_view(),
    ),
    # 5.2- get - put - delete   -> from rest framework class based view mixins
    path(
        "rest/mixinslist/<int:pk>",
        tickets_views.mixins_pk.as_view(),
    ),
    # =================================================================
    # 6.1- get - post           -> from rest framework class based view Generics
    path(
        "rest/genericslist/",
        tickets_views.generics_list.as_view(),
    ),
    # 6.2- get - put - delete   -> from rest framework class based view Generics
    path(
        "rest/genericslist/<int:pk>",
        tickets_views.generics_pk.as_view(),
    ),
    # =================================================================
    # 7 viewsets
    path("rest/viewsets/", include(router.urls)),
    # =================================================================
    # 8 find movie
    path("fbv/findmovie/", tickets_views.find_movie),
    # =================================================================
    # 9 new_reservation
    path("fbv/newreservation/", tickets_views.new_reservation),
    # =================================================================
    # 10 rest auth url
    path("api-auth", include("rest_framework.urls")),
    # =================================================================
    # 11 Token Authentication
    path("api-token-auth", obtain_auth_token),
    # =================================================================
    # 12- post pk generics post_pk -
    # path(
    #     "post/genericslist/",
    #     tickets_views.Post_List.as_view(),
    # ),
    path(
        "post/genericslist/<int:pk>",
        tickets_views.Post_pk.as_view(),
    ),
    # =================================================================
]
