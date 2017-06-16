import os
import json
import logging

import speedtest
import tweepy

# configure logging
logging.basicConfig(
    filename="info.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

# load config file
with open('config.json') as f:    
    cfg = json.load(f)

# define constants
bps_to_mbps = 1.0/1000000.0

# connect to twitter api
auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
twitter_api = tweepy.API(auth)
logging.info('connected to Twitter API')

# run speed test
logging.info('start speed test...')
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
results_dict = s.results.dict()
logging.info(results_dict)

# write results
with open('results.log', 'a') as f:
    json.dump(results_dict, f)
    f.write(os.linesep)

# convert speeds to Mbps
download_speed = results_dict['download'] * bps_to_mbps
upload_speed = results_dict['upload'] * bps_to_mbps

plan_speed = cfg['plan_speed']
percent_degraded = round(100*download_speed/plan_speed, 2)
logging.info('percent_degraded: ' + str(percent_degraded))

if percent_degraded < cfg['tweet_threshold']:
    status = cfg['isp_twitter_handle'] + ' Service degraded to ' + str(percent_degraded) + '% of ' + \
            str(plan_speed) + 'Mbps plan. ' + str(round(download_speed, 2)) + 'down ' + str(round(upload_speed, 2)) + 'up ' + \
            str(results_dict['server']['latency']) + 'ms ping on ' + cfg['connection_type'] + ' via ' + results_dict['server']['host']
    logging.info('tweeting: ' + status)
    twitter_api.update_status(status=status)
else:
    logging.info('speed above ' + str(cfg['tweet_threshold']) + '% degradation threshold. not tweeting.')


