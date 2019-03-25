from multiprocessing import Process
import os
import requests
import time
import sched
import datetime
import sys
import threading


def call(url, request_type):
    r = None
    try:
        if request_type == "GET":
            r = requests.get(url=url)
        elif request_type == "POST":
            r = requests.post(url=url+"/"+"fooParameter")
        else:
            raise Exception("unknown request type"+request_type)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as ex:
        print ("ProcessId:", os.getpid(), "Connection Error happend, will be ignored")
        print (ex)
        return 0

    if(r.status_code == 200 and r.reason == "OK"):
        return True
    else:
        raise Exception('Elastic API didnt response as expected', {'statusCode': r.status_code, 'reason': r.reason, 'content': r.content})



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
                p = Process(target=call, args=(url,self.request_type))
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

                print(self.function_name, "- ProcessId:", os.getpid(), " - ", "Runned: ", end - start, "seconds - Time:",
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


if __name__ == '__main__':
    base_url = "https://b002lhcuyb.execute-api.eu-central-1.amazonaws.com/dev/"
    CallInfo(base_url=base_url, function_name="hello4", requests_per_second=40, request_type="GET").schedule_per_second()
