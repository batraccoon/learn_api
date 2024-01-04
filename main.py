# from fastapi import FastAPI, HTTPException, Header

# app = FastAPI()

# API_KEY = "angger123" #testing api token key 1234

# @app.get("/")
# def home():
#   return {"message":"This is my API. Welcome!"}

# @app.get("/protected")
# def protect(api_key: str = Header(None)):
#   # di postman, api_key jadi api-key

#   if api_key is None or api_key != API_KEY:
#         raise HTTPException(status_code=401, detail="Invalid API Key")

#   return {"message":"This endpoint is protected by API Token Key.",
#           "data":{"1":{"username":"fahmi","password":"1234"},
#                   "2":{"username":"raka","password":"abcd123"},
#                   "3":{"username":"rachman","password":"h8teacher"}
#                  }
#           }

# from fastapi import FastAPI, HTTPException, Header
# import pandas as pd

# app = FastAPI()

# df = pd.read_csv('D:/backup/backup/Punya Anggerr/Hacktiv8/API/dataset-of-songs-in-spotify/genres_v2.csv')


# API_KEY = "testingapitokenkey1234" #testing api token key 1234

# @app.get("/") #root endpoint
# def home():
#   return df.head()

# @app.get("/protected/{title}") #protected api
# def protect(title:str,api_key: str = Header(None)):

#   if api_key is None or api_key != API_KEY:
#         raise HTTPException(status_code=401, detail="Invalid API Key")
#   else:
#     query = df[df['time']==title.capitalize()].to_dict(orient='records')
#     if len(query)==0:
#        raise HTTPException(status_code=404, detail="Data Not Found")
#     else:
#         return query 

from fastapi import FastAPI, HTTPException

app = FastAPI()

data = {"name":"shopping cart",
        "columns":["prod_name","price","num_items"],
        "items":{}}

@app.get("/")
def root():
    return {"message":"Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu":{1:"See shopping cart (/cart)",
                    2:"Add item (/add) - You may need request",
                    3:"Edit shopping cart (/edit/id)",
                    4:"Delete item from shopping cart (/del/id)"}}

@app.get("/cart")
def show():
    return data

@app.post("/add")
def add_item(added_item:dict):
    id = len(data["items"].keys())+1
    data["items"][id] = added_item
    return f"Item successfully added into your cart with ID {id}"

@app.put("/edit/{id}")
def update_cart(id:int,updated_cart:dict):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        data["items"][id].update(updated_cart)
        return {"message": f"Item with ID {id} has been updated successfully."}

@app.delete("/del/{id}")
def remove_row(id:int):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        data["items"].pop(id)
        return {"message": f"Item with ID {id} has been deleted successfully."}