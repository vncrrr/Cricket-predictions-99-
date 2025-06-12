import streamlit as st
from updatedatascraper import get_lineup
from teamgenerator import generate_multiple_teams
import pandas as pd

st.set_page_config(page_title="Rezon X Fantasy Team Generator")
st.title("📝 Rezon X Fantasy Team Generator")
st.markdown("Generate 20 Dream11-style fantasy teams using AI!")

url = st.text_input("📎 Paste AdvanceCricket Match URL:", 
    "https://advancecricket.com/match/mk-w-vs-hd-w-match-1-bengal-womens-league-2025/82326066")

if st.button("🚀 Generate Fantasy Teams"):
    try:
        players = get_lineup(url)
        fantasy_teams = generate_multiple_teams(players)

        st.subheader("🌐 Sample Team 1:")
        team = fantasy_teams[0]
        for p in team["team"]:
            mark = ""
            if p == team["captain"]:
                mark = " (C)"
            elif p == team["vice_captain"]:
                mark = " (VC)"
            st.write(f"- {p}{mark}")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
