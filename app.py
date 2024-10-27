import os
import pandas as pd
import streamlit as st

#--------------------------------------------------------------------------------------------

#pricing functions

def calc_for_core_service(scope, service):
    if scope == "Top and Bottom" and service == "Same Day Dentures":
        qty_denture = 2
        qty_implant = 0
        qty_discount = 1
        price_denture_low = qty_denture * 595
        price_denture_high = qty_denture * 1595
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Top and Bottom" and service == "Snap In Dentures":
        qty_denture = 2
        qty_implant = 6
        qty_discount = 1
        price_denture_low = qty_denture * 795
        price_denture_high = qty_denture * 795
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Top and Bottom" and service == "All On 4":
        qty_denture = 2
        qty_implant = 0  
        qty_discount = 0
        price_denture_low = qty_denture * 19995
        price_denture_high = qty_denture * 19995
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Top" and service == "Same Day Dentures":
        qty_denture = 1
        qty_implant = 0
        qty_discount = 0
        price_denture_low = qty_denture * 595
        price_denture_high = qty_denture * 1595
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Top" and service == "Snap In Dentures":
        qty_denture = 1
        qty_implant = 4
        qty_discount = 0
        price_denture_low = qty_denture * 795
        price_denture_high = qty_denture * 795
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Top" and service == "All On 4":
        qty_denture = 1
        qty_implant = 0
        qty_discount = 0
        price_denture_low = qty_denture * 19995
        price_denture_high = qty_denture * 19995
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Bottom" and service == "Same Day Dentures":
        qty_denture = 1
        qty_implant = 0
        qty_discount = 0
        price_denture_low = qty_denture * 595
        price_denture_high = qty_denture * 1595
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Bottom" and service == "Snap In Dentures":
        qty_denture = 1
        qty_implant = 2
        qty_discount = 0
        price_denture_low = qty_denture * 795
        price_denture_high = qty_denture * 795
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    elif scope == "Bottom" and service == "All On 4":
        qty_denture = 1
        qty_implant = 0
        qty_discount = 0
        price_denture_low = qty_denture * 19995
        price_denture_high = qty_denture * 19995
        price_implant = qty_implant * 1295
        price_discount = qty_discount * 195
    
    return(qty_denture, qty_implant, qty_discount, price_denture_low, price_denture_high, price_implant, price_discount)

def calc_for_new_patient_premium(service, select_history, select_teeth, qty_dentures):
    if select_history == 'New' and service != "All On 4":
        price_new_extractions = select_teeth * 125
        premium_for_dentures = qty_dentures * 400
    elif select_history == 'New' and service == "All On 4":
        price_new_extractions = select_teeth * 125
        premium_for_dentures = 0
    elif select_history == 'Existing':
        price_new_extractions = 0
        premium_for_dentures = 0
    
    return(price_new_extractions, premium_for_dentures)

#--------------------------------------------------------------------------------------------

#Page

st.title('Texoma Pricing Model')

#sidebar - patient inputs
st.sidebar.title('Patient Inputs')
select_history = st.sidebar.selectbox("Patient History", ['New', 'Existing'])
select_scope = st.sidebar.selectbox("Procedure Scope", ['Top', 'Bottom', 'Top and Bottom'])
select_service = st.sidebar.selectbox("Service Tier", ['Same Day Dentures', 'Snap In Dentures', 'All On 4'])
select_teeth = st.sidebar.number_input("Natural Teeth", min_value=0, max_value=20, step=1, format="%0.1f")

#--------------------------------------------------------------------------------------------

#Patient Outputs

qty_dentures = int(calc_for_core_service(select_scope, select_service)[0])
qty_implants = int(calc_for_core_service(select_scope, select_service)[1])
qty_discounts = int(calc_for_core_service(select_scope, select_service)[2])

price_denture_low = int(calc_for_core_service(select_scope, select_service)[3])
price_denture_high = int(calc_for_core_service(select_scope, select_service)[4])
price_implant = int(calc_for_core_service(select_scope, select_service)[5])
price_discount = int(calc_for_core_service(select_scope, select_service)[6])

price_extractions = int(calc_for_new_patient_premium(select_service, select_history, select_teeth, qty_dentures)[0])
price_denture_premium = int(calc_for_new_patient_premium(select_service, select_history, select_teeth, qty_dentures)[1])

total_gross_low = int(price_denture_low + price_implant + price_extractions + price_denture_premium)
total_gross_high = int(price_denture_high + price_implant + price_extractions + price_denture_premium)

total_net_low = int(total_gross_low - price_discount)
total_net_high = int(total_gross_high - price_discount)

#--------------------------------------------------------------------------------------------

#Visual Summary

st.write('---')
st.write('#### Estimate Summary')
st.write('')

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

col1.write("###### Line Item")
col2.write("###### Quantity")
col3.write("###### Low Estimate")
col4.write("###### High Estimate")

col1.write("Extractions")
col2.write(f"{select_teeth}")
col3.write(f"{price_extractions}")
col4.write(f"{price_extractions}")

col1.write("Dentures")
col2.write(f"{qty_dentures}")
col3.write(f"{price_denture_low}")
col4.write(f"{price_denture_high}")

col1.write("Dentures New Patient Premium")
col2.write(f"###### -")
col3.write(f"{price_denture_premium}")
col4.write(f"{price_denture_premium}")

col1.write("Implants")
col2.write(f"{qty_implants}")
col3.write(f"{price_implant}")
col4.write(f"{price_implant}")

col1.write("###### Total Gross")
col2.write(f"###### -")
col3.write(f"###### {total_gross_low}")
col4.write(f"###### {total_gross_high}")

st.write('')

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

col1.write("Discounts")
col2.write(f"{qty_discounts}")
col3.write(f"{price_discount}")
col4.write(f"{price_discount}")

col1.write("###### Total Net")
col2.write(f"###### -")
col3.write(f"###### {total_net_low}")
col4.write(f"###### {total_net_high}")

