from django.views import generic
from coffee_shop.products.forms import ProductForm # type: ignore

class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm