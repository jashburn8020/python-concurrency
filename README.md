# Python Concurrency

Summary of concurrency in Python sourced from various articles.

- [Python Concurrency](#python-concurrency)
  - [Introduction](#introduction)
  - [Concurrency and Parallelism](#concurrency-and-parallelism)
  - [When Is Concurrency Useful](#when-is-concurrency-useful)
  - [Sources](#sources)

## Introduction

- Concurrency is when two tasks overlap in execution
- With concurrent programming, the performance of our applications and software systems can be improved because we can concurrently deal with the requests rather than waiting for a previous one to be completed
- **Thread**
  - smallest unit of execution that can be performed in an operating system
  - runs within a program
  - threads are not independent of one other
    - each thread shares code section, data section, etc. with other threads
  - also known as lightweight processes
  - consists of the following components:
    - program counter which consist of the address of the next executable instruction
    - stack
    - set of registers
    - unique id
- **Multithreading**
  - the ability of a CPU to manage the use of operating system by executing multiple threads concurrently
  - achieve parallelism by dividing a process into multiple threads
- **Process**
  - represents the basic unit of work to be implemented in the system
  - when a computer program is executed, it becomes a process that performs all the tasks mentioned in the program
  - the process life cycle passes through different stages:
    - Start: can progress to Ready
    - Ready: can progress to Running
    - Running: can progress to Ready, Wait or Terminated
    - Wait: can progress to Ready
    - Terminated
  - can have
    - only one thread, called primary thread
    - multiple threads each having their own set of registers, program counter and stack
- **Multiprocessing**
  - the use of two or more CPUs within a single computer system
- **GIL (Global Interpreter Lock)**
  - in CPython, GIL is the mutex - the mutual exclusion lock - which makes things thread-safe
  - prevents multiple threads from executing Python code in parallel
  - the lock can be held by only one thread at a time and if we want to execute a thread then it must acquire the lock first
  - necessary because CPython's memory management is not thread-safe
  - there are some libraries and implementations in Python such as Numpy, Jython and IronPython that work without any interaction with GIL

## Concurrency and Parallelism

- Concurrency: making progress on more than 1 task simultaneously
  - in Python, `threading` and `asyncio` both run on a single processor and therefore only run one at a time
    - they find ways to take turns to speed up the overall process
  - `threading`: uses _pre-emptive multitasking_
    - the operating system actually knows about each thread and can interrupt it at any time to start running a different thread, i.e., pre-empt your thread to make the switch
    - this switch can happen at any time, including in the middle of a single Python statement
  - `asyncio`: uses _cooperative multitasking_
    - tasks must coded to cooperate by announcing when they are ready to be switched out
    - you always know where your task will be swapped out
- Parallelism: process tasks or subtasks (by splitting a task) in parallel, for instance on multiple CPUs or cores, at the exact same time
  - with `multiprocessing`, Python creates new processes
    - each task in a multiprocessing program can run on a different core, and at the same time

## When Is Concurrency Useful

- Concurrency can make a big difference for two types of problems: I/O-bound and CPU-bound
- **I/O-bound** problems cause your program to slow down because it frequently must wait for input/output (I/O) from some external resource
  - arise frequently when your program is working with things that are much slower than your CPU
  - the slow things your program will interact with most frequently are the file system and network connections
- **CPU-bound** programs: programs that do significant computation without talking to the network or accessing a file
  - the resource limiting the speed of your program is the CPU

## Sources

- "Concurrency in Python - Quick Guide." _Tutorialspoint_, [www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm](https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm).
- Anderson, Jim. "Speed Up Your Python Program With Concurrency." _Real Python_, Real Python, 3 July 2020, [realpython.com/python-concurrency/](https://realpython.com/python-concurrency/).
- McCurdy, Marcus. "Python Multithreading and Multiprocessing Tutorial." _Toptal Engineering Blog_, Toptal, 14 Jan. 2020, [www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python](https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python).
