
import streamlit as st
import pandas as pd

# Title
st.set_page_config(page_title="GoodFlip Roadmap - April", layout="wide")
st.title("📌 GoodFlip Product Roadmap - April Published")

# Data from 10 GF tabs
roadmap_data = {
    "GF April Publish": [
        {"Item": "Liver forever (lipaglyn)", "Why?": "PSP", "Status": "Picked in april", "Comments": None},
        {"Item": "Niva Bupa Launch with LSQ integration", "Why?": "Visit integration", "Status": "Picked in april", "Comments": None},
        {"Item": "New SDK with Tracky BCA integrated and working (tech debt from Coding studio)", "Why?": "Visit integration", "Status": "Picked in april", "Comments": None},
        {"Item": "Viemax", "Why?": "PSP", "Status": "Picked in april", "Comments": None},
        {"Item": "Tracky CGM Integration", "Why?": "Revenue", "Status": "Picked in april", "Comments": None},
        {"Item": "Migration of old users to GoodFlip", "Why?": "CX", "Status": "Picked in april", "Comments": None},
        {"Item": "User registration API performance (takes 7-8 seconds as of today)", "Why?": "Affects funnels of acquisition", "Status": "Picked in april", "Comments": None},
        {"Item": "LSQ intergrations for Pre journey - activity pushing ", "Why?": "Sales enablement", "Status": "Picked in april", "Comments": None},
        {"Item": "Coach portal - editing questionnaire so that goals created (addition and deletion from coach side from portal side) - super imp", "Why?": "Ops enablement", "Status": "Picked in april", "Comments": None},
        {"Item": "Coach portal - patient history and profile as a patient profile - creat a form. Instead of part of each assessment - important", "Why?": "Ops enablement", "Status": "Picked in april. Not sure of delivery", "Comments": None},
        {"Item": "MedEco - Remote care enablement ( for referred patients --> show Achieve) + close referral flow?", "Why?": "Dr Channel - Remote Care", "Status": "Picked in april", "Comments": None},
        {"Item": "AI med report-- > in range and out of range value problems --> split the prompt into digitizing and then fixing the range (celebal can do)", "Why?": "CX", "Status": "Picked in april", "Comments": None},
        {"Item": "Post purchase journey MoEngage Events", "Why?": "Imp for adherence", "Status": "Picked in april", "Comments": None},
        {"Item": "Whatsapp Comms post purchase - score notifications when coach changes score", "Why?": "CX", "Status": "Picked in april", "Comments": None},
        {"Item": "Messaging on app for UX - in app show limit of lab report to 30 MB on records screen", "Why?": "CX", "Status": "Picked in april", "Comments": None},
        {"Item": "Error handling of AI med report on UI - shows \"error detected\"", "Why?": None, "Status": "Picked in april", "Comments": None},
        {"Item": "Change app name GoodFlip(Mytatva) so that searching MyT shows GF", "Why?": "CX", "Status": "Picked in april", "Comments": None},
        {"Item": "Logging mechanisms of APIs to track user journey (last 9 integration for all critical APIs)", "Why?": "Tech debt", "Status": "Picked in april", "Comments": None},
        {"Item": "List of bugs reported by Sahana", "Why?": "CX", "Status": "Picked in april", "Comments": None},
        {"Item": "Change the slot of coaches to 30 mins instead of 1 hour(PSP slots don’t need so much)", "Why?": "Ops enablement", "Status": "Picked in april", "Comments": None}
    ],
    "GF From Ops": [
        {"Name": "Coach portal - editing questionnaire so that goals created (addition and deletion from coach side from portal side) - super imp", "Why": "During assessment if coaches feel goals need to be added, important to add this to be able to have better scores", "Status": "Planned for April", "Comments": None},
        {"Name": "Coach portal - patient history and profile as a patient profile - creat a form. Instead of part of each assessment - important", "Why": "Old assessment form questions have been translated into Custom goals. Some questions are history based. Important to have these separated from custom goals", "Status": "Planned for April - likely to slip to may", "Comments": None},
        {"Name": "Unicommerce automation", "Why": "Automating the punching process", "Status": "Planned for April - likely to slip to may", "Comments": None}
    ],
    "GF tech debt": [
        {"Item": "Logging mechanisms of APIs to track user journey (last 9 integration for all critical APIs)", "Why": "Debugging issues is not possible without this", "Status": None, "Comments": None},
        {"Item": "Group Chat tech debt (yet to figure answer for inefficient use)", "Why": None, "Status": None, "Comments": None},
        {"Item": "AI med report --> no standard unit. Conversion of units vs showing in range", "Why": None, "Status": None, "Comments": None},
        {"Item": "AI med report-- > in range and out of range value problems --> split the prompt into digitizing and then fixing the range (celebal can do)", "Why": "Important for experience. Also for scoring", "Status": None, "Comments": None},
        {"Item": "Graphs on diet and exercise are not correct for months , 6 months --> identify and fix logic for diet and exercise.", "Why": None, "Status": None, "Comments": None},
        {"Item": "User registration API performance (takes 7-8 seconds as of today)", "Why": "Can affect marketing funnels", "Status": None, "Comments": None},
        {"Item": "Front end component loading enhancement (huge images -- change to a diff format called webp - do this across the whole app). This affects loading times on screens", "Why": None, "Status": None, "Comments": None},
        {"Item": "Shopify orders to flow into our system", "Why": None, "Status": None, "Comments": None}
    ],
    "GF PSP": [
        {"Item": "Niva Bupa Launch with LSQ integration", "Why?": None, "Status": "Picked in April", "Comments": None},
        {"Item": "Viemax", "Why?": None, "Status": "Picked in April", "Comments": None},
        {"Item": "Liver forever (lipaglyn)", "Why?": None, "Status": "Picked in April", "Comments": None},
        {"Item": "Prerak 90 day journey", "Why?": None, "Status": None, "Comments": None},
        {"Item": "Bilypsa 90 day journey", "Why?": None, "Status": None, "Comments": None},
        {"Item": "Akumentis journey for future (see data to see if necessary)", "Why?": None, "Status": None, "Comments": None},
        {"Item": "Endometriosis", "Why?": None, "Status": None, "Comments": None},
        {"Item": "Migraine", "Why?": None, "Status": None, "Comments": None}
    ],
    "GF From Marketing": [
        {"Item": "Push Notifications for Android also not working", "Why?": None, "Status": None, "Comments": None},
        {"Item": "Push Notifications for IOS not activated", "Why?": None, "Status": None, "Comments": "P0"},
        {"Item": "Current Paid Patients Attribute not present", "Why?": None, "Status": None, "Comments": None},
        {"Item": "In-app campaigns not working", "Why?": None, "Status": None, "Comments": "P1"},
        {"Item": "LSQ Integration", "Why?": None, "Status": "Picked in Apr", "Comments": "P0"},
        {"Item": "Referral program", "Why?": None, "Status": None, "Comments": "P1"},
        {"Item": "Non disease marked Metabolic Score to have a free journey", "Why?": None, "Status": None, "Comments": None}
    ],
    "GF from Sales": [
        {"Item": "Remote care visibility to Dr. with achieve", "Why?": None, "Status": None, "Comments": None},
        {"Item": "Custom plan creations at backend with customisability", "Why?": None, "Status": "Delivered in April", "Comments": None},
        {"Item": "MedEco - Remote care enablement ( for referred patients --> show Achieve) + close referral flow?", "Why?": None, "Status": None, "Comments": None}
    ],
    "GF Innovation": [
        {"Item": "3 D image scanning", "Why?": None, "Status": None, "Comments": None}
    ],
    "GF repetitive bugs": [],
    "GF Finance": []
}

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
