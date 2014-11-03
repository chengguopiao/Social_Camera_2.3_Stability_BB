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
Scenes            = ['auto', 'landscape', 'portrait', 'night', 'sports'] #_0_0
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
        sm.switchCaptureMode('Burst','Fast')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        self._pressBack(4)
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
        so.setCameraOption('Exposure',randomoption)
        tb.captureAndCheckPicCount('single',3)

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
        so.setCameraOption('Scenes',randomoption)
        tb.captureAndCheckPicCount('single',3)

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
        so.setCameraOption('Picture Size',randomoption)
        tb.captureAndCheckPicCount('single',3)

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
        so.setCameraOption('Geo Location',randomoption)
        tb.captureAndCheckPicCount('single',3)

    def _captureAndCheckPicCount(self,capturemode,delaytime=2):
        beforeNo = AD.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count before capturing
        TB.takePicture(capturemode)
        time.sleep(delaytime) #Sleep a few seconds for file saving
        afterNo = AD.cmd('ls','/sdcard/DCIM/100ANDRO') #Get count after taking picture
        if beforeNo != afterNo - 10: #If the count does not raise up after capturing, case failed
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
