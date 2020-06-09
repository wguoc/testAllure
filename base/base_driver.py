from appium import webdriver


def init_driver():
    desired_caps = {}
    #设置参数 - 平台
    desired_caps['platformName'] = 'android'
    #平台版本
    desired_caps['paltformVersion'] = '6.0'
    #设备IP和端口
    desired_caps['deviceName'] = "192.168.67.101:5555"
    #要打开的应用包名和页面
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    #中文键盘
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    #远程连接
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
