import streamlit as st

st.set_page_config(page_title="Serpent's Hand Generator", page_icon="🐍", layout="centered")

# === SCP-Inspired Terminal CSS with scoped division buttons colors ===
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    html, body, .stApp {
        background-color: #000;
        color: #00ff88;
        font-family: 'Share Tech Mono', monospace;
    }

    h1 {
        font-size: 2.8em;
        text-align: center;
        text-shadow: 0 0 10px #00ff8855, 0 0 20px #00ff8855;
        margin-bottom: 0;
    }

    .stTextInput input {
        background-color: #001a11;
        color: #00ff88;
        border: 1px solid #00ff88;
        border-radius: 6px;
    }

    .stButton>button {
        border-radius: 6px;
        font-weight: bold;
        padding: 0.5em 1.2em;
        transition: all 0.2s ease-in-out;
    }

    /* Target only buttons inside the division buttons container */
    div[data-testid="stVerticalBlock"] > div > div > div > button:nth-child(1) {
        background-color: #1aff66 !important;
        color: black !important;
        border: 1px solid #1aff66 !important;
        box-shadow: 0 0 8px #1aff6655 !important;
    }
    div[data-testid="stVerticalBlock"] > div > div > div > button:nth-child(1):hover {
        background-color: #33ff77 !important;
        box-shadow: 0 0 16px #33ff77aa !important;
    }

    div[data-testid="stVerticalBlock"] > div > div > div > button:nth-child(2) {
        background-color: #00e673 !important;
        color: black !important;
        border: 1px solid #00e673 !important;
        box-shadow: 0 0 8px #00e67355 !important;
    }
    div[data-testid="stVerticalBlock"] > div > div > div > button:nth-child(2):hover {
        background-color: #1aff88 !important;
        box-shadow: 0 0 16px #1aff88aa !important;
    }

    div[data-testid="stVerticalBlock"] > div > div > div > button:nth-child(3) {
        background-color: #009966 !important;
        color: black !important;
        border: 1px solid #009966 !important;
        box-shadow: 0 0 8px #00996655 !important;
    }
    div[data-testid="stVerticalBlock"] > div > div > div > button:nth-child(3):hover {
        background-color: #00cc88 !important;
        box-shadow: 0 0 16px #00cc88aa !important;
    }

    .stCodeBlock {
        border: 1px solid #00ff88;
        background-color: #001a11;
        color: #00ff88;
        border-radius: 6px;
    }

    hr {
        border-color: #00ff88;
    }
</style>
""", unsafe_allow_html=True)

# === Serpent’s Hand Logo + Title ===
st.image("https://i.imgur.com/QA192Wd.png", width=300)
st.title("Serpent's Hand Morph Generator")
st.markdown("---")

# === Session State Defaults ===
for key in ["division", "rank", "name", "generate"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "name" else ""

# === Division Buttons ===
st.subheader("Select Division:")
div_cols = st.columns(3)

with div_cols[0]:
    if st.button("Ψ Combat Ψ", key="division_combat"):
        st.session_state.division = "combat"
        st.session_state.rank = None
        st.session_state.generate = False

with div_cols[1]:
    if st.button("Φ Diplomat Φ", key="division_diplomat"):
        st.session_state.division = "diplomat"
        st.session_state.rank = None
        st.session_state.generate = False

with div_cols[2]:
    if st.button("Σ Librarian Σ", key="division_librarian"):
        st.session_state.division = "librarian"
        st.session_state.rank = "Σ-X | Whisperer"
        st.session_state.generate = False

# === Name Input ===
st.session_state.name = st.text_input("Enter your Roblox Name", st.session_state.name or "").strip()

# === Rank Buttons ===
if st.session_state.division == "combat":
    st.subheader("Select Ψ Rank:")
    cols = st.columns(9)
    for i in range(9):
        with cols[i]:
            if st.button(f"Ψ-{i+1}", key=f"rank_combat_{i+1}"):
                st.session_state.rank = i + 1
                st.session_state.generate = False

elif st.session_state.division == "diplomat":
    st.subheader("Select Φ Rank:")
    d1, d2, d3 = st.columns(3)
    if d1.button("Φ-1", key="rank_diplomat_1"):
        st.session_state.rank = "Φ-1 | Jr. Scribe"
        st.session_state.generate = False
    if d2.button("Φ-2", key="rank_diplomat_2"):
        st.session_state.rank = "Φ-2 | Scribe"
        st.session_state.generate = False
    if d3.button("Φ-3", key="rank_diplomat_3"):
        st.session_state.rank = "Φ-3 | Sr. Scribe"
        st.session_state.generate = False

# === Generate Button ===
if st.button("Generate Command", key="generate_command"):
    st.session_state.generate = True

# === Output Command ===
if st.session_state.generate and st.session_state.name and st.session_state.rank:
    name = st.session_state.name
    rank = st.session_state.rank
    div = st.session_state.division
    morph = ""
    hp = 100
    rank2 = ""

    if div == "combat":
        morphs = ["TSHLR", "TSHPLR", "TSHMR"]
        titles = [
            "INITIATE", "SPELLMARKED", "VEILWALKER",
            "EDGEBEARER", "LOREHUNTER", "MINDSHROUND",
            "PATHBINDER", "SERPENT'S EYE", "GLYPHBLADE"
        ]
        morph = morphs[(rank - 1) // 3]
        hp = 125 if rank > 6 else 100
        rank2 = f"Serpent's Hand | Ψ-{rank} | {titles[rank - 1]}"

    elif div == "diplomat":
        idx = int(rank[2]) - 1
        morph = ["TSHJSC", "TSHSC", "TSHSSC"][idx]
        rank2 = f"Serpent's Hand | Φ-{idx + 1} | {['Jr. Scribe', 'Scribe', 'Sr. Scribe'][idx]}"

    elif div == "librarian":
        morph = "TSHWS"
        rank2 = "Serpent's Hand | Σ-X | Whisperer"

    cmd = (
        f"run permmorph {name} {morph} & "
        f"permmaxhealth {name} {hp} & "
        f"cntag {name} 110 110 110 & "
        f"crtag {name} 110 139 61 & "
        f"rtag {name} {rank2}"
    )

    st.markdown("---")
    st.subheader("✅ Generated Morph Command")
    st.code(cmd, language="bash")

elif st.session_state.generate and not st.session_state.name:
    st.warning("Please enter a name.")
