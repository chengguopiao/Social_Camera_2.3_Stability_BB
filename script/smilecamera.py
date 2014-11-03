#!/usr/bin/env python
from uiautomatorplug.android import device as d
import time
import unittest
import commands
import util
import string
import random

a  = util.Adb()
sm = util.SetCaptureMode()
so = util.SetOption()
tb = util.TouchButton()

Exposure          = ['-6','-3','0','3','6'] #_0_0
ISO               = ['iso-auto','iso-100','iso-200','iso-400','iso-800'] #_0_0
White_Balance     = ['auto','incandescent','fluorescent','cloudy-daylight','daylight'] #_0_0
Switch_Camera     = ['1','0'] #_0
Face_Detection    = ['off','on'] #_0
Scenes            = ['auto','landscape','portrait','night','sports'] #_0_0 ,'night-portrait'
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
        sm.switchCaptureMode('Single','Smile')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        self._pressBack(4)

    # Testcase 4
    def testCaptureSmileImageWithExposure(self):
        """
        Summary:Capture image with Exposure mode.
        Step:
        1.Launch smile capture activity
        2.Set exposure mode
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Exposure)
        so.setCameraOption('Exposure',randomoption)
        tb.captureAndCheckPicCount('smile')

    # Testcase 9
    def testCaptureSmileImageWithScene(self):
        """
        Summary:Capture image with Scene mode.
        Step:
        1.Launch smile capture activity
        2.Set scene mode
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Scenes)
        so.setCameraOption('Scenes',randomoption)
        tb.captureAndCheckPicCount('smile')

    # Testcase 16
    def testCaptureSmileImageWithPictureSize(self):
        """
        Summary:Capture image with Photo size.
        Step:
        1.Launch smile capture activity
        2.Set photo size
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Picture_Size)
        so.setCameraOption('Picture Size',randomoption)
        tb.captureAndCheckPicCount('smile')

    # Testcase 18
    def testCaptureSmileImageWithLocation(self):
        """
        Summary:Capture image with Geo-tag.
        Step:
        1.Launch smile capture activity
        2.Set Ge0-tag
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Geo_Location)
        so.setCameraOption('Geo Location',randomoption)
        tb.captureAndCheckPicCount('smile')

    # Testcase 20
    def testCaptureSmileImageWithISO(self):
        """
        Summary:Capture image with ISO Setting.
        Step:
        1.Launch smile capture activity
        2.Set ISO Setting
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(ISO)
        so.setCameraOption('ISO',randomoption)
        tb.captureAndCheckPicCount('smile')

    # Testcase 25
    def testCaptureSmileImageWithWB(self):
        """
        Summary:Capture image with White Balance.
        Step:
        1.Launch smile capture activity
        2.Set White Balance
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(White_Balance)
        so.setCameraOption('White Balance',randomoption)
        tb.captureAndCheckPicCount('smile')

    def _pressBack(self,touchtimes):
        for i in range(1,touchtimes+1):
            d.press('back')

    def _confirmSettingMode(self,sub_mode,option):
        if sub_mode == 'location':
            result = a.cmd('cat','/data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep '+ sub_mode)
            if result.find(option) == -1:
                self.fail('set camera setting ' + sub_mode + ' to ' + option + ' failed')
        else:
            result = a.cmd('cat','/data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep ' + sub_mode)
            if result.find(option) == -1:
                self.fail('set camera setting ' + sub_mode + ' to ' + option + ' failed')

    def _capturePictureAndConfirm(self,timer=0):
        beforeC = a.cmd('ls','/sdcard/DCIM/100ANDRO')
        TB.takePicture('smile')
        time.sleep(timer)       
        afterC  = a.cmd('ls','/sdcard/DCIM/100ANDRO')
        if afterC == beforeC:
            self.fail('take picture failed !!')
