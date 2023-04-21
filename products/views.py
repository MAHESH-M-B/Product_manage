
import pandas as pd
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UploadExcelForm
from .models import Product
from django.contrib import messages

from django.db import models
from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'home.html')



# def upload_excel(request):
#     if request.method == 'POST':
#         form = UploadExcelForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['excel_file']
#             data = pd.read_excel(excel_file)
#             for index, row in data.iterrows():
#                 product = Product(
#                     item_code=row['Item Code'],
#                     item_name=row['Item Name'],
#                     category_l1=row['Category L1'],
#                     category_l2=row['Category L2'],
#                     upc=row['UPC'],
#                     parent_code=row['Parent Code'],
#                     mrp_price=row['MRP Price'],
#                     size=row['Size'],
#                     enabled=row['Enabled'] == 'Y'
#                 )
#                 product.save()
#             return render(request, 'upload_success.html')
#     else:
#         form = UploadExcelForm()
#     return render(request, 'upload_excel.html', {'form': form})



# def upload_excel(request):
#     if request.method == 'POST':
#         excel_file = request.FILES.get('excel-file', None)
#         if not excel_file:
#             messages.error(request, 'Please select an Excel file to upload.')
#             return redirect('upload_excel')
#         try:
#             # Load the Excel file into a pandas dataframe
#             df = pd.read_excel(excel_file)
#             # Loop through the rows of the dataframe and create Product objects
#             for _, row in df.iterrows():
#                 product = Product.objects.create(
#                     item_code=row['Item Code'],
#                     item_name=row['Item Name'],
#                     category_l1=row['Category L1'],
#                     category_l2=row['Category L2'],
#                     mrp_price=row['MRP Price'],
#                     enabled=row['Enabled']
#                 )
#             messages.success(request, 'Excel file uploaded successfully.')
#         except Exception as e:
#             messages.error(request, f'Error uploading Excel file: {e}')
#         return redirect('upload_excel')
#     return render(request, 'upload_excel.html')






def upload_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel-file', None)
        print(excel_file)
        if not excel_file:
            messages.error(request, 'Please select an Excel file to upload.')
            return redirect('upload_excel')
        else:
            try:
                data = pd.read_excel(excel_file)
                print(data)

                for index, row in data.iterrows():
                    product = Product(
                        item_code=row['Item Code'],
                        item_name=row['Item Name'],
                        category_l1=row['Category L1'],
                        category_l2=row['Category L2'],
                        upc=row['UPC'],
                        parent_code=row['Parent Code'],
                        mrp_price=row['MRP Price'],
                        size=row['Size'],
                        enabled=row['Enabled']
                    )
                    print(product)
                    product.save()
                messages.success(request, 'Excel file uploaded successfully.')
            except Exception as e:
                print(f"Error reading Excel file: {e}")
                messages.error(request, f'Error uploading Excel file: {e}')
            return redirect('home')
    return render(request, 'upload_excel.html')





def get_top_most_parent(request):
    search_term = request.GET.get('search_term', '')
    product = Product.objects.filter(item_name=search_term).first() or Product.objects.filter(item_code=search_term).first()
    if not product:
        return render(request, 'product_search.html', {'error': f'No product found with name or code: {search_term}'})
    
    parent_product = None
    current_product = product
    while current_product.parent_code:
        parent_product = Product.objects.filter(item_code=current_product.parent_code).first()
        if not parent_product:
            break
        current_product = parent_product
    
    child_products = list(Product.objects.filter(parent_code=product.item_code).order_by('item_name').values_list('item_name', flat=True))
    
    return render(request, 'product_search.html', {'product': product, 'parent_product': parent_product, 'child_products': child_products})

def get_children(request):
    search_term=request.GET.get('search_term', '')
    product = Product.objects.filter(item_name=search_term).first()
    print(product)
    # children = Product.objects.filter(parent_code=product.item_code).order_by('item_name')
    # return render(request, 'product_children.html', {'children': children})
    return render(request, 'products_children.html')



# def product_children(request):
#     search_term = request.GET.get('search_term')
#     children = []
#     if search_term:
#         children = get_children(search_term)
#     return render(request, 'product_children.html', {'children': children, 'search_term': search_term})


# def count_active_inactive_products():
#     active_count = Product.objects.filter(enabled=True).count()
#     inactive_count = Product.objects.filter(enabled=False).count()
#     return active_count, inactive_count

def active_inactive_products(request):
    active_count = Product.objects.filter(enabled="Yes").count()
    inactive_count = Product.objects.filter(enabled="No").count()
    print(active_count)
    print(inactive_count)
    context = {
        'active_count': active_count,
        'inactive_count': inactive_count,
    }
    print(context)
    return render(request, 'active_count.html', context)

# def get_average_product_price():
#     category_l1_avg_price = Product.objects.values('category_l1').annotate(avg_price = models.Avg('mrp_price')).values_list('category_l1', 'avg_price')
#     category_l2_avg_price = Product.objects.values('category_l1', 'category_l2').annotate(avg_price = models.Avg('mrp_price')).values_list('category_l1', 'category_l2', 'avg_price')
#     return category_l1_avg_price, category_l2_avg_price


def average_product_price(request):
    category_l1_avg_price = Product.objects.values('category_l1').annotate(avg_price = models.Avg('mrp_price')).values_list('category_l1', 'avg_price')
    category_l2_avg_price = Product.objects.values('category_l1', 'category_l2').annotate(avg_price = models.Avg('mrp_price')).values_list('category_l1', 'category_l2', 'avg_price')
    avg_prices = {
        'avg_prices': category_l2_avg_price
    }
    return render(request, 'average_price.html', avg_prices)