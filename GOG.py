import streamlit as st

# Page config and style
st.set_page_config(page_title="Serpent's Hand Generator", page_icon="🐍", layout="centered")
st.markdown("""
    <style>
        .stApp { background-color: #0e1117; }
        h1, h2, h3 { color: #58a6ff; text-align: center; }
        .stTextInput>div>div>input {
            background-color: #161b22;
            color: white;
            border: 1px solid #30363d;
        }
        .stButton>button {
            background-color: #238636;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            margin: 4px;
        }
    </style>
""", unsafe_allow_html=True)

# 🐍 Logo and title
st.image("https://upload.wikimedia.org/wikipedia/commons/f/fe/Serpent%E2%80%99s_Hand_logo.png?20220801160440", width=150)
st.title("Serpent's Hand Command Generator")
st.markdown("Select your division and rank, then enter your name to generate a command.")

# Initialize session state
if "division" not in st.session_state:
    st.session_state.division = None
if "rank" not in st.session_state:
    st.session_state.rank = None
if "name" not in st.session_state:
    st.session_state.name = ""
if "generate" not in st.session_state:
    st.session_state.generate = False

# Division buttons
st.subheader("Choose Division")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Ψ Combat"):
        st.session_state.division = "combat"
        st.session_state.rank = None
        st.session_state.generate = False
with col2:
    if st.button("Φ Diplomat"):
        st.session_state.division = "diplomat"
        st.session_state.rank = None
        st.session_state.generate = False
with col3:
    if st.button("Σ Librarian"):
        st.session_state.division = "librarian"
        st.session_state.rank = "Σ-X | Whisperer"
        st.session_state.generate = False

# Name input
name_input = st.text_input("Name", st.session_state.name)
st.session_state.name = name_input.strip()

# Rank buttons
if st.session_state.division == "combat":
    st.subheader("Choose Rank")
    cols = st.columns(9)
    for i in range(9):
        with cols[i]:
            if st.button(f"Ψ-{i+1}"):
                st.session_state.rank = i + 1
                st.session_state.generate = False

elif st.session_state.division == "diplomat":
    st.subheader("Choose Rank")
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

# Generate button
if st.button("Generate Command"):
    st.session_state.generate = True

# Command output
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
    st.success("✅ Command Generated:")
    st.code(cmd, language="bash")
elif st.session_state.generate and not st.session_state.name:
    st.warning("Please enter a name.")
