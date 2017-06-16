# isp-degradation-tweet

## Basic Overview

Runs an internet speed test and tweets at your ISP if service is degraded below a threshold.

## Setup

### Installation

`git clone https://github.com/dylancaponi/isp-degradation-tweet.git`

`cd isp-degradation-tweet`

`venv virtualenv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### Configuration

`cp config_template.json config.json`

Edit config.json.  Keep double quote formatting around all values except those for plan_speed and tweet_threshold.

#### Parameters

`connection_type` - put wifi or ethernet

`isp_twitter_handle` - the twitter handle of your ISP or whoever you want to complain to

`plan_speed` - the expected download rate in Mbps of your plan

`tweet_threshold` - the percentage of your actual speed over your plan speed where

Follow these instructions to setup a Twitter dev app and get the following parameters:

`consumer_key`

`consumer_secret`

`access_token`

`access_token_secret`
