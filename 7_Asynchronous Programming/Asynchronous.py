#Asynchronous Programming
print("\nASYNCHRONOUS PROGRAMMING\n")
import asyncio

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())


async def task1():
    print("Task 1 starting...")
    await asyncio.sleep(2)
    print("Task 1 done.")

async def task2():
    print("Task 2 starting...")
    await asyncio.sleep(1)
    print("Task 2 done.")

async def main():
    await asyncio.gather(task1(), task2(),say_hello()) 
asyncio.run(main())
