import datetime
import decimal
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import datetime_safe
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.template import RequestContext
from django.template.loader import render_to_string

class JSONResponse(HttpResponse):
    """
    A self serializing Json Response
    """
    def __init__(self, obj, callback=None, code=200):
        self.status_code = code
        content = json_dumps(obj, ensure_ascii=False, separators=(',',':'))
        if callback:
            content = '%s(%s);' % (callback, content)
        super(JSONResponse, self).__init__(content, mimetype='text/javascript')

def json_dumps(obj, **kwargs):
    return simplejson.dumps(obj, **kwargs)

# Simple view to output object to json
def to_json(request, obj=None):
    if obj:
        if callable(obj):
            return JSONResponse(obj())
        return JSONResponse(obj)
    else:
        return JSONResponse({})

# Simple view to output object to jsonp
def to_jsonp(request, obj):
    if obj:
        if callable(obj):
            return JSONResponse(obj(), callback=request.GET.get('callback', None))
        return JSONResponse(obj, callback=request.GET.get('callback', None))
    else:
        return JSONResponse({}, callback=request.GET.get('callback', None))

def render_to_typed_response(request, template, context, type_key="type", json_key="content", allow_origin=None):
    rendered = render_to_string(
        template, context,
        context_instance=RequestContext(request)
    )

    if request.GET.get(type_key) in ['json', 'jsonp']:
        response = JSONResponse({json_key: rendered}, callback=request.GET.get('callback', None))
    else:
        response = HttpResponse(content=rendered)

    if allow_origin:
        response['Access-Control-Allow-Origin'] = allow_origin

    return response
