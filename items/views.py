
from .models import Item
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from.forms import NewItemForm
# Create your views here.
def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(Category=item.Category,is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items,
    })

@login_required
def new(request):
    form=NewItemForm()

    return render(request,'items/form.html',{'form':form,
                                            'title':'New Item',
                                             })