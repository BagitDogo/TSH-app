import streamlit as st

st.set_page_config(page_title="Serpent's Hand Generator", page_icon="🐍", layout="centered")

# === SCP-Inspired Terminal CSS ===
st.markdown("""
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

    /* Base button style */
    .stButton>button {
        border-radius: 6px;
        font-weight: bold;
        padding: 0.5em 1.2em;
        transition: all 0.2s ease-in-out;
    }

    /* Combat button */
    .stButton>button:has-text("Ψ Combat Ψ") {
        background-color: #1aff66;
        color: black;
        border: 1px solid #1aff66;
        box-shadow: 0 0 8px #1aff6655;
    }
    .stButton>button:has-text("Ψ Combat Ψ"):hover {
        background-color: #33ff77;
        box-shadow: 0 0 16px #33ff77aa;
        transform: scale(1.04);
    }

    /* Diplomat button */
    .stButton>button:has-text("Φ Diplomat Φ") {
        background-color: #00e673;
        color: black;
        border: 1px solid #00e673;
        box-shadow: 0 0 8px #00e67355;
    }
    .stButton>button:has-text("Φ Diplomat Φ"):hover {
        background-color: #1aff88;
        box-shadow: 0 0 16px #1aff88aa;
        transform: scale(1.04);
    }

    /* Librarian button */
    .stButton>button:has-text("Σ Librarian Σ") {
        background-color: #009966;
        color: black;
        border: 1px solid #009966;
        box-shadow: 0 0 8px #00996655;
    }
    .stButton>button:has-text("Σ Librarian Σ"):hover {
        background-color: #00cc88;
        box-shadow: 0 0 16px #00cc88aa;
        transform: scale(1.04);
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
st.image("https://i.imgur.com/QA192Wd.png", width=250)
st.title("Serpent's Hand Morph Generator")
st.markdown("---")

# === Session State ===
if "division" not in st.session_state:
    st.session_state.division = None
if "rank" not in st.session_state:
    st.session_state.rank = None
if "name" not in st.session_state:
    st.session_state.name = ""
if "generate" not in st.session_state:
    st.session_state.generate = False

# === Division Buttons ===
st.subheader("Select Division:")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Ψ Combat Ψ"):
        st.session_state.division = "combat"
        st.session_state.rank = None
        st.session_state.generate = False
with col2:
    if st.button("Φ Diplomat Φ"):
        st.session_state.division = "diplomat"
        st.session_state.rank = None
        st.session_state.generate = False
with col3:
    if st.button("Σ Librarian Σ"):
        st.session_state.division = "librarian"
        st.session_state.rank = "Σ-X | Whisperer"
        st.session_state.generate = False

# === Name Input ===
name_input = st.text_input("Enter your Roblox Name", st.session_state.name)
st.session_state.name = name_input.strip()

# === Rank Buttons ===
if st.session_state.division == "combat":
    st.subheader("Select Ψ Rank:")
    cols = st.columns(9)
    for i in range(9):
        with cols[i]:
            if st.button(f"Ψ-{i+1}"):
                st.session_state.rank = i + 1
                st.session_state.generate = False

elif st.session_state.division == "diplomat":
    st.subheader("Select Φ Rank:")
    d1, d2, d3 = st.columns(3)
    if d1.button("Φ-1"):
        st.session_state.rank = "Φ-1 | Jr. Scribe"
        st.session_state.generate = False
    if d2.button("Φ-2"):
        st.session_state.rank = "Φ-2 | Scribe"
        st.session_state.generate = False
    if d3.button("Φ-3"):
        st.session_state.rank = "Φ-3 | Sr. Scribe"
        st.session_state.generate = False

# === Generate Button ===
if st.button("Generate Command"):
    st.session_state.generate = True

# === Command Output ===
if st.session_state.generate and st.session_state.name and st.session_state.rank:
    div = st.session_state.division
    rank = st.session_state.rank
    name = st.session_state.name
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
