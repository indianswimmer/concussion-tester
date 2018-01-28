import csv
import numpy
#parses data to list

f=open('/Users/Andrew/Downloads/adi_first_recording.csv')
reader = csv.reader(f)
acc = []
count=0
#running numpi on whole file is too time consuming
numlines = 46419
while(count<300):
    row = next(reader)
    row = row[2:]
    for x in row:
        try:
            fx = float(x)
            acc.append(fx)
        except:
            continue
    count=count+1

        
if __name__=='__main__':
    #fourier transform seems to work idk what to do w it tho...
    d=numpy.fft.fft(acc)
    count=0
    while(count<20):
        print(d[count])
        count= count+1
        
        
        
