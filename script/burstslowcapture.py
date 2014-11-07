#!/usr/bin/python
# coding:utf-8

from uiautomatorplug.android import device as d
import unittest
import commands
import os
import string
import time
import sys
import util 
import string
import random

AD           = util.Adb()
tb           = util.TouchButton()
so           = util.SetOption()
sm           = util.SetCaptureMode()
modeNumber   = util.ModeNumber['burst']
Exposure     = util.Exposure
Scenes       = util.Scenes
Geo_Location = util.Geo_Location
Picture_Size = util.Picture_Size

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        AD.setUpDevice(False)
        sm.switchCaptureMode('Burst','Slow')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        AD.pressBackKey(4)
        time.sleep(2)

    def testCaptureWithExposure(self):
        '''
            Summary: Capture image with Exposure
            Steps  :  
                1.Launch burst activity and select fast burst mode
                2.Check exposure setting icon, random set a value
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Exposure) #Random select an option
        so.setCameraOption('Exposure',randomoption,modeNumber)
        tb.captureAndCheckPicCount('single',10)

    def testCapturePictureWithScenes(self):
        '''
            Summary: Capture image with Scene
            Steps  :  
                1.Launch burst activity and select fast burst mode
                2.Check scence mode ,set mode
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Scenes) #Random select an option
        so.setCameraOption('Scenes',randomoption,modeNumber)
        tb.captureAndCheckPicCount('single',10)
        so.setCameraOption('Scenes','auto',modeNumber) #Force set scenes to auto

    def testCaptureWithPictureSize(self):
        '''
            Summary: Capture image with Photo size
            Steps  :  
                1.Launch burst activity and select fast burst mode
                2.Check photo size ,set its size
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Picture_Size) #Random select an option
        so.setCameraOption('Picture Size',randomoption,modeNumber)
        tb.captureAndCheckPicCount('single',10)

    def testCapturepictureWithGeoLocation(self):
        '''
            Summary: Capture image with Geo-tag
            Steps  : 
                1.Launch burst activity and select fast burst mode
                2.Check geo-tag ,set Geo on/off
                3.Touch shutter button to capture burst picture
                4.Exit activity
        '''
        randomoption = random.choice(Geo_Location) #Random select an option
        so.setCameraOption('Geo Location',randomoption,modeNumber)
        tb.captureAndCheckPicCount('single',10)
