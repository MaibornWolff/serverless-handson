from multiprocessing import Process
import os
import requests
import time
import sched
import datetime
import sys
import threading


def call(url):
    try:
        r = requests.get(url=url)
    except KeyboardInterrupt:
        sys.exit(0)


class RequestThread (threading.Thread):
    base_url = None
    function_name = None
    request_type = None
    requests_per_second = None

    def __init__(self, thread_id, thread_name, requests_per_second, base_url, function_name, request_type):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = thread_name
        self.requests_per_second = requests_per_second
        self.base_url = base_url
        self.function_name = function_name
        self.request_type = request_type

    def run(self):
        print (threading.currentThread().getName(), ":", "Starting " + self.name)
        CallInfo(base_url=self.base_url, function_name=self.function_name, requests_per_second=self.requests_per_second,
                 request_type=self.request_type).schedule_per_second()
        print (threading.currentThread().getName(), ":", "Exiting " + self.name)


class CallInfo():
    base_url = None
    requests_per_second = None
    function_name = None
    request_type = None

    def __init__(self,base_url, requests_per_second, function_name, request_type):
        self.base_url = base_url
        self.requests_per_second = requests_per_second
        self.function_name = function_name
        self.request_type = request_type

    def start_processes(self, request_per_second):
        url = str(self.base_url)+str(self.function_name)
        index = 0

        try:
            while index < request_per_second:
                p = Process(target=call, args=(url,))
                p.start()
                index +=1
        except KeyboardInterrupt:
            sys.exit(0)

    def schedule_per_second(self):
        s = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)

        def run_task():
            delay = 1
            try:
                start = time.time()
                self.start_processes(self.requests_per_second)
                end = time.time()
                delay = 1-(end-start)


                print("ProcessId:", os.getpid(), " - ", "Runned: ", end - start, "seconds - Time:",
                      str(datetime.datetime.now().time()))
            finally:
                try:
                    s.enter(delay=delay, priority=1, action=run_task)
                except KeyboardInterrupt:
                    sys.exit(0)

        run_task()
        try:
            s.run()
        except KeyboardInterrupt:
            sys.exit(0)

def run(base_url, function_name, requests_per_second, request_type):
    index=0
    while index < requests_per_second:
        thread = RequestThread(index, "Thread-" + function_name + "-" + str(index), index, base_url, function_name, request_type)
        thread.start()
        index +=1

    print("Calling", base_url+function_name, requests_per_second, "times per second")


if __name__ == '__main__':
    base_url = "https://to73aro3i5.execute-api.eu-central-1.amazonaws.com/dev/"
    run(base_url=base_url, function_name="hello42", requests_per_second=10, request_type="GET")
    run(base_url=base_url, function_name="hello43", requests_per_second=20, request_type="GET")
    run(base_url=base_url, function_name="hello44", requests_per_second=30, request_type="GET")
    run(base_url=base_url, function_name="hello45", requests_per_second=50, request_type="GET")
