# coding=utf-8
import requests
import os
from config import *

header = {
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en,zh-CN;q=0.8,zh;q=0.6,zh-TW;q=0.4',
	'Connection':'keep-alive',
	'Content-Length':'32',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie':cookie,
	'Host':'m.01zhuanche.com',
	'Origin':'http://m.01zhuanche.com',
	'Referer':'http://m.01zhuanche.com/touch/h5Home/wxpub/n_jishi',
	#'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
	'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
	'X-Requested-With':'XMLHttpRequest'
}

book_data = {
	'bookingDate':curr_time,
	'bookingStartPointLo':StartPointLo,
	'bookingStartPointLa':StartPointLa,
	'bookingEndPointLo':EndPointLo,
	'bookingEndPointLa':EndPointLa,
	'bookingStartAddr':StartAddr,
	'bookingEndAddr':EndAddr,
	'groupIds':'34',
	'estimatedAmount':'53',
	'channel':'wxpub'
}

for i in range(1, 200):
	try:
		r = requests.post('http://m.01zhuanche.com/touch/order/bookingCar', headers=header, data=book_data).json()
	except:
		print ('cookie过期，请重新获取')
		break
	#print r['errmsg']
	print ( r )
	if r['data']['returnCode'] == '0':
		print ('Order success! pooling...')
		print ('Order time:')
		print (time.localtime(float(curr_time)) )

	cancel_data={
		'orderNo':r['data']['orderNo'],
		'orderId':r['data']['orderId'],
		'cancelType':'11'
	}

	pool_data = {
		'orderNo':r['data']['orderNo'],
		'channel':'wxpub'
	}

	for j in range(1, 41):
		r = requests.post('http://m.01zhuanche.com/touch/order/pollingOrder', headers=header, data=pool_data).json()
		print (r)
		if r['data']['returnCode'] == '0':
			print ('success')
			car_number = r['data']['order']['licensePlates']
			driver_phone = r['data']['order']['phone']
			driver_name = r['data']['order']['driverName']
			color = r['data']['order']['color']
			print (car_number)
			print (driver_phone)
			print (driver_name)
			print (color)
			os._exit(0)
		print (j, 'no car, pooling...')
		time.sleep(5)
	requests.post('http://m.01zhuanche.com/touch/order/cancelOrderBeforeAccepted', headers=header, data=cancel_data).json()

