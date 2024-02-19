from ninja import NinjaAPI
from apps.summoners.api import summoners_router


api = NinjaAPI()

api.add_router('summoners/', summoners_router)
