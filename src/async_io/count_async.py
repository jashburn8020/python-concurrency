"""Simple `async` and `await`."""

import asyncio
import time


async def count() -> None:
    """Print a count of two, sleeping for 1 second between them."""
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main() -> None:
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start

    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
