"""Coroutine with return value."""

import asyncio
import random
from typing import Final, List


async def makerandom(identifier: int) -> int:
    """Generate a random number between 0 and 10, and terminates if greater than 7."""
    threshold: Final = 7
    print(f"Initiated makerandom #{identifier} with threshold at {threshold}.")

    while (random_int := random.randint(0, 10)) <= threshold:
        print(f"makerandom #{identifier} == {random_int} too low; retrying.")
        await asyncio.sleep(identifier + 1)

    print(f"---> Finished: makerandom #{identifier} == {random_int}")
    return random_int


async def main() -> List[int]:
    """Execute coroutines and return their results."""
    res = await asyncio.gather(*(makerandom(i) for i in range(3)))
    return res


if __name__ == "__main__":
    random.seed()
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
