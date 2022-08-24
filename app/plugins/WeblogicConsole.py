#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
import sys
import requests

from ..platform import ManageProcessor,Color

logging.basicConfig(filename='Weblogic.log',
                        format='%(asctime)s %(message)s',
                        filemode="w", level=logging.INFO)

@ManageProcessor.plugin_register('weblogic-console')
class WeblogicCosole(object):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    def process(self,ip,port,protocol):
        self.run(ip,port,protocol)
    def islive(self,ur,port,protocol):
        url=protocol + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
        r = requests.get(url, headers=self.headers)
        return r.status_code

    def run(self,url,port,protocol):
        if self.islive(url,port)==200:
            u=protocol + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
            logging.info("[+]The target Weblogic console address is exposed! The path is: {} Please try weak password blasting!".format(u))
            print(Color.OKBLUE+"[+]The target Weblogic console address is exposed!\n[+]The path is: {}\n[+]Please try weak password blasting!".format(u)+Color.ENDC)
            print(Color.OKGREEN+'[+]Weblogic后台路径存在'+Color.ENDC)
        else:
            logging.info('[-]Target Weblogic console address not found!')
            print(Color.FAIL+"[-]Target Weblogic console address not found!"+Color.ENDC)
