from django.shortcuts import render
from .models import user, Product, Category, Order, OrderDetail
import random
from django.shortcuts import get_object_or_404
from django.http import Http404
# Create your views here.

# user
def main(request):
    categories = Category.objects.all()
    full_products = Product.objects.all()
    fd2 = sorted(full_products, key=lambda x: random.random())
    fd3 = sorted(full_products, key=lambda x: random.random())
    rd = sorted(full_products, key=lambda x: random.random())
    eight_rd = rd[:8]
    return render(request, "user/index.html", {'categories': categories, 'random_eight': eight_rd,
     'all_products': full_products, 'all_products2':fd2, 'all_products3':fd3})




def shop_details(request):
    categories = Category.objects.all()
    name = request.GET.get('name', '')
    try:
        product_detail = Product.objects.get(name=name)
    except Product.DoesNotExist:
        product_detail = None
    rd_cmt = random.randint(5, 50000)
    rd_wg = random.uniform(0.01, 3.5)
    rd_wg = round(rd_wg, 2)
    return render(request, "user/shop-details.html", {'product_detail': product_detail, 'cmt' : rd_cmt, 'weight' : rd_wg, 'categories': categories})

def name_key(request):
    try:
        key = request.GET['keyy']
    except ValueError:
        key = 'All'
    
    try:
        num = int(request.GET['page'])
    except KeyError:
        num = 1


    if (key == 'All'):
        return shop_gridbyNumber(request)
    else:
        start_index = (num - 1) * 9
        end_index = start_index + 9
        categories = Category.objects.all()
        products = Product.objects.all()[start_index:end_index]
        full_products = Product.objects.all()
        all_pro_with_key = Product.objects.filter(name__icontains=key)
        length = len(all_pro_with_key)
        iteration_range = range(1, length // 9 + 2)

        return render(request, "user/shop-grid.html", {'categories': categories, 'products': all_pro_with_key, 'quantity': length, 'iteration_range': iteration_range, 'all_products': full_products})


def genre_list(request):
    try:
        num = int(request.GET.get('page', 1))
    except ValueError:
        num = 1

    category_name = request.GET.get('category')
    if not category_name:
        raise Http404("Category not specified")

    category = get_object_or_404(Category, name=category_name)
    products_in_category = Product.objects.filter(category=category)

    start_index = (num - 1) * 9
    end_index = start_index + 9
    products = products_in_category[start_index:end_index]

    full_products = Product.objects.all()
    length = len(products_in_category)
    iteration_range = range(1, length // 9 + 2)

    categories = Category.objects.all()

    return render(request, "user/shop-grid.html", {'categories': categories, 'products': products, 'quantity': length, 'iteration_range': iteration_range, 'all_products': full_products})

def shop_gridbyNumber(request):
    try:
        num = int(request.GET['page'])
    except KeyError:
        num = 1
    start_index = (num - 1) * 9
    end_index = start_index + 9
    categories = Category.objects.all()
    products = Product.objects.all()[start_index:end_index]
    full_products = Product.objects.all()
    length = len(full_products)
    iteration_range = range(1, length // 9 + 2)

    return render(request, "user/shop-grid.html", {'categories': categories, 'products': products, 'quantity': length, 'iteration_range': iteration_range, 'all_products': full_products})

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