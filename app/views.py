from django.shortcuts import render

# Create your views here.

# user
def main(request):
    return render(request, "user/index.html")

def shop_details(request):
    return render(request, "user/shop-details.html")

def shop_grid(request):
    return render(request, "user/shop-grid.html")

def shopping_cart(request):
    return render(request, "user/shopping-cart.html")

# account
def login(request):
    return render(request, "account/login.html")

def signup(request):
    return render(request, "account/signup.html")

# admin
def admin_list(request):
    return render(request, "admin/admin-list.html")

def form_add(request):
    return render(request, "admin/form_add.html")

def form_update(request):
    return render(request, "admin/form_update.html")

# user logged
def index_logged(request):
    return render(request, "user_logged/index_logged.html")

def shop_details_logged(request):
    return render(request, "user_logged/shop-details_logged.html")

def shop_grid_logged(request):
    return render(request, "user_logged/shop-grid_logged.html")

def shopping_cart_logged(request):
    return render(request, "user_logged/shopping-cart_logged.html")