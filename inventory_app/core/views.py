from django.shortcuts import render
from .models import Category, Tag, Product

# Create your views here.

def inventory(request):
    return render(request, 'core/inventory.html')

def inventory_view(request):
    #retrieves all of the categories from the database
    categories = Category.objects.all()

    #retrieves all of the tags from the database
    tags = Tag.objects.all()
    
    #retrieves all of the products from the database
    products = Product.objects.all()

    #get the filters from the front end
    category_filter = request.GET.get('category', None)
    tag_filter = request.GET.get('tag', None)
    search_query = request.GET.get('search', '')

    
    if category_filter:
        products = products.filter(category__name=category_filter)

    if tag_filter:
        products = products.filter(tags__name=tag_filter)

    if search_query:
        products = products.filter(description__icontains=search_query)

    #data to pass to the template
    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'core/inventory.html', context)