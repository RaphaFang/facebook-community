import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# 創建事件循環並運行協程
async def main():
    await say_hello()

# Python 3.7+
asyncio.run(main())
