from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    # path('product_details/', views.product_details, name='product_details'),
    path('parent_product/', views.get_top_most_parent, name='get_top_most_parent'),
    path('child_products/', views.get_children, name='get_children'),
    path('active_inactive_count/', views.active_inactive_products, name='active_inactive_products'),
    path('average_price/', views.average_product_price, name='average_product_price'),
]
