# ====================== IMPORT PACKAGES ==============

import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing 

import streamlit as st
import base64

 # ------------ TITLE 

st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:36px;">{"Log Analysis and Threat Detection Using Machine Learning"}</h1>', unsafe_allow_html=True)


# ================ Background image ===

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.avif')



import pickle

with open('model.pickle', 'rb') as f:
    rf = pickle.load(f)
    
    
    
    
with open('finalpred.pickle', 'rb') as f:
     pred_rf = pickle.load(f)  
     

# pred_rf = pred_rf

# ================== PREDICTION  ====================

st.write("-----------------------------------------------------------------")
st.write(" Kindly Enter the following details for network log analysis     ")
st.write("------------------------------------------------------=----------")
print()


q1=st.text_input("Enter the Frame Number")

q2=st.text_input("Enter the Frame Time")

q3=st.text_input("Enter the Frame Length")

q4=st.text_input("Enter the source MAC (Media Access Control) address of the Ethernet frame")

q5=st.text_input("Enter the Destination MAC (Media Access Control) address of the Ethernet frame")

q6=st.text_input("Enter the source IP address of the packet")

q7=st.text_input("Enter the Destination IP address of the packet")

q8=st.selectbox("Choose Protocol",('-1','1','6','2','17'))

q9=st.text_input("Enter the length of the IP packet")

q10=st.text_input("Enter the length of the TCP segment")

q11=st.text_input("Enter The source port number in the TCP protocol")

q12=st.text_input("Enter The destination port number in the TCP protocol")

q13=st.text_input("Enter the value associated with the packet or session such as total bytes transferred")


aa = st.button("PREDICT")


if aa:
    
    # try:
        
    #     st.warning("Error!!!")
        
    # except:
    
        data =[float(q1),float(q2),float(q3),float(q4),float(q5),float(q6),float(q7),int(q8),float(q9),float(q10),float(q11),float(q12),float(q13)]
        data1=np.array(data).reshape(1, -1)
        pred_rf = rf.predict(data1)


        if pred_rf == 0:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:30px;font-family:Caveat, sans-serif;">{"Identified = NORMAL (No attack)"}</h1>', unsafe_allow_html=True)
            

    
        elif pred_rf == 1:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:30px;font-family:Caveat, sans-serif;">{"Identified = WRONG SETUP"}</h1>', unsafe_allow_html=True)
    
    

            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            st.write("----------------------------------------------------------------------------------")

            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )
            
            st.write("----------------------------------------------------------------------------------")
            
            st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;font-family:verdana;">{"Ensure proper configuration and hardening of network devices and servers to minimize misconfigurations that can expose vulnerabilities."}</h1>', unsafe_allow_html=True)



        elif pred_rf== 2:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:30px;font-family:Caveat, sans-serif;">{"Identified = DDOS"}</h1>', unsafe_allow_html=True)
    
    
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            st.write("----------------------------------------------------------------------------------")

            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )     
            
            st.write("----------------------------------------------------------------------------------")
            
            st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Implement rate limiting, traffic filtering, and use DDoS protection services like Cloudflare or AWS Shield to absorb high traffic volumes."}</h1>', unsafe_allow_html=True)

            

    
        elif pred_rf == 3:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:30px;font-family:Caveat, sans-serif;">{"Identified = DATA TYPE PROBING (ultrasonic sensor was used so in data type probing mostly string values are sent to the server)"}</h1>', unsafe_allow_html=True)
    
            
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            st.write("----------------------------------------------------------------------------------")

            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )   
            
            st.write("----------------------------------------------------------------------------------")
            
            st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Use input validation and strict data type checks on server-side to prevent the acceptance of unexpected or malformed data."}</h1>', unsafe_allow_html=True)
           

            
        elif pred_rf == 4:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:30px;font-family:Caveat, sans-serif;">{"Identified = SCAN ATTACK "}</h1>', unsafe_allow_html=True)
    
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            st.write("----------------------------------------------------------------------------------")

            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )
            
            st.write("----------------------------------------------------------------------------------")
            
            st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Employ firewalls and intrusion detection/prevention systems (IDS/IPS) to block unauthorized scanning attempts and monitor for unusual port scanning activity."}</h1>', unsafe_allow_html=True)
           
    
    
        elif pred_rf == 5:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:30px;font-family:Caveat, sans-serif;">{"Identified = MAN IN THE MIDDLE"}</h1>', unsafe_allow_html=True)
    
                
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )  
            
            st.write("----------------------------------------------------------------------------------")
            
            st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Use end-to-end encryption (e.g., SSL/TLS) for all communications to ensure data integrity and confidentiality between clients and servers."}</h1>', unsafe_allow_html=True)
           