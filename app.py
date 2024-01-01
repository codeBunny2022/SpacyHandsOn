import streamlit as st
import spacy
from textblob import TextBlob
# from gensim.summarization import summarize

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def sumy_summarizer(doc):
    parser=PlaintextParser.from_string(doc,tokenizer="PlaintextParser")
    lex_summarizer=LexRankSummarizer()
    summary=lex_summarizer(parser.document,3)
    summary_list=[str(sentence) for sentence in summary]
    result=''.join(summary_list)
    return result



def text_analyzer(mytext):
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(mytext)
    tokens=[token.text for token in doc]
    allData = [{"Token": token.text, "Lemma": token.lemma_} for token in doc]
    return allData

def entities_analyzer(mytext):
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(mytext)
    entities=[(entity.text,entity.label_) for entity in doc.ents]
    return entities

def main():
    st.title("Pilosopher")
    st.subheader("NLP on the GO!")

    if st.checkbox("Extract Tokens and Lemma"):
        st.subheader("Tokenieze the text")
        message = st.text_area("Feed the content","Type Here")
        if st.button("Analyze"):
            nlp_result=text_analyzer(message)
            st.success(nlp_result)


    if st.checkbox("Extract Named Entities"):
        st.subheader("Recognize Named entities from the text")
        message = st.text_area("Feed the content","Type Here")
        if st.button("Extract"):
            nlp_result=entities_analyzer(message)
            st.success(nlp_result)


    if st.checkbox("Reveal Sentiments"):
        st.subheader("Recognize Sentiments from the text")
        message = st.text_area("Feed the content","Type Here")
        if st.button("Reveal"):
            blob=TextBlob(message)
            resultSentiment=blob.sentiment
            st.success(resultSentiment)
    
    
    if st.checkbox("Text Summarizer"):
        st.subheader("Briefly summairze your text")
        message = st.text_area("Feed the content","Type Here")
        summary_options=st.selectbox("Choose your Summarizer",("gensim","sumy"))
        if st.button("Summary"):
            # if summary_options == 'gensim':
            #     st.text("Using Gensim...")
            #     summaryResult=summarize(message)
            # elif summary_options == 'sumy':
            #     st.text("Using Sumy...")
            #     summaryResult=sumy_summarizer(message)
            # else:
            #     st.warning("Using default Summarizer...")
            #     st.text("Using Gensim...")
            #     summaryResult=summarize(message)
            st.text("Using Sumy...")
            summaryResult=sumy_summarizer(message)
            st.success(summaryResult)





if __name__ == "__main__":
    main()