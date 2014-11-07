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
modeNumber   = util.ModeNumber['panorama']
Exposure     = util.Exposure
Geo_Location = util.Geo_Location
ISO          = util.ISO

class CameraTest(unittest.TestCase):

    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Panorama')
        time.sleep(1)

    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.tearDownDevice()

# Test case 1
    def testCaptureWithExposure(self):
        """
        Summary:testCaptureWithExposurePlusOne:capture Panorama picture with Exposure +1
        Steps  : 1.Launch Panorama activity
                 2.Touch Exposure Setting icon, set Exposure +1
                 3.Touch shutter button to capture picture
                 4.Exit  activity 
        """
        #step 2
        exposure = random.choice(Exposure)
        so.setCameraOption('Exposure',exposure,modeNumber)
        # Step 3
        tb.captureAndCheckPicCount('smile')

# Test case 2
    def testCapturepictureWithGeoLocation(self):
        """
        Summary:testCapturepictureWithGeoLocationOff: capture Panorama picture in geolocation off mode
        Steps:  1.Launch Panorama activity
                2.Check geo-tag ,set to Off
                3.Touch shutter button to capture picture
                4.Exit activity
        """   
        #Step 2
        location = random.choice(Geo_Location)
        so.setCameraOption('Geo Location',location,modeNumber)
        # Step 3
        tb.captureAndCheckPicCount('smile')

# Test case 3
    def testCapturepictureWithISOSetting(self):
        """
        Summary:testCapturepictureWithISOSettingAuto: Capture image with ISO Setting Auto
        Steps:  1.Launch Panorama activity
                2.Touch Geo-tag setting  icon,Set Geo-tag OFF
                3.Touch shutter button
                4.Touch shutter button to capture picture
        5.Exit  activity 
        """

        #Step 2
        iso = random.choice(ISO)
        so.setCameraOption('ISO',iso,modeNumber)
        # Step 3
        tb.captureAndCheckPicCount('smile')