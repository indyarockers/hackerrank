#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
p=0
sum=0
arr.sort()
while (p<len(arr)):
    print len(arr)-p
    temp=arr[p]
    while(arr[p]==temp):
        p+=1
    