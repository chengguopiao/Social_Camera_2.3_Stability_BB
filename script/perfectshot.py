#!/usr/bin/python
# coding:utf-8

from uiautomatorplug.android import device as d
import commands
import re
import subprocess
import os
import string
import time
import sys
import util 
import unittest
import random

a            = util.Adb()
sm           = util.SetCaptureMode()
so           = util.SetOption()
tb           = util.TouchButton()
Scenes       = util.Scenes
Exposure     = util.Exposure
Geo_Location = util.Geo_Location
modeNumber   = util.ModeNumber['perfectshot']

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Perfect Shot')
        time.sleep(1)


    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        a.tearDownDevice()

# Test case 1
    def testCapturepictureWithGeoLocation(self):
        """
        Summary:testCapturepictureWithGeoLocationOn: capture PerfectShot picture in geolocation on mode
        Steps:  1.Launch perfect shot activity
                2.Check geo-tag ,set to ON
                3.Touch shutter button to capture picture
                4.Exit activity
        """ 
        location = random.choice(Geo_Location)
        #Step 2
        so.setCameraOption('Geo Location',location,modeNumber)
        # Step 3
        tb.captureAndCheckPicCount('single',2)

# Test case 2
    def testCaptureWithExposure(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take burst piture with exposure +1
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to +1
                3.Touch shutter button to capture picture
                4.Exit  activity
        """          
        #Step 2
        exposure = random.choice(Exposure)
        so.setCameraOption('Exposure',exposure,modeNumber)
        tb.captureAndCheckPicCount('single',2)
        
# Test case 3
    def testCapturePictureWithScenes(self):
        """
        Summary:testCapturePictureWithScenesSport: Take picture with set scenes to Sports
        Steps:  1Launch perfect shot activity
                2.Check scence mode ,set mode to Sports
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # Step 2
        scence = random.choice(Scenes)
        #print scence
        so.setCameraOption('Scenes',scence,modeNumber)
        tb.captureAndCheckPicCount('single',2)
