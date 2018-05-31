import numpy as np
import urllib.request
import pandas as pd
from  pandas  import  Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
url1 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170101&stockNo=2330'
url2 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170201&stockNo=2330'
url3 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170301&stockNo=2330'
url4 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170401&stockNo=2330'
url5 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170501&stockNo=2330'
url6 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170601&stockNo=2330'
url7 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170701&stockNo=2330'
url8 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170801&stockNo=2330'
url9 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20170901&stockNo=2330'
url10 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20171001&stockNo=2330'
url11 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20171101&stockNo=2330'
url12 = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=20171201&stockNo=2330'
DataFrame1 = pd.read_html(url1)[0]
DataFrame2 = pd.read_html(url2)[0]
DataFrame3 = pd.read_html(url3)[0]
DataFrame4 = pd.read_html(url4)[0]
DataFrame5 = pd.read_html(url5)[0]
DataFrame6 = pd.read_html(url6)[0]
DataFrame7 = pd.read_html(url7)[0]
DataFrame8 = pd.read_html(url8)[0]
DataFrame9 = pd.read_html(url9)[0]
DataFrame10 = pd.read_html(url10)[0]
DataFrame11 = pd.read_html(url11)[0]
DataFrame12 = pd.read_html(url12)[0]
DataFrame1_1 = DataFrame1.drop(DataFrame1.columns[[0]],axis=1)
DataFrame2_1 = DataFrame2.drop(DataFrame2.columns[[0]],axis=1)
DataFrame3_1 = DataFrame3.drop(DataFrame3.columns[[0]],axis=1)
DataFrame4_1 = DataFrame4.drop(DataFrame4.columns[[0]],axis=1)
DataFrame5_1 = DataFrame5.drop(DataFrame5.columns[[0]],axis=1)
DataFrame6_1 = DataFrame6.drop(DataFrame6.columns[[0]],axis=1)
DataFrame7_1 = DataFrame7.drop(DataFrame7.columns[[0]],axis=1)
DataFrame8_1 = DataFrame8.drop(DataFrame8.columns[[0]],axis=1)
DataFrame9_1 = DataFrame9.drop(DataFrame9.columns[[0]],axis=1)
DataFrame10_1 = DataFrame10.drop(DataFrame10.columns[[0]],axis=1)
DataFrame11_1 = DataFrame11.drop(DataFrame11.columns[[0]],axis=1)
DataFrame12_1 = DataFrame12.drop(DataFrame12.columns[[0]],axis=1)
#plt.subplot(6,2,1)
#plt.plot(DataFrame1_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,2)
#plt.plot(DataFrame2_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,3)
#plt.plot(DataFrame3_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,4)
#plt.plot(DataFrame4_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,5)
#plt.plot(DataFrame5_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,6)
#plt.plot(DataFrame6_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,7)
#plt.plot(DataFrame7_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,8)
#plt.plot(DataFrame8_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,9)
#plt.plot(DataFrame9_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,10)
#plt.plot(DataFrame10_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,11)
#plt.plot(DataFrame11_1,lw=3)
#plt.yticks(range(170,270,20))
#plt.subplot(6,2,12)
#plt.plot(DataFrame12_1,lw=3)
DoubleDataFrame1 = pd.concat([DataFrame1_1, DataFrame2_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame3_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame4_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame5_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame6_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame7_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame8_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame9_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame10_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame11_1], axis=0, ignore_index=True)
DoubleDataFrame1 = pd.concat([DoubleDataFrame1, DataFrame12_1], axis=0, ignore_index=True)
plt.plot(DoubleDataFrame1,lw=2)
plt.yticks(range(170,270,20))
plt.show()


DoubleDataFrame1