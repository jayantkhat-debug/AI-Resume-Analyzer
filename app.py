import streamlit as st

st.title("AI Resume Analyzer V2")

resume = st.text_area(
    "Paste Your Resume Here",
    height=300
)

if st.button("Analyze Resume"):

    score = 50

    st.subheader("ATS Score")

    if "skills" in resume.lower():
        score += 10

    if "projects" in resume.lower():
        score += 10

    if "linkedin.com" in resume.lower():
        score += 10

    if "github.com" in resume.lower():
        score += 10

    if len(resume) > 500:
        score += 10

    if score > 100:
        score = 100

    st.write(f"ATS Score: {score}/100")

    st.subheader("Checks")

    if "skills" in resume.lower():
        st.success("Skills section found")
    else:
        st.error("Skills section missing")

    if "projects" in resume.lower():
        st.success("Projects section found")
    else:
        st.error("Projects section missing")

    if "linkedin.com" in resume.lower():
        st.success("LinkedIn profile found")
    else:
        st.error("LinkedIn profile missing")

    if "github.com" in resume.lower():
        st.success("GitHub profile found")
    else:
        st.error("GitHub profile missing")

    st.subheader("Recommendations")

    if "github.com" not in resume.lower():
        st.write("• Add your GitHub profile")

    if "linkedin.com" not in resume.lower():
        st.write("• Add your LinkedIn profile")

    if "projects" not in resume.lower():
        st.write("• Add a Projects section")

    if "skills" not in resume.lower():
        st.write("• Add a Skills section")

    st.write("• Add measurable achievements")
    st.write("• Include relevant certifications")
    