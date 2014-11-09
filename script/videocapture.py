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

AD            = util.Adb()
tb            = util.TouchButton()
so            = util.SetOption()
sm            = util.SetCaptureMode()
Exposure      = util.Exposure
White_Balance = util.White_Balance
Geo_Location  = util.Geo_Location
Video_Size    = util.Video_Size
modeNumber    = util.ModeNumber['video']

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        AD.setUpDevice(False)
        sm.switchCaptureMode('Video')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        AD.pressBackKey(4)
        time.sleep(2)

    def testRecordVideoWithVideoSize(self):
        '''
            Summary: Capture video with setting size
            Steps  :  
                1.Launch video activity
                2.Check video size ,set its size setting
                3.Touch shutter button to capture 30s video
                4.Exit activity 
        '''
        randomoption = random.choice(Video_Size) #Random select an option
        so.setCameraOption('Video Size',randomoption,modeNumber)
        tb.captureAndCheckPicCount('video',5)


    def testRecordVideoWithGeoLocation(self):
        '''
            Summary: Record an video with GeoLocation setting
            Steps  :  
                1.Launch video activity
                2.Check geo-tag ,set to ON/OFF
                3.Touch shutter button to capture 30s video
                4.Exit activity 
        '''
        randomoption = random.choice(Geo_Location) #Random select an option
        so.setCameraOption('Geo Location',randomoption,modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithBalance(self):
        '''
            Summary: Capture video with White Balance
            Steps  :  
                1.Launch video activity
                2.Set White Balance
                3.Touch shutter button to capture 30s video
                4.Exit activity
        '''
        randomoption = random.choice(White_Balance) #Random select an option
        so.setCameraOption('White Balance',randomoption,modeNumber)
        tb.captureAndCheckPicCount('video',5)

    def testRecordVideoCaptureVideoWithExposure(self):
        '''
            Summary: Capture video with Exposure
            Steps  :  
                1.Launch Video activity
                2.Touch Exposure Setting icon, set Exposure settings
                3.Touch shutter button
                4.Touch shutter button to capture picture
                5.Exit activity
        '''
        randomoption = random.choice(Exposure) #Random select an option
        so.setCameraOption('Exposure',randomoption,modeNumber)
        tb.captureAndCheckPicCount('video',5)
