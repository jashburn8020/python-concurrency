# Python Concurrency

Summary of concurrency in Python sourced from various articles.

- [Python Concurrency](#python-concurrency)
  - [Introduction](#introduction)
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
  - in CPython, GIL is the mutex - the mutual exclusion lock - which makes things thread safe
  - prevents multiple threads from executing Python code in parallel
  - the lock can be held by only one thread at a time and if we want to execute a thread then it must acquire the lock first
  - there are some libraries and implementations in Python such as Numpy, Jython and IronPython that work without any interaction with GIL

## Sources

- "Concurrency in Python - Quick Guide." _Tutorialspoint_, [www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm](https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm).
- Anderson, Jim. "Speed Up Your Python Program With Concurrency." _Real Python_, Real Python, 3 July 2020, [realpython.com/python-concurrency/](https://realpython.com/python-concurrency/).
- McCurdy, Marcus. "Python Multithreading and Multiprocessing Tutorial." _Toptal Engineering Blog_, Toptal, 14 Jan. 2020, [www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python](https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python).
