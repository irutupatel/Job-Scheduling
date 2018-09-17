# Scheduler.py
# Rutu Patel
# rpatel53@stu.parkland.edu
# CSC 220, Spring 2017

from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from time import sleep
from Empty import Empty


class Scheduler(AdaptableHeapPriorityQueue):
    class _Job:
        def __init__(self, name, priority, length):
            self._name = name
            self._priority = priority
            self._length = length
            self._totalNumber = length

        def get_name(self):
            return self._name

        def set_name(self, name):
            self._name = name

        def get_priority(self):
            return self._priority

        def set_priority(self, priority):
            if not isinstance(priority, int):
                raise TypeError('Priority values should be an integers')
            if not -20 <= priority <= 19:
                raise ValueError('Priority values should be between -20 and 19')
            self._priority = priority

        def get_length(self):
            return self._length

        def set_length(self, length):
            if not isinstance(length, int):
                raise TypeError('Length values should be an integer')
            if not 1 <= length <= 100:
                raise ValueError('Length values es should be between 0 and 100')
            self._length = length

        def get_totalNumber(self):
            return self._totalNumber

        def printJobs(self):
            # Not sure if printing jobs should have been in _Job or Scheduler. But I felt that it
            # should be here in _Job inner class.
            output = "Current job is '{0}', priority {1}" \
                     " iteration {2} of {3}.".format(self._name, self._priority,self._totalNumber - self._length + 1,
                                                                                       self._totalNumber)
            print(output)

    def __init__(self):
        super().__init__()
        self.__locators = []

    def loadJobs(self, file):
        with open(file, 'r') as infile:
            text = infile.read()
            lines = text.split('\n')
            for line_number, line_value in enumerate(lines):
                if line_value is not '':
                    if not line_value.startswith('JOB,PRIORITY,LENGTH'):
                        element = line_value.split(',')
                        job = self._Job(element[0], int(element[1]), int(element[2]))
                        locator = self.add((job.get_priority(), job.get_length()), job)
                        self.__locators.append(locator)

    def Run(self, sleepTime):
        while self:
            try:
                # Here I'm printing the stats as of its current status
                currentKey, currentJob = self.min()
                self._Job.printJobs(currentJob)
                sleep(sleepTime)
                # This is for Updating, check the length, and then making a newLength for
                # saving and then assigning it to currentJob. Because each job should run according to its length, so -1 at a time.
                if currentJob.get_length() > 1:
                    newLength = currentJob.get_length() - 1
                    currentJob.set_length(newLength)
                else:
                    removed_item = self.remove_min()
            except KeyboardInterrupt:
                self.Halt()

    def Halt(self):
        '''Halt lets the user halt the scheduler and allow the user to add new job, or alter job, or
        allow the user to change priority. It also allows user to sort like they want, say by job,
        by priority, by length or by heap which would be the default order.'''

        # First let the user know that the scheduler is been halted.
        print(" \n Scheduler has been halted ... ")
        # Now because of halt, the minimum would have to be updates with the remaining length.
        # CurrentKey and CurrentJob are values at time of halt, just like above.
        currentKey, currentJob = self.remove_min()
        self.add((currentKey[0], currentJob.get_length()), currentJob)

        sortBy = input(" Sort by (j/p/l/h) : ")  # All input allows user to input what they want to change


        self._sort_and_print(sortBy)

        # When user wants to add a new job
        newJob = input("New job? (y/n) : ")
        if newJob == 'y':
            name = input("New job name: ")
            priority = int(input("New job priority: "))
            length = int(input("New job length: "))
            newJob = self._Job(name, priority, length)
            locator = self.add((priority, length), newJob)
            self.__locators.append(locator)

        # When user wants to alter priority of any job
        alterPriority = input("Alter priority? (y/n : )")
        if alterPriority == 'y':
            locator = ''
            name = input("Job name: ")
            priority = int(input("New Priority: "))
            # Don't need length here, just altering priority
            triggered = False
            for loc in self._data:
                if loc._value.get_name() == name:
                    locator = loc
                    triggered = True
            if triggered:
                newJob = self._Job(name, priority, locator._key[1])
                self.update(locator, (priority, locator._key[1]), newJob)

        # Back to job scheduling
        print("Restart Scheduling...")

    def _sort_and_print(self, sortby):
        bucklelist = list()
        # If the user input says sort by job other, not default(heap order)
        if sortby == 'j':
            for element in self._data:
                bucklelist.append([element._value.get_name(), element._value])
        elif sortby == 'p':
            for element in self._data:
                bucklelist.append([element._value.get_priority(), element._value])
        elif sortby == 'l':
            for element in self._data:
                bucklelist.append([element._value.get_length(), element._value])
        elif sortby == 'h':
            while self:
                bucklelist.append(self.remove_min())
            for element in bucklelist:
                self.add(element[0], element[1])
        else: #default sort
            print(self)
            return
        sortedlist = sorted(bucklelist, key=lambda job: job[0])
        output = '{0:<20}{1:>15}{2:>15}'.format('Name', 'Priority', 'Length')
        output += '\n' + '-' * 50 + '\n'
        for element in sortedlist:
            output += '{0:<20}{1:>15}{2:>15}\n'.format(element[1].get_name(),
                                                       element[1].get_priority(),
                                                       element[1].get_length())
        print(output)

    def __repr__(self):
        output = '{0:<20}{1:>15}{2:>15}'.format('Name', 'Priority', 'Length')
        output += '\n' + '-' * 50 + '\n'
        for element in self.__locators:
            if element._value.get_length() > 1:
                output += '{0:<20}{1:>15}{2:>15}\n'.format(element._value.get_name(), element._value.get_priority(),
                                                       element._value.get_length())
        return output


if __name__ == '__main__':
    print("Batch Job scheduling")
    print("Run as python project.py <inputfile> <sleeptime>")
