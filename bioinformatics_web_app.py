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
        radio = st.radio("Select option to view", ('DNA sequence','RNA sequence', 'Protein sequence'))
        seq_record = SeqIO.read(file, "fasta")
        sequence = str(seq_record.seq)
        seq_ob = Seq(sequence)
        transcribed = seq_ob.transcribe()
        translated = seq_ob.translate()
        if radio == 'DNA sequence':
            st.write(seq_ob)
        elif radio == 'RNA sequence':
            st.write(transcribed)
        elif radio == 'Protein sequence':
            st.write(translated)
        
   
            
            

   
            
 

        
        

    
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
    

    
    
# TO RUN THE FILE, in cmd typ:   streamlit run nameoffile.py

