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

a  = util.Adb()
sm = util.SetCaptureMode()
so = util.SetOption()
tb = util.TouchButton()

#Written by XuGuanjun

PACKAGE_NAME  = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '/.Camera'

#All setting info of camera could be cat in the folder
PATH_PREF_XML  = '/data/data/com.intel.camera22/shared_prefs/'

#FDFR / GEO / BACK&FROUNT xml file in com.intelcamera22_preferences_0.xml
PATH_0XML      = PATH_PREF_XML + 'com.intel.camera22_preferences_0.xml'

#PICSIZE / EXPROSURE / TIMER / WHITEBALANCE / ISO / HITS / VIDEOSIZE in com.intel.camera22_preferences_0_0.xml
PATH_0_0XML    = PATH_PREF_XML + 'com.intel.camera22_preferences_0_0.xml'

#####                                    #####
#### Below is the specific settings' info ####
###                                        ###
##                                          ##
#                                            #
#Exposure options
EXPOSURE_OPTION = ['-6','-3','0','3','6']

#Scene options
SCENE_OPTION    = ['barcode','night-portrait','portrait','landscape','night','sports','auto']

#Picture size options
PICSIZE_OPTION  = ['WideScreen','StandardScreen']

#Geo options
GEO_OPTION      = ['off','on']

#Flash options
FLASH_OPTION    = ['off','on']

#Video size options
VSIZE_OPTION    = ['4','5','5','6','6']

#White balance options
WBALANCE_OPTION = ['cloudy','fluorescent','daylight','incandescent','auto']

#FD/FR options
FDFR_OPTION     = ['on','off']

#Self timer options
TIMER_OPTION    = ['0','3','5','10']

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        #Delete all image/video files captured before
        #a.cmd('rm','/sdcard/DCIM/*')
        #Refresh media after delete files
        #a.cmd('refresh','/sdcard/DCIM/*')
        #Launch social camera
        #self._launchCamera()
        a.setUpDevice()
        sm.switchCaptureMode('Single','HDR')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        self._pressBack(4)

    def testCapturePictureWithFD(self):
        '''
            Summary: Capture image with FD/FR
            Steps  : 
                1.Launch HDR capture activity
                2.Set FD/FR ON/OFF
                3.Touch shutter button to capture picture
                4.Exit activity
        '''
        fdfr = random.choice(FDFR_OPTION)
        # Step 2
        so.setCameraOption('Face Detection',fdfr)
        # Step 3
        tb.captureAndCheckPicCount('single')

    def testCapturepictureWithGeoLocation(self):
        '''
            Summary: Capture image with Geo-tag
            Steps  : 
                1.Launch HDR capture activity
                2.Set photo Geo-tag ON/OFF
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        geo = random.choice(GEO_OPTION)
        # Step 2
        so.setCameraOption('Geo Location',geo)
        # Step 3
        tb.captureAndCheckPicCount('single')

    def testCapturePictureWithPictureSize(self):
        '''
            Summary: Capture image with Photo size
            Steps  : 
                1.Launch HDR capture activity
                2.Set photo size 6MP/13MP
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        size = random.choice(PICSIZE_OPTION)
        # Step 2
        so.setCameraOption('Picture Size',size)
        # Step 3
        tb.captureAndCheckPicCount('single')
        so.setCameraOption('Picture Size','WideScreen') #Force set to the default setting

    def testCapturePictureWithSelfTimer(self):
        '''
        Summary: Capture image with Self-timer
        Steps  :  1.Launch HDR capture activity
                2.Set Self-timer setting
                3.Touch shutter button to capture picture
                4.Exit  activity
        '''
        timer = random.choice(TIMER_OPTION)
        # Step 2
        so.setCameraOption('Self Timer',timer)
        # Step 3
        tb.captureAndCheckPicCount('smile')
        so.setCameraOption('Self Timer','0') #Force set timer to off

    def _launchCamera(self):
        d.start_activity(component = ACTIVITY_NAME)
        #When it is the first time to launch camera there will be a dialog to ask user 'remember location', so need to check
        try:
            if d(text = 'Yes').wait.exists(timeout = 3000):
                d(text = 'Yes').click.wait() 
            assert d(text = 'Skip').wait.exists(timeout = 2000)
            d(text = 'Skip').click.wait()
        except:
            pass
        assert d(resourceId = 'com.intel.camera22:id/mode_button').wait.exists(timeout = 3000), 'Launch camera failed in 3s'

    def _pressBack(self,touchtimes):
        for i in range(0,touchtimes):
            d.press('back')
