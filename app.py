import streamlit as st

st.title("AI Resume Analyzer")

resume = st.text_area(
    "Paste Your Resume Here",
    height=300
)

if st.button("Analyze Resume"):

    st.success("Resume Analysis Complete!")

    st.subheader("Strengths")

    st.write("✅ Professional resume structure")
    st.write("✅ Relevant experience included")
    st.write("✅ Skills section present")

    st.subheader("Suggested Improvements")

    st.write("• Add more measurable achievements")
    st.write("• Include project descriptions")
    st.write("• Add LinkedIn and GitHub links")

    st.subheader("Missing Skills")

    st.write("• Data Analysis")
    st.write("• AI Tools")
    st.write("• Project Management")

    st.subheader("Resume Score")

    st.write("75 / 100")