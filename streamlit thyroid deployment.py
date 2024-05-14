import streamlit as st
import pickle
import pandas as pd
#setting the interface 
st.title('thyroid diseases classification ')
st.info('web page for thyroid DIDEADES ')
st.sidebar.header('Features')
#assigned faeatures columns to our streamlit app
Age=st.text_input('age')
Sex=st.text_input('sex')
query_on_thyroxine = st.text_input('query on thyroxine')
sick = st.text_input('sick')
pregnant = st.text_input('pregnant')
thyroid_surgery =st.text_input('thyroid surgery')
I131_treatment=st.text_input('I131 treatment')
query_hyperthyroid =st.text_input('query hyperthyroid')
lithium = st.text_input('lithium') 
query_goitre=st.text_input('goitre')
tumor=st.text_input('tumor')
hypopituitary=st.text_input('hypopituitary')
psych=st.text_input('psych')
TSH =st.text_input('TSH')
T3=st.text_input('T3')
TT4=st.text_input('TT4')
T4U=st.text_input('T4U')
FTI=st.text_input('FTI')
composite_health_indicator=st.text_input('composite_health_indicator')
T3_T4_ratio=st.text_input('T3_T4_ratio')
TSH_TT4_ratio=st.text_input('TSH_TT4_ratio')
T4U_FTI_ratio = st.text_input('T4U_FTI_ratio')
#creating dataform
df=pd.DataFrame({'age':[Age],'sex':[Sex],
'query on thyroxine':[query_on_thyroxine], 'sick':[sick],
'pregnant':[pregnant],'thyroid surgery':[thyroid_surgery],'I131 treatment':[I131_treatment],
'query hyperthyroid':[query_hyperthyroid],'lithium':[lithium],'goitre':[query_goitre],'tumor':[tumor],'hypopituitary':[hypopituitary],'psych':[psych],
'TSH':[TSH] , 'T3':[T3],'TT4':[TT4],'T4U':[T4U] , 'FTI':[FTI] ,'composite_health_indicator':[composite_health_indicator],
'T3_T4_ratio':[T3_T4_ratio] , 'TSH_TT4_ratio':[TSH_TT4_ratio] ,'T4U_FTI_ratio':[T4U_FTI_ratio]},index=[0])
#load our previously implementated model 
model=pickle.load(open(r"C:\Users\Dell\Downloads\savemodel_1 (1).sav",'rb'))
Confirmation=st.sidebar.button('confirm')
if Confirmation:
    result=model.predict(df)
    st.write(result)