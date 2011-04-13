from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cah.accounts.models import FavoriteItem
from cah.utils.json import JSONResponse

#Pagination
def paginate(request, objects):
    p = Paginator(objects, 10)

    page = request.GET.get('page')
    try:
        obj_list = p.page(page)
    except PageNotAnInteger:
        obj_list = p.page(1)
    except TypeError:
        obj_list = p.page(1)
    except EmptyPage:
        obj_list = p.page(p.num_pages)

    return obj_list

@login_required
def favorited_items(request, model):
    if request.is_ajax():
        items = FavoriteItem.objects.filter(user=request.user, content_type=ContentType.objects.get_for_model(model))
        item_pks = [i.object_id for i in items]
        return JSONResponse({
            'items': item_pks
        })
    else:
        pass