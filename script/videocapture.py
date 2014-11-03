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

AD = util.Adb()
tb = util.TouchButton()
so = util.SetOption()
sm = util.SetCaptureMode()

#Written by XuGuanjun

PACKAGE_NAME  = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '/.Camera'

Exposure          = ['-6','-3','0','3','6'] #_0_0
ISO               = ['iso-auto','iso-100','iso-200','iso-400','iso-800'] #_0_0
White_Balance     = ['auto','incandescent','fluorescent','cloudy-daylight','daylight'] #_0_0
Switch_Camera     = ['1','0'] #_0
Face_Detection    = ['off','on'] #_0
Scenes            = ['auto','landscape','portrait','night','sports','night-portrait'] #_0_0
Self_Timer        = ['0','3','5','10'] #_0_0
Geo_Location      = ['off','on'] #_0
Picture_Size      = ['WideScreen','StandardScreen'] #_0_0
Hints             = ['off','on'] #_0_0
Video_Size        = [['false','4'],['false','5'],['true','5'],['false','6'],['true','6']] #_0_0
Settings_Layout   = ['Mini','Large'] #_0
Shortcut_Button_1 = ['exposure','iso','whitebalance','flashmode','id','fdfr','scenemode','delay','geo'] #_0
Shortcut_Button_2 = ['exposure','iso','whitebalance','flashmode','id','fdfr','scenemode','delay','geo'] #_0
Shortcut_Button_3 = ['exposure','iso','whitebalance','flashmode','id','fdfr','scenemode','delay','geo'] #_0

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        #self._launchCamera()
        #time.sleep(2)
        #if d(text = 'Yes').wait.exists(timeout = 3000):
        #    d(text = 'Yes').click.wait()
        #if d(text = 'Skip').wait.exists(timeout = 3000):
        #    d(text = 'Skip').click.wait()
        AD.setUpDevice(False)
        sm.switchCaptureMode('Video')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        self._pressBack(4)
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
        so.setCameraOption('Video Size',randomoption)
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
        so.setCameraOption('Geo Location',randomoption)
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
        so.setCameraOption('White Balance',randomoption)
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
        so.setCameraOption('Exposure',randomoption)
        tb.captureAndCheckPicCount('video',5)

    def _takeVideoAndCheckCount(self,recordtime=30,delaytime=2,capturetimes=0):
        beforeNo = AD.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count before capturing
        TB.takeVideo(recordtime,capturetimes)
        time.sleep(delaytime) #Sleep a few seconds for file saving
        afterNo = AD.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count after taking picture
        if beforeNo != afterNo - capturetimes - 1: #If the count does not raise up after capturing, case failed
            self.fail('Taking picture failed!')

    def _launchCamera(self):
        d.start_activity(component = ACTIVITY_NAME)
        time.sleep(2)
        #When it is the first time to launch camera there will be a dialog to ask user 'remember location', so need to check
        if d(text = 'OK').wait.exists(timeout = 2000):
            d(text = 'OK').click.wait()
        #assert d(resourceId = 'com.intel.camera22:id/shutter_button').wait.exists(timeout = 3000), 'Launch camera failed in 3s'

    def _pressBack(self,touchtimes):
        for i in range(0,touchtimes):
            d.press('back')
