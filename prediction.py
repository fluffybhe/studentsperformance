# dashboard.py
import streamlit as st 
import pandas as pd
import plotly.graph_objects as go

# Set pink-themed layout
st.set_page_config(layout="wide", page_title="💗 Jaya Jaya Institute Students Performance", page_icon="🌸")

# Apply custom CSS
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(to right, #ffe6f0, #ffe6fa);
            color: #cc0066;
        }
        .main {
            background-color: #fff0f5;
        }
        .stSelectbox > div {
            background-color: #ffccdd !important;
            color: #cc0066 !important;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #ff99cc;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 24px;
        }
        .block-container {
            padding: 2rem 3rem;
        }
        h1, h2, h3 {
            color: #ff3399;
        }
    </style>
""", unsafe_allow_html=True)

# Load data
data = pd.read_csv("datafinal.csv", delimiter=",")
data_0 = data[data['Status'] == 0]
data_1 = data[data['Status'] == 1]
data_2 = data[data['Status'] == 2]

# Map course
category_mapping = {
    33: 'Biofuel Production Technologies', 171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)', 9003: 'Agronomy',
    9070: 'Communication Design', 9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering', 9130: 'Equinculture',
    9147: 'Management', 9238: 'Social Service',
    9254: 'Tourism', 9500: 'Nursing',
    9556: 'Oral Hygiene', 9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication', 9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}
data['Course_Label'] = data['Course'].replace(category_mapping)

# Sidebar
st.sidebar.markdown("## 🎀 Filter Here")
status_list = ['All', 'Dropout', 'Enrolled', 'Graduated']
status = st.sidebar.selectbox("🎓 Select Status", status_list)

courses = ["All"] + sorted(data['Course_Label'].unique())
course = st.sidebar.selectbox("📘 Select Course", courses)

gender_list = ['All', 'Male', 'Female']
gender = st.sidebar.selectbox("👩‍🎓 Gender", gender_list)

time_list = ['All', 'Daytime', 'Evening']
time = st.sidebar.selectbox("🕐 Attendance Time", time_list)

# Filter
kelas = data.copy()
if status != 'All':
    if status == 'Dropout':
        kelas = kelas[kelas['Status'] == 0]
    elif status == 'Enrolled':
        kelas = kelas[kelas['Status'] == 1]
    elif status == 'Graduated':
        kelas = kelas[kelas['Status'] == 2]

if course != 'All':
    kelas = kelas[kelas['Course_Label'] == course]
if gender != 'All':
    kelas = kelas[kelas['Gender'] == (1 if gender == 'Male' else 0)]
if time != 'All':
    kelas = kelas[kelas['Daytime_evening_attendance'] == (1 if time == 'Daytime' else 0)]

# Title
st.markdown("<h1 style='text-align: center;'>🌸 Jaya Jaya Institute : Students Performance 💫</h1>", unsafe_allow_html=True)

# Metric Cards
col1, col2, col3 = st.columns(3)
total = len(kelas)
do = len(kelas[kelas['Status'] == 0])
enrolled = len(kelas[kelas['Status'] == 1])
graduated = len(kelas[kelas['Status'] == 2])

with col1:
    st.metric("💔 Dropped Out", f"{do}", delta=f"{(do/total)*100:.2f}%" if total else "0%")
with col2:
    st.metric("📚 Enrolled", f"{enrolled}", delta=f"{(enrolled/total)*100:.2f}%" if total else "0%")
with col3:
    st.metric("🎓 Graduated", f"{graduated}", delta=f"{(graduated/total)*100:.2f}%" if total else "0%")

st.markdown("---")

# Charts
col4, col5 = st.columns(2)
with col4:
    st.subheader("💖 Scholarship Holders by Status")
    chart_data = kelas.groupby('Status')['Scholarship_holder'].sum()
    if not chart_data.empty:
        fig = go.Figure(go.Bar(
            x=['Dropout', 'Enrolled', 'Graduated'],
            y=chart_data,
            marker_color=['#ff99cc', '#ff66b2', '#ff3399']
        ))
        fig.update_layout(plot_bgcolor='#fff0f5', paper_bgcolor='#fff0f5')
        st.plotly_chart(fig)

with col5:
    st.subheader("📊 Average Grades (Semesters)")
    avg1 = kelas.groupby('Status')['Curricular_units_1st_sem_grade'].mean()
    avg2 = kelas.groupby('Status')['Curricular_units_2nd_sem_grade'].mean()
    fig = go.Figure(data=[
        go.Bar(name='1st Semester', x=['Dropout', 'Enrolled', 'Graduated'], y=avg1, marker_color='#ff66cc'),
        go.Bar(name='2nd Semester', x=['Dropout', 'Enrolled', 'Graduated'], y=avg2, marker_color='#ff99dd')
    ])
    fig.update_layout(barmode='group', plot_bgcolor='#fff0f5', paper_bgcolor='#fff0f5')
    st.plotly_chart(fig)


# Dropout by Course Chart
with col5:
    st.subheader("📊 Dropout by Course")
    dropout_by_course = kelas[kelas['Status'] == 0].groupby('Course_Label').size()
    dropout_by_course = dropout_by_course.sort_values(ascending=False).head(10)  # Top 10 courses
    fig_course = go.Figure(go.Bar(
        x=dropout_by_course.index,
        y=dropout_by_course.values,
        marker_color='#ff66b2'
    ))
    fig_course.update_layout(
        title="Dropout by Course",
        xaxis_title="Course",
        yaxis_title="Number of Dropouts",
        plot_bgcolor='#fff0f5',
        paper_bgcolor='#fff0f5'
    )
    st.plotly_chart(fig_course)

# Age at Enrollment Distribution Chart
with col4:
    st.subheader("📊 Age at Enrollment Distribution")
    # Menghitung usia minimum, rata-rata, dan maksimum
    min_age = kelas['Age_at_enrollment'].min()
    avg_age = kelas['Age_at_enrollment'].mean()
    max_age = kelas['Age_at_enrollment'].max()

    # Menampilkan metrik
    st.markdown(f"**Minimum Age**: {min_age}")
    st.markdown(f"**Average Age**: {avg_age:.2f}")
    st.markdown(f"**Maximum Age**: {max_age}")

    # Membuat histogram untuk distribusi usia
    fig_age = go.Figure(go.Histogram(
        x=kelas['Age_at_enrollment'],
        nbinsx=20,  # Menentukan jumlah bin untuk histogram
        marker_color='#ff99cc'
    ))
    fig_age.update_layout(
        title="Age Distribution at Enrollment",
        xaxis_title="Age at Enrollment",
        yaxis_title="Number of Students",
        plot_bgcolor='#fff0f5',
        paper_bgcolor='#fff0f5'
    )
    st.plotly_chart(fig_age)


# Educational Special Needs Distribution Chart
with col5:
    st.subheader("📊 Educational Special Needs Distribution")
    special_needs_dist = kelas['Educational_special_needs'].value_counts()

    # Membuat Pie Chart
    fig_special_needs = go.Figure(go.Pie(
        labels=['No Special Needs', 'With Special Needs'],
        values=special_needs_dist,
        marker_colors=['#ffcc99', '#ff66b2']
    ))
    fig_special_needs.update_layout(
        title="Distribution of Educational Special Needs",
        plot_bgcolor='#fff0f5',
        paper_bgcolor='#fff0f5'
    )
    st.plotly_chart(fig_special_needs)

# Tuition Fees Up to Date Distribution Chart
with col4:
    st.subheader("📊 Tuition Fees Up to Date Distribution")
    tuition_fees_dist = kelas['Tuition_fees_up_to_date'].value_counts()

    # Membuat Pie Chart
    fig_tuition_fees = go.Figure(go.Pie(
        labels=['Not Paid', 'Paid'],
        values=tuition_fees_dist,
        marker_colors=['#ffcc99', '#ff3399']
    ))
    fig_tuition_fees.update_layout(
        title="Distribution of Tuition Fees Up to Date",
        plot_bgcolor='#fff0f5',
        paper_bgcolor='#fff0f5'
    )
    st.plotly_chart(fig_tuition_fees)

# Debtor Distribution Chart
with col4:
    st.subheader("📊 Debtor Distribution")
    debtor_dist = kelas['Debtor'].value_counts()

    # Membuat Pie Chart
    fig_debtor = go.Figure(go.Pie(
        labels=['Non-Debtor', 'Debtor'],
        values=debtor_dist,
        marker_colors=['#ffcc99', '#ff3399']
    ))
    fig_debtor.update_layout(
        title="Distribution of Debtors",
        plot_bgcolor='#fff0f5',
        paper_bgcolor='#fff0f5'
    )
    st.plotly_chart(fig_debtor)

import streamlit as st
import pandas as pd
from joblib import load


import streamlit as st
import pandas as pd
from joblib import load

if st.sidebar.selectbox("Choose page", ["Prediction"], key="sidebar_page") == "Prediction":
    st.title("💫 Predict Student Dropout")

    st.markdown(
        """
        <div style="background-color: #ffe1f0; padding: 20px; border-radius: 10px; text-align: center;">
            <h3 style="color: #d5006c;">Enter student data below to predict dropout risk!</h3>
            <p style="font-size: 18px; color: #d5006c;">Fill out the form to predict if a student is likely to drop out based on their information.</p>
        </div>
        """, unsafe_allow_html=True)


    # Course selection
    course_list = list(data.Course_Label.unique())[::-1]
    course_list.sort()
    if 'pred_selected' not in st.session_state:
        st.session_state.pred_selected = None

    if st.session_state.pred_selected is None:
        course_selected = st.selectbox('📘 Choose Course', ['None', *course_list], key='course_select')
    else:
        course_selected = st.selectbox('📘 Choose Course', course_list, key='course_select')

    if course_selected == 'None':
        st.error("❌ Please select a valid course.")
    else:
        st.session_state.course_selected = course_selected

    reverse_mapping = {v: k for k, v in category_mapping.items()}
    if course_selected != 'None':
        course_selected = reverse_mapping[course_selected]

    # Time based on course selection
    time_selected = 1 if course_selected not in [9991, 8014] else 0

    # User inputs for prediction
    admgrade_selected = st.number_input("🎓 Admission grade", value=0.0, step=0.1, min_value=0.0, max_value=200.0)
    admgrade_selected = round(admgrade_selected, 1)

    colGender, colAge = st.columns(2)
    with colGender:
        gender_list = ['Male', 'Female']
        gender_selected = st.selectbox('👩‍🎓 Gender', gender_list)
        gender_selected = 1 if gender_selected == "Male" else 0

    with colAge:
        age_selected = st.number_input("👶 Age at enrollment", step=1, min_value=17, max_value=70)

    bool1, bool2 = st.columns(2)
    with bool1:
        special_list = ['Yes', 'No']
        special_selected = st.radio('📚 Special education needs?', special_list)
        special_selected = 1 if special_selected == "Yes" else 0

    with bool2:
        debtor_list = ['Yes', 'No']
        debtor_selected = st.radio('💰 Debtor?', debtor_list)
        debtor_selected = 1 if debtor_selected == "Yes" else 0

    bool3, bool4 = st.columns(2)
    with bool3:
        tuition_list = ['Yes', 'No']
        tuition_selected = st.radio('💵 Tuition up to date?', tuition_list)
        tuition_selected = 1 if tuition_selected == "Yes" else 0

    with bool4:
        scholarship_list = ['Yes', 'No']
        scholarship_selected = st.radio('🎓 Scholarship holder?', scholarship_list)
        scholarship_selected = 1 if scholarship_selected == "Yes" else 0

    grade1, grade2 = st.columns(2)
    with grade1:
        grade1_selected = st.number_input("📑 1st Semester Grade", value=0.0, step=0.1, min_value=0.0, max_value=20.0)
        grade1_selected = round(grade1_selected, 2)

    with grade2:
        grade2_selected = st.number_input("📑 2nd Semester Grade", value=0.0, step=0.1, min_value=0.0, max_value=20.0)
        grade2_selected = round(grade2_selected, 2)

    # Predict button with stylish appearance
    button_predict = st.button("🔮 Predict", key='custom_button', help="Click to see the prediction!")
    
    if button_predict:
        if course_selected == "None":
            st.write("❌ Please select a valid course.")
        else:
            # Load the model
            model = load('logistic_regression_model.joblib')
            user_data = {
                'Course': [course_selected],
                'Daytime_evening_attendance': [time_selected],
                'Admission_grade': [admgrade_selected],
                'Educational_special_needs': [special_selected],
                'Debtor': [debtor_selected],
                'Tuition_fees_up_to_date': [tuition_selected],
                'Gender': [gender_selected],
                'Scholarship_holder': [scholarship_selected],
                'Age_at_enrollment': [age_selected],
                'Curricular_units_1st_sem_grade': [grade1_selected],
                'Curricular_units_2nd_sem_grade': [grade2_selected]
            }

            X_new = pd.DataFrame(user_data)
            predictions = model.predict(X_new)
            
            # Stylish prediction result
            if predictions == 0:
                st.markdown("""
                    <div style="background-color: #ffcccc; padding: 20px; border-radius: 10px; text-align: center;">
                        <h3 style="color: #cc0000;">🚨 Prediction: Likely to Drop Out!</h3>
                        <p style="font-size: 18px;">Based on the provided data, this student is predicted to drop out.</p>
                    </div>
                """, unsafe_allow_html=True)
            elif predictions == 1:
                st.markdown("""
                    <div style="background-color: #ccffcc; padding: 20px; border-radius: 10px; text-align: center;">
                        <h3 style="color: #009900;">🌟 Prediction: Likely to Stay!</h3>
                        <p style="font-size: 18px;">This student is likely to stay enrolled and complete the course.</p>
                    </div>
                """, unsafe_allow_html=True)



# Footer
st.markdown("<br><br><center>🌷 Designed with 💕 by <b>Febhe Maulita May Pramasta </b> 🌷</center>", unsafe_allow_html=True)


