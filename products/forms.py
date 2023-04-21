from django import forms
from .models import Product


class UploadExcelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item_code', 'item_name', 'category_l1', 'category_l2',
                  'upc', 'parent_code', 'mrp_price', 'size', 'enabled']
