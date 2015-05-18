cd /vagrant
sh getProdukter.sh
/opt/logstash/bin/logstash agent -verbose -f vinMonopoletCsvFileLogstash.conf