import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot
#matplotlib.pyplot.ioff()
import matplotlib.pyplot as plt
from pylab import plot,show
from numpy import vstack,array
import json
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
import csv
from Tkinter import *
import numpy as np
# data generation
import urllib2
from bottle import route, run, template
from bottle import route, request, response, template, HTTPResponse
from bottle import static_file
fields = ['sepelLength','sepelWidth','petalLength','petalWidth']
@route('/home')
def index():
    return template('try.html')
   
    
@route('/bar1')
def bar():
    return template('bar1.html')
    
@route('/bar2')
def bar2():
    return template('bar2.html')
    
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static') 

    
@route('/input')
def input():
    return template('main')
    
@route('/get_cluster')
def get_cluster():
    return template('cluster.html')
    
@route('/cluster',  method='POST')
def cluster():  
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        k = posted_dict["k"][0]
        x_param = posted_dict["x_param"][0]
        y_param = posted_dict["y_param"][0]
        print k
        print x_param
        print y_param
        data_arr = []
        x_data_arr = []
        y_data_arr = []
        meal_name_arr = []
        
        vector = getList(x_param,y_param)
        #Fvector = getVector(xList,yList,vector)
        
            
        
        data = vstack(vector)
        
        centroids,_ = kmeans(data,int(k))
        # assign each sample to a cluster
        idx,_ = vq(data,centroids)

       
        print data
        jsonData = []
        
        for i in range(0,int(k)):
                result_names = data[idx==i, 0]
                print "================================="
                print "Cluster " + str(i+1)
                count = 0
                for name in result_names:
                    print name
                    count +=1
                print(count)
                jsonData.append(count)
                
                
                
        fig = plt.figure()
        colors=['ob','og','or','oc','om','oy','ok']
        for i in range(0,int(k)):
            for j in range(0,1):
                plt.plot(data[idx==i,j],data[idx==i,j+1],colors[i])
        
        print idx
        po = []
        
        for p in idx:
           po.append(p)
        print len(po)
       
        file_arr=[]
        r2=[]
        
        csvfile = open("iris_data.csv","r")
        fileDesc = csv.reader(csvfile)
        clusterData=[]
        x_value = []
        y_value = []
        for row in fileDesc:
            
            x_value.append(float(row[0]))
            y_value.append(float(row[1]))
        
        
        with open('kmeans.csv', 'wb') as csvfile:
            fieldnames = ['clusters','x_value','y_value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0, len(idx)):
                writer.writerow({'clusters':str(idx[i]),'x_value':x_value[i],'y_value':y_value[i]})
            
            
            
                
           
        
       
        
       
      #  plt.scatter(data[:,0],data[:,1]),plt.xlabel(x_param),plt.ylabel(y_param)
        plt.plot(centroids[:,0],centroids[:,1],'ok',markersize=8)
        #fig.savefig('temp.png')
        filename = "temp.png"
        fig.savefig("./static/"+filename)
        name = json.dumps({'filename':filename,'jsonData':jsonData})
        resp = HTTPResponse(body = name , status= 200)
        return resp
    
        show()
    
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static') 
    


def getList(x_param,y_param):
    xList = []
    yList = []
    vector = []
    
    csvfile = open("iris_data.csv","r")
    with open('iris_data.csv', 'rb') as f:
            reader = csv.DictReader(f , fieldnames = fields)
            for row in reader:
                v = []
               
                v.append(float(row[x_param]))
                v.append(float(row[y_param]))
                vector.append(v)
           
            return vector
            

    

run(host='0.0.0.0', port=5000, debug = True)
