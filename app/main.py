#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from .platform import ManageProcessor

def pentest(ip, port, protocol):
    processor = ManageProcessor()
    #print(processor.PLUGINS) # {’plugin1': <class '__main__.CleanMarkdownBolds'>}
    processed = processor.process(ip, port, protocol)
    #processed = processor.process(text="**foo bar**", plugins=('plugin2',))
