# Python Concurrency

Summary of concurrency in Python sourced from various articles.

- [Python Concurrency](#python-concurrency)
  - [Introduction](#introduction)
    - [Concurrency and Parallelism](#concurrency-and-parallelism)
    - [When Is Concurrency Useful](#when-is-concurrency-useful)
  - [`asyncio`](#asyncio)
    - [The `async`/`await` Syntax and Native Coroutines](#the-asyncawait-syntax-and-native-coroutines)
    - [The Rules of Async IO](#the-rules-of-async-io)
  - [Sources](#sources)

## Introduction

- **Parallelism**
  - performing multiple operations at the same time
- **Multiprocessing**
  - a means to effect parallelism
  - entails spreading tasks over a computer's central processing units (CPUs, or cores)
  - well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category
- **Concurrency**
  - a slightly broader term than parallelism
  - multiple tasks have the ability to run in an overlapping manner
  - does not necessarily imply parallelism
- **Threading**
  - a concurrent execution model whereby multiple threads take turns executing tasks
  - one process can contain multiple threads
  - Python has a complicated relationship with threading thanks to its GIL
- **GIL (Global Interpreter Lock)**
  - in CPython, GIL is the mutex - the mutual exclusion lock - which makes things thread-safe
  - prevents multiple threads from executing Python code in parallel
  - the lock can be held by only one thread at a time and if we want to execute a thread then it must acquire the lock first
  - necessary because CPython's memory management is not thread-safe
  - there are some libraries and implementations in Python such as Numpy, Jython and IronPython that work without any interaction with GIL

### Concurrency and Parallelism

- Concurrency
  - encompasses both multiprocessing and threading
  - in Python, `threading` and `asyncio` both run on a single processor and therefore only run one at a time
    - they find ways to take turns to speed up the overall process
  - `threading`
    - uses _pre-emptive multitasking_
    - the operating system actually knows about each thread and can interrupt it at any time to start running a different thread, i.e., pre-empt your thread to make the switch
    - this switch can happen at any time, including in the middle of a single Python statement
  - asynchronous IO
    - a style of concurrent programming
      - is neither threading nor multiprocessing
    - uses _cooperative multitasking_
    - a single-threaded, single-process design
    - tasks must coded to cooperate by announcing when they are ready to be switched out
      - you always know where your task will be swapped out
    - enabled in CPython through the standard library's `asyncio` package
- Parallelism
  - a specific type of concurrency
  - with `multiprocessing`, Python creates new processes
    - each task in a multiprocessing program can run on a different core, and at the same time

### When Is Concurrency Useful

- Concurrency can make a big difference for two types of problems: I/O-bound and CPU-bound
- **I/O-bound** problems cause your program to slow down because it frequently must wait for input/output (I/O) from some external resource
  - arise frequently when your program is working with things that are much slower than your CPU
  - the slow things your program will interact with most frequently are the file system and network connections
- **CPU-bound** programs: programs that do significant computation without talking to the network or accessing a file
  - the resource limiting the speed of your program is the CPU

## `asyncio`

- Async IO takes long waiting periods in which functions would otherwise be blocking and allows other functions to run during that downtime
  - a function that blocks effectively forbids others from running from the time that it starts until the time that it returns
- "Use async IO when you can; use threading when you must"

### The `async`/`await` Syntax and Native Coroutines

- **Awaitables**
  - an object is an awaitable object if it can be used in an `await` expression
  - 3 main types of awaitable objects: coroutines, Tasks, and Futures, or an object with an [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__) method
- **Coroutines**
  - the heart of async IO
  - specialized version of a Python generator function
  - a function that can suspend its execution before reaching return
    - can indirectly pass control to another coroutine for some time
- See [`async_io/count_async.py`](src/async_io/count_async.py)
  - talking to each of the calls to `count()` is a single event loop, or coordinator
  - when each task reaches `await asyncio.sleep(1)`, the function informs the event loop and gives control back to it
    - stand-in for any time-intensive processes that involve wait time
    - the benefit of awaiting something is that the surrounding function can temporarily cede control to another function that's more readily able to do something immediately
  - [`async def`](https://docs.python.org/3/reference/compound_stmts.html#coroutine-function-definition)
    - introduces either a _native coroutine_ or an _asynchronous generator_
  - [`await`](https://docs.python.org/3/reference/expressions.html#await-expression)
    - suspend the execution of coroutine on an awaitable object
    - can only be used inside a coroutine function
  - [`asyncio.run(coro, *, debug=False)`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run)
    - runs the passed coroutine `coro`, taking care of managing the asyncio event loop and finalizing asynchronous generators
    - always creates a new event loop and closes it at the end
      - cannot be called when another asyncio event loop is running in the same thread
    - should be used as a main entry point for asyncio programs
      - ideally called only once
    - if `debug` is `True`, the event loop will be run in debug mode
  - [`awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather)
    - runs awaitable objects in the `aws` sequence concurrently
    - if any awaitable in `aws` is a coroutine, it is automatically scheduled as a Task
    - if all awaitables are completed successfully, the result is an aggregate list of returned values
      - order of result values corresponds to the order of awaitables in `aws`
    - `return_exceptions`
      - `False` (default): the first raised exception is immediately propagated to the task that awaits on `gather()`
        - other awaitables in the `aws` sequence won't be cancelled and will continue to run
      - `True`: exceptions are treated the same as successful results, and aggregated in the result list
  - [`coroutine asyncio.sleep(delay, result=None, *, loop=None)`](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep)
    - blocks for `delay` seconds
      - suspends the current task, allowing other tasks to run
    - if `result` is provided, it is returned to the caller when the coroutine completes

```console
$ python count_async.py
One
One
One
Two
Two
Two
count_async.py executed in 1.00 seconds.
```

### The Rules of Async IO

- A coroutine may use `await`, `return`, or `yield`, but all of these are optional
  - using `await` and/or `return` creates a coroutine function
  - to call a coroutine function, you must `await` it to get its results
  - using `yield` in an `async def` block creates an _asynchronous generator_, which you iterate over with `async for`
- Anything defined with `async def` may not use `yield from`, which will raise a `SyntaxError`
- It is a `SyntaxError` to use `await` outside of an `async def` coroutine
- An older way of marking a function as a coroutine is to decorate a normal `def` function with `@asyncio.coroutine`
  - a generator-based coroutine
  - deprecated, scheduled for removal in Python 3.10
- See [`async_io/rand_async.py`](src/async_io/rand_async.py)

## Sources

- "Concurrency in Python - Quick Guide." _Tutorialspoint_, [www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm](https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm).
- Anderson, Jim. "Speed Up Your Python Program With Concurrency." _Real Python_, Real Python, 3 July 2020, [realpython.com/python-concurrency/](https://realpython.com/python-concurrency/).
- McCurdy, Marcus. "Python Multithreading and Multiprocessing Tutorial." _Toptal Engineering Blog_, Toptal, 14 Jan. 2020, [www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python](https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python).
- Solomon, Brad. "Async IO in Python: A Complete Walkthrough." _Real Python_, Real Python, 16 Jan. 2019, [realpython.com/async-io-python/](https://realpython.com/async-io-python/).
