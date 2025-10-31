from . models import Category_items

def links(request):
    c=Category_items.objects.all()
    return{'links':c}