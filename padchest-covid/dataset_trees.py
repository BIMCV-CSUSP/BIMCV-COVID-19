import streamlit as st
import pandas as pd
import numpy as np

import os
import io
import re
import yaml
from anytree import AnyNode, Node, RenderTree, AsciiStyle
from anytree.exporter import DictExporter
from anytree.importer import DictImporter
from pprint import pprint  # just for nice printing
from anytree import RenderTree , search # just for nice printing
import base64


#Return tree terms given a query term: It finds the node in the trees and get all child terms classified under the query term.
#return terms and CUIs
def get_childs(query_term = "radiological finding"):
    tree = None
    s = {}
    stream = open("trees_code.txt", "r")
    docs = yaml.load_all(stream, Loader=yaml.FullLoader)
    print("Starting to search " + query_term +  " in the following trees:")
    for doc in docs:
        tree_root = DictImporter().import_(doc)
        print("\t" + tree_root.label)
        r = search.findall(tree_root, lambda node: node.label == query_term)
        if r:
            tree = RenderTree(r[0])
            for pre, _, node in tree:
                CUI = None
                try:
                    CUI = node.concept
                    m = re.search('\((\w+)\)', CUI)
                    if m:
                        CUI = m.group(0).strip('(').strip(')')
                        cui.add(CUI)
                except:
                    pass
                s[node.label] = CUI
    if tree: 
        
        t = str(tree.by_attr(lambda n: n.label + '\n' ))
        
        st.sidebar.markdown("## Tree of child terms")
        st.sidebar.markdown(t)
        
    return s, t
            

#Return images given a query term. First if finds the node in the trees and optionally get all child terms classified under the query term if argument childs is True.
#return two dictionaries of retrieved images and total counts: one for each term with its corresponding images and other with the OR operation for all terms and correspoding aggregated images.
def get_images_by_term(query_term , childs = True):
    images = {}
    images_OR = set()
    df = pd.read_csv('PADCHEST_chest_x_ray_images_labels_160K_01.02.19.csv', header = 0, dtype=str)
    #retrieve term childs
    terms_cuis, _ = get_childs(query_term)
    terms = terms_cuis.keys()
    if not childs: 
        terms = [list(terms)[0]]
        print(terms)
    
    for t in terms:
        mask =  df.LabelsLocalizationsBySentence.str.contains(t, regex=False)
        s = df[mask.fillna(False)].ImageID.values 
        images[t] = list(s)
        images_OR.update(s)
    return len(images_OR), images, {'query': ' OR '.join(terms), 'ImageID': list(images_OR)} 



def get_all_terms():
    labels = {}
    stream = open("trees_code.txt", "r")
    docs = yaml.load_all(stream, Loader=yaml.FullLoader)
    for doc in docs:
        tree_root = DictImporter().import_(doc)
        labels[tree_root.label] = ''
        for pre, _, node in RenderTree(tree_root):
            CUI = ''
            try:
                CUI = node.concept
                m = re.search('\((\w+)\)', CUI)
                if m:
                    CUI = m.group(0).strip('(').strip(')')
            except:
                pass
            labels[node.label] = CUI
    return labels


all_terms = list(get_all_terms().keys())

add_selectbox = st.sidebar.selectbox(
    'Select query term',
    all_terms
)

query_term = add_selectbox

count, dict_by_terms, all = get_images_by_term(query_term)

st.write("# PadChest Explorer" )
st.write("## Query term: " + query_term)

st.write("### Total images:  " ,count)

def get_table_download_link(df):
    """Generates a link allowing the data  to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'

df =  pd.DataFrame(all['ImageID'],columns = ['ImageID'])

#st.sidebar.markdown(get_table_download_link(df), unsafe_allow_html=True)



st.write("### Images by each node term  " )
st.json(dict_by_terms)
st.write("### Images by any node term (OR operation):  " ,count)
st.json(all)




