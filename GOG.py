import streamlit as st

st.set_page_config(page_title="Serpent's Hand Generator", page_icon="🐍", layout="centered")

# Optional logo (upload your own image file or use a URL)
st.image("https://static.wikia.nocookie.net/scp-db/images/e/e7/Serpent%27s_Hand.png/revision/latest/scale-to-width-down/1000?cb=20220430175904", width=150)
st.title("Serpent's Hand Command Generator")
st.markdown("Generate role commands for the **Serpent's Hand** in style.")

div = st.selectbox("Division", ["Ψ Combat", "Φ Diplomat", "Σ Librarian"])

rank = None
rank_display = ""
if div == "Ψ Combat":
    rank = st.selectbox("Rank", list(range(1, 10)))
elif div == "Φ Diplomat":
    rank = st.selectbox("Rank", ["Φ-1 | Jr. Scribe", "Φ-2 | Scribe", "Φ-3 | Sr. Scribe"])
else:
    rank_display = "Σ-X | Whisperer"

name = st.text_input("Name")

if st.button("Generate Command"):
    morph = ""
    hp = 100
    rank2 = ""

    if div == "Ψ Combat":
        r = rank
        morph = ["TSHLR", "TSHPLR", "TSHMR"][(r - 1) // 3]
        hp = 125 if r > 6 else 100
        titles = ["INITIATE", "SPELLMARKED", "VEILWALKER", "EDGEBEARER", "LOREHUNTER", "MINDSHROUND", "PATHBINDER", "SERPENT'S EYE", "GLYPHBLADE"]
        rank2 = f"Serpent's Hand | Ψ-{r} | {titles[r - 1]}"

    elif div == "Φ Diplomat":
        idx = ["Φ-1", "Φ-2", "Φ-3"].index(rank.split(" ")[0])
        morph = ["TSHJSC", "TSHSC", "TSHSSC"][idx]
        titles = ["Jr. Scribe", "Scribe", "Sr. Scribe"]
        rank2 = f"Serpent's Hand | Φ-{idx + 1} | {titles[idx]}"

    else:
        morph = "TSHWS"
        hp = 100
        rank2 = "Serpent's Hand | Σ-X | Whisperer"

    if name.strip() == "":
        st.error("Please enter a name.")
    else:
        cmd = f"""run permmorph {name} {morph} & permmaxhealth {name} {hp} & cntag {name} 110 110 110 & crtag {name} 110 139 61 & rtag {name} {rank2}"""
        st.success("Command Generated:")
        st.code(cmd, language="bash")
