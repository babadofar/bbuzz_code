
Code for presentation at Berlin Buzzwords and NDC 2015
 
This code presupposes that you have already started up the vagrant box at https://github.com/comperiosearch/vagrant-elk-box
 
With the box installed and running, execute  `vagrant ssh`  to enter the shell of the machine
Clone this repo:
````
sudo apt-get install -yq git 
git clone https://github.com/babadofar/bbuzz_code.git
````

To download csv file from Vinmonopolet.no and feed it into elasticsearch using logstash, use
 ````
cd /bbuzz_code
sh getProdukter.sh
/opt/logstash/bin/logstash agent --verbose -l logstash.log   -f vinMonopoletCsvFileLogstash.conf
````

To use this index in Kibana:

* Create new index pattern
* Unselect - Index contains time-based events  
* type in "vinmonopolet" for index name



You may want to add the scripted field
`
pricePrAlcohol
floor(doc['Literpris'].value/doc['Alkohol'].value)
`


To run the twitter feed using elasticsearch-eslib.

````
 git clone https://github.com/comperiosearch/elasticsearch-eslib
 cd elasticsearch-eslib
 pip install -e .
 python twitterfeed.py
 ````




