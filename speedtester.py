import speedtest
from datetime import datetime
import json


def test():
	print('started test')

	speedtester = speedtest.Speedtest()
	print('established speedtester')

	speedtester.get_best_server()
	print('found server')

	toJson = speedtester.download()
	print('downloaded file')

	toJson /= 1000000
	print('converted speed')

	print(toJson)
	return(toJson)

def update(day,time):
	speed = test()
	with open('speed_now.txt','w') as f:
		f.write('at {0}:{1} the speed was {2} MBPS'.format(time[0],time[1],speed))
	f.close()
	print('wrote to now')

	d = open(str(day) + '.json','r+')
	dj = json.load(d)

	if dj.get('{0}:{1}'.format(time[0],time[1])) == None:
		dj['{0}:{1}'.format(time[0],time[1])] = {'avespeed': 0,'number of values': 0,'last speed': 0}

	numVals = dj['{0}:{1}'.format(time[0],time[1])]['number of values']

	avespeed = (speed + (dj['{0}:{1}'.format(time[0],time[1])]['avespeed']*numVals))/(numVals + 1)

	numVals += 1

	dj['{0}:{1}'.format(time[0],time[1])] = {'avespeed': avespeed,'number of values': numVals,'last speed': speed}


	d.seek(0)
	json.dump(dj,d)
	d.truncate()


while 1 == 1: 
	time = str(datetime.now().time())
	day = datetime.today().weekday()

	time = time.split(':')

	print(time)

	time[0] = int(time[0])
	time[1] = int(time[1])
	time[2] = float(time[2])



	#Check time
	if time[0] >= 8:
		if time[0] < 16:
			if day <= 5:
				if time[1] % 5 == 0:
					if time[2] < 1:
						update(day,time)
					else:
						print('not sec 1')
				else:
					print('not min 5')
			else:
				print('weekend')
		else:
			print('too late')
	else:
		print('too early')







