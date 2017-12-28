Root Server Configuration: 
db.nik changed to db.root
db.root moved to db.rootoriginal(not required)

db.root contents
;                                                                                                                  
; BIND data file for local loopback interface                                                                      
;                                                                                                                  
$TTL    604800                                                                                                     
@       IN      SOA     nsr.root. root.localhost. (                                                                
                              2         ; Serial                                                                   
                         604800         ; Refresh                                                                  
                          86400         ; Retry                                                                    
                        2419200         ; Expire                                                                   
                         604800 )       ; Negative Cache TTL                                                       
;                                                                                                                  
@       IN      NS      nsr.root.                                                                                  
nsr     IN      A       172.20.4.8                                                                                 
@       IN      A       172.20.4.8                                                                                 
                                                                                                                   
tld1    86400   IN      NS      nst.tld1.root.                                                                     
nst.tld1.root.  86400   IN      A       172.20.1.4  

Commented the below line in named.conf
//include "/etc/bind/named.conf.default-zones"; 

Contents of named.conf.custom-zones
zone "root" {                                                                                                      
        type master;                                                                                               
        file "/etc/bind/db.root";                                                                                  
}; 

named.conf.options Contents
options {                                                                                                          
        directory "/var/cache/bind"; 
        //dnssec-validation auto;                                                                                  
        //recursion no;                                                                                            
        auth-nxdomain no;    # conform to RFC1035                                                                  
        listen-on-v6 { any; };                                                                                     
};

TLD Server Configuration:
db.tld1.root Contents
;                                                                                                                  
; BIND data file for local loopback interface                                                                      
;                                                                                                                  
$TTL    604800                                                                                                     
@       IN      SOA     nst.tld1.root. root.localhost. (                                                           
                              2         ; Serial                                                                   
                         604800         ; Refresh                                                                  
                          86400         ; Retry                                                                    
                        2419200         ; Expire                                                                   
                         604800 )       ; Negative Cache TTL                                                       
;                                                                                                                  
@       IN      NS      nst.tld1.root.                                                                             
nst     IN      A       172.20.1.4                                                                                 
@       IN      A       172.20.1.4                                                                                 
                                                                                                                   
ans1    86400   IN      NS      nsa.ans1.tld1.root.                                                                
nsa.ans1.tld1.root.     86400   IN      A       172.20.2.8

named.conf.custom-zones Contents
zone "tld1.root" {                                                                                                 
        type master;                                                                                               
        file "/etc/bind/db.tld1.root";                                                                             
}; 

named.conf.options Contents
options {                                                                                                          
        directory "/var/cache/bind";
        //dnssec-validation auto;                                                                                  
        //recursion no;                                                                                            
        auth-nxdomain no;    # conform to RFC1035                                                                  
        listen-on-v6 { any; };                                                                                     
};

ANS Server Configuration
db.ans1.tld1.root Contents
;                                                                                                                  
; BIND data file for local loopback interface                                                                      
;                                                                                                                  
$TTL    604800                                                                                                     
@       IN      SOA     nsa.ans1.tld1.root. root.localhost. (                                                      
                              2         ; Serial                                                                   
                         604800         ; Refresh                                                                  
                          86400         ; Retry                                                                    
                        2419200         ; Expire                                                                   
                         604800 )       ; Negative Cache TTL                                                       
;                                                                                                                  
@       IN      NS      nsa.ans1.tld1.root.                                                                        
nsa     IN      A       172.20.2.8                                                                                 
@       IN      A       172.20.2.8                                                                                 
                                                                                                                   
ex1     IN      A       1.2.3.4                                                                                    
ex2     IN      A       5.6.7.8                                                                                    
ex3     IN      CNAME   ex1 

// be authoritative for the localhost forward and reverse zones, and for                                           
// broadcast zones as per RFC 1912                                                                                 
  
named.conf.custom-zones Contents  
zone "ans1.tld1.root" {                                                                                            
        type master;                                                                                               
        file "/etc/bind/db.ans1.tld1.root";                                                                        
};
   
named.conf.options Contents   
options {                                                                                                          
        directory "/var/cache/bind";
        //dnssec-validation auto;                                                                                  
        recursion no;                                                                                              
        auth-nxdomain no;    # conform to RFC1035                                                                  
        listen-on-v6 { any; };                                                                                     
};

RR Server Configuration
db.root Contents
; formerly NS.INTERNIC.NET                                                                                         
;                                                                                                                  
.                        3600000      IN NS    nsr.root.                                                           
nsr.root.      3600000      A     172.20.4.8(address of root)       


named.conf.options Contents
options {                                                                                                          
        directory "/var/cache/bind";
        //dnssec-validation auto;                                                                                  
        recursion yes;                                                                                             
        auth-nxdomain no;    # conform to RFC1035                                                                  
        listen-on-v6 { any; };                                                                                     
}; 

Client Configuration
Navigate to /etc/
vim dnsmasq.conf
Uncomment the below line($G to navigate to last line)
conf-dir=/etc/dnsmasq.d

cd dnsmasq.d
vim dnscache.conf
no-hosts                                                                                                           
no-resolv                                                                                                          
listen-address=127.0.0.1                                                                                           
bind-interfaces                                                                                                    
server=/.root/172.20.4.3                                                                                           
log-facility=/var/log/dnsmasq.log                                                                                  
log-queries
//no-negcache  (To disable negative cache at LC - query goes RR everytime)
