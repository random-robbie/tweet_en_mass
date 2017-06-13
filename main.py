import tweepy
import re
import fileinput

###CONFIG###
consumer_key = ""
consumer_secret = ""
access_token_key  = ""
access_token_secret = ""
####################


#### TWEET CONFIG ####
message = "Antigua"
LAT = "17.1255097"
LON = "-61.8621107"
######################



#################################################
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token_key, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 
# Grabbing list of usernames to tweet
for line in fileinput.input(['users.txt']):
	#Remove newlines and return carridges
	line = line.replace("\n","")
	line = line.replace ("\r","")
	# Join @user with message
	tweet = "@"+line+" "+message+""
	# Send Tweet
	try:
		Sendtweet = api.update_status(tweet,lat=LAT,long=LON)
		print (Sendtweet)
	except tweepy.TweepError as e:
			error_code = re.sub('[^0-9]','',str(e.response))
			if  error_code == '404':
				error = 'Twitter name not found. Please try again:'
				print (error)
			elif error_code == '403':
				error = 'Twitter forbid the request....Possible Dupe Please try again'
				print (error)
			else:
				error = 'Internal Error, please try again: ' + error_code
				print (error)
