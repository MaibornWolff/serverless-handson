import requests
import logging
import threading
import sched, time, datetime

class RequestThread (threading.Thread):
    base_url = None
    function_name = None
    request_type = None

    def __init__(self, thread_id, thread_name, counter, base_url, function_name, request_type):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = thread_name
        self.counter = counter
        self.base_url = base_url
        self.function_name = function_name
        self.request_type = request_type

    def run(self):
        print (threading.currentThread().getName(), ":", "Starting " + self.name)
        call_lambda_continously(self.base_url, self.function_name, self.request_type)
        print (threading.currentThread().getName(), ":", "Exiting " + self.name)


def call_lambda(url, request_type):
    try:
        r = None
        if request_type == "GET":
            r = requests.get(url=url)
        elif request_type == "POST":
            r = requests.post(url=url+"/"+"fooParameter")
        else:
            raise Exception("unknown request type"+request_type)

        if(r.status_code == 200 and r.reason == "OK"):
            return True
        else:
            raise Exception('Elastic API didnt response as expected', {'statusCode': r.status_code, 'reason': r.reason, 'content': r.content})
    except Exception as ex:
        print (threading.currentThread().getName(), ":", "Connection Error happend, will be ignored")



def schedule_per_second(url, request_type):
    s = sched.scheduler(timefunc=time.time,delayfunc=time.sleep)

    def run_task():
        delay = 1
        try:
            start = time.time()
            call_lambda(url, request_type)
            end = time.time()
            delay = 1-(end-start)

            if "Thread-hello44" in threading.currentThread().getName():
                print(threading.currentThread().getName(), ":", "Runned ", end - start, "seconds - Time", str(datetime.datetime.now().time()))
        finally:
            s.enter(delay=delay, priority=1, action=run_task)

    run_task()
    try:
        s.run()
    except KeyboardInterrupt:
        print('Manual break by user')
        return 10

    return 0

def call_lambda_continously(base_url, function_name, request_type):
    url = base_url+function_name

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info("Calling lambda function")

    schedule_per_second(url, request_type)

def run(base_url, function_name, requests_per_second, request_type):
    counter=0
    while counter < requests_per_second:
        thread = RequestThread(counter, "Thread-" + function_name + "-" + str(counter), counter, base_url,function_name, request_type)
        thread.start()
        counter +=1

    print("Calling", base_url+function_name, requests_per_second, "times per second")


if __name__ == "__main__":
    base_url = "https://b002lhcuyb.execute-api.eu-central-1.amazonaws.com/dev/"

    run(base_url=base_url, function_name="hello1", requests_per_second=100, request_type="POST")
    #run(base_url=base_url, function_name="hello2", requests_per_second=50, request_type="GET")
    #run(base_url=base_url, function_name="hello3", requests_per_second=50, request_type="GET")
    #run(base_url=base_url, function_name="hello4", requests_per_second=50, request_type="GET")
    #run(base_url=base_url, function_name="hello5", requests_per_second=50, request_type="GET")
