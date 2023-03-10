import httpx
from nonebot import logger, on_command
from nonebot.adapters import Message
from nonebot.matcher import Matcher
from nonebot.params import CommandArg

tiangou_matcher = on_command("一句")
meiyan_matcher = on_command("一言")
dujitang_matcher = on_command("毒鸡汤")
caihongpi_matcher = on_command("彩虹屁")
wangyiyun_matcher = on_command("网易云热评")

#舔狗日记
@tiangou_matcher.handle()
async def hitokoto(matcher: Matcher, args: Message = CommandArg()):
    if args:
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://cloud.qqshabi.cn/api/tiangou/api.php")
    if response.is_error:
        logger.error("获取舔狗日记失败")
        return
    msg = response.text
    await matcher.finish(msg)

#一句美言
@meiyan_matcher.handle()
async def hitokoto(matcher: Matcher, args: Message = CommandArg()):
    if args:
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://cloud.qqshabi.cn/api/hitokoto/hitokoto.php")
    if response.is_error:
        logger.error("获取美言失败")
        return
    msg = response.text
    await matcher.finish(msg)

#毒鸡汤
@dujitang_matcher.handle()
async def hitokoto(matcher: Matcher, args: Message = CommandArg()):
    if args:
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://cloud.qqshabi.cn/api/poison/api.php")
    if response.is_error:
        logger.error("获取毒鸡汤失败")
        return
    data = response.json()
    add = ""
    if msg := data["data"]:
         add += f"{msg}"
    await matcher.finish(msg)

#彩虹屁
@caihongpi_matcher.handle()
async def hitokoto(matcher: Matcher, args: Message = CommandArg()):
    if args:
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://cloud.qqshabi.cn/api/rainbow/api.php")
    if response.is_error:
        logger.error("获取彩虹屁失败")
        return
    data = response.json()
    add = ""
    if msg := data["data"]:
         add += f"{msg}"
    await matcher.finish(add)

#网易云热评
@wangyiyun_matcher.handle()
async def hitokoto(matcher: Matcher, args: Message = CommandArg()):
    if args:
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://cloud.qqshabi.cn/api/comments/api.php?format=text")
    if response.is_error:
        logger.error("获取网易云热评失败")
        return
    msg = response.text
    await matcher.finish(msg)