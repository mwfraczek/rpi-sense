#!/usr/bin/env python

from sense_hat import SenseHat
from influxdb import InfluxDBClient
import datetime
import argparse

sense = SenseHat()

host = "localhost"
port = 8086
user = "grafana"
password = "polska32"
db = "home"

t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

time = datetime.datetime.utcnow()

parser = argparse.ArgumentParser(description='Program writes measurements data from SenseHat to influx')
parser.add_argument(

data = [
	       {
		"measurement": session,
		"time": time,
		"fields":
			{
			"temperaturevalue": t,
			"pressurevalue": p,
			"humidityvalue": h,
			}
		}
		]

ifclient = InfluxDBClient(host,port,user,password,db)
ifclient.write_points(data)
