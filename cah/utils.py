#Pagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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