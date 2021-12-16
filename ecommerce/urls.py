from django.urls import path
from ecommerce.views import *
# from . import api

app_name = 'ecommerce'

urlpatterns = [
    
    # App URLS.........
    
    # home page url
    path('',HomeView.as_view(),name='home'),
    
    # about us page url
    path('about/',AboutView.as_view(),name='about_us'),
    
    # contact us page url
    path('contact-us/',ContactUsView.as_view(),name='contact_us'),
    
    # why us page url
    path('why-us/',WhyUsView.as_view(),name='why_us'),

    # products url
    path('all-products/',AllProductsView.as_view(),name='all_products'),
    path('product/<slug:slug>/',ProductDetailView.as_view(),name='product_detail'),
    
    # categories url
    path('all-categories/',CategoriesView.as_view(),name='all_categories'),
    
    # cart url
    path('my-cart/',CartView.as_view(),name='my_cart'),
    path('add-to-cart/<int:pro_id>/',AddToCartView.as_view(),name='add_to_cart'),
    path('manage-cart/<int:cp_id>/',ManageCartView.as_view(),name='manage_cart'),
    path('empty-cart/',EmptyCartView.as_view(),name='empty_cart'),
    
    # check out url
    path('check-out/',CheckOutView.as_view(),name='check_out'),
    
    # payments methods with khalti url
    path("khalti-request/", KhaltiRequestView.as_view(), name="khalti_request"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khalti_verify"),
    
    # payments methods with esewa url
    path('esewa-request/',EsewaRequestView.as_view(), name="esewa_request"),
    path('esewa-verify/',EsewaVerifyView.as_view(), name="esewa_verify"),
    
    # customers urls
    path('customer-register/',CustomerRegisterView.as_view(),name='customer_register'),
    path('customer-login/',CustomerLoginView.as_view(),name='customer_login'),
    path('customer-logout/',CustomerLogoutView.as_view(),name='customer_logout'),
    path('customer-profile/',CustomerProfileView.as_view(),name='customer_profile'),
    path('customer-edit-profile/<int:pk>',UpdateProfileView.as_view(),name='customer_edit_profile'),
    path('profile/order-<int:pk>/',CustomerOrderDetailView.as_view(),name='customer_order_detail'),
    
    # passwords urls
    path('forgot-password/',ForgotPasswordView.as_view(),name="forgot_password"),
    path('reset-password/<email>/<token>/',ResetPasswordView.as_view(),name="reset_password"),
    
    # Admins urls 
    path("admin-login/", AdminLoginView.as_view(), name="admin_login"),
    path("admin-home/", AdminHomeView.as_view(), name="admin_home"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(), name="admin_order_detail"),
    path("admin-all-orders/", AdminAllOrderView.as_view(), name="admin_all_order"),
    path("admin-order-<int:pk>-change/", AdminOrderStatusChangeView.as_view(), name="admin_order_status_change"),
    path("admin-product/list/",AdminProductList.as_view(), name="admin_product_list"),
    path("admin-product/add/",AdminProductAdd.as_view(), name="admin_add_product"),
    
    # filter by search urls 
    path("search/", SearchView.as_view(), name="search"),
    
]