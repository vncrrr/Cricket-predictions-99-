import streamlit as st
from updatedatascraper import get_lineup
from teamgenerator import generate_multiple_teams, export_teams_to_csv
import pandas as pd

st.set_page_config(page_title="Rezon X Fantasy Generator", layout="centered")
st.title("🏏 Rezon X Fantasy Team Generator")
st.markdown("Generate 20 Dream11-style fantasy teams based on real data!")

# Input for AdvanceCricket match URL
url = st.text_input("🔗 Paste AdvanceCricket Match URL:", 
    "https://advancecricket.com/match/mk-w-vs-hd-w-match-1-bengal-womens-league-2025/82326066")

# Generate Button
if st.button("🚀 Generate Fantasy Teams"):
    try:
        # 1. Scrape player data
        players = get_lineup(url)

        # 2. Generate 20 fantasy teams
        fantasy_teams = generate_multiple_teams(players, num_teams=20)

        # 3. Show first team sample
        st.subheader("🔮 Sample Team 1:")
        team = fantasy_teams[0]
        for p in team["team"]:
            tag = ""
            if team["captain"] in p:
                tag = " 🏅 (Captain)"
            elif team["vice_captain"] in p:
                tag = " 🥈 (Vice-Captain)"
            st.markdown(f"- {p}{tag}")

        st.markdown(f"💰 **Total Credit**: {team['total_credit']}/100")
        st.markdown(f"🟢 **Team Split**: {team['split']}")

        # 4. Export all 20 teams to CSV
        export_teams_to_csv(fantasy_teams, "fantasy_teams.csv")
        df = pd.read_csv("fantasy_teams.csv")

        # 5. Download button
        st.download_button(
            label="📥 Download All 20 Teams (CSV)",
            data=df.to_csv(index=False),
            file_name="fantasy_teams.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Something went wrong:\n{e}")