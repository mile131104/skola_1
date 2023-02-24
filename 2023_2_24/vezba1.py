import asyncio
import time

async def vozikamion():
    print("Vozim kamion...")
    await asyncio.sleep(6)
    print("Stigao kamion")
async def vozi():
    print("Vozim...")
    await asyncio.sleep(5)
    print("Zavrsio sam voznju")

def f():
    print("Hello from function!!!")

async def main():
    # print("Pocinje program")
    # f()
    # await vozi()
    # print("Hello man")
    t1 = asyncio.create_task(vozi())
    t2 = asyncio.create_task(vozikamion())
    await asyncio.sleep(10)
    

asyncio.run(main())
