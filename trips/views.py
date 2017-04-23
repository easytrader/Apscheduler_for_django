from django.shortcuts import render,render_to_response
from django.template import RequestContext
import sys
import os

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def test_1():
    print("test1")
    print('Tick! The time is: %s' % datetime.now())

def test_2():
    print("test2")
    print('Tick! The time is: %s' % datetime.now())

# Create your views here.
def hello_world(request):
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))

def test1(request):
    print("test1 ")
    scheduler = BackgroundScheduler()
    scheduler.add_job(test_1, 'interval', seconds=3)
    scheduler.start()
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))

def test2(request):
    print("test2 ")
    scheduler = BackgroundScheduler()
    scheduler.add_job(test_2, 'interval', seconds=3)
    scheduler.start()
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))