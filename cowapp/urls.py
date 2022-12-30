from django.urls import path
from .import views

from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
     #path('signup/', SignUpView.as_view(), name='signup'),
     path('', views.home_view, name=''),
     path('afterlogin', views.afterlogin_view, name='afterlogin'),
     path('admindashboard', views.admin_dashboard_view, name='admindashboard'),
     path('logout/', LogoutView.as_view(template_name='navbar.html'), name='logout'),
     path('adminlogin', LoginView.as_view(template_name='adminlogin.html'), name='adminlogin'),
     path('adminclick', views.adminclick_view),

    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='customerlogin.html'), name='customerlogin'),
    path('customerhome', views.customer_home_view, name='customerhome'),


    path('show', views.ShowView, name='show'),
    path('add', views.add, name='add'),
    path('delete/<int:id>', views.delete),

    path('showvaccine', views.ShowVaccine, name='showvaccine'),
    path('addvaccine', views.addvaccine, name='addvaccine'),
    path('deletevaccine/<int:id>', views.deletevaccine),

    path('showeartag', views.ShowEartag, name='showeartag'),
    path('addeartag', views.addEartag, name='addeartag'),
    path('deleteeartag/<int:id>', views.deleteEartag),

    path('showneweartag', views.ShowNewEartag, name='showneweartag'),
    path('addneweartag', views.addNewEartag, name='addneweartag'),
    path('deleteneweartag/<int:id>', views.deleteNewEartag),

    path('show-milkrecord', views.ShowMilkRecord, name='show-milkrecord'),
    path('add-milkrecord', views.addMilkRecord, name='add-milkrecord'),
    path('delete-milkrecord/<int:id>', views.deleteMilkRecord),

    path('admin-products', views.admin_products_view, name='admin-products'),
    path('admin-add-product', views.admin_add_product_view, name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view, name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view, name='update-product'),
    path('admin-view-booking', views.admin_view_booking_view, name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view, name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view, name='update-order'),

    path('add-to-cart/<int:pk>', views.add_to_cart_view, name='add-to-cart'),
    path('cart', views.cart_view, name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view, name='remove-from-cart'),

    path('customer-address', views.customer_address_view, name='customer-address'),
    path('payment-success', views.payment_success_view, name='payment-success'),

    path('my-profile', views.my_profile_view, name='my-profile'),
    path('edit-profile', views.edit_profile_view, name='edit-profile'),


    ]