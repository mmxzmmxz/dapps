#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import json
from lib import runTest
from subprocess import getstatusoutput as rt
from lib import window

class DFM_OpenFile(unittest.TestCase):
    caseid = '0000000'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName = 'testOpenFile.doc'
        cls.eventType = 'OpenFile'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.windowName = 'testOpenFile.doc - WPS 文字 - 兼容模式'

    @classmethod
    def tearDownClass(cls):
        pass

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testOpenFile_URL(self):
        args = {"eventType": self.eventType,
                "url": self.testFilePath,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        (status, output) = rt(cmdstring)

        docwin = window.findWindow(self.windowName)
        self.assertTrue(None != docwin)

        window.closeWindow(docwin)

        docwinclose = window.findWindow(self.windowName, mode="nowait")
        self.assertTrue(None == docwinclose)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_OpenFile('testOpenFile_URL'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_OpenFile)

