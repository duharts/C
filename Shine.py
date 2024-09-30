import streamlit as st
import pandas as pd
import plotly.express as px

# Function to equalize the lengths of arrays
def equalize_array_lengths(data_dict, fill_value="ND"):
    # Find the maximum length among all arrays in the dictionary
    max_length = max(len(arr) for arr in data_dict.values())
    
    # Pad each array to the maximum length with the fill_value
    for key, arr in data_dict.items():
        if len(arr) < max_length:
            data_dict[key] = arr + [fill_value] * (max_length - len(arr))
    
    return data_dict

# Add the Green Analytics logo to the header and center it
logo_url = "https://www.greenanalyticsllc.com/logo.png"
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='{logo_url}' width='200'>
    </div>
    """, 
    unsafe_allow_html=True
)

# Title and Client Information
st.title("Green Analytics NY, LLC - Certificate of Analysis")
st.subheader("Full Compliance Test")

# Use tabs to organize information for better navigation
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
    "Metals", "Pesticides", "Mycotoxins", "Microbiological Screen", "Moisture & Water Activity", "Filth & Foreign Material"
])

# Client Information Tab
with tab1:
    st.header("Client Information")
    st.write("""
    - **Client Name:** GTI Warwick Medical
    - **Sample Name:** Afternoon Delight #4 Pre-Pack (Select Grind) 7g - andShine (Hybrid)
    - **Sampling Location:** Warwick, New York
    - **Contact Name:** Cole Miller
    - **Contact Email:** cole.miller@gtigrows.com
    - **Sample Subtype:** Flower
    - **License Number:** MM0706M
    - **Package ID:** 20240520AD4-FSG-1
    - **Medical/Adult Use:** Medical
    - **Batch Lot ID:** 20240520AD4-FSG-1
    - **Sampling Date:** 08/14/2024 01:58:00 PM
    - **Batch Size:** 1592
    - **Serving Size (g):** 0.35
    """)

# Potency and Cannabinoid Analysis Tab
with tab2:
    st.header("Potency and Cannabinoid Analysis")
    
    # Potency data (unequal arrays will be fixed with equalize_array_lengths)
    potency_data = {
        "Analyte": ["CBDV", "CBDA", "CBGA", "CBG", "CBD", "THCV", "CBN", "D9-THC", "D8-THC", "D10-THC-S", "D10-THC-R", "CBC", "THCA"],
        "Percentage (% w/w)": ["< MRL", "0.062", "1.611", "0.104", "< MRL", "< MRL", "< MRL", "1.818", "< MRL", "< MRL", "< MRL", "< MRL", "31.093"],
        "mg/serving": ["< MRL", "0.219", "5.639", "0.366", "< MRL", "< MRL", "< MRL", "6.364", "< MRL", "< MRL", "< MRL", "< MRL", "108.826"]
    }
    
    # Equalize array lengths
    potency_data = equalize_array_lengths(potency_data, fill_value="ND")
    potency_df = pd.DataFrame(potency_data)

    # Interactive Line Chart for Potency Results
    st.write("### Potency Analysis Chart")
    fig = px.line(potency_df, x="Analyte", y="Percentage (% w/w)", title="Potency Analysis", markers=True)
    st.plotly_chart(fig)

    # Table for Potency Data
    st.write("### Potency Measurement Table")
    st.table(potency_df)

    # Summary
    st.write("""
    **Summary**:
    - Total THC: 29.087% (101.804 mg/
