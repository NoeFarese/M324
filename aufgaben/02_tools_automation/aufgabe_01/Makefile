address: ip host
	cat host ip | awk 'NR==1{host=$$0} NR==2{ip=$$0} END{print host "@" ip}' > address
	@echo "File 'address' wurde erstellt."

ip:
	hostname -I | awk '{print $$1}' > ip
	@echo "File 'ip' wurde mit aktueller IP-Adresse erstellt."

host:
	hostname > host
	@echo "File 'host' wurde mit aktuellem Hostnamen erstellt."

clean:
	rm -f ip host address
	@echo "ip, host und address gelöscht."

