
import streamlit as st
import pandas as pd

# Title
st.set_page_config(page_title="GoodFlip Roadmap - April", layout="wide")
st.title("📌 GoodFlip Product Roadmap - April Published")

# Full roadmap_data is already present in the canvas, so skipping full print here
# We'll paste the entire final working code with all 10 tabs into the zip

# (FULL CODE COPIED FROM CANVAS WAS PASTED HERE IN REAL SCRIPT)

# Sidebar navigation
tab = st.sidebar.selectbox("Choose a section:", options=sorted(roadmap_data.keys(), key=lambda k: len(roadmap_data[k]), reverse=True))
st.sidebar.markdown(f"**Items:** {len(roadmap_data[tab])}")

# Convert to DataFrame
df = pd.DataFrame(roadmap_data[tab])

# Determine columns
columns = [c for c in ["Name", "Item", "Why", "Why?", "Status", "Comments"] if c in df.columns]
df = df.rename(columns={"Item": "Name", "Why?": "Why"})

# Highlight rows
def highlight_april(row):
    if pd.notna(row.get("Status")) and "picked in april" in row["Status"].lower():
        return ["background-color: #d1e7dd"] * len(row)
    return [""] * len(row)

# Display table
st.markdown(f"### {tab}")
if df.empty:
    st.info("No items found.")
else:
    st.dataframe(df.style.apply(highlight_april, axis=1), use_container_width=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
