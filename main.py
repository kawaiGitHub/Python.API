from fastapi import FastAPI

app = FastAPI()

@app.get("/countries/{country_name}")
async def contry(country_name: str='japan',city_name: str = 'tokyo'): 
    return{
        "country_name":country_name,
        "city_name" : city_name
        }
