from django.shortcuts import render,render_to_response
from django.template import RequestContext
import sys
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,Http404
from datetime import datetime
import time
import os
import json

from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

jobstores = {

    'default': SQLAlchemyJobStore(url='sqlite:///db.sqlite3')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
scheduler.start()

def test_1():
    print("test1")
    print('Tick! The time is: %s' % datetime.now())

def test_2():
    print("test2")
    print('Tick! The time is: %s' % datetime.now())

def test_3():
    print("test3")
    print('Tick! The time is: %s' % datetime.now())

# Create your views here.
def hello_world(request):
    #scheduler = BackgroundScheduler()
    running_jobs = scheduler.get_jobs()
    print("leo test scheduler.get_jobs()")
    #print("len(running_jobs)")
    #print(len(running_jobs))
    #print("running_jobs")
    #print(running_jobs)
    s_running_jobs = []
    re_running_jobs = []
    #re_running_jobs = [['a','b'],['c','d']]

    if len(running_jobs)>=2:
        """    
        print("running_jobs[0]")
        print(running_jobs[0].name)
        print(running_jobs[0].next_run_time)
        print("running_jobs[1]")
        print(running_jobs[1].name)
        print(running_jobs[1].next_run_time)
        """
        for running_job in running_jobs:
            #print(running_job.name)
            #print(running_job.next_run_time)
            re_running_jobs.append([running_job.name,running_job.next_run_time])
        #print("re_running_job")
        #print(re_running_jobs)
    today = datetime.now()
    return render_to_response('hello_world.html',{"running_jobs": running_jobs,"today":today},context_instance = RequestContext(request))

def test1(request):
    print("test1 ")
    #scheduler = BackgroundScheduler()
    scheduler.add_job(test_1, 'interval',id='my_test_job1', seconds=3)
    #scheduler.start()
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))

def test2(request):
    print("test2 ")
    #scheduler = BackgroundScheduler()
    scheduler.add_job(test_2, 'interval',id='my_test_job2', seconds=3)
    #scheduler.start()
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))

def test3(request):
    print("test3 ")
    #scheduler = BackgroundScheduler()
    scheduler.add_job(test_3, 'cron',id='my_test_job3', day_of_week='0-5', hour='17', minute='21')
    #scheduler.add_job(test_2, 'cron', id='my_test_job3', day_of_week='0-5', hour='17', minute='19')
    #scheduler.start()
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))

@csrf_exempt
def aps_del(request):
    #print("leo test in aps del")

    if request.is_ajax():
        print("leo test in aps del")
        if request.POST.get('job-id') is not None:
            #print("job del:"+request.POST.get('job-id'))
            jobid = request.POST.get('job-id')
            scheduler.remove_job(jobid)

        return HttpResponse(json.dumps({'name': ""}), content_type="application/json")
    else:
        raise Http404