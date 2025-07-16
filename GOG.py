import streamlit as st

# 🔧 Styling
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

# 🐍 Header
st.image("https://upload.wikimedia.org/wikipedia/commons/f/fe/Serpent%E2%80%99s_Hand_logo.png?20220801160440", width=150)
st.title("Serpent's Hand Command Generator")
st.markdown("Select your division and rank, then enter your name to generate a command.")

# 👉 Division buttons
st.subheader("Choose Division")
div = None
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Ψ Combat"):
        div = "combat"
with col2:
    if st.button("Φ Diplomat"):
        div = "diplomat"
with col3:
    if st.button("Σ Librarian"):
        div = "librarian"

if div:
    name = st.text_input("Name")
    rank = None

    # 🧱 Rank buttons
    if div == "combat":
        st.subheader("Choose Rank")
        rcols = st.columns(9)
        for i in range(9):
            with rcols[i]:
                if st.button(f"Ψ-{i+1}"):
                    rank = i + 1

    elif div == "diplomat":
        st.subheader("Choose Rank")
        d1, d2, d3 = st.columns(3)
        if d1.button("Φ-1"):
            rank = "Φ-1 | Jr. Scribe"
        if d2.button("Φ-2"):
            rank = "Φ-2 | Scribe"
        if d3.button("Φ-3"):
            rank = "Φ-3 | Sr. Scribe"

    elif div == "librarian":
        rank = "Σ-X | Whisperer"

    # ✅ Command generation
    if rank and name.strip():
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

        # 🔥 Final output
        cmd = (
            f"run permmorph {name} {morph} & "
            f"permmaxhealth {name} {hp} & "
            f"cntag {name} 110 110 110 & "
            f"crtag {name} 110 139 61 & "
            f"rtag {name} {rank2}"
        )
        st.success("✅ Command Generated:")
        st.code(cmd, language="bash")

    elif not name.strip():
        st.warning("Please enter a name.")
