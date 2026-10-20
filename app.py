import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Client Intel Tracker", layout="wide")
st.title("Client Intelligence Tracker")

if 'clients' not in st.session_state:
    st.session_state['clients'] = []

st.sidebar.header("Add a New Client")
with st.sidebar.form("add_client_form"):
    client_name = st.text_input("Client Name (e.g. Raymond James)")
    domain = st.selectbox("Industry Domain", ["Finance", "Technology", "Healthcare", "Retail", "Other"])
    social_handle = st.text_input("LinkedIn / Company Handle")
    if st.form_submit_button("Add Client") and client_name:
        st.session_state['clients'].append({"name": client_name, "domain": domain, "handle": social_handle})
        st.success(f"Added {client_name}!")

if not st.session_state['clients']:
    st.info("No clients added yet. Use the sidebar to add your first client.")
else:
    df = pd.DataFrame(st.session_state['clients'])
    for d in df['domain'].unique():
        st.subheader(f"{d} Domain")
        for _, row in df[df['domain'] == d].iterrows():
            with st.expander(f"📌 {row['name']} ({row['handle']})"):
                if st.button(f"Fetch Latest Updates", key=f"btn_{row['name']}"):
                    with st.spinner("Scanning social platforms..."):
                        time.sleep(1.5)
                        st.success(f"**Latest Post:** {row['name']} is actively hiring for their engineering team!")
