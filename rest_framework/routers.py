from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates

rest_api = Starlette(debug=True)
templates = Jinja2Templates(directory='rest_framework/templates')

@rest_api.route("/")
async def homepage(request):
    return JSONResponse({'hello': 'world'})


#async def generic_view(request):#
#
#    return templates.TemplateResponse("base.html", {'request': request })


class DefaultRouter:

    def __init__(self):
        print("initializing routerrrrr")

    def register_app(self, app):
        print("registering app")
        self.app = app
        app.mount("/api", rest_api)

    def register(self, path, model_class, basename=""):
        print(path)

        rest_api.add_route(path, model_class)
        rest_api.add_route(path+"/{id:int}", model_class)

