from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from . import forms, models
from .models import Post,MilkRecord,Eartag,NewEartag,Vaccine,Product,Orders
def home_view(request):
    products = models.Product.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'index.html', {'products': products, 'product_count_in_cart': product_count_in_cart})


# for showing login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def customer_signup_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request, 'customersignup.html', context=mydict)





# -----------for checking user iscustomer
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()





# ---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,CUSTOMER
def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customerhome')
    else:
        return redirect('admindashboard')
def admin_dashboard_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'admin_dashboard.html', context)



def add(request):
    if request.method == "POST":
        d = Post()
        d.name = request.POST.get('name')
        d.breed = request.POST.get('breed')
        d.eartag = request.POST.get('eartag')
        d.age = request.POST.get('age')
        d.type = request.POST.get('type')
        d.weight = request.POST.get('weight')
        d.save()
        return HttpResponse('The file is saved')
       # return redirect('/')
    return render(request, 'cowapp/add.html')


def ShowView(request):
    d = Post.objects.all()
    return render(request, 'cowapp/show.html', {'d': d})


def delete(request, id):
    d = Post.objects.get(id=id)
    d.delete()
    return redirect('/show')


###vaccine

def addvaccine(request):
    if request.method == "POST":
        d = Vaccine()
        d.date_of_vaccination = request.POST.get('date_of_vaccination')
        d.save()
        return HttpResponse('The file is saved')
        #return redirect('/showvaccine')
    return render(request, 'vaccine/add.html')


def ShowVaccine(request):
    d = Vaccine.objects.all()
    return render(request, 'vaccine/show.html', {'d': d})


def deletevaccine(request, id):
    d = Vaccine.objects.get(id=id)
    d.delete()
    return redirect('/showvaccine')


#######Eartag

def addEartag(request):
    if request.method == "POST":
        d = Eartag()
        d.type = request.POST.get('type')
        d.previoustag = request.POST.get('previoustag')
        d.save()
        return HttpResponse('The file is saved')
        #return redirect('/showeartag')
    return render(request, 'eartag/add.html')


def ShowEartag(request):
    d = Eartag.objects.all()
    return render(request, 'eartag/show.html', {'d': d})


def deleteEartag(request, id):
    d = Eartag.objects.get(id=id)
    d.delete()
    return redirect('/showeartag')


############New Eartag
def addNewEartag(request):
    if request.method == "POST":
        d = NewEartag()
        d.name = request.POST.get('name')
        d.type = request.POST.get('type')
        d.age = request.POST.get('age')
        d.save()
        return HttpResponse('The file is saved')
        #return redirect('/showneweartag')
    return render(request, 'neweartag/add.html')


def ShowNewEartag(request):
    d = NewEartag.objects.all()
    return render(request, 'neweartag/show.html', {'d': d})


def deleteNewEartag(request, id):
    d = NewEartag.objects.get(id=id)
    d.delete()
    return redirect('/showneweartag')


################milkrecord

def addMilkRecord(request):
    if request.method == "POST":
        d = MilkRecord()
        d.name = request.POST.get('name')
        d.userid = request.POST.get('userid')
        d.address = request.POST.get('address')
        d.date = request.POST.get('date')
        d.morning_milk_record = request.POST.get('morning_milk_record')
        d.evening_milk_record = request.POST.get('evening_milk_record')
        d.payment = request.POST.get('payment')
        d.save()
        return HttpResponse('The file is saved')
        #return redirect('/show-milkrecord')
    return render(request, 'milkrecord/add.html')


def ShowMilkRecord(request):
    d = MilkRecord.objects.all()
    return render(request, 'milkrecord/show.html', {'d': d})


def deleteMilkRecord(request, id):
    d = MilkRecord.objects.get(id=id)
    d.delete()
    return redirect('/show-milkrecord')
# admin view the product
@login_required(login_url='adminlogin')
def admin_products_view(request):
    products = models.Product.objects.all()
    return render(request, 'admin_products.html', {'products': products})


# admin add product by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_product_view(request):
    productForm = forms.ProductForm()
    if request.method == 'POST':
        productForm = forms.ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return HttpResponseRedirect('admin-products')
    return render(request, 'admin_add_products.html', {'productForm': productForm})


@login_required(login_url='adminlogin')
def delete_product_view(request, pk):
    product = models.Product.objects.get(id=pk)
    product.delete()
    return redirect('admin-products')


@login_required(login_url='adminlogin')
def update_product_view(request, pk):
    product = models.Product.objects.get(id=pk)
    productForm = forms.ProductForm(instance=product)
    if request.method == 'POST':
        productForm = forms.ProductForm(request.POST, request.FILES, instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect('admin-products')
    return render(request, 'admin_update_product.html', {'productForm': productForm})
@login_required(login_url='adminlogin')
def admin_view_booking_view(request):
    orders = models.Orders.objects.all()
    ordered_products = []
    ordered_bys = []
    for order in orders:
        ordered_product = models.Product.objects.all().filter(id=order.product.id)
        ordered_by = models.Customer.objects.all().filter(id=order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)
    return render(request, 'admin_view_booking.html', {'data': zip(ordered_products, ordered_bys, orders)})


@login_required(login_url='adminlogin')
def delete_order_view(request, pk):
    order = models.Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')


# for changing status of order (pending,delivered...)
@login_required(login_url='adminlogin')
def update_order_view(request, pk):
    order = models.Orders.objects.get(id=pk)
    orderForm = forms.OrderForm(instance=order)
    if request.method == 'POST':
        orderForm = forms.OrderForm(request.POST, instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('admin-view-booking')
    return render(request, 'update_order.html', {'orderForm': orderForm})


def add_to_cart_view(request, pk):
    products = models.Product.objects.all()

    # for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 1

    response = render(request, 'index.html',
                      {'products': products, 'product_count_in_cart': product_count_in_cart})

    # adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids == "":
            product_ids = str(pk)
        else:
            product_ids = product_ids + "|" + str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    product = models.Product.objects.get(id=pk)
    messages.info(request, product.name + ' added to cart successfully!')

    return response


# for checkout of cart
def cart_view(request):
    # for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    # fetching product details from db whose id is present in cookie
    products = None
    total = 0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart = product_ids.split('|')
            products = models.Product.objects.all().filter(id__in=product_id_in_cart)

            # for total price shown in cart
            for p in products:
                total = total + p.price
    return render(request, 'cart.html',
                  {'products': products, 'total': total, 'product_count_in_cart': product_count_in_cart})


def remove_from_cart_view(request, pk):
    # for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    # removing product id from cookie
    total = 0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart = product_ids.split('|')
        product_id_in_cart = list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products = models.Product.objects.all().filter(id__in=product_id_in_cart)
        # for total price shown in cart after removing product
        for p in products:
            total = total + p.price

        #  for update coookie value after removing product id in cart
        value = ""
        for i in range(len(product_id_in_cart)):
            if i == 0:
                value = value + product_id_in_cart[0]
            else:
                value = value + "|" + product_id_in_cart[i]
        response = render(request, 'cart.html',
                          {'products': products, 'total': total, 'product_count_in_cart': product_count_in_cart})
        if value == "":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids', value)
        return response

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    products = models.Product.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0
    return render(request, 'customer_home.html',
                  {'products': products, 'product_count_in_cart': product_count_in_cart})

# shipment address before placing order
@login_required(login_url='customerlogin')
def customer_address_view(request):
    # this is for checking whether product is present in cart or not
    # if there is no product in cart we will not show address form
    product_in_cart = False
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart = True
    # for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    addressForm = forms.AddressForm()
    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from customer account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile = addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            # for showing total price on payment page.....accessing id from cookies then fetching  price of product from db
            total = 0
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                if product_ids != "":
                    product_id_in_cart = product_ids.split('|')
                    products = models.Product.objects.all().filter(id__in=product_id_in_cart)
                    for p in products:
                        total = total + p.price

            response = render(request, 'payment.html', {'total': total})
            response.set_cookie('email', email)
            response.set_cookie('mobile', mobile)
            response.set_cookie('address', address)
            return response
    return render(request, 'customer_address.html',
                  {'addressForm': addressForm, 'product_in_cart': product_in_cart,
                   'product_count_in_cart': product_count_in_cart})


# here we are just directing to this view...actually we have to check whther payment is successful or not
# then only this view should be accessed
@login_required(login_url='customerlogin')
def payment_success_view(request):
    # Here we will place order | after successful payment
    # we will fetch customer  mobile, address, Email
    # we will fetch product id from cookies then respective details from db
    # then we will create order objects and store in db
    # after that we will delete cookies because after order placed...cart should be empty
    customer = models.Customer.objects.get(user_id=request.user.id)
    products = None
    email = None
    mobile = None
    address = None
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart = product_ids.split('|')
            products = models.Product.objects.all().filter(id__in=product_id_in_cart)
            # Here we get products list that will be ordered by one customer at a time

    # these things can be change so accessing at the time of order...
    if 'email' in request.COOKIES:
        email = request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile = request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address = request.COOKIES['address']

    # here we are placing number of orders as much there is a products
    # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
    # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
    for product in products:
        models.Orders.objects.get_or_create(customer=customer, product=product, status='Pending', email=email,
                                            mobile=mobile, address=address)

    # after order placed cookies should be deleted
    response = render(request, 'ecom/payment_success.html')
    response.delete_cookie('product_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    return response


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def my_order_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    orders = models.Orders.objects.all().filter(customer_id=customer)
    ordered_products = []
    for order in orders:
        ordered_product = models.Product.objects.all().filter(id=order.product.id)
        ordered_products.append(ordered_product)

    return render(request, 'my_order.html', {'data': zip(ordered_products, orders)})


# shipment address before placing order
@login_required(login_url='customerlogin')
def customer_address_view(request):
    # this is for checking whether product is present in cart or not
    # if there is no product in cart we will not show address form
    product_in_cart = False
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart = True
    # for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    addressForm = forms.AddressForm()
    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from customer account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile = addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            # for showing total price on payment page.....accessing id from cookies then fetching  price of product from db
            total = 0
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                if product_ids != "":
                    product_id_in_cart = product_ids.split('|')
                    products = models.Product.objects.all().filter(id__in=product_id_in_cart)
                    for p in products:
                        total = total + p.price

            response = render(request, 'payment.html', {'total': total})
            response.set_cookie('email', email)
            response.set_cookie('mobile', mobile)
            response.set_cookie('address', address)
            return response
    return render(request, 'customer_address.html',
                  {'addressForm': addressForm, 'product_in_cart': product_in_cart,
                   'product_count_in_cart': product_count_in_cart})


# here we are just directing to this view...actually we have to check whther payment is successful or not
# then only this view should be accessed
@login_required(login_url='customerlogin')
def payment_success_view(request):
    # Here we will place order | after successful payment
    # we will fetch customer  mobile, address, Email
    # we will fetch product id from cookies then respective details from db
    # then we will create order objects and store in db
    # after that we will delete cookies because after order placed...cart should be empty
    customer = models.Customer.objects.get(user_id=request.user.id)
    products = None
    email = None
    mobile = None
    address = None
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart = product_ids.split('|')
            products = models.Product.objects.all().filter(id__in=product_id_in_cart)
            # Here we get products list that will be ordered by one customer at a time

    # these things can be change so accessing at the time of order...
    if 'email' in request.COOKIES:
        email = request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile = request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address = request.COOKIES['address']

    # here we are placing number of orders as much there is a products
    # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
    # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
    for product in products:
        models.Orders.objects.get_or_create(customer=customer, product=product, email=email,
                                            mobile=mobile, address=address)

    # after order placed cookies should be deleted
    response = render(request, 'payment_success.html')
    response.delete_cookie('product_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    return response


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def my_order_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    orders = models.Orders.objects.all().filter(customer_id=customer)
    ordered_products = []
    for order in orders:
        ordered_product = models.Product.objects.all().filter(id=order.product.id)
        ordered_products.append(ordered_product)

    return render(request, 'my_order.html', {'data': zip(ordered_products, orders)})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def my_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    return render(request, 'my_profile.html', {'customer': customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    user = models.User.objects.get(id=customer.user_id)
    userForm = forms.CustomerUserForm(instance=user)
    customerForm = forms.CustomerForm(request.FILES, instance=customer)
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST, instance=user)
        customerForm = forms.CustomerForm(request.POST, instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('my-profile')
    return render(request, 'edit_profile.html', context=mydict)


