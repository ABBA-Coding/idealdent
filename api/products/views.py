from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from api.products.models import Category, SubCategory, Product


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        subcategories = SubCategory.objects.filter(category=category)
        context['subcategories'] = subcategories
        return context


class ProductListView(ListView):
    model = Category


class SubCategoryDetailView(DetailView):
    model = SubCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory = self.object
        products = Product.objects.filter(subcategory=subcategory)

        # Pagination
        paginator = Paginator(products, 6)  # items_per_page is the number of items per page
        page = self.request.GET.get('page')  # Get the current page number from the request

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page of results.
            products = paginator.page(paginator.num_pages)

        context['products'] = products
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
