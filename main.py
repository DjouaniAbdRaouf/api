from fastapi import FastAPI
from routes.index import user_route
app = FastAPI()
app.include_router(user_route)




#
# @app.get("/")
# def getitems():
#     return {"items": "item1"}
#
#
# @app.post("/add-item/{item}")
# def additem(item: str):
#     return {"items": str(item)}
#
#
# @app.delete("/delete-item/{item}")
# def delete_item(item: str):
#     return {"items": str(item), "msf": "item deleted from database"}
