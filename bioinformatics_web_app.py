# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:24:19 2020

@author: oscar
"""

# a comment

import streamlit as st
from Bio import SeqIO
from Bio.Seq import Seq
import SessionState
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




#@st.cache(suppress_st_warning=True)
def main():
    """bioinformatics_web_app"""
    st.title('Sequence Analysis')
    #st.header('This is a header')
    #st.subheader('This is a subheader')
    st.set_option('deprecation.showfileUploaderEncoding', False)
    file = st.file_uploader("Upload FASTA file of DNA", type=["fasta", "txt"])
    session_state = SessionState.get(status = 'off')
    if st.button("submit"):
        if file is not None:
            session_state.status = 'on'
        else:
            st.error('Need to upload file')
    if session_state.status == 'on':       
        radio = st.radio("Select option to view", ('DNA analysis','RNA analysis', 'Protein analysis'))
        seq_record = SeqIO.read(file, "fasta")
        sequence = str(seq_record.seq)
        seq_ob = Seq(sequence).upper()
        transcribed = seq_ob.transcribe()
        translated = seq_ob.translate()
        if radio == 'DNA analysis':
            st.write('DNA sequence:  ', seq_ob)
            lenght = str(len(seq_ob))
            section = '### Sequence length:  ' + "**" + str(len(seq_ob)) + "**"
            st.markdown(section)
            st.write("")
            G = [seq_ob.count('G')]
            A = [seq_ob.count('A')]
            T = [seq_ob.count('T')]
            C = [seq_ob.count('C')]
            GC_content = round((G[0]+C[0])/len(seq_ob)*100, 2)
            AT_content = round((A[0]+T[0])/len(seq_ob)*100, 2)
            st.write('GC content: ', GC_content, '%')
            st.write('AT content: ', AT_content, '%')
            rows = ['G', 'A', 'T', 'C']
            df = pd.DataFrame(np.array([G,A,T,C]), columns = ['Count'], index = rows)
            st.markdown("### Nucleotide count:")
            st.dataframe(data=df, width=1000, height=1000)
            #hide auto-error message with matplotlib
            st.set_option('deprecation.showPyplotGlobalUse', False)
            #plot bar graph of nucleotide frequencies
            plt.bar(rows, [G[0],A[0],T[0],C[0]])
            plt.title('Nucleotide frequencies')
            st.pyplot()
        elif radio == 'RNA analysis':
            st.write(transcribed)
        elif radio == 'Protein analysis':
            st.write(translated)
        
   
            
            

   
            
# Do hydrophobic/ hydrophillic regions of protein sequence?

        
        

    
# =============================================================================
#     st.text('writing some text')
#     if st.checkbox('check-me'):
#         st.write('i am checked!')
#     st.markdown("##### This is markdown 5")
#     st.markdown("# This is markdown 1")
#     st.success("success!")
#     st.warning("Warning!")
#     st.info("Information")
#     st.error("Error!")
#     radio = st.radio("Yes or No?", ('Yes', 'No'))
#     if radio == 'Yes':
#         st.write("you've selected yes")
#     else:
#         st.write("you've selected no")
# =============================================================================
if __name__ == '__main__':
    main()
    

    
# chdir C:/Users/oscar/OneDrive/Documents/python-scripts/Bioinformatics-web-app
# streamlit run bioinformatics_web_app.py

#TO DO
# tidy up and comment code