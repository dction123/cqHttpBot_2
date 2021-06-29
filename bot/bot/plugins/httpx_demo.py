import asyncio
import httpx
import json

key = '261df40ecdb84b30881f7352396c2d46'
locationId = {}
wheather = {}


async def get_Location_ID(city: str):
    print('city:', city)
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://geoapi.qweather.com/v2/city/lookup?location={city}&key={key}')
        text = response.text
        try:
            print(text)
            data = json.loads(text)
            # print(text)
            # print(dict)
            # print(len(dict)
            # print(data['location'],type(data['location']))
            for link in data['location']:
                locationId[link['name']] = link['id']
            print(locationId)
        except:
            return ""


async def getCity_Weather(loctionId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'https://devapi.qweather.com/v7/weather/now?location={loctionId}&key={key}')
        text = response.text
        data = json.loads(text)
        wheather = data['now']
        return wheather

# asyncio.run(get_Location_ID('成都'))
# asyncio.run(getCity_Weather('101270116'))
