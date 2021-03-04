#!/usr/bin/python
# -*- coding:utf-8

import os
import csv
import json
import sys


from common.font import *
from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())


print(red('''
    ___       ___       ___       ___       ___       ___ 
   /\  \     /\  \     /\  \     /\  \     /\  \     /\  \ 
  /::\  \   /::\  \    \:\  \   /::\  \    \:\  \   /::\  \ 
 /::\:\__\ /:/\:\__\   /::\__\ /::\:\__\   /::\__\ /:/\:\__\ ''')+blue(''' 
 \/\::/  / \:\/:/  /  /:/\/__/ \/\::/  /  /:/\/__/ \:\/:/  / 
    \/__/   \::/  /   \/__/      /:/  /   \/__/     \::/  / 
             \/__/               \/__/               \/__/ 
'''))
print(red('''
    ____        __        __      
   / __ \____ _/ /_____ _/ /_____ 
  / /_/ / __ `/ __/ __ `/ __/ __ \ ''')+blue(''' 
 / ____/ /_/ / /_/ /_/ / /_/ /_/ / 
/_/    \____/\__/\__,_/\__/\____/ 
'''))
print(red('''
                 __        __      
    ____  ____ _/ /_____ _/ /_____ 
   / __ \/ __ `/ __/ __ `/ __/ __ \ 
  / /_/ / /_/ / /_/ /_/ / /_/ /_/ / ''')+blue(''' 
 / .___/\____/\__/\__,_/\__/\____/ 
/_/  
'''))