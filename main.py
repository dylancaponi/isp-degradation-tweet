import json
import logging

import speedtest
import tweepy

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

with open('credentials.json') as f:    
    creds = json.load(f)

# the speed in Mbps that you are paying for 
plan_speed = 300
# your ISP's twitter handle
isp_twitter_handle = '@Ask_Spectrum'
# wifi or ethernet or anything you want to add to the message
connection_type = 'wifi'
# tweet will send under this percentage of degradation
tweet_threshold = 80
# number of tests to average
# num_to_average = 3

# constants
bps_to_mbps = 1.0/1000000.0

auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
auth.set_access_token(creds['access_token'], creds['access_token_secret'])
twitter_api = tweepy.API(auth)
print twitter_api.me().name


s = speedtest.Speedtest()
# s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
# s.share()

results_dict = s.results.dict()
download_speed = results_dict['download'] * bps_to_mbps
upload_speed = results_dict['upload'] * bps_to_mbps

print results_dict
logging.info(results_dict)

percent_degraded = str(round(100*download_speed/plan_speed, 2))

if percent_degraded < tweet_threshold:
	
	status = isp_twitter_handle + ' Service degraded to ' + percent_degraded + '% of ' + \
			str(plan_speed) + 'Mbps plan. ' + str(round(download_speed, 2)) + 'down ' + str(round(upload_speed, 2)) + 'up ' + \
			str(results_dict['server']['latency']) + 'ping via ' + connection_type
	print status
	quit()
	twitter_api.update_status(status=str(results_dict['download'] * bps_to_mbps))

