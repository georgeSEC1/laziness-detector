#Copyright - 2023 - George Wagenknecht

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from androidhelper import sl4a
import random
droid = sl4a.Android()
import time
dt = 10 #100ms between sensings
droid.startSensingTimed(2,dt) 
n = 0
m = 0
def getRandNGram(data):
    i = random.randint(2,len(data)-2)
    return data[i]
def gather(file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    return text.split(" ")
data = gather("/storage/emulated/0/qpython/scripts3/xbt")

f = open("/storage/emulated/0/qpython/scripts3/log.txt","a", encoding="utf8")
f.write("\n\n")
f.close()
while(True):
    var = droid.sensorsReadAccelerometer().result
    m+=1
    if var[2] is not None and var[2] == 9.9375:       
        n+=1
        if m > 10:
            m = 0
            print(n)
            if n >= 11:   
                var = getRandNGram(data)
                print (var)
                #droid.mediaPlay("/storage/emulated/0/qpython/scripts3/beep.mp3")
                f = open("/storage/emulated/0/qpython/scripts3/log.txt","a", encoding="utf8")
                f.write(var + " ")
                f.close()
            n = 0