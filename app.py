import streamlit as st
import pandas as pd
import time
import random

st.set_page_config(page_title="Executive Client Intel", layout="wide")

st.title("Executive Intelligence Tracker")
st.write("Monitor strategic shifts, leadership changes, and investments across your client portfolio.")

# Pre-load banking clients into the session state
if 'clients' not in st.session_state:
    st.session_state['clients'] = [
        {"name": "Raymond James", "domain": "Banking & Finance", "handle": "@RaymondJames"},
        {"name": "JPMorgan Chase", "domain": "Banking & Finance", "handle": "@jpmorgan"},
        {"name": "Goldman Sachs", "domain": "Banking & Finance", "handle": "@GoldmanSachs"}
    ]

# Sidebar: Add New Clients
st.sidebar.header("Add a New Client")
with st.sidebar.form("add_client_form"):
    client_name = st.text_input("Client Name (e.g. Morgan Stanley)")
    domain = st.selectbox("Industry Domain", ["Banking & Finance", "Technology", "Healthcare", "Retail", "Other"])
    social_handle = st.text_input("Social/Company Handle")
    submit_button = st.form_submit_button("Add Client")

    if submit_button and client_name:
        st.session_state['clients'].append({
            "name": client_name,
            "domain": domain,
            "handle": social_handle
        })
        st.success(f"Added {client_name} to the tracker!")

# Main Layout: Client Dashboard
df = pd.DataFrame(st.session_state['clients'])
domains = df['domain'].unique()

for d in domains:
    st.header(f"🏛️ {d} Portfolio")
    domain_clients = df[df['domain'] == d]
    
    # Create columns for a cleaner grid layout
    cols = st.columns(3)
    
    for index, row in domain_clients.iterrows():
        col = cols[index % 3]
        with col:
            with st.container(border=True):
                st.subheader(row['name'])
                st.caption(f"Tracking: {row['handle']}")
                
                if st.button("Run Intel Scan", key=f"scan_{row['name']}_{index}"):
                    with st.spinner("Analyzing news, PR feeds, and executive announcements..."):
                        time.sleep(1.5) # Simulate scraping delay
                        
                        # Real 2026 data injected for Raymond James; generic strategic data for others
                        if row['name'] == "Raymond James":
                            updates = [
                                "🏢 M&A Activity: Completed acquisition of Clark Capital Management Group (May 2026).",
                                "👤 Leadership Change: Kristi Higgins appointed as new Head of ETF Strategy.",
                                "💻 Tech Investment: Rolled out proprietary AI operations agent 'Rai' following a $1.1B annual technology investment plan.",
                                "👤 Leadership Change: Jeff Ringdahl took over as President of Raymond James Investment Management."
                            ]
                        else:
                            updates = [
                                f"👤 Leadership Change: {row['name']} announces transition plan for outgoing Chief Information Officer.",
                                f"📉 Restructuring: Market reports indicate {row['name']} is rebalancing headcount in its consumer banking division.",
                                f"💰 Investment: {row['name']} just launched a new $500M venture fund targeting early-stage AI infrastructure.",
                                f"💻 Tech Initiative: {row['name']} CTO announces full migration of legacy mainframes to cloud-native architecture by Q3."
                            ]
                        
                        st.success("High-Priority Intelligence Found")
                        for update in random.sample(updates, 2):
                            st.info(update)
