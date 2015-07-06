#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# This script indexes tweets intoe elasticsearch using comperiosearch eslib https://github.com/comperiosearch/elasticsearch-eslib
# requires python 2.7
# installation of the comperiosearch eslib
# git clone https://github.com/comperiosearch/elasticsearch-eslib
# cd elasticsearch-eslib
# pip install -e .

from eslib.procs import TwitterMonitor, FileWriter, ElasticsearchWriter, Transformer
#Register an app on dev.twitter.com, copy in keys, tokens and secrets into config.py. use config.sample.py as sample
from config import *

# A function that is called by a Transformer in the pipeline, so we can do fun stuff if we like...
def do_stuff(proc, doc):
    print "incoming tweet: %s" % doc["_source"]["text"]
    tags = []
    #print doc
    for ent in doc["_source"]["entities"]["hashtags"]:
        print ent["text"]
        tags.append(ent["text"])
    doc["_source"]["hashtags"] = tags
    yield doc

# Set up

m = TwitterMonitor(
    consumer_key        = cred["consumer_key"],
    consumer_secret     = cred["consumer_secret"],
    access_token        = cred["access_token"],
    access_token_secret = cred["access_token_secret"],

    track = ["#ndcroi",  "#ndcoslo"]
)

t = Transformer(func=do_stuff)

#w = FileWriter(filename="TWEET_OUT")  # Writes to stdout
# Alternatively, write to local Elasticsearch:
w = ElasticsearchWriter(index="demo_index")

# Set up the pipeline
t.subscribe(m)
w.subscribe(t)

# Run the stuff

import logging
logging.basicConfig()

print "*** STARTING"
m.start()
try:
    print "*** WAITING UNTIL USER INTERRUPT"
    w.wait()
except KeyboardInterrupt:
    print "*** STOPPING DUE TO USER INTERRUPT"
    m.stop()
    w.wait()
print "*** ALL DONE"
