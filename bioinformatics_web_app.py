# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:24:19 2020

@author: oscar
"""

""" A bioinformatics web app with streamlit and biopython """
# a comment

import streamlit as st

def main():
    """bioinformatics_web_app"""
    st.title('This is a title')
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.text('writing some text')
    
if __name__ == '__main__':
    main()
    

    
    
# in cmd:   streamlit run nameoffile.py