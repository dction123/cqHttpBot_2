#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/7/5 22:11'
__author__ = 'Liang'

签到系统
"""
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

sing = on_command('签到', priority=2)


@sing.handle()
async def sing_in_handle(bot: Bot, event: Event, state: T_State):
    #  读取当前成员id
    print('1')
    print(event.get_event_name())
    print(event.get_session_id())
    print(event.get_user_id())
    print('2')
