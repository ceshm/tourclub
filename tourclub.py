import json

import uvicorn

from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from tortoise.contrib.starlette import register_tortoise

from db_settings import DB_CONF
from models import Tour, Team
from tour_api.urls import router

app = Starlette(debug=True)

with open('config.json') as config_file:
    register_tortoise(app, config=DB_CONF, modules={"models": ["models"]}, generate_schemas=True)

# resta_api initializatibn
router.register_app(app)


@app.route('/')
async def homepage(request):
    #tour = Tour()
    #tour.name = ""
    #await tour.save()
    tours = await Tour.all()
    #teams = await Team.all()
    return JSONResponse({"tours": [ {"name": x.name, "id": x.id} for x in tours] })


@app.route('/tour')
async def homepage(request):

    return JSONResponse({'hello': 'world'})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
