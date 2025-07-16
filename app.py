# IPD Case Sheet Generator Web Interface for Dr. Doodley Pet Hospital

import datetime
import streamlit as st

def generate_ipd_case_sheet(data):
    lines = []
    lines.append('Dr. Doodley Pet Hospital, Jayanagar Branch')
    lines.append('In-Patient Department (IPD) Case Sheet')
    lines.append(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y')}")
    lines.append("Doctor-in-Charge: " + ', '.join(data['doctor_in_charge']))
    lines.append("\n")

    lines.append('1. Patient Details')
    for key, value in data['patient_details'].items():
        lines.append(f"{key}: {value}")
    lines.append("\n")

    lines.append('2. Clinical Presentation')
    for key, value in data['clinical_presentation'].items():
        lines.append(f"{key}: {value}")
    lines.append("\n")

    lines.append('3. Vitals')
    for key, value in data['vitals'].items():
        lines.append(f"{key}: {value}")
    lines.append("\n")

    lines.append('4. Diagnostic Tests Done')
    for key, value in data['diagnostic_tests'].items():
        lines.append(f"{key}: {value}")
    lines.append("\n")

    lines.append('5. Provisional Diagnosis')
    lines.append(data['provisional_diagnosis'])
    lines.append('6. Differential Diagnosis')
    lines.append(data['differential_diagnosis'])
    lines.append('7. Final Diagnosis')
    lines.append(data['final_diagnosis'])
    lines.append("\n")

    lines.append('8. Treatment Plan')
    headers = ['Drug/Fluid Name', 'Dosage (mg/ml)', 'Route', 'Frequency', 'Duration']
    lines.append(" | ".join(headers))
    lines.append(" | ".join(['-' * len(h) for h in headers]))
    for item in data['treatment_plan']:
        row = [item['name'], item['dosage'], item['route'], item['frequency'], item['duration']]
        lines.append(" | ".join(row))
    lines.append("\n")

    lines.append('9. Special Procedures / Surgery Done')
    lines.append(data['special_procedures'])
    lines.append("\n")

    lines.append('10. Follow-up Instructions')
    lines.append(data['follow_up'])
    lines.append("\n")

    lines.append('11. Discharge Summary')
    lines.append(data['discharge_summary'])

    return "\n".join(lines)

# Streamlit Web UI
st.title("Dr. Doodley Pet Hospital - IPD Case Sheet Generator")

with st.form("ipd_form"):
    st.header("1. Patient Details")
    patient_details = {
        "Pet name": st.text_input("Pet name"),
        "Age": st.text_input("Age"),
        "Species & breed": st.text_input("Species & breed"),
        "Sex": st.selectbox("Sex", ["Male", "Female"]),
        "Body weight": st.text_input("Body weight"),
        "Owner name & contact": st.text_input("Owner name & contact")
    }

    st.header("2. Clinical Presentation")
    clinical_presentation = {
        "Date of admission": st.date_input("Date of admission"),
        "Chief complaints": st.text_area("Chief complaints"),
        "History": st.text_area("History")
    }

    st.header("3. Vitals")
    vitals = {
        "Temperature": st.text_input("Temperature"),
        "Heart rate": st.text_input("Heart rate"),
        "Respiratory rate": st.text_input("Respiratory rate"),
        "Mucous membrane color": st.text_input("Mucous membrane color"),
        "CRT": st.text_input("CRT"),
        "Hydration status": st.text_input("Hydration status")
    }

    st.header("4. Diagnostic Tests Done")
    diagnostic_tests = {
        "CBC with interpretation": st.text_area("CBC with interpretation"),
        "LFT": st.text_area("LFT"),
        "KFT": st.text_area("KFT"),
        "X-ray findings": st.text_area("X-ray findings"),
        "USG findings": st.text_area("USG findings"),
        "ECG": st.text_area("ECG"),
        "Others": st.text_area("Others")
    }

    st.header("5-7. Diagnosis")
    provisional_diagnosis = st.text_input("Provisional Diagnosis")
    differential_diagnosis = st.text_input("Differential Diagnosis")
    final_diagnosis = st.text_input("Final Diagnosis")

    st.header("8. Treatment Plan")
    treatment_plan = []
    for i in range(1, 6):
        with st.expander(f"Treatment {i}"):
            name = st.text_input(f"Drug/Fluid Name {i}", key=f"name_{i}")
            dosage = st.text_input(f"Dosage (mg/ml) {i}", key=f"dosage_{i}")
            route = st.text_input(f"Route {i}", key=f"route_{i}")
            frequency = st.text_input(f"Frequency {i}", key=f"frequency_{i}")
            duration = st.text_input(f"Duration {i}", key=f"duration_{i}")
            if name:
                treatment_plan.append({"name": name, "dosage": dosage, "route": route, "frequency": frequency, "duration": duration})

    st.header("9. Special Procedures / Surgery Done")
    special_procedures = st.text_area("Special Procedures")

    st.header("10. Follow-up Instructions")
    follow_up = st.text_area("Follow-up Instructions")

    st.header("11. Discharge Summary")
    discharge_summary = st.text_area("Discharge Summary")

    doctor_in_charge = st.multiselect("Doctor-in-Charge", ["Dr. Revathi", "Dr. Suhan H M, MVSc (Surgery & Radiology), F.VMAS, PGDAW"])

    submitted = st.form_submit_button("Generate Case Sheet")

    if submitted:
        result = generate_ipd_case_sheet({
            "patient_details": patient_details,
            "clinical_presentation": clinical_presentation,
            "vitals": vitals,
            "diagnostic_tests": diagnostic_tests,
            "provisional_diagnosis": provisional_diagnosis,
            "differential_diagnosis": differential_diagnosis,
            "final_diagnosis": final_diagnosis,
            "treatment_plan": treatment_plan,
            "special_procedures": special_procedures,
            "follow_up": follow_up,
            "discharge_summary": discharge_summary,
            "doctor_in_charge": doctor_in_charge
        })
        st.download_button("Download Case Sheet", result.encode('utf-8'), file_name="IPD_Case_Sheet.txt")
