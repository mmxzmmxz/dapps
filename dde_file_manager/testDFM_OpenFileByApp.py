#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from time import sleep
import json
from lib import runTest
from subprocess import getstatusoutput as rt
from lib import window

#2017-05-11 created by cherry
class DFM_OpenFileByApp(unittest.TestCase):
    caseid = '0000001'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testOpenFile.doc'
        cls.eventType = 'OpenFileByApp'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.appName = '/usr/share/applications/wps-office-wps.desktop'
        #cls.applicationName = 'testOpenFile.doc - WPS 文字 - 兼容模式'
        cls.applicationName = 'WPS 文字'

    @classmethod
    def tearDownClass(cls):
        pass

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testOpenFileByApp_URL_APPNAME(self):
        args = {"eventType": self.eventType,
                "url": self.testFilePath,
                "appName": self.appName,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        (status, output) = rt(cmdstring)

        docwin = window.findWindowByAppName(self.applicationName)
        #sleep(2)
        self.assertTrue(None != docwin)

        #sleep(2)
        window.closeWindow(docwin)

        docwinclose = window.findWindowByAppName(self.applicationName, mode="nowait")
        self.assertTrue(None == docwinclose)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_OpenFileByApp('testOpenFileByApp_URL_APPNAME'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_OpenFileByApp)

