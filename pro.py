import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Deepak Shelke - Python & Data Science Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- GLOBAL STYLES (Optional: for minor adjustments, can be expanded) ---
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    font-weight: bold;
}
.medium-font {
    font-size:18px !important;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
with st.container():
    col1, col2 = st.columns([1, 4]) # Adjust column ratio as needed for image size and text

    with col1:
        try:
            # Ensure the image file 'Gemini_Generated_Image_lgv3cjlgv3cjlgv3.jpg' is in the same directory as this script
            profile_image = Image.open("Gemini_Generated_Image_lgv3cjlgv3cjlgv3.png")
            st.image(profile_image, width=150) # Consistent width for professional look
        except FileNotFoundError:
            st.warning("Profile image not found. Please ensure 'Gemini_Generated_Image_lgv3cjlgv3cjlgv3.jpg' is in the same directory as the script.")
    with col2:
        st.title("Deepak Shelke")
        st.write("### Python Developer | Data Science Enthusiast") # More descriptive title
        st.markdown("[GitHub](https://github.com/deepak5521) | [LinkedIn](https://www.linkedin.com/in/deepak-shelke-b6130222a/)") # Concise links

st.write("---")

# --- ABOUT ME ---
with st.container():
    st.header("About Me")
    st.write(
        """
        A highly motivated and detail-oriented Computer Engineering graduate with a robust foundation in Python and Data Science.
        I am passionate about leveraging machine learning, data analysis, and automation to develop innovative solutions for real-world challenges.
        Eager to contribute to a dynamic technology team and grow as a dedicated Data Scientist or Python Developer.
        """
    )
st.write("---")

# --- CONTACT INFORMATION ---
with st.container():
    st.header("Contact Information")
    st.markdown(f"**Email:** [shelkedeepakds@gmail.com](mailto:shelkedeepakds@gmail.com)")
    st.write(f"**Phone:** +91 9371065521")
    st.write(f"**Location:** Pune, Maharashtra, India")
st.write("---")

# --- TECHNICAL SKILLS ---
with st.container():
    st.header("Technical Skills")
    st.markdown("""
    * **Programming Languages:** Python, SQL, HTML, CSS, JavaScript (Basics)
    * **Libraries & Frameworks:** Pandas, NumPy, Matplotlib, Tkinter
    * **Databases:** MySQL
    * **Tools & Platforms:** Jupyter Notebook, Git, GitHub, VS Code, Ethereum Blockchain (Basic understanding)
    """)
st.write("---")

# --- EDUCATION ---
with st.container():
    st.header("Education")

    st.markdown("""
    **Bachelor of Engineering (Computer Engineering)**
    * AAEMF'S College of Engineering, Pune | Savitribai Phule Pune University (SPPU) CGPA:-7.38
    * Year of Passing:* 2025
    """)

    st.markdown("""
    **Higher Secondary Certificate (HSC)**
    * New Arts, Commerce and Science College Shevgaon | *Percentage:* 81.30%
    * *Year of Passing:* 2021
    """)

    st.markdown("""
    **Secondary School Certificate (SSC)**
    * Timurti Public School, Shevgaon | *Percentage:* 56.16%
    * *Year of Passing:* 2019
    """)
st.write("---")

# --- INTERNSHIP EXPERIENCE ---
with st.container():
    st.header("Internship Experience")
    st.markdown("""
    **Web Development Intern**
    * *ProAzure Software Solutions Pvt. Ltd.* | *Duration:* 2 Months
    * Developed a **Countdown Event Management** project, enabling users to create and track event countdowns.
    * Utilized **HTML, CSS, and JavaScript** to build an interactive and user-friendly interface.
    """)
st.write("---")

# --- PROJECTS ---
with st.container():
    st.header("Projects")

    # Project 1
    with st.expander("**Employee Management System (Python + SQL)**"):
        st.write("A GUI-based mini-project developed using **Tkinter** and **MySQL** for efficient management of employee records.")

    # Project 2
    with st.expander("**Blockchain Based Crowdfunding System**"):
        st.write("Designed and implemented a transparent crowdfunding model on the **Ethereum Blockchain**.")
        st.markdown("Published in IEEE format. Access the paper here: [IEEE Paper Link](http://ijcrt.org/viewfull.php?&pid=IJCRT25A4430)")
st.write("---")

# --- CERTIFICATIONS ---
with st.container():
    st.header("Certifications")
    st.markdown(
        """
        * **Python Programming** - SevenMentor Pvt.Ltd
        * **MySQL Basics** - SevenMentor Pvt.Ltd
        * **NISM Certified** - SEBI Investor Certification
        """
    )
st.write("---")

# --- LANGUAGES & INTERESTS ---
with st.container():
    st.header("Additional Information")
    st.markdown(f"**Languages Known:** English, Hindi, Marathi")
    st.markdown(
        """
        **Hobbies & Interests:**
        * Photography and Editing (Founder of Tripixo_)
        * Exploring new technologies and financial markets
        """
    )
st.write("---")

st.info("Thank you for visiting my portfolio!")