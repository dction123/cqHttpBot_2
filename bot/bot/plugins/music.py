from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.plugin import on_keyword

music = on_keyword(['歌','听歌'],rule=to_me(), priority=5)

@music.handle()

async def handle_recevice(bot: Bot, event: Event, state: T_State):
    print(event.get_event_name())
    data = '查找歌曲'
    music.finish(data)

    await music.finish(data)
