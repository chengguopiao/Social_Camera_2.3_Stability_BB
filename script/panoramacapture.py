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

a  = util.Adb()
sm = util.SetCaptureMode()
so = util.SetOption()
tb = util.TouchButton()
#Written by Piao chengguo
#################################################
EXPOSURE_OPTION=['-6','-3','0','3','6']
LOCATION_OPTION =['off','on']
IOS_OPTION = ['iso-800', 'iso-400','iso-200','iso-100','iso-auto']

#################################

PACKAGE_NAME = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '/.Camera'

class CameraTest(unittest.TestCase):

    def setUp(self):
        super(CameraTest,self).setUp()
        # rm DCIM folder and refresh from adb shell
        #a.cmd('rm','/sdcard/DCIM/100ANDRO')
        #a.cmd('refresh','/sdcard/DCIM/100ANDRO')
        #Because default camera after launching is single mode, so we set this step in setUp().
        #Step 1. Launch single capture activity
        #a.cmd('launch','com.intel.camera22/.Camera')
        #time.sleep(2)
        #if d(text = 'Yes').wait.exists(timeout = 3000):
        #    d(text = 'Yes').click.wait()
        #if d(text = 'Skip').wait.exists(timeout = 3000):
        #    d(text = 'Skip').click.wait()
        #assert d(resourceId = 'com.intel.camera22:id/shutter_button'),'Launch camera failed!!'
        a.setUpDevice()
        sm.switchCaptureMode('Panorama')
        time.sleep(1)

    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        #self._pressBack(4)
        #a.cmd('pm','com.intel.camera22')
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
        #exposure = random.choice( ['3', '6', '0','-3','-6'] )
        exposure = random.choice(EXPOSURE_OPTION)
        so.setCameraOption('Exposure',exposure)
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
        location = random.choice(LOCATION_OPTION)
        so.setCameraOption('Geo Location',location)
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
        iso = random.choice(IOS_OPTION)
        so.setCameraOption('ISO',iso)
        # Step 3
        tb.captureAndCheckPicCount('smile')

######################################
    def _pressBack(self,touchtimes):
        for i in range(1,touchtimes+1):
            d.press('back')


if __name__ =='__main__':  
    unittest.main() 
