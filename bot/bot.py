#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.cqhttp import Bot


nonebot.init()
"""
说明

初始化 NoneBot 以及 全局 Driver 对象。

NoneBot 将会从 .env 文件中读取环境信息，并使用相应的 env 文件配置。

你也可以传入自定义的 _env_file 来指定 NoneBot 从该文件读取配置。
"""
driver = nonebot.get_driver()
"""
说明

获取全局 Driver 对象。可用于在计划任务的回调中获取当前 Driver 对象。
"""
driver.register_adapter("cqhttp", Bot)
"""
注册 CQHTTP 的 Adapter
"""

nonebot.load_plugins("bot/plugins")
nonebot.load_plugins("bot/qq_plugins")


"""
加载插件目录，该目录下为各插件，以下划线开头的插件将不会被加载
"""
app = nonebot.get_asgi()
"""
说明

获取全局 Driver 对应 Asgi 对象。
"""

if __name__ == "__main__":

    nonebot.run()
