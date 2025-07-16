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

    /* ONLY Division Buttons inside #division-buttons container */
    #division-buttons button {
        font-weight: bold;
        color: black;
        border: 1px solid transparent;
        box-shadow: 0 0 8px transparent;
        background-color: #222; /* fallback */
        transition: all 0.2s ease-in-out;
    }
    #division-buttons button:nth-child(1) {
        background-color: #1aff66;
        border-color: #1aff66;
        box-shadow: 0 0 8px #1aff6655;
    }
    #division-buttons button:nth-child(1):hover {
        background-color: #33ff77;
        box-shadow: 0 0 16px #33ff77aa;
    }
    #division-buttons button:nth-child(2) {
        background-color: #00e673;
        border-color: #00e673;
        box-shadow: 0 0 8px #00e67355;
    }
    #division-buttons button:nth-child(2):hover {
        background-color: #1aff88;
        box-shadow: 0 0 16px #1aff88aa;
    }
    #division-buttons button:nth-child(3) {
        background-color: #009966;
        border-color: #009966;
        box-shadow: 0 0 8px #00996655;
    }
    #division-buttons button:nth-child(3):hover {
        background-color: #00cc88;
        box-shadow: 0 0 16px #00cc88aa;
    }

    /* Rank buttons & others keep default Streamlit style */

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

# === Session State Defaults ===
for key in ["division", "rank", "name", "generate"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "name" else ""

# === Division Buttons inside a container with id ===
st.subheader("Select Division:")
with st.container():
    # Add an HTML div with an id to wrap the buttons for styling scope
    st.markdown('<div id="division-buttons">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

# === Name Input ===
st.session_state.name = st.text_input("Enter your Roblox Name", st.session_state.name or "").strip()

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
