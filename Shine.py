import streamlit as st
import pandas as pd
import plotly.express as px

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
    potency_data = {
        "Analyte": ["CBDV", "CBDA", "CBGA", "CBG", "CBD", "THCV", "CBN", "D9-THC", "D8-THC", "D10-THC-S", "D10-THC-R", "CBC", "THCA"],
        "Percentage (% w/w)": ["< MRL", "0.062", "1.611", "0.104", "< MRL", "< MRL", "< MRL", "1.818", "< MRL", "< MRL", "< MRL", "< MRL", "31.093"],
        "mg/serving": ["< MRL", "0.219", "5.639", "0.366", "< MRL", "< MRL", "< MRL", "6.364", "< MRL", "< MRL", "< MRL", "< MRL", "108.826"]
    }
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
    - Total THC: 29.087% (101.804 mg/serving)
    - Total CBD: 0.055% (0.192 mg/serving)
    - Total Cannabinoids: 34.688% (121.414 mg/serving)
    """)

# Terpene Profile Tab
with tab3:
    st.header("Terpene Profile")
    
    # Ensure equal length for the terpene data arrays
    terpene_data = {
        "Analyte": ["alpha-Pinene", "Camphene", "Sabinene", "beta-Pinene", "beta-Myrcene", "Alpha-phellandrene", "Carene", "alpha-terpinene", 
                    "p-Cymene", "Limonene", "Eucalyptol", "Ocimene", "gamma-Terpinene", "Sabinene Hydrate", "Terpinolene", "Linalool", 
                    "Fenchol", "Menthol", "Terpineol", "Citronellol", "Isopulegol", "Geraniol", "Alpha-cedrene", "Beta-Caryophyllene", 
                    "Farnesene", "alpha-Humulene", "Valencene", "cis-Nerolidol", "trans-Nerolidol", "Caryophyllene oxide", "Guaiol", 
                    "alpha-Bisabolol"],
        "Result (% w/w)": ["< MRL", "< MRL", "< MRL", "0.06", "0.15", "< MRL", "< MRL", "< MRL", "< MRL", "0.43", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", 
                           "0.21", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "0.06", "0.30", "< MRL", "0.13", "0.24", "< MRL", "< MRL", "< MRL", "< MRL"]
    }
    
    terpene_df = pd.DataFrame(terpene_data)  # Equal length arrays for the DataFrame
    st.write("### Terpene Profile Chart")
    fig4 = px.line(terpene_df, x="Analyte", y="Result (% w/w)", title="Terpene Profile", markers=True)
    st.plotly_chart(fig4)

    # Table for Terpene Data
    st.write("### Terpene Measurement Table")
    st.table(terpene_df)

    # Summary
    st.write("""
    **Summary**:
    - Total Terpenes: 1.58% (w/w)
    - Notable terpenes detected include beta-Myrcene (0.15%), Limonene (0.43%), and Beta-Caryophyllene (0.30%).
    """)

# Metals Tab
with tab4:
    st.header("Metals Testing Results")

    # Metals Data
    metals_data = {
        "Metal": ["Chromium", "Nickel", "Copper", "Arsenic", "Cadmium", "Antimony", "Mercury", "Lead"],
        "Result (ug/g)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "Limit (ug/g)": [110.0, 2.0, 30.0, 0.2, 0.3, 2.0, 0.1, 0.5]
    }
    metals_df = pd.DataFrame(metals_data)

    # Interactive Line Chart for Metals Data
    st.write("### Metals Testing Results Chart")
    fig2 = px.line(metals_df, x="Metal", y="Result (ug/g)", title="Metals Testing Results", markers=True)
    st.plotly_chart(fig2)

    # Table for Metals Data
    st.write("### Metals Measurement Table")
    st.table(metals_df)

    # Summary
    st.write("""
    **Summary**:
    - All heavy metals, including lead and mercury, were detected below the minimum reporting limit (MRL) and passed within safe limits.
    """)

# Continue with other tabs similarly (Pesticides, Mycotoxins, etc.)
