from django.shortcuts import render
from .models import user, Product, Category, Order, OrderDetail
import random
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
# user
def main(request):
    user = request.user
    if user.is_authenticated:
        latest_order = Order.objects.filter(user=user).order_by('-id').first()
        order_details = OrderDetail.objects.filter(order=latest_order)
        qty_buy = len(order_details)
        tt_price = [carting.quantity * carting.product.price for carting in order_details]
        full_pr = 0
        for zx in tt_price:
            full_pr += zx
    else:
        qty_buy = 0
        full_pr = 0
    
    categories = Category.objects.all()
    full_products = Product.objects.all()
    fd2 = sorted(full_products, key=lambda x: random.random())
    fd3 = sorted(full_products, key=lambda x: random.random())
    rd = sorted(full_products, key=lambda x: random.random())
    eight_rd = rd[:8]
    return render(request, "user/index.html", {'username' : user.username ,'categories': categories, 'random_eight': eight_rd,
     'all_products': full_products, 'all_products2':fd2, 'all_products3':fd3, 'qty_buy': qty_buy, 'full_pr':full_pr})



def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        
        if user.is_authenticated:
            prod_name = request.POST['product_name_add']
            prod_QTY  = int(request.POST['product_quantity_add'])
            product_add = Product.objects.get(name=prod_name)
            
            # Lấy đơn hàng mới nhất của người dùng
            latest_order = Order.objects.filter(user=user).order_by('-id').first()
            if not latest_order:
                latest_order = Order.objects.create(user=user, status='Pending')
            
            # Kiểm tra nếu sản phẩm đã có trong chi tiết đơn hàng của đơn hàng mới nhất
            order_detail = OrderDetail.objects.filter(order=latest_order, product=product_add).first()

            if order_detail:
                order_detail.quantity += prod_QTY
                if order_detail.quantity > product_add.stock:
                    order_detail.quantity = product_add.stock
                order_detail.price = order_detail.product.price * order_detail.quantity
                order_detail.save()
            else:
                OrderDetail.objects.create(
                    order=latest_order,
                    product=product_add,
                    quantity=prod_QTY,
                    price=product_add.price * prod_QTY
                )
            return redirect('../shopping_cart/')
        else:
            return redirect('login')
         




def shop_details(request):
    user = request.user
    if user.is_authenticated:
        latest_order = Order.objects.filter(user=user).order_by('-id').first()
        order_details = OrderDetail.objects.filter(order=latest_order)
        qty_buy = len(order_details)
        tt_price = [carting.quantity * carting.product.price for carting in order_details]
        full_pr = 0
        for zx in tt_price:
            full_pr += zx
    else:
        qty_buy = 0
        full_pr = 0
    
    cart_items = request.session.get('cart_items', [])
    categories = Category.objects.all()
    name = request.GET.get('name', '')
    try:
        product_detail = Product.objects.get(name=name)
    except Product.DoesNotExist:
        product_detail = None
    
    rd_cmt = random.randint(5, 50000)
    rd_wg = random.uniform(0.01, 3.5)
    rd_wg = round(rd_wg, 2)
    return render(request, "user/shop-details.html", {'username' : user.username,'product_detail': product_detail,
                             'cmt' : rd_cmt, 'weight' : rd_wg, 'categories': categories, 'qty_buy':qty_buy, 'full_pr': full_pr})

def name_key(request):
    user = request.user
    if user.is_authenticated:
        latest_order = Order.objects.filter(user=user).order_by('-id').first()
        order_details = OrderDetail.objects.filter(order=latest_order)
        qty_buy = len(order_details)
        tt_price = [carting.quantity * carting.product.price for carting in order_details]
        full_pr = 0
        for zx in tt_price:
            full_pr += zx
    else:
        qty_buy = 0
        full_pr = 0
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

        return render(request, "user/shop-grid.html", {'username': user.username,'categories': categories,
                                                        'products': all_pro_with_key, 'quantity': length,
                                                 'iteration_range': iteration_range,
                                                     'all_products': full_products, 'qty_buy':qty_buy, 'full_pr': full_pr})


def genre_list(request):
    user = request.user
    if user.is_authenticated:
        latest_order = Order.objects.filter(user=user).order_by('-id').first()
        order_details = OrderDetail.objects.filter(order=latest_order)
        qty_buy = len(order_details)
        tt_price = [carting.quantity * carting.product.price for carting in order_details]
        full_pr = 0
        for zx in tt_price:
            full_pr += zx
    else:
        qty_buy = 0
        full_pr = 0
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

    return render(request, "user/shop-grid.html", {'username' : user.username,'categories': categories, 'products': products, 
                                                   'quantity': length, 'iteration_range': iteration_range,
                                                     'all_products': full_products, 'qty_buy':qty_buy, 'full_pr': full_pr})

def shop_gridbyNumber(request):
    user = request.user
    if user.is_authenticated:
        latest_order = Order.objects.filter(user=user).order_by('-id').first()
        order_details = OrderDetail.objects.filter(order=latest_order)
        qty_buy = len(order_details)
        tt_price = [carting.quantity * carting.product.price for carting in order_details]
        full_pr = 0
        for zx in tt_price:
            full_pr += zx
    else:
        qty_buy = 0
        full_pr = 0
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

    return render(request, "user/shop-grid.html", {'username': user.username, 'categories': categories,
                                                    'products': products, 'quantity': length,
                                                      'iteration_range': iteration_range, 'all_products': full_products,
                                                        'qty_buy':qty_buy, 'full_pr': full_pr})

def shopping_cart(request):
    user = request.user
    if request.user.is_authenticated:

        latest_order = Order.objects.filter(user=user).order_by('-id').first()

    else:
        return redirect('../login')
    if not latest_order:
        return render(request, 'error.html', {'message': 'Bạn chưa có đơn hàng nào.'})
    categories = Category.objects.all()
    order_details = OrderDetail.objects.filter(order=latest_order)
    qty_buy = len(order_details)
    tt_price = [carting.quantity * carting.product.price for carting in order_details]
    # zipped_data = zip(order_details, tt_price)
    full_pr = 0
    for zx in tt_price:
        full_pr += zx
    return render(request, "user/shopping-cart.html", {'username': user.username, 'order_details': order_details, 'full_pr': full_pr, 'categories': categories, 'qty_buy':qty_buy})

def delete_cart(request):
    prod_name_del = request.GET['name']
    prod_del = Product.objects.get(name=prod_name_del)
    cart_to_delete = OrderDetail.objects.get(product=prod_del)
    cart_to_delete.delete()
    return redirect('../shopping_cart/')

def proceed_cart(request):
    user=request.user
    if request.method == 'POST':
       for key, value in request.POST.items():
            if key.startswith('quantity_'):
                product_id = key.split('_')[1]
                quantity = int(value)
                product = get_object_or_404(Product, id=product_id)
                product.stock -= quantity
                if product.stock < 0:
                    product.stock = 1
                latest_order = Order.objects.filter(user=user).order_by('-id').first()
                latest_order.status = 'Delivered'
                latest_order.save()
                user = request.user
                Order.objects.create(user=user)
                product.save()
    return render(request, "user/complete.html")

def reset_cart(request):
    user = request.user
    Order.objects.create(user=user)
    return redirect('../shop_grid')


def updateQTY_cart(request):
    if request.method == 'POST':
        user = request.user
        latest_order = Order.objects.filter(user=user).order_by('-id').first()
        if 'update_cart' in request.POST:
            for key, value in request.POST.items():
                if key.startswith('quantity_'):
                    product_id = key.split('_')[1]
                    quantity = int(value)
                    product = get_object_or_404(Product, id=product_id)
                    order_detail, created = OrderDetail.objects.get_or_create(order=latest_order, product=product)
                    order_detail.quantity = quantity
                    order_detail.price = product.price * quantity
                    order_detail.save()
        
            return redirect('../shopping_cart/')
        
        elif 'continue_shopping' in request.POST:
            cart_items = []
            for item in OrderDetail.objects.filter(order=latest_order):
                cart_items.append({
                    'product_id': item.product.id,
                    'quantity': item.quantity,
                    'product_name': item.product.name,
                    'product_price': item.product.price,
                    'product_img_url': item.product.img.url,
                    'total_price': item.price,
                })
            request.session['cart_items'] = cart_items
            return redirect('../shop_grid/')
        
    return redirect('../shopping_cart/')
        


# account
def login(request):
    return render(request, "account/login.html")

def logout(request):
    auth.logout(request)
    return redirect("../")


User = get_user_model()


def login_handler(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                if not user.is_staff:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    return render(request, 'account/login.html', {'error': 'Permission denied-Only users are allowed'})
            else:
                return render(request, 'account/login.html', {'error': 'User account is disabled'})
        
        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, "account/signup.html")

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