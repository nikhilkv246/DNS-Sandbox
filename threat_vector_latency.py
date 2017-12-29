import string
import random
import pandas as pd
import socket
import timeit
import subprocess


#Create a dataframe with the output from your CISCO file
emp_df = pd.read_csv("C:\\3rd Semester\\RA\\top-1m_csv\\top-1m_csv\\top-1m.csv", header=None, names = ["id","domain"])	 

#trim your dataframe to 1000 records
emp_df = emp_df.truncate(after=1000)    

#function to perform dns query	     	     
def query_record(domain):
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
            print( 'Hostname could not be resolved. Exiting. {}' .format(domain))
    except socket.error:
            print( "Couldn't connect to server. {}" .format(domain))

#empty list to hold the crafted domain names for each threat vectors  
legitimate_tld = []
legitimate_domain = []
arbitrary_and_long = []

#craft specific domain name and create list of threat vectors
for i in range(0,1000,1):
    arbitrary_and_long.insert(i,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))+".wkyk")

for i in range(0,1000,1):
    legitimate_tld.insert(i,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))+".de")
    
   
for i in range(0,1000,1):
    legitimate_domain.insert(i,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))+".cnn.com")
    
df_legitimate_tld = pd.DataFrame({"domain":legitimate_tld})
df_legitimate_domain = pd.DataFrame({"domain":legitimate_domain})
df_arbitrary_and_long = pd.DataFrame({"domain":arbitrary_and_long})   

cmd = 'ipconfig /flushdns'
subprocess.Popen(cmd,stdout=subprocess.PIPE)

#loop to time the latency of respective queries
for i in range(1,5,1):
    df_legitimate_tld["latency"+str(i)] = df_legitimate_tld.apply(lambda row: timeit.timeit('query_record("{}")' .format(row["domain"]), 'from __main__ import query_record', number = 1), 1)
    df_legitimate_domain["latency"+str(i)] = df_legitimate_domain.apply(lambda row: timeit.timeit('query_record("{}")' .format(row["domain"]), 'from __main__ import query_record', number = 1), 1)
    df_arbitrary_and_long["latency"+str(i)] = df_arbitrary_and_long.apply(lambda row: timeit.timeit('query_record("{}")' .format(row["domain"]), 'from __main__ import query_record', number = 1), 1)
    emp_df["latency"+str(i)] =  emp_df.apply(lambda row: timeit.timeit('query_record("{}")' .format(row["domain"]), 'from __main__ import query_record', number = 1), 1)
    
    cmd = 'ipconfig /flushdns'
    subprocess.Popen(cmd,stdout=subprocess.PIPE)

#convert latency to millisecond
for i in range(1,5,1):
    df_legitimate_tld["latency"+str(i)] = df_legitimate_tld["latency"+str(i)]*1000
    df_legitimate_domain["latency"+str(i)] = df_legitimate_domain["latency"+str(i)]*1000
    df_arbitrary_and_long["latency"+str(i)] = df_arbitrary_and_long["latency"+str(i)]*1000
    emp_df["latency"+str(i)] = emp_df["latency"+str(i)]*1000

    
#output latecny of each threat vectors in specific file            
df_legitimate_tld.to_csv("C:\\3rd Semester\\RA\\top-1m_csv\\top-1m_csv\\threat_vectors\\df_legitimate_tld.csv")
df_legitimate_domain.to_csv("C:\\3rd Semester\\RA\\top-1m_csv\\top-1m_csv\\threat_vectors\\df_legitimate_domain.csv")
df_arbitrary_and_long.to_csv("C:\\3rd Semester\\RA\\top-1m_csv\\top-1m_csv\\threat_vectors\\arbitrary_and_long.csv")
emp_df.to_csv("C:\\3rd Semester\\RA\\top-1m_csv\\top-1m_csv\\threat_vectors\\empirical_1k.csv")

      


    

    
    