from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
import __fun_test as myfunc


import json
import requests
import time
import re

# 天行 key
APIKEY = '243c5b58aa7db32f8a20fdb6512cb4a3'
today = on_command("菜单", priority=1)


@today.handle()
async def handle_system(bot: Bot, event: Event, state: T_State):
    # url = 'http://www.tianque.top/d2api/today/'
    #
    # r = urllib3.PoolManager().request('GET', url)
    # hjson = json.loads(r.data.decode())
    # img_url = hjson["img_url"]
    cq = """欢迎使用沙雕机器人v0.1 
    ------功能列表------
    [CQ:face,id=260]签到功能
    [CQ:face,id=260]娱乐功能
    [CQ:face,id=260]抖音热榜
    [CQ:face,id=260]舔狗日记

    --我是有底线的--
    -by:明明明明明-
        
        """
    await today.send(Message(cq))


dogDiary = on_command('舔狗日记')


@dogDiary.handle()
async def handle_dogDiary(bot: Bot, event: Event, state: T_State):
    '''
    舔狗日记
    :param bot:
    :param event:
    :param state:
    :return:
    '''
    url = 'http://api.tianapi.com/txapi/tiangou/index?key=' + APIKEY
    try:
        req = requests.get(url)
        text = req.text
        text = json.loads(text)
        dogDiaryText = text['newslist'][0]['content']  # 正文内容

        tm_year = str(time.localtime().tm_year)
        tm_month = str(time.localtime().tm_mon)
        tm_today = str(time.localtime().tm_mday)
        tm_hour = str(time.localtime().tm_hour)
        tm_min = str(time.localtime().tm_min)
        now_time = tm_year + '年' + tm_month + '月' + tm_today + '日' + ' ' + tm_hour + '点' + tm_min + '分'
        # print(now_time)

        oneGetText = await myfunc.one_get()
        print('oneGetText:', oneGetText)
        cq = f"""{now_time}  舔狗日记
        {dogDiaryText}\n
        [CQ:face,id=49]{oneGetText}
        """
        await dogDiary.send(Message(cq))

    except:
        await dogDiary.send('调用 舔狗日记失败')


tiktokTops = on_command('抖音热榜', priority=2)


@tiktokTops.handle()
async def handle_tiktokTops(bot: Bot, event: Event, state: T_State):
    try:
        ar = await myfunc.dyvideohot()
        str1 = ""
        # print(ar)
        for link in ar:
            title = link['title']
            shareurl = myfunc.urlParse(link['shareurl'])
            print('shareurl:', shareurl)
            coverurl =myfunc.urlParse(link['coverurl'])
            print('coverurl:', coverurl)

            str1 = str1 + f"""
                        [CQ:share,title=抖音热榜,content={title},image={coverurl},url={shareurl}]
                        """
        await tiktokTops.send(Message(str1))
    except:
        tiktokTops.send(Message('抖音热榜调用失败'))

set_group_ban =on_command('炸弹')

@set_group_ban.handle()
async def handle_set_group_ban(bot: Bot, event: Event, state: T_State):
    msg = str(event.get_message())
    attack_qq = str(event.get_user_id())
    kill_qq = int(re.findall('\d+',msg)[0])
    event_description = event.get_event_description()
    user_id = event.get_user_id()

    print('event_description:',event_description)
    print('user_id:',user_id)

    if  msg.startswith('[CQ'):
        cq = f"""[CQ:image,file=http://q1.qlogo.cn/g?b=qq&nk={kill_qq}&s=5]
        
        
[CQ:face,id=55][CQ:face,id=55]蹦瞎卡拉卡
[CQ:at,qq={kill_qq}]
你被[CQ:at,qq={attack_qq}]炸弹炸了,禁言1分钟
想要还击 发送 炸弹 @某人
            """
        print('cq:',cq)
        await set_group_ban.send(Message(cq))
        await bot.call_api('set_group_ban', group_id=819240753, user_id=kill_qq, duration=30)
    else:
        await set_group_ban.send('扔炸弹格式错误 请正确输入！ 炸弹 @某人')



    #
    # bot.call_api('get_msg',message_id=)
    # await set_group_ban.send('禁言成功')