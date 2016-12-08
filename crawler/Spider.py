# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import cx_Oracle
class QDW:
    #http://python.jobbole.com/81353/
    def __init__(self):
        self.file=None
    def getInfo(self):
#        self.file = open("file.txt",'w+');
        url = self.readUrl()
        print url[0]
        print url[0]
        try:
            request = urllib2.request(url[0])
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            print content
            #    print content
            pattern = re.compile(
                '<td class="w184">' + u'\u54c1\u724c\u540d\u79f0\uff1a' + '<span title="(.*?)">.*?</span></td>.*?<td>' + u'\u884c\u4e1a\u5206\u7c7b\uff1a' +
                '<span title="(.*?)">.*?<td>' + u'\u62db\u5546\u5730\u533a\uff1a' + '<span .*?>(.*?)</span>.*?' + u'\u54c1\u724c\u53d1\u6e90\uff1a' +
                '<span title="(.*?)">.*?</span>.*?' + u'\u6295\u8d44\u91d1\u989d\uff1a' + '.*?<span .*?>(.*?)</span>.*?' + u'\u52a0\u76df\u8d39\u7528\uff1a' +
                '<span .*?>(.*?)</span>.*?' + u'\u5408\u4f5c\u6a21\u5f0f\uff1a' + '<span .*?>(.*?)</span>.*?' + u'\u4e3b\u8425\u4ea7\u54c1\uff1a' +
                '<span title="(.*?)">.*?' + u'\u8fd0\u8425\u673a\u6784\uff1a' + '<span title="(.*?)">.*?' + u'\u516c\u53f8\u5730\u5740\uff1a' +
                '<span title="(.*?)">', re.s)
            print '------1'
            items = re.findall(pattern, content)
            iteminfo = ''
            print '-------2'
            for item in items:
                print len(item)
                for index in range(len(item)):
                    if index != len(item) - 1:
                        iteminfo = iteminfo + item[index] + "***"
                    else:
                        iteminfo = iteminfo + item[index] + "\n"
            print iteminfo
            #             self.writedata(iteminfo.encode('utf-8'))
        except urllib2.urlerror, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
     # 写入文件
    def writeData(self,info):
        self.file.write(info)
    #从数据库读取数据
    def readUrl(self):
        conn = cx_Oracle.connect('orcl/orcl@localhost/orcl')
        cursor = conn.cursor()
        cursor.execute('select url from qdw_cy_wc')
        row = cursor.fetchone()
        cursor.close()
        return row
    def start(self):
       self.getInfo(self)
    def insertOracle(self):
        conn = cx_Oracle.connect('orcl/orcl@localhost/ORCL')


spider = QDW()
spider.getInfo()
























