import streamlit as st

def calculate_grade(midterm_score, final_score, attendance_score, midterm_weight, final_weight, attendance_weight):
    total_score = (midterm_score * midterm_weight/100) + (final_score * final_weight/100) + (attendance_score * attendance_weight/100)
    
    if total_score >= 90:
        grade = 'A'
    elif total_score >= 80:
        grade = 'B'
    elif total_score >= 70:
        grade = 'C'
    elif total_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return total_score, grade

st.title("Student Grade Calculator @YED")

midterm_score = st.slider("Midterm Score (0-100)", min_value=0, max_value=100, value=75, step=1)
final_score = st.slider("Final Score (0-100)", min_value=0, max_value=100, value=80, step=1)
attendance_score = st.slider("Attendance Score (0-100)", min_value=0, max_value=100, value=90, step=1)

midterm_weight = st.slider("Midterm Weight (%)", min_value=0, max_value=100, value=30, step=1)
final_weight = st.slider("Final Weight (%)", min_value=0, max_value=100, value=50, step=1)
attendance_weight = st.slider("Attendance Weight (%)", min_value=0, max_value=100, value=20, step=1)

total_score, grade = calculate_grade(midterm_score, final_score, attendance_score, midterm_weight, final_weight, attendance_weight)

st.write(f"Total Score: {total_score:.2f}")
st.write(f"Grade: {grade}")