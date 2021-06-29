from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import httpx_demo

weather = on_command("天气", rule=to_me(), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["cityName"] = args  # 如果用户发送了参数则直接赋值
        result = await httpx_demo.get_Location_ID(args)
        if result == "":
            await weather.reject("你的输入有误，请重新输入具体的城市名！")


@weather.got("cityName", prompt="欢迎使用明爸爸天气查询"+"\n"
                                "输入你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: T_State, ):
    cityName = state["cityName"]
    await httpx_demo.get_Location_ID(cityName)

    if cityName not in httpx_demo.locationId:
        await weather.reject("你的输入有误，请重新输入具体的城市名！")
    city_weather = await get_weather(httpx_demo.locationId[cityName],cityName)
    await weather.finish(city_weather)


async def get_weather(city: str,cityName:str):
    print('city-code:', city)
    data = await httpx_demo.getCity_Weather(city)
    print(data)

    obsTime = data['obsTime']  # 数据观测时间
    temp = data['temp']  # 温度，默认单位：摄氏度
    humidity = data['humidity']  # 相对湿度，百分比数值
    windDir = data['windDir']  # 风向
    text = data['text']  # 风向
    str = f'''
        天气查询成功
           城市
        {cityName}
        查询日期为：
        {obsTime}
        今天天气为：{text}
        当前温度为：{temp}
        当前湿度为：{humidity}
        风向为：{windDir}
        
        '''
    return str
