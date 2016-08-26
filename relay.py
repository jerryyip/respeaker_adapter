# -*- coding: utf-8 -*- 
import re
import json
import requests
from player import Player
import time
#import monotonic
#import Queue
#import threading

#ACCESS_TOKEN = "c79dfaf4d5f720b925e2b262220d99fd"

class Relay(object):
	def __init__(self, ACCESS_TOKEN):
		self.text = ""
		self.ACCESS_TOKEN = ACCESS_TOKEN
		self.onoff = 0
		
    	def set_tts(self, tts):
        	self.tts = tts
		
    	def set_player(self, ply):
        	self.player = ply
		
	def play_text(self, text):
		try:
			self.player.play_buffer(self.tts.speak(text))
		except Exception as e:
			print e	
				
	def run(self, ):
		if re.search(r'turn on', self.text) or re.search(r'open', self.text):
			self.play_text("Relay turn on now")
			self.onoff = 1
			self._post_relay_onoff()
		elif re.search(r'turn off', self.text) or re.search(r'close', self.text):
			self.play_text("Relay turn off now")
			self.onoff = 0
			self._post_relay_onoff()
		elif re.search(r'status',self.text):
			resp = 'the relay is %s now' % (self._URL_RELAY_STATUS())
			self.play_text(resp)
		elif re.search(r'thank you', self.text):
            		self.play_text("you're welcome!")
	        elif re.search(r'how(\'re)?.*(are)?.*you', self.text):
        		self.play_text("good, thank you.")
	        elif re.search(r'bye bye', self.text):
			self.play_text("bye!")
	        elif re.search(r'shut.*down', self.text):
			self.play_text("see you next time")
        	else:
		        print 'unknown command, ignore.'
      			self.play_text("I don't know your command.")
			
	def _get_relay_status(self, ):
		_URL_RELAY_STATUS = "https://cn.wio.seeed.io/v1/node/GroveRelayD0/onoff_status?access_token=%s" % (self.ACCESS_TOKEN)
		time_out = 0
		result = requests.get(_URL_RELAY_STATUS)
		while result.status_code != 200:	#if response error try again 5 times
			time_out = time_out + 1
			time.sleep(1)
			result = requests.get(_URL_RELAY_STATUS)
			if (time_out >= 5):
				print ("can't get relay status")
				return "ERROR"
		print ("get relay status success")
		status_text = result.json()
		if (status_text["onoff"] == 0):
			return "OFF"
		elif (status_text["onoff"] == 1):
			return "ON"
		else:
			return "UNKNOWN"
		
	def _post_relay_onoff(self, ):
		_URL_RELAY_ONOFF = "https://cn.wio.seeed.io/v1/node/GroveRelayD0/onoff/%d?access_token=%s" % (self.onoff,self.ACCESS_TOKEN)
		time_out = 0
		result = requests.post(_URL_RELAY_ONOFF)
		while result.status_code != 200:	#if response error try again 5 times
			time_out = time_out + 1
			time.sleep(1)
			result = requests.post(_URL_RELAY_ONOFF)			
			if (time_out >= 5):
				print ("can't post relay onoff")
				return "ERROR"		
		print ("post relay onoff success")
		return "SUCCESS"


	
if __name__ == "__main__":

#	postRelayOnoff(onoff=1)
#	print(getRelayStatus())
#	postRelayOnoff(onoff=0)
#	print(getRelayStatus())
	relay1 = Relay("c79dfaf4d5f720b925e2b262220d99fd")
	print(relay1._get_relay_status())
	relay1.onoff = 1
	relay1._post_relay_onoff()
	print(relay1._get_relay_status())
	
