import streamlit as st
from updatedatascraper import get_lineup
from teamgenerator import generate_multiple_teams
import pandas as pd

st.set_page_config(page_title="Rezon X Fantasy Team Generator")

st.title("📝 Rezon X Fantasy Team Generator")
st.markdown("Generate 20 Dream11-style fantasy teams from AdvanceCricket URL")

# Input field for match URL
url = st.text_input("🔗 Paste AdvanceCricket Match URL", 
                    "https://m.cricbuzz.com/live-cricket-scores/106673/aus-vs-rsa-final-icc-world-test-championship-final-2025")

if st.button("🚀 Generate Fantasy Teams"):
    try:
        # Step 1: Scrape the player lineup
        players = get_lineup(url)
        st.success("✅ Lineup successfully fetched!")
        st.write(players)

        # Step 2: Generate fantasy teams
        fantasy_teams = generate_multiple_teams(players)

        # Step 3: Display sample team
        st.subheader("🧠 Sample Team 1:")
        team = fantasy_teams[0]
        for p in team["team"]:
            mark = ""
            if p == team["captain"]:
                mark = " (C)"
            elif p == team["vice_captain"]:
                mark = " (VC)"
            st.write(f"• {p}{mark}")

        # Step 4: Optionally download JSON
        st.download_button("📥 Download All 20 Teams (JSON)", 
                           data=str(fantasy_teams), 
                           file_name="fantasy_teams.json")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
