import requests
import base64
import json
import logging
import time

logging.basicConfig(filename='o365.log',level=logging.DEBUG)

log = logging.getLogger(__name__)

class Location( object ):
	'''
	Location manages the location on an associated Event on office365.
	
	Methods:
		setLocation - sets the location of the event.
	'''
	con_url = 'https://outlook.office365.com/api/v1.0/me/contacts/{0}'
	time_string = '%Y-%m-%dT%H:%M:%SZ'

	def __init__(self, json=None, auth=None):
		'''
		Wraps all the information for managing the location.
		'''
		self.json = json
		self.auth = auth

		if json:
			log.debug('translating location information into local variables.')
			self.contactId = json['Id']
			self.name = json['DisplayName']
		else:
			log.debug('there was no json, putting in some dumby info.')
			self.json = {'Location':'Somewhere'}

        def setLocation(self,val):
                '''sets event location'''
                self.json['Location'] = val
