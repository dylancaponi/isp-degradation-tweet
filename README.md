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

`tweet_threshold` - the threshold of your actual speed over your plan speed where you want to complain.  For example 90 would mean you tweet when you're getting less than 90Mbps on a 100Mbps plan.

[Follow these instructions](https://stackoverflow.com/a/12335636/1236326) to get Twitter dev account and app credentials.
These are: `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret`

### Usage

After following Installation and Configuration sections type:

`venv/bin/python main.py`

If everything is configured properly, a tweet will be sent when your internet speed degrades bellow your set degradation_threshold.

* Results of runs are stored in results.log

* Info logging is in info.log

### Run on a schedule

Type `pwd` to get path of your installed folder.

Eg. `$ pwd`

`/Users/dc/repo/isp-degradation-tweet`

Enter crontab: `EDITOR=nano crontab -e`

Scroll to the bottom and add a line.  Match the path to what you found when you typed pwd.

Eg. `30 14 * * * cd /Users/dc/Repo/isp-degradation-tweet && venv/bin/python main.py`

This example would run the script at 2:30pm every day.  [Learn more about cron here.](http://man7.org/linux/man-pages/man5/crontab.5.html)

### Graph results over time

This is a WIP
