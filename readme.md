
THIS IS SOME CODE THAT NEEDS TO BE MANUAL EXECUTIONED
OR; OF COURSE YOU CAN PUT IT IN A SHELL SCRIPT BUT WHAT'S SO FUN ABOUT THAT
````
 sudo apt-get install git
git clone https://github.com/babadofar/bbuzz_code.git
cd /bbuzz_code
sh getProdukter.sh
 /opt/logstash/bin/logstash agent --verbose -l logstash.log -t  -f vinMonopoletCsvFileLogstash.conf
````

You may want to add the scripted field
`
pricePrAlcohol
floor(doc['Literpris'].value/doc['Alkohol'].value)
`
