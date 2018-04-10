**************THIS REPOSITORY IS UNDER DEVELOPMENT******************
**************WILL BE COMPLETED SOON********************************

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




************************************************************************************************************************************************************LATESTFILES*************************************************************************************************************************************************************************************************************************************************

ROOT Server
db.root original contents not required
db.root
; BIND data file for local loopback interface                                                                                     
;                                                                                                                                 
$TTL    604800                                                                                                                    
@       IN      SOA     nsr. root.localhost. (                                                                                    
                              2         ; Serial                                                                                  
                         604800         ; Refresh                                                                                 
                          86400         ; Retry                                                                                   
                        2419200         ; Expire                                                                                  
                         604800 )       ; Negative Cache TTL                                                                      
;                                                                                                                                 
@       IN      NS      nsr.                                                                                                      
nsr     IN      A       172.20.4.8                                                                                                
@       IN      A       172.20.4.8                                                                                                
                                                                                                                                  
tld1    86400   IN      NS      nst.tld1.                                                                                         
nst.tld1.       86400   IN      A       172.20.1.4                                                                                
                                                                                                                                  
tld2    86400   IN      NS      nst.tld2.                                                                                         
nst.tld2.       86400   IN      A       172.20.1.5 


named.conf                                                                                                                              
include "/etc/bind/named.conf.options";                                                                                           
include "/etc/bind/named.conf.local";                                                                                             
//include "/etc/bind/named.conf.default-zones";                                                                                   
include "/etc/bind/named.conf.custom-zones"; 

named.conf.custom-zones
zone "." {                                                                                                                        
        type master;                                                                                                              
        file "/etc/bind/db.root";                                                                                                 
}; 

named.conf.options
        directory "/var/cache/bind"; 
        //dnssec-validation auto;                                                                                                 
        //recursion no;                                                                                                           
        auth-nxdomain no;    # conform to RFC1035                                                                                 
        listen-on-v6 { any; }; 

TLD1 Serevr
db.tld1
; BIND data file for local loopback interface                                                                                     
;                                                                                                                                 
$TTL    604800                                                                                                                    
@       IN      SOA     nst.tld1. root.localhost. (                                                                               
                              2         ; Serial                                                                                  
                         604800         ; Refresh                                                                                 
                          86400         ; Retry                                                                                   
                        2419200         ; Expire                                                                                  
                         604800 )       ; Negative Cache TTL                                                                      
;                                                                                                                                 
@       IN      NS      nst.tld1.                                                                                                 
nst     IN      A       172.20.1.4                                                                                                
@       IN      A       172.20.1.4                                                                                                
                                                                                                                                  
ans1    86400   IN      NS      nsa.ans1.tld1.                                                                                    
nsa.ans1.tld1.  86400   IN      A       172.20.2.8                                                                                
                                                                                                                                  
ans2    86400   IN      NS      nsa.ans2.tld1.                                                                                    
nsa.ans2.tld1.  86400   IN      A       172.20.3.3 

named.conf
include "/etc/bind/named.conf.options";                                                                                           
include "/etc/bind/named.conf.local";                                                                                             
include "/etc/bind/named.conf.default-zones";                                                                                     
include "/etc/bind/named.conf.custom-zones";

named.conf.custom-zones
zone "tld1" {                                                                                                                     
        type master;                                                                                                              
        file "/etc/bind/db.tld1";                                                                                                 
};  

named.conf.options
directory "/var/cache/bind";
//dnssec-validation auto;                                                                                                 
auth-nxdomain no;    # conform to RFC1035                                                                                 
listen-on-v6 { any; };

TLD2 Server
db.tld2
; BIND data file for local loopback interface                                                                                     
;                                                                                                                                 
$TTL    604800                                                                                                                    
@       IN      SOA     nst.tld2. root.localhost. (                                                                               
                              2         ; Serial                                                                                  
                         604800         ; Refresh                                                                                 
                          86400         ; Retry                                                                                   
                        2419200         ; Expire                                                                                  
                         604800 )       ; Negative Cache TTL                                                                      
;                                                                                                                                 
@       IN      NS      nst.tld2.                                                                                                 
nst     IN      A       172.20.1.5                                                                                                
@       IN      A       172.20.1.5                                                                                                
                                                                                                                                  
ans3    86400   IN      NS      nsa.ans3.tld2.                                                                                    
nsa.ans3.tld2.  86400   IN      A       172.20.4.7                                                                                
                                                                                                                                  
ans4    86400   IN      NS      nsa.ans4.tld2.                                                                                    
nsa.ans4.tld2.  86400   IN      A       172.20.2.9 

named.conf
include "/etc/bind/named.conf.options";                                                                                           
include "/etc/bind/named.conf.local";                                                                                             
include "/etc/bind/named.conf.default-zones";                                                                                     
include "/etc/bind/named.conf.custom-zones";

named.conf.custom-zones
zone "tld2" {                                                                                                                     
        type master;                                                                                                              
        file "/etc/bind/db.tld2";                                                                                                 
};

named.conf.options
directory "/var/cache/bind";
//dnssec-validation auto;                                                                                                 
auth-nxdomain no;    # conform to RFC1035                                                                                 
listen-on-v6 { any; };  

ANS1 Server
db.ans1.tld1
;                                                                                                                                 
; BIND data file for local loopback interface                                                                                     
;                                                                                                                                 
$TTL    604800                                                                                                                    
@       IN      SOA     nsa.ans1.tld1. root.localhost. (                                                                          
                              2         ; Serial                                                                                  
                         604800         ; Refresh                                                                                 
                          86400         ; Retry                                                                                   
                        2419200         ; Expire                                                                                  
                         604800 )       ; Negative Cache TTL                                                                      
;                                                                                                                                 
@       IN      NS      nsa.ans1.tld1.                                                                                            
nsa     IN      A       172.20.2.8                                                                                                
@       IN      A       172.20.2.8                                                                                                
                                                                                                                                  
ex1     IN      A       1.1.1.10                                                                                                  
ex2     IN      A       2.1.1.10                                                                                                  
ex3     IN      CNAME   ex1 

named.conf
include "/etc/bind/named.conf.options";                                                                                           
include "/etc/bind/named.conf.local";                                                                                             
include "/etc/bind/named.conf.default-zones";                                                                                     
include "/etc/bind/named.conf.custom-zones";


named.conf.custom-zones
zone "ans1.tld1" {                                                                                                                
        type master;                                                                                                              
        file "/etc/bind/db.ans1.tld1";                                                                                            
}; 

named.conf.options
directory "/var/cache/bind"; 
//dnssec-validation auto;
recursion no; 
auth-nxdomain no;    # conform to RFC1035    
listen-on-v6 { any; }; 

RR Server
db.root
.                        3600000      IN NS    nsr.                                                                               
nsr.      3600000      A     172.20.4.8   

named.conf.options
        directory "/var/cache/bind";   
        //dnssec-validation auto;                                                                                                 
        recursion yes;                                                                                                            
        auth-nxdomain no;    # conform to RFC1035                                                                                 
        listen-on-v6 { any; };
        

Client 
cd /etc/ 
ls
vim dnsmasq.conf
//Uncomment the below line as it is required
conf-dir=/etc/dnsmasq.d 
Save the file

cd dnsmasq.d
vim dnscache.conf  - Neg Cache enabled at Client (To disable add no-negcache)
no-hosts                                                                                                            
no-resolv                                                                                                           
listen-address=127.0.0.1                                                                                            
bind-interfaces                                                                                                     
server=172.20.4.3    ////For Resolving - IP of RR                                                                                       
#server=8.8.8.8     ////For Internet - to download                                                                                       log-facility=/var/log/dnsmasq.log                                                                                   
log-queries

To Restart servers
/etc /init.d/bind9 restart
/etc /init.d/dnsmasq restart
