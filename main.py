import json
import logging

import speedtest
import tweepy

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

with open('config.json') as f:    
    cfg = json.load(f)

# constants
bps_to_mbps = 1.0/1000000.0

auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
twitter_api = tweepy.API(auth)
print twitter_api.me().name

# servers = [1]
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

plan_speed = cfg['plan_speed']
percent_degraded = round(100*download_speed/plan_speed, 2)
print percent_degraded
print cfg['tweet_threshold']
if percent_degraded < cfg['tweet_threshold']:
	status = cfg['isp_twitter_handle'] + ' Service degraded to ' + str(percent_degraded) + '% of ' + \
			str(plan_speed) + 'Mbps plan. ' + str(round(download_speed, 2)) + 'down ' + str(round(upload_speed, 2)) + 'up ' + \
			str(results_dict['server']['latency']) + 'ping on ' + cfg['connection_type'] + ' via ' + results_dict['server']['sponsor']
	print status
	quit()
	twitter_api.update_status(status=str(results_dict['download'] * bps_to_mbps))

