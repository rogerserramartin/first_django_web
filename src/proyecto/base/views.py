from django.shortcuts import render
from django.http import HttpResponse


def list_todo(task):
    return HttpResponse('TODO list') # this is what this method returns


