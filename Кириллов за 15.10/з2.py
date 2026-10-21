import asyncio

async def ticker(name, n):
    for i in range(1, n + 1):
        await asyncio.sleep(0.5)
        print(f"{name}: {i}")

async def main():
    await asyncio.gather(
        ticker("A", 5),
        ticker("B", 3)
    )

if __name__ == "__main__":
    asyncio.run(main())