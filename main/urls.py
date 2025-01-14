from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('',views.main_view, name='home'),
    path('products',views.products, name='products'),
    path('products/<str:name>/',views.details, name='details'),
    path('payment/', views.payment_page, name='payment_page'),  # صفحة الدفع
    path('success/', views.success, name='success'),  # صفحة النجاح
    path('cancel/', views.cancel, name='cancel'), 
    path('card/', views.card, name='card'), 
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('card/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('card/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('color/', views.color, name='color'),
    path('update-color/<int:item_id>/', views.update_color, name='update_color'),
    path('cart/', views.card, name='cart'),
]

