import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

from selenium import webdriver
driver = webdriver.Chrome(executable_path='E:\谷歌\chromedriver_win32\chromedriver.exe')  # 创建一个 Chrome WebDriver 实例
driver.get('https://www.baidu.com/')  # 打开网址
