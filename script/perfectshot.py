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
#####################################
EXPOSURE_OPTION = ['-6','-3','0','3','6']
LOCATION_OPTION = ['off','on']
SCENCE_OPTION = ['auto', 'landscape', 'portrait', 'night', 'sports']

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
        sm.switchCaptureMode('Perfect Shot')
        time.sleep(1)


    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        #self._pressBack(4)
        #a.cmd('pm','com.intel.camera22')
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
        location = random.choice(LOCATION_OPTION)
        #Step 2
        so.setCameraOption('Geo Location',location)
        # Step 3
        tb.captureAndCheckPicCount('single')

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
        exposure = random.choice(EXPOSURE_OPTION)
        so.setCameraOption('Exposure',exposure)
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
        scence = random.choice(SCENCE_OPTION)
        print scence
        so.setCameraOption('Scenes',scence)
        tb.captureAndCheckPicCount('single',2)

########################################################3

    def _checkCapturedPic(self):
        beforeNo = a.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count before capturing
        tb.takePicture('single')
        time.sleep(2)
        afterNo = a.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count after taking picture
        if beforeNo == afterNo: #If the count does not raise up after capturing, case failed
            self.fail('Taking picture failed!')
    
    
    def _pressBack(self,touchtimes):
        for i in range(1,touchtimes+1):
            d.press('back')


if __name__ =='__main__':  
    unittest.main() 
