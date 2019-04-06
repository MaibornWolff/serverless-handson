from multiprocessing import Process
import os
import requests
import time
import sched
import datetime
import sys


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
    function_id = None
    runtime_in_seconds = None
    request_type = None

    def __init__(self, base_url, requests_per_second, function_id, runtime_in_seconds, request_type):
        self.base_url = base_url
        self.requests_per_second = requests_per_second
        self.function_id = function_id
        self.runtime_in_seconds = runtime_in_seconds
        self.request_type = request_type

    def start_processes(self, request_per_second):
        url = str(self.base_url)+str(self.function_id)
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

        def run_task(runtime_in_seconds):
            delay = 1
            try:
                start = time.time()
                self.start_processes(self.requests_per_second)
                end = time.time()
                delay = 1-(end-start)

                print("Function:", self.function_id, "- ProcessId:", os.getpid(), "- Counter:", runtime_in_seconds, "- ", "Duration: ", round(end - start,3),
                      "seconds - Time:",
                      str(datetime.datetime.now().time()))
            finally:
                try:
                    runtime_in_seconds -= 1
                    if runtime_in_seconds > 0:
                        s.enter(delay=delay, priority=1, action=run_task,argument=(runtime_in_seconds,))
                except KeyboardInterrupt:
                    sys.exit(0)

        run_task(self.runtime_in_seconds)
        try:
            s.run()
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == '__main__':
    function_id = sys.argv[1]
    #runtime_in_seconds = sys.argv[2]
    #requests_per_second_list = sys.argv[3:]
    print ("Function id: "+str(function_id))
    #print("Runtime in seconds: "+ str(runtime_in_seconds))
    #print ("Requests per second"+ str(requests_per_second_list))
    base_url = "https://7gq3h2i9m3.execute-api.eu-central-1.amazonaws.com/dev/hello"

    while True:
        keypress = input()

        if keypress == "exit":
            exit(0)
        else:
            print("  RUN")
            call(base_url+str(function_id), "GET")
            print("  END")
