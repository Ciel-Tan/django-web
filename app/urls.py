from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.main, name="index"),
    path("shop_details/", views.shop_details, name="shop_details"),
    path("shop_grid/", views.shop_gridbyNumber, name="shop_grid"),
    path("shopping_cart/", views.shopping_cart, name="shopping_cart"),
    path("genre_list/", views.genre_list, name="genre_list"),
    path("search/", views.name_key, name="name_key"),
    path("reset_cart/", views.reset_cart, name="reset_cart"),

    path('login/', views.login, name='login'),
    path('login_handler/', views.login_handler, name='login_handler'),
    path("signup/", views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),

    path("admin_list/", views.admin_list, name="admin_list"),
    path("form_add/", views.form_add, name="form_add"),
    path("form_update/", views.form_update, name="form_update"),

    path("index_logged", views.index_logged, name="index_logged"),
    path("shop_details_logged/", views.shop_details_logged, name="shop_details_logged"),
    path("shop_grid_logged/", views.shop_grid_logged, name="shop_grid_logged"),
    path("shopping_cart_logged/", views.shopping_cart_logged, name="shopping_cart_logged"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)