#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import argparse

from app.main import pentest
from app.platform import Color

version = "1.4.0"
banner='''
__        __   _     _             _        ____                  
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/ 
      From WeblogicScan V1.2 Fixed by BaiZhu | V {} 
'''.format(version)
print(Color.OKYELLOW+banner+Color.ENDC)
# print('Welcome To WeblogicScan !!')

parse = argparse.ArgumentParser()
parse.add_argument("-u", "--host", type=str, help="Target Host", required=True)
parse.add_argument("-p", "--port", type=int, help="Target Port", required=True)
parse.add_argument("-s", "--ssl", type=bool, help="Is https", required=False, default=False)
args = parse.parse_args()
protocol = "https://" if args.ssl else "http://"
pentest(args.host, args.port, protocol)

