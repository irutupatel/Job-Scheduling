# project3.py
# Rutu Patel
# rpatel53@stu.parkland.edu
# CSC 220, Spring 2017

import sys
from Scheduler import Scheduler


if __name__ == '__main__':
    file = sys.argv[1]
    sleepTime = float(sys.argv[2])

    jobsdata = Scheduler()

    jobsdata.loadJobs(sys.argv[1])
    run = jobsdata.Run(sleepTime)



