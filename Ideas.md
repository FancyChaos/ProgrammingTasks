# Ideas/Suggestions for future tasks
Different programming tasks ideas can be found here which should get implemented in the future.

If you have a great idea for one then please write it down in this document and do a pull request so that others can implement your task :)\
Of course you can implement you own idea by yourself, this document should just show what will be included in the future and serves as a notebook.

Suggestions for improvements of already existing task can be written down too.

You don't need to write down your idea in great detail, a small explanation of what the task is about and what should it teach is just enough.

If someone is willing to implement an idea he/she should put his name behind the chosen task.\
That way there won't be two people who are working on the same thing.

## 1 - Basic OOP task (Will be implemented by Felix)
The task is to create a simple **Car** class.\
The class should contain attributes related to a car e.g. how much fuel is left, as well as methods which will do something. For example a **drive** method which will drain the fuel of the car.

The goal is to teach the **fundamentals** of OOP in python.

## 2 - Subprocess (feel free to build!)
Use subprocess in combination with pipes in both directions - STDIN and STDOUT
May be combined with io streaming tasks. Lessons should be to avoid creating
huge memory footprints by saving huge amount of data in python variables.

## 3 - asyncio "Hello World" (feel free to build!)
Create a program using an asyncio event loop to run many tasks in parallel.
Maybe something like a very simple async HTTP server?

# Old Ideas Done in some way

## 1 - Working with io lib (Done in /moderate/iolib by Maxi)
Create python2 / python3 compatible programs with low memory footprint handling
huge volumes of data. Buzzword "Streaming"

## 2 - Flask / Django "Hello World" (Done in /hard/flask by Maxi)
Using different frameworks is useful to understand why Zope + DB_Utils is in
fact a very powerful toolkit.

Building a small web application, maybe add database connector for persistence layer.
Add frontend magic using JS libs and stuff

## 3 - Multithreading (Done in hard/Sockets_Multithreading by Maxi)
Tasks creating a high i/o load can be parallelized using threads. Most popular
example is fetching content from different urls in parallel to save time.

Task could be something like: Create a program fetching content from N given URLs
as fast as possible using one thread per URL.

Thoughts:
+ Use Multithreading Queue

## 4 - Multiprocessing (Done in expert/multiprocessing by Maxi)
Tasks creating a high cpu load can be parallelized using multiprocessing.

Tasks could be something like: Create a program taking N integers checking those
to be a prime number - in parallel using one process per integer.

Thoughts:
+ Use Multiprocessing Queue

## 5 - Sockets (Done in hard/Sockets_Multithreading by Maxi)
Use builtin socket lib to build a simple telnet chat program. Do NOT use higher
level APIs!


## 6 - Python GUI "Hello World" (Done in /hard/Gui_kivy by Maxi)
Use a python gui framework of your trust and choice (wx, kivy, tkinter ...) to
create a simple GUI, e.g. a logfile reader/editor.

## 7 - Selenium Hello World (Done in /hard/Selenium by Maxi)
