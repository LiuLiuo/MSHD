import os
from django.http import HttpResponse
from django.shortcuts import render
from receiveData.views import *

# Create your views here.
def upload(request):
 if request.method == "POST": # 请求方法为POST时，进行处理
    myFile = request.FILES.get("myfile", None) # 获取上传的文件，如果没有文件，则默认为None
    if not myFile:
        return HttpResponse("no files for upload!")
 # destination=open(os.path.join('upload',myFile.name),'wb+')
    destination = open(os.path.join("D:/upload", myFile.name),'wb+') # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks(): # 分块写入文件
      destination.write(chunk)
      destination.close()
    MSCode='202'
    savetheData(MSCode)
    return HttpResponse("upload over!")
 else:
    file_list = []
    files = os.listdir('D:/upload')
    for i in files:
        file_list.append(i)
 return render(request, 'upload.html', {'file_list': file_list})
