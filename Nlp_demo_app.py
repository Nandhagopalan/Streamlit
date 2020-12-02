#!/usr/bin/python
# -*- coding: utf-8 -*-
import streamlit as st
import os

# NLP Pkgs

from textblob import TextBlob
import spacy
from gensim.summarization import summarize


@st.cache
def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)

    # tokens = [ token.text for token in docx]

    allData = ['"Token":{},\n"Lemma":{}'.format(token.text,
               token.lemma_) for token in docx]
    return allData


# Function For Extracting Entities

@st.cache
def entity_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    allData = ['"Token":{},\n"Entities":{}'.format(tokens, entities)]
    return allData


def main():
    """ NLP Based App with Streamlit """

    # Title

    st.title('NLPiffy with Streamlit')
    st.subheader('Natural Language Processing On the Go..')
    st.markdown("""
    	#### Description
    	+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
    	Tokenization,NER,Sentiment,Summarization
    	""")

    # Tokenization

    if st.checkbox('Show Tokens and Lemma'):
        st.subheader('Tokenize Your Text')

        message = st.text_area('Enter Text', 'Type Here ..')
        if st.button('Analyze'):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)

    # Entity Extraction

    if st.checkbox('Show Named Entities'):
        st.subheader('Analyze Your Text')

        message = st.text_area('Enter Text', 'Type Here ..')
        if st.button('Extract'):
            entity_result = entity_analyzer(message)
            st.json(entity_result)

    # Sentiment Analysis

    if st.checkbox('Show Sentiment Analysis'):
        st.subheader('Analyse Your Text')

        message = st.text_area('Enter Text', 'Type Here ..')
        if st.button('Analyze'):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)

    # Summarization

    if st.checkbox('Show Text Summarization'):
        st.subheader('Summarize Your Text')
        message = st.text_area('Enter Text', 'Type Here ..')
        summary_options = st.selectbox('Choose Summarizer', ['sumy','gensim'])
        
        if st.button("Summarize"):
            if summary_options=='sumy':
                st.text("Using spacy...")
                result=summarize(message)
            
            st.success(result)


    st.sidebar.subheader("About App")
    st.sidebar.text("NLPiffy App with Streamlit")
    st.sidebar.info("Cudos to the Streamlit Team")

if __name__ == '__main__':
    main()
