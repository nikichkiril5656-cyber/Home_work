import asyncio
import time

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    print("--- Последовательный запуск ---")
    start_time = time.perf_counter()

    await say_hello("Alice", 1)
    await say_hello("Bob", 1)
    await say_hello("Charlie", 1)

    end_time = time.perf_counter()
    print(f"Время последовательно: {end_time - start_time:.2f} сек.\n")

    print("--- Параллельный запуск (gather) ---")
    start_time = time.perf_counter()

    await asyncio.gather(
        say_hello("Alice", 1),
        say_hello("Bob", 1),
        say_hello("Charlie", 1)
    )

    end_time = time.perf_counter()
    print(f"Время параллельно: {end_time - start_time:.2f} сек.")

if __name__ == "__main__":
    asyncio.run(main())