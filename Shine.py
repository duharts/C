import streamlit as st
import pandas as pd
import plotly.express as px

# Function to equalize the lengths of arrays and replace non-numerical values with 0 for charts
def equalize_array_lengths(data_dict, fill_value="ND", numerical_only=False):
    max_length = max(len(arr) for arr in data_dict.values())
    for key, arr in data_dict.items():
        if len(arr) < max_length:
            data_dict[key] = arr + [fill_value] * (max_length - len(arr))
        if numerical_only:
            # Replace non-numerical values with 0 for plotting
            data_dict[key] = [0 if isinstance(x, str) and not x.replace('.', '', 1).isdigit() else x for x in arr]
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
    
    # Potency data
    potency_data = {
        "Analyte": ["CBDV", "CBDA", "CBGA", "CBG", "CBD", "THCV", "CBN", "D9-THC", "D8-THC", "D10-THC-S", "D10-THC-R", "CBC", "THCA"],
        "Percentage (% w/w)": ["< MRL", "0.062", "1.611", "0.104", "< MRL", "< MRL", "< MRL", "1.818", "< MRL", "< MRL", "< MRL", "< MRL", "31.093"],
        "mg/serving": ["< MRL", "0.219", "5.639", "0.366", "< MRL", "< MRL", "< MRL", "6.364", "< MRL", "< MRL", "< MRL", "< MRL", "108.826"]
    }

    # Equalize array lengths and replace non-numerical values with 0 for plotting
    potency_chart_data = equalize_array_lengths(potency_data.copy(), numerical_only=True)
    potency_df = pd.DataFrame(potency_data)
    potency_chart_df = pd.DataFrame(potency_chart_data)

    # Convert chart data to numeric, setting invalid values to 0
    potency_chart_df["Percentage (% w/w)"] = pd.to_numeric(potency_chart_df["Percentage (% w/w)"], errors='coerce').fillna(0)

    # Interactive Line Chart for Potency Results
    st.write("### Potency Analysis Chart")
    fig = px.line(potency_chart_df, x="Analyte", y="Percentage (% w/w)", title="Potency Analysis", markers=True)
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
    
    # Terpene data
    terpene_data = {
        "Analyte": ["alpha-Pinene", "Camphene", "Sabinene", "beta-Pinene", "beta-Myrcene", "Alpha-phellandrene", "Carene", "alpha-terpinene", 
                    "p-Cymene", "Limonene", "Eucalyptol", "Ocimene", "gamma-Terpinene", "Sabinene Hydrate", "Terpinolene", "Linalool", 
                    "Fenchol", "Menthol", "Terpineol", "Citronellol", "Isopulegol", "Geraniol", "Alpha-cedrene", "Beta-Caryophyllene", 
                    "Farnesene", "alpha-Humulene", "Valencene", "cis-Nerolidol", "trans-Nerolidol", "Caryophyllene oxide", "Guaiol", 
                    "alpha-Bisabolol"],
        "Result (% w/w)": ["< MRL", "< MRL", "< MRL", "0.06", "0.15", "< MRL", "< MRL", "< MRL", "< MRL", "0.43", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", 
                           "0.21", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "0.06", "0.30", "< MRL", "0.13", "0.24", "< MRL", "< MRL", "< MRL", "< MRL"]
    }

    # Equalize array lengths and replace non-numerical values with 0 for plotting
    terpene_chart_data = equalize_array_lengths(terpene_data.copy(), numerical_only=True)
    terpene_df = pd.DataFrame(terpene_data)
    terpene_chart_df = pd.DataFrame(terpene_chart_data)

    # Convert chart data to numeric, setting invalid values to 0
    terpene_chart_df["Result (% w/w)"] = pd.to_numeric(terpene_chart_df["Result (% w/w)"], errors='coerce').fillna(0)

    # Interactive Line Chart for Terpenes
    st.write("### Terpene Profile Chart")
    fig4 = px.line(terpene_chart_df, x="Analyte", y="Result (% w/w)", title="Terpene Profile", markers=True)
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

       # Equalize array lengths and replace non-numerical values with 0 for plotting
    metals_chart_data = equalize_array_lengths(metals_data.copy(), numerical_only=True)
    metals_df = pd.DataFrame(metals_data)
    metals_chart_df = pd.DataFrame(metals_chart_data)

    # Convert chart data to numeric, setting invalid values to 0
    metals_chart_df["Result (ug/g)"] = pd.to_numeric(metals_chart_df["Result (ug/g)"], errors='coerce').fillna(0)

    # Interactive Line Chart for Metals Data
    st.write("### Metals Testing Results Chart")
    fig2 = px.line(metals_chart_df, x="Metal", y="Result (ug/g)", title="Metals Testing Results", markers=True)
    st.plotly_chart(fig2)

    # Table for Metals Data
    st.write("### Metals Measurement Table")
    st.table(metals_df)

    # Summary
    st.write("""
    **Summary**:
    - All heavy metals, including lead and mercury, were detected below the minimum reporting limit (MRL) and passed within safe limits.
    """)

# Pesticides Tab
with tab5:
    st.header("Pesticides Testing Results")

    # Pesticides Data
    pesticides_data = {
        "Analyte": ["Abamectin", "Acephate", "Acequinocyl", "Acetamiprid", "Aldicarb", "Azadirachtin", "Azoxystrobin"],
        "Result (ug/g)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "Limit (ug/g)": [0.50, 0.40, 2.00, 0.20, 0.40, 1.00, 0.20]
    }

    # Equalize array lengths and replace non-numerical values with 0 for plotting
    pesticides_chart_data = equalize_array_lengths(pesticides_data.copy(), numerical_only=True)
    pesticides_df = pd.DataFrame(pesticides_data)
    pesticides_chart_df = pd.DataFrame(pesticides_chart_data)

    # Convert chart data to numeric, setting invalid values to 0
    pesticides_chart_df["Result (ug/g)"] = pd.to_numeric(pesticides_chart_df["Result (ug/g)"], errors='coerce').fillna(0)

    # Pesticides Testing Chart
    st.write("### Pesticides Testing Results Chart")
    fig8 = px.line(pesticides_chart_df, x="Analyte", y="Result (ug/g)", title="Pesticides Testing Results", markers=True)
    st.plotly_chart(fig8)

    # Table for Pesticides Data
    st.write("### Pesticides Measurement Table")
    st.table(pesticides_df)

    # Summary
    st.write("""
    **Summary**:
    - All tested pesticides passed, with no detectable levels above the minimum reporting limit.
    """)

# Mycotoxins Tab
with tab6:
    st.header("Mycotoxins Testing Results")

    # Mycotoxins Data
    mycotoxins_data = {
        "Analyte": ["Ochratoxin", "Total Aflatoxins"],
        "Result (ug/g)": ["< MRL", "< MRL"],
        "Limit (ug/g)": [0.02, 0.02]
    }

    # Equalize array lengths and replace non-numerical values with 0 for plotting
    mycotoxins_chart_data = equalize_array_lengths(mycotoxins_data.copy(), numerical_only=True)
    mycotoxins_df = pd.DataFrame(mycotoxins_data)
    mycotoxins_chart_df = pd.DataFrame(mycotoxins_chart_data)

    # Convert chart data to numeric, setting invalid values to 0
    mycotoxins_chart_df["Result (ug/g)"] = pd.to_numeric(mycotoxins_chart_df["Result (ug/g)"], errors='coerce').fillna(0)

    # Mycotoxins Testing Chart
    st.write("### Mycotoxins Testing Results Chart")
    fig9 = px.line(mycotoxins_chart_df, x="Analyte", y="Result (ug/g)", title="Mycotoxins Testing Results", markers=True)
    st.plotly_chart(fig9)

    # Table for Mycotoxins Data
    st.write("### Mycotoxins Measurement Table")
    st.table(mycotoxins_df)

    # Summary
    st.write("""
    **Summary**:
    - The mycotoxins test passed, with no detectable levels of harmful mycotoxins like ochratoxin or aflatoxins.
    """)

# Microbiological Screen Tab
with tab7:
    st.header("Microbiological Screen Results")

    # Microbiological Data
    microbial_data = {
        "Analyte": ["Total Aerobic Bacteria", "Total Yeast & Mold", "Salmonella spp", "Shiga toxin-producing E. coli", "Aspergillus"],
        "Result (CFU/g)": ["< MRL", "< MRL", "Absent", "Absent", "Absent"],
        "Limit (CFU/g)": ["100000", "10000", "Absent", "Absent", "Absent"]
    }

    # Equalize array lengths and replace non-numerical values with 0 for plotting
    microbial_chart_data = equalize_array_lengths(microbial_data.copy(), numerical_only=True)
    microbial_df = pd.DataFrame(microbial_data)
    microbial_chart_df = pd.DataFrame(microbial_chart_data)

    # Convert chart data to numeric, setting invalid values to 0
    microbial_chart_df["Result (CFU/g)"] = pd.to_numeric(microbial_chart_df["Result (CFU/g)"], errors='coerce').fillna(0)

    # Microbiological Testing Chart
    st.write("### Microbiological Screen Testing Results Chart")
    fig10 = px.line(microbial_chart_df, x="Analyte", y="Result (CFU/g)", title="Microbiological Screen Results", markers=True)
    st.plotly_chart(fig10)

    # Table for Microbiological Data
    st.write("### Microbiological Measurement Table")
    st.table(microbial_df)

    # Summary
    st.write("""
    **Summary**:
    - All microbial tests passed, including tests for total aerobic bacteria, yeast, mold, and pathogenic microbes like Salmonella and E. coli.
    """)

# Moisture & Water Activity Tab
with tab8:
    st.header("Moisture & Water Activity Results")

    # Moisture data
    moisture_data = {
        "Analyte": ["Moisture", "Water Activity"],
        "Result": ["10.3%", "0.57"],
        "Limit": ["15%", "0.65"]
    }

    # Equalize array lengths and replace non-numerical values with 0 for plotting
    moisture_chart_data = equalize_array_lengths(moisture_data.copy(), numerical_only=True)
    moisture_df = pd.DataFrame(moisture_data)
    moisture_chart_df = pd.DataFrame(moisture_chart_data)

    # Convert chart data to numeric, removing percentage symbol and invalid values to 0
    moisture_chart_df["Result"] = pd.to_numeric(moisture_chart_df["Result"].str.replace('%', ''), errors='coerce').fillna(0)

    # Moisture & Water Activity Chart
    st.write("### Moisture & Water Activity Results Chart")
    fig11 = px.line(moisture_chart_df, x="Analyte", y="Result", title="Moisture & Water Activity Results", markers=True)
    st.plotly_chart(fig11)

    # Table for Moisture & Water Activity Data
    st.write("### Moisture & Water Activity Measurement Table")
    st.table(moisture_df)

    # Summary
    st.write("""
    **Summary**:
    - The sample's moisture content (10.3%) and water activity (0.57 aw) are within acceptable limits, indicating product freshness and stability.
    """)

# Filth & Foreign Material Tab
with tab9:
    st.header("Filth & Foreign Material Results")

    # Filth & Foreign Material Data
    filth_data = {
        "Analyte": ["Foreign Material (other)", "Foreign Material (stems)", "Mammalian Excreta"],
        "Result": ["ND", "ND", "ND"],
        "Limit": ["2%", "5%", "1 mg/lb"]
    }

    # Equalize array lengths and replace non-numerical values with 0 for plotting
    filth_chart_data = equalize_array_lengths(filth_data.copy(), numerical_only=True)
    filth_df = pd.DataFrame(filth_data)
    filth_chart_df = pd.DataFrame(filth_chart_data)

    # Filth & Foreign Material Chart
    st.write("### Filth & Foreign Material Results Chart")
    fig12 = px.line(filth_chart_df, x="Analyte", y="Result", title="Filth & Foreign Material Results", markers=True)
    st.plotly_chart(fig12)

    # Table for Filth & Foreign Material Data
    st.write("### Filth & Foreign Material Measurement Table")
    st.table(filth_df)

    # Summary
    st.write("""
    **Summary**:
    - No filth or foreign material, including stems or mammalian excreta, was detected in the sample.
    """)

# Footer with a link to the original report
st.write("**Analysis Date:** 08/19/2024")
st.write("**Lab:** Green Analytics NY, LLC, Pearl River, NY")

# Link to the original report
st.markdown("""
    **[View Original Report](https://www.greenanalyticsllc.com/reports/20240814-GTIWMed-003.pdf)**
""")
