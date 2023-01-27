import streamlit as st
import requests 
import json
import pubchempy as pcp
import re

KEY = st.secrets.DeeplAPIKEY.APIKEY

st.write('化合物名からCAS番号を探します')
t=st.text_input('化合物名を入力', 'ジクロロメタン')

# APIから翻訳情報を取得
result = requests.get( 
    # 無料版のURL
    "https://api-free.deepl.com/v2/translate",
    params={ 
        "auth_key": "KEY",
        "target_lang": "EN",
        "text": t,
    },
) 

b = result.json()["translations"][0]["text"]

st.subheader(b)


compounds = pcp.get_compounds(b,'name')

a = compounds[0].synonyms

first_match = None
for element in a:
    match = re.search(r'\d+-\d+-\d+', element)
    if match:
        if first_match is None:
            first_match = match.group()
        break

st.subheader(first_match)