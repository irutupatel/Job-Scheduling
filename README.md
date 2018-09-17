Description:
This project is a simulator for a batch job scheduler. Initial jobs are read 
from a user-supplied input file, placed into the queue, and then scheduler is
started. Jobs run by priority (-20 highest priorty to 19 lowest priority), 
then by shortest length. Users may halt the scheduler in order to add new jobs or alter the priority of an existing job.

Dependencies:
from textbook --
- adaptable_heap_priority_queue.py
- heap_priority_queue.py
- priority_queue_base.py
- Empty.py
original --
- project3.py
- Scheduler.py

Requirements:
- Python 3  
- sys module
- time module
- input csv of jobs

Run as:
$ python3 project3.py <input-job-listing> <sleep-time>

Operation:
Ctrl-C once to pause scheduler. Prompts for entering new job or altering
existing job follow. 
Ctrl-C twice to exit.

Output:
Running output on screen is name, priority and remaining length of
current job. Halted scheduler prints table of all jobs.
