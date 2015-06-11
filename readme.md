
THIS IS SOME CODE THAT NEEDS TO BE MANUAL EXECUTIONED
OR; OF COURSE YOU CAN PUT IT IN A SHELL SCRIPT BUT WHAT'S SO FUN ABOUT THAT
````
sudo apt-get install -yq git 
git clone https://github.com/babadofar/bbuzz_code.git
cd /bbuzz_code
sh getProdukter.sh
/opt/logstash/bin/logstash agent --verbose -l logstash.log   -f vinMonopoletCsvFileLogstash.conf
````

In Kibana:

* Create new index pattern
* Unselect - Index contains time-based events  
* type in "vinmonopolet" for index name



You may want to add the scripted field
`
pricePrAlcohol
floor(doc['Literpris'].value/doc['Alkohol'].value)
`
