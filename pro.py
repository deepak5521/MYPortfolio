import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Deepak Shelke - Python & Data Science Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- GLOBAL STYLES (for professional look, image border, and icons) ---
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<style>
/* Font sizes */
.big-font {
    font-size:20px !important;
    font-weight: bold;
}
.medium-font {
    font-size:18px !important;
}

/* Profile image styling */
.profile-image-container img {
    border: 3px solid #4CAF50;
    border-radius: 10px;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
}


</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
with st.container():
    col1, col2 = st.columns([1, 4])

    with col1:
        st.markdown('<div class="profile-image-container">', unsafe_allow_html=True)
        try:
            # Ensure the image file 'Gemini_Generated_Image_lgv3cjlgv3cjlgv3.jpg' is in the same directory as this script
            profile_image = Image.open("Gemini_Generated_Image_lgv3cjlgv3cjlgv3.png")
            st.image(profile_image, width=150)
        except FileNotFoundError:
            st.warning(
                "Profile image not found. Please ensure 'Gemini_Generated_Image_lgv3cjlgv3cjlgv3.jpg' is in the same directory as the script.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.title("Deepak Shelke")
        st.write("### Python Developer | Data Science Enthusiast")
        st.markdown(
            "[GitHub](https://github.com/deepak5521) | [LinkedIn](https://www.linkedin.com/in/deepak-shelke-b6130222a/)")

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

    st.markdown("<h5 style='margin-bottom: 0px;'>Programming Languages:</h5>", unsafe_allow_html=True)
    st.markdown(
        '<div class="skill-item"><i class="fab fa-python" style="color:#3776AB;"></i> <span>Python</span></div>',
        unsafe_allow_html=True)
    st.markdown('<div class="skill-item"><i class="fas fa-database" style="color:#00758F;"></i> <span>SQL</span></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="skill-item"><i class="fab fa-html5" style="color:#E34F26;"></i> <span>HTML</span></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="skill-item"><i class="fab fa-css3-alt" style="color:#1572B6;"></i> <span>CSS</span></div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="skill-item"><i class="fab fa-js-square" style="color:#F7DF1E;"></i> <span>JavaScript (Basics)</span></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div class="skill-item"><i class="fab fa-php" style="color:#777BB4;"></i> <span>PHP (Basics)</span></div>',
        unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add a line break for spacing
    st.markdown("<h5 style='margin-bottom: 0px;'>Libraries & Frameworks:</h5>", unsafe_allow_html=True)
    st.markdown(
        '<div class="skill-item"><i class="fas fa-cogs" style="color:#6C757D;"></i> <span>Pandas, NumPy, Matplotlib, Tkinter</span></div>',
        unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add a line break for spacing
    st.markdown("<h5 style='margin-bottom: 0px;'>Databases:</h5>", unsafe_allow_html=True)
    st.markdown(
        '<div class="skill-item"><i class="fas fa-database" style="color:#00758F;"></i> <span>MySQL</span></div>',
        unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add a line break for spacing
    st.markdown("<h5 style='margin-bottom: 0px;'>Tools & Platforms:</h5>", unsafe_allow_html=True)
    st.markdown(
        '<div class="skill-item"><i class="fas fa-tools" style="color:#212529;"></i> <span>Jupyter Notebook, Git, GitHub, VS Code, Ethereum Blockchain (Basic understanding)</span></div>',
        unsafe_allow_html=True)

st.write("---")

# --- EDUCATION ---
with st.container():
    st.header("Education")

    st.markdown("""
    **Bachelor of Engineering (Computer Engineering)**
    * AAEMF'S College of Engineering, Pune | Savitribai Phule Pune University (SPPU) CGPA :- 7.38
    * Year of Passing: 2025
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

    # Project 1: Employee Management System (Existing Content)
    with st.expander("**Employee Management System (Python + SQL)**"):
        st.write("""
        An Employee Management System (EMS) developed as a GUI-based mini-project using Python's **Tkinter** library for the graphical user interface and **MySQL** for database management. This system offers a robust solution for efficient employee record management.

        **Key Features and Functionalities:**
        * **Employee Information Management:** Facilitates the storage and retrieval of comprehensive employee details such as employee ID, name, designation, contact information, date of joining, salary, and other relevant personal and professional data.
        * **CRUD Operations:** Users can perform essential **Create, Read, Update, and Delete (CRUD)** operations on employee records. This includes adding new employees, viewing existing records, modifying employee details, and removing records when necessary.
        * **Search and Filter Capabilities:** Incorporates functionalities to search for specific employees based on various criteria (e.g., name, ID) and filter records to display subsets of data.
        * **User-Friendly Interface:** **Tkinter** provides the tools to create an intuitive and easy-to-navigate graphical user interface, enhancing user experience and streamlining data entry and retrieval.
        * **Database Integration with MySQL:** **MySQL** serves as the backend database, ensuring efficient and secure storage of employee data. Python's database connectors (like `pymysql` or `mysql-connector-python`) enable seamless interaction between the Tkinter GUI and the MySQL database.
        * **Data Validation:** Includes mechanisms for data validation to ensure data integrity and prevent errors during data entry.
        """)

    # Project 2: Blockchain Based Crowdfunding System (Updated Content)
    with st.expander("**Blockchain Based Crowdfunding System**"):
        st.write("""
        In my final year, I developed a Blockchain-Based Crowdfunding System using **Ethereum smart contracts**.
        This project aims to provide a secure and transparent platform for fundraising by eliminating third-party involvement.
        All transactions are recorded on the **blockchain**, ensuring trust, immutability, and automated fund management based on predefined rules.
        """)
        st.markdown(
            "Published in IEEE format. Access the paper here: [IEEE Paper Link](https://ijcrt.org/download.php?file=IJCRT25A4430.pdf)")

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
