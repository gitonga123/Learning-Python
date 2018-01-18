def switchLights(spotLight):
	for key in stoplight.keys():
		if spotLight[key] =='green':
			stoplight[key]='yellow'
		elif stoplight[key]='yello':
			stoplight[key]='red'
		elif stoplight[key]='red':
			stoplight[key]='green'
	assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)