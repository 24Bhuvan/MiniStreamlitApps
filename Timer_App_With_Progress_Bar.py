import streamlit as st
import time as ts
from datetime import time
def converter(value):
    m,s,ms=str(value).split(":")
    t_s=int(m)*60+int(s)+int(m)/1000
    return t_s
time_in=st.time_input(label="Set timer",value=time(0,0,0))
if str(time_in)=="00:00:00":
    st.write("please set timer")
else:
    sec=converter(time_in)
    bar=st.progress(0)
    per=sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1)+"%")
        ts.sleep(per)