from lib import *

def test_tvOn():
    tv = Television(True, 1, 1, False)
    tv.tvOnOff()
    assert tv.on == False
    tv.tvOnOff()
    assert tv.on == True

def test_chUpDownGet():
    tv = Television(True, 1, 1, False)
    assert tv.getCh() == 1
    tv.chUp()
    assert tv.getCh() == 2
    tv.chDown()
    assert tv.getCh() == 1

def test_volDownUpGet():
    tv = Television(True, 1, 1, False)
    assert tv.getVol() == 1
    tv.volUp()
    assert tv.getVol() == 2
    tv.volDown()
    assert tv.getVol() == 1

def test_mute():
    tv = Television(True, 1, 1, False)
    assert tv.getMuted() == False
    tv.mute()
    assert tv.getMuted() == True