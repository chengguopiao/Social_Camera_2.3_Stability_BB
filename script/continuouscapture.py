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

#Written by ZhuYanbo

a              = util.Adb()
sm             = util.SetCaptureMode()
so             = util.SetOption()
tb             = util.TouchButton()
Exposure       = util.Exposure
Geo_Location   = util.Geo_Location
ISO            = util.ISO
Picture_Size   = util.Picture_Size
Hints          = util.Hints
White_Balance  = util.White_Balance
Scenes         = util.Scenes
Face_Detection = util.Face_Detection

class CameraTest(unittest.TestCase):
    
    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Single')    

    def tearDown(self):
        super(CameraTest,self).tearDown()
        a.tearDownDevice()

    # # Test case 1
    # def testCapturePictureWithFlash(self):
    #     """
    #     Summary:testCapturePictureWithFlashOn: Take a picture with flash on
    #     Steps:  1.Launch single capture activity
    #             2.Set flash ON
    #             3.Touch shutter button to capture picture
    #             4.Exit  activity
    #     """
    #     flash = random.choice(FLASH_OPTION)
    #     sm.setCameraSetting('single','flash',flash)
    #     assert bool(a.cmd('cat',PATH + FLASH_STATE).find(flash)+1)
    #     # Step 3
    #     self._continuouCapturePic()


    # Test case 2
    def testCaptureWithExposure(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take a picture with Exposure +1
        Steps: 1.Launch single capture activity
               2.Set exposure +1
               3.Touch shutter button to capture picture
               4.Exit  activity
        """       
        # Step 2
        exposure = random.choice(Exposure)
        so.setCameraOption('Exposure',exposure)
        # Step 3
        tb.captureAndCheckPicCount('longclick')


    # Test case 3
    def testCapturePictureWithScenes(self):
        """
        Summary:testCapturePictureWithScenesSport: Take a picture with set scenes to Sports
        Steps:  1.Launch single capture activity
                2.Set scene mode Sports
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # Step 2
        scenes = random.choice(Scenes)
        so.setCameraOption('Scenes',scenes)
        # Step 3
        tb.captureAndCheckPicCount('longclick')


    # Test case 4
    def testCapturePictureWithFD(self):
        """
        Summary:testCapturePictureWithFDON: Take a picture with set FD/FR on
        Steps:  1.Launch single capture activity
                2.Set FD/FR ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        fdfr =random.choice(Face_Detection)
        # Step 2
        so.setCameraOption('Face Detection',fdfr)
        # Step 3
        tb.captureAndCheckPicCount('longclick')


    # Test case 5
    def testCapturePictureWithPictureSize(self):
        """
        Summary:testCapturePictureWithPictureSizeStandard: Take a picture with picture size is standard
        Steps:  1.Launch single capture activity
                2.Set picture size is standard
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        picturesize = random.choice(Picture_Size)
        # Step 2
        so.setCameraOption('Picture Size',picturesize)
        # Step 3
        tb.captureAndCheckPicCount('longclick')


    # Test case 6
    def testCapturepictureWithGeoLocation(self):
        """
        Summary:testCapturepictureWithGeoLocationOn:Take a picture with  geolocation is on
        Steps:  1.Launch camera app
                2.Set geo location on 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        location = random.choice(Geo_Location)
        # Step 2
        so.setCameraOption('Geo Location',location)
        # Step 3
        tb.captureAndCheckPicCount('longclick')

    # Test case 7
    def testCapturepictureWithHints(self):
        """
        Summary:testCapturepictureWithHintsOn: Take a picture with  hints is on
        Steps:  1.Launch camera app
                2.Set hints on
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        hints = random.choice(Hints)
        # Step 2
        so.setCameraOption('Hints',hints)
        # Step 3
        tb.captureAndCheckPicCount('longclick')


    # Test case 8
    def testRearFaceCapturePictureWithFD(self):
        """
        Summary:testRearFaceCapturePictureWithFDON: Take a picture using fear face camera and set FD/FR on
        Steps:  1.Launch single capture activity
                2.Set FD/FR ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        tb.switchBackOrFrontCamera('front')
        fdfr =random.choice(Face_Detection)
        # Step 2
        so.setCameraOption('Face Detection',fdfr)
        # Step 3
        tb.captureAndCheckPicCount('longclick')
        tb.switchBackOrFrontCamera('back')


    # Test case 9
    def testRearFaceCapturepictureWithGeoLocation(self):
        """
        Summary:testRearFaceCapturepictureWithGeoLocationOn: Take a picture using fear face camera and set geolocation on 
        Steps:  1.Launch camera app
                2.Set geolocation on 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        tb.switchBackOrFrontCamera('front')
        location =random.choice(Geo_Location)
        # Step 2
        so.setCameraOption('Geo Location',location)
        # Step 3
        tb.captureAndCheckPicCount('longclick')
        tb.switchBackOrFrontCamera('back')

    # Test case 10
    #def testCapturepictureWithSelfTimer(self):
        """
        Summary:testCapturepictureWithSelfTimerOff: Capture image with Self-timer off
        Steps:  1.Launch single capture activity
                2.Set Self-timer off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # Step 2
     #   selftimer = random.choice(SELFTIMER_OPTION)
      #  sm.setCameraSetting('single',9,SELFTIMER_OPTION.index(selftimer)+1)
       # assert bool(a.cmd('cat',PATH + TIMER_KEY).find(selftimer)+1)
        #self._continuouCapturePic()

    # Test case 11
    def testCapturepictureWithISO(self):
        """
        Summary:testCapturepictureWithISOAuto: Capture image with ISO Setting Auto
        Steps:  1.Launch single capture activity
                2.Set ISO Setting Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        iso = random.choice(ISO)
        # Step 2
        so.setCameraOption('ISO',iso)
        # Step 3
        tb.captureAndCheckPicCount('longclick')


    # Test case 12
    def testCapturepictureWithWhiteBalance(self):
        """
        Summary:testCapturepictureWithWhiteBalanceAuto: Capture image with White Balance Auto
        Steps:  1.Launch single capture activity
                2.Set White Balance Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        # Step 2
        whitebalance = random.choice(White_Balance)
        # Step 2
        so.setCameraOption('White Balance',whitebalance)
        # Step 3
        tb.captureAndCheckPicCount('longclick')
