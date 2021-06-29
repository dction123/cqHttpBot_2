from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.plugin import on_keyword

musicList = ['我要听歌', '歌曲', '音乐']
# cmusic = on_command('音乐', rule=to_me(), priority=5)
music = on_keyword(musicList, rule=to_me(), priority=5)


@music.handle()
async def handle_recevice(bot: Bot, event: Event, state: T_State):
    await music.finish('你要听什么歌？')
