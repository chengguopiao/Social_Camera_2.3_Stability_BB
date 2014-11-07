#!/usr/bin/env python
from uiautomatorplug.android import device as d
import time
import unittest
import commands
import util
import string
import random

#Written by ZhuYanbo

a             = util.Adb()
sm            = util.SetCaptureMode()
so            = util.SetOption()
tb            = util.TouchButton()
modeNumber    = util.ModeNumber['smile']
Exposure      = util.Exposure
ISO           = util.ISO
White_Balance = util.White_Balance
Scenes        = util.Scenes
Geo_Location  = util.Geo_Location
Picture_Size  = util.Picture_Size

class CameraTest(unittest.TestCase):

    def setUp(self):
        super(CameraTest,self).setUp()
        a.setUpDevice()
        sm.switchCaptureMode('Single','Smile')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        a.pressBackKey(4)

    # Testcase 1
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
        so.setCameraOption('Exposure',randomoption,modeNumber)
        tb.captureAndCheckPicCount('smile')

    # Testcase 2
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
        so.setCameraOption('Scenes',randomoption,modeNumber)
        tb.captureAndCheckPicCount('smile')
        so.setCameraOption('Scenes','auto',modeNumber) #Force set scenes to auto
        time.sleep(2)

    # Testcase 3
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
        so.setCameraOption('Picture Size',randomoption,modeNumber)
        tb.captureAndCheckPicCount('smile')

    # Testcase 4
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
        so.setCameraOption('Geo Location',randomoption,modeNumber)
        tb.captureAndCheckPicCount('smile')

    # Testcase 5
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
        so.setCameraOption('ISO',randomoption,modeNumber)
        tb.captureAndCheckPicCount('smile')

    # Testcase 6
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
        so.setCameraOption('White Balance',randomoption,modeNumber)
        tb.captureAndCheckPicCount('smile')
