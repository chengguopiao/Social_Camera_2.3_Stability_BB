#!/usr/bin/env python
from uiautomatorplug.android import device as d
import time
import unittest
import commands
import util
import string
import random

a              = util.Adb()
sm             = util.SetCaptureMode()
so             = util.SetOption()
tb             = util.TouchButton()
Exposure       = util.Exposure
ISO            = util.ISO
White_Balance  = util.White_Balance
Switch_Camera  = ['1','0'] #_0
Face_Detection = util.Face_Detection
Scenes         = util.Scenes
Self_Timer     = util.Self_Timer
Geo_Location   = util.Geo_Location
Picture_Size   = util.Picture_Size
Hints          = util.Hints

class CameraTest(unittest.TestCase):

    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Single')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        tb.switchBackOrFrontCamera('back')
        a.pressBackKey(4)

    # Testcase 2
    def testCaptureSingleImageWithExposure(self):
        """
        Summary:Capture image with Exposure mode.
        Step:
        1.Launch single capture activity
        2.Set exposure mode
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Exposure)
        so.setCameraOption('Exposure',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 3
    def testCaptureSingleImageWithScene(self):
        """
        Summary:Capture image with Scene mode.
        Step:
        1.Launch single capture activity
        2.Set scene mode
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Scenes)
        so.setCameraOption('Scenes',randomoption)
        tb.captureAndCheckPicCount('single')
        so.setCameraOption('Scenes','auto') #Force set scenes to auto

    # Testcase 4
    def testCaptureSingleImageWithFDFR(self):
        """
        Summary:Capture image with FD/FR.
        Step:
        1.Launch single capture activity
        2.Set FD/FR ON
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Face_Detection)
        so.setCameraOption('Face Detection',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 5
    def testCaptureSingleImageWithPictureSize(self):
        """
        Summary:Capture image with Photo size.
        Step:
        1.Launch single capture activity
        2.Set photo size
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Picture_Size)
        so.setCameraOption('Picture Size',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 6
    def testCaptureSingleImageWithHits(self):
        """
        Summary:Capture image with Hints.
        Step:
        1.Launch single capture activity
        2.Set Hints
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Hints)
        so.setCameraOption('Hints',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 7
    def testCaptureSingleImageWithSelfTimer(self):
        """
        Summary:Capture image with Self-timer.
        Step:
        1.Launch single capture activity
        2.Set Self-timer
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Self_Timer)
        so.setCameraOption('Self Timer',randomoption)
        tb.captureAndCheckPicCount('single',int(randomoption))
        so.setCameraOption('Self Timer','0') #Force set timer to off

    # Testcase 8
    def testCaptureSingleImageWithISO(self):
        """
        Summary:Capture image with ISO Setting.
        Step:
        1.Launch single capture activity
        2.Set ISO Setting
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(ISO)
        so.setCameraOption('ISO',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 9
    def testCaptureSingleImageWithWB(self):
        """
        Summary:Capture image with White Balance.
        Step:
        1.Launch single capture activity
        2.Set White Balance
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(White_Balance)
        so.setCameraOption('White Balance',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 10
    def testCapturepictureWithLocation(self):
        """
        Summary:Capture image with Location.
        Step:
        1.Launch single capture activity
        2.Set Geo location
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Geo_Location)
        so.setCameraOption('Geo Location',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 11
    def testFrontFaceCapturePictureWithFD(self):
        """
        Summary:Capture image with FD/FR on front camera.
        Step:
        1.Launch single capture activity
        2.Switch to front camera
        3.Set FD/FR
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        so.setCameraOption('Switch Camera','1')
        randomoption = random.choice(Face_Detection)
        so.setCameraOption('Face Detection',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 12
    def testFrontFaceCapturepictureWithLocation(self):
        """
        Summary:Capture image with location front camera.
        Step:
        1.Launch single capture activity
        2.Switch to front camera
        3.Set Geo location
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        so.setCameraOption('Switch Camera','1')
        randomoption = random.choice(Geo_Location)
        so.setCameraOption('Geo Location',randomoption)
        tb.captureAndCheckPicCount('single')
