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




aas = pd.read_csv('csv_of_aas.txt')
full_names = [name for name in aas['Full_name']]
abbreviation = [ab for ab in aas['Abbreviation']]
aa_dict = dict(zip(abbreviation, full_names))
aa_dict['*'] = 'Stop'


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
            st.write('RNA sequence:  ', transcribed)
            lenght = str(len(transcribed))
            section = '### Sequence length:  ' + "**" + str(len(transcribed)) + "**"
            st.markdown(section)
            st.write("")
            G = [transcribed.count('G')]
            A = [transcribed.count('A')]
            U = [transcribed.count('U')]
            C = [transcribed.count('C')]
            GC_content = round((G[0]+C[0])/len(seq_ob)*100, 2)
            AU_content = round((A[0]+U[0])/len(seq_ob)*100, 2)
            st.write('GC content: ', GC_content, '%')
            st.write('AU content: ', AU_content, '%')
            rows = ['G', 'A', 'U', 'C']
            df = pd.DataFrame(np.array([G,A,U,C]), columns = ['Count'], index = rows)
            st.markdown("### Nucleotide count:")
            st.dataframe(data=df, width=1000, height=1000)
            #hide auto-error message with matplotlib
            st.set_option('deprecation.showPyplotGlobalUse', False)
            #plot bar graph of nucleotide frequencies
            plt.bar(rows, [G[0],A[0],U[0],C[0]])
            plt.title('Nucleotide frequencies')
            st.pyplot()
        elif radio == 'Protein analysis':
            st.write('Protein sequence: ', translated)
            lenght = str(len(translated))
            section = '### Sequence length:  ' + "**" + str(len(translated)) + "**"
            st.markdown(section)
            st.write("")
            aa_count = {}
            for letter in translated:
                if letter in aa_count.keys():
                    aa_count[letter] += 1
                else:
                     aa_count[letter] = 1
            display_dict = {}
            for key, value in aa_count.items():
                display_dict[aa_dict[key]] = value
            reverse_aa_dict = {value:key for key,value in aa_dict.items()}
            display_names = [key for key in display_dict.keys()]
            display_counts = [value for value in display_dict.values()] 
            temp_zip = list(zip(display_names, display_counts))
            temp_zip.sort(key= lambda x: x[1], reverse=True)
            names = [tup[0] for tup in temp_zip]
            names2 = [(name + "(" + str(reverse_aa_dict[name]) + ")") for name in names]
            counts = [tup[1] for tup in temp_zip]
            aa_df = pd.DataFrame(counts, columns = ['Count'], index = names2)
            st.markdown("### Amino Acid count:")
            st.dataframe(aa_df, width=1000, height=1000)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            #plot bar graph of amino acid frequencies
            ordered_abbreviations = [reverse_aa_dict[name] for name in names]
            plt.bar(ordered_abbreviations, counts)
            plt.title('Amio Acid frequencies')
            st.pyplot()

   
            
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
