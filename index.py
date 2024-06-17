import streamlit as st
from PIL import Image

# Load CSS files
# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")
load_css('components.css')

# Load the image from file
profile_image = Image.open(r"images\WhatsApp Image 2024-06-17 at 19.41.29_e44ff362.jpg")
project_images = [
    Image.open(r"images\WhatsApp Image 2024-06-17 at 19.43.02_84c87f06.jpg"),
    Image.open(r"images\WhatsApp Image 2024-06-17 at 19.42.36_1f474e6e.jpg"),
    Image.open(r"images\WhatsApp Image 2024-06-17 at 19.42.22_23814bfd.jpg"),
    Image.open(r"images\WhatsApp Image 2024-06-17 at 19.43.41_6dbcaeb1.jpg"),
]


# Define content for each section
about_me_content = """
### About Me

Hello! Welcome to my portfolio. I am Pravallika K.R, an Artificial Intelligence and Data Science Student. 
Explore my skills and experiences across various disciplines. From innovative projects to insightful publications,
delve into a journey of passion and dedication. Discover how my expertise in skills, hobbies, and professional 
contacts can contribute to your next venture. Whether you're here to explore potential collaborations, learn 
about my skills, or simply gain inspiration, I hope my portfolio leaves you inspired and eager to connect.

An enthusiastic learner with a strong technical acumen in Python, Machine Learning, Neural Networks, and Data Visualization using Power BI. My expertise extends to Natural Language Processing and web development with Streamlit, where I create intuitive and interactive applications. Proficient in SQL and NoSQL databases, I leverage data management skills to derive actionable insights. In addition to technical prowess, I prioritize holistic development, nurturing exceptional leadership, presentation, effective communication, and teamwork skills. These attributes have been refined through active involvement in extracurricular activities, fostering a well-rounded approach to problem-solving and collaboration. Passionate about leveraging technology to innovate and drive impactful solutions, I am committed to continuous learning and professional growth in the ever-evolving field of data science and analytics.
[Check Out: Resume]()
"""

education_content = """
### Education

- *Btech in Artificial Intelligence & Data Science*  
  Reva University - 2025  
  CGPA: 9.08 / 10 (Till Date)
  
- *Secondary Education*  
  Poorna Prajna PU College - 2021  
  Board: STATE  
  Percentage: 93.33%
  
- *Schooling*  
  Narayana E-techno School - 2019  
  Board: CBSE  
  Percentage: 80%
"""

# Project descriptions
projects_content = [
    {
        "title": "Bank Loan Analysis using Power BI and SQL",
        "description": "Developed and implemented a bank loan analysis dashboard using Power BI and SQL to provide actionable insights into loan approval trends, customer credit profiles, and risk assessment metrics.",
        "technologies": "Power BI, SQL, Data Modeling",
        "image": project_images[0]
    },
    {
        "title": "Comprehensive SQL Data Analysis on Pizza Sales Dataset",
        "description": "Completed an end-to-end data analysis project using SQL, focusing on a pizza sales dataset. This project involved loading the dataset into a SQL database and performing various queries to uncover insights and support data-driven business decisions.",
        "technologies": "SQL, Data Analysis",
        "image": project_images[1]
    },
    {
        "title": "Voice-Activated Food Order Management Chatbot",
        "description": "Created a chatbot using FastAPI and Dialogflow for managing food orders through real-time interactions. It utilizes Dialogflow's NLP for precise command interpretation and integrates with SQLite database for order processing and updates.",
        "technologies": "FastAPI, Dialogflow, SQLite",
        "image": project_images[2]
    },
    {
        "title": "RecipeRadar - AI-Powered Recipe Generator",
        "description": "Web app that uses AI to generate customized recipes using Streamlit and Gemini Pro API. It employs advanced NLP for content generation and image processing for visual appeal.",
        "technologies": "Streamlit, Gemini Pro API, NLP",
        "image": project_images[3]
    }
]

technical_skills_content = """
### Technical Skills

#### Python
- *Description:* Proficient in Python programming language, with experience in developing applications and scripts for various domains including data science, automation, and web development.

#### Java
- *Description:* Solid understanding of Java programming language, with expertise in building robust and scalable applications.

#### Data Structures and Algorithms (DSA)
- *Description:* Strong knowledge and practical experience in fundamental data structures and algorithms, enabling efficient problem-solving in software development and algorithm design.

#### Machine Learning
- *Description:* Knowledgeable in machine learning techniques and algorithms, with practical experience in building predictive models and analyzing data patterns.

#### HTML/CSS/JavaScript (Basics)
- *Description:* Familiarity with front-end web technologies including HTML for structure, CSS for styling, and JavaScript for interactivity.

#### Neural Networks and Deep Learning (NNDL)
- *Description:* Proficient in neural networks and deep learning concepts, with hands-on experience in building and training models for image recognition and natural language processing tasks.

#### Natural Language Processing (NLP)
- *Description:* Skilled in natural language processing techniques, including text preprocessing, sentiment analysis, and language modeling.

#### Data Visualization using Power BI
- *Description:* Experienced in creating interactive visualizations and dashboards using Power BI to derive insights from complex datasets.

#### Streamlit (Basics)
- *Description:* Familiar with Streamlit framework for building and deploying interactive data applications with Python.

#### Pandas
- *Description:* Proficient in using Pandas library for data manipulation and analysis, including data cleaning, transformation, and aggregation.

#### NumPy
- *Description:* Strong understanding of NumPy library for numerical computing in Python, essential for scientific and mathematical operations.

#### Database Management Systems (DBMS) - SQL and NoSQL basics
- *Description:* Knowledgeable in database systems, including relational databases (SQL) and non-relational databases (NoSQL), with skills in querying and data management.

#### Generative Artificial Intelligence (GenAI) (Basics)
- *Description:* Familiar with generative artificial intelligence concepts, including generative models and their applications in creative fields.
"""


softskills_content = """
### SoftSkills

#### Leadership
- *Description:* Capable of guiding and motivating teams towards achieving common goals.

#### Presentation
- *Description:* Skilled in delivering clear and engaging presentations to communicate ideas effectively.

#### Effective Communication
- *Description:* Strong ability to express ideas clearly both verbally and in writing, ensuring understanding and engagement.

#### Teamwork
- *Description:* Collaborative team player, adept at building relationships and contributing to group success.
"""





publication_content = """
### Publications

#### Retina Vigil: Deep Learning-Enabled Retinopathy Detection
- *Team Lead, Paper Submission:* Deep learning for retinopathy detection at IEEE MysuruCon-2023
- *Description:* Deep learning methodologies, strong understanding of medical imaging, academic publication.
- *Project Methodology:* Researched and analyzed current processes, gathered and processed retinal image data, developed and evaluated deep learning models.
- [Check Out: Paper Publication Link](https://ieeexplore.ieee.org/document/10396854/authors)
"""




certifications_content = """
### Certifications

#### Machine learning with Python
- *Issued by:* IBM Organization in collaboration with Cognitive Class
- *Details:* Received for actively participating in the course event held in 2023.
- [View Certificate 1](https://www.example.com/certificate1)

#### Python for Data Science
- *Issued by:* IBM Organization in collaboration with Cognitive Class
- *Details:* Received for actively participating in the course event held in 2023.
- [View Certificate 2](https://www.example.com/certificate2)

#### Natural Language Processing using Python
- *Issued by:* Infosys Organization in Infosys SpringBoard
- *Details:* Received for actively participating in the course event held in 2023.
- [View Certificate 3](https://www.example.com/certificate3)

#### SQL and Relational Databases 101
- *Issued by:* IBM Organization in collaboration with Cognitive Class
- *Details:* Received for actively participating in the course event held in 2023.
- [View Certificate 4](https://www.example.com/certificate4)
"""
participations_content = """
### Participations

#### Smart India Hackathon (SIH) at Reva University
- *Project:* BeFit Website
- *Description:* Participated in the Smart India Hackathon held at Reva University, where our team developed the BeFit website. As part of the team of five, I focused on integrating a chatbot into our project, enhancing user interaction and engagement.

#### Cybercrime Conclave at IISC , Bengaluru
- *Project:* Cybercrime Awareness Website
- *Description:* Contributed to the development of a website focused on educating users about cyber crimes and various cyber bullying modules. During this event, I gained practical experience in web development technologies including HTML, CSS, and JavaScript, assisting in the design and functionality of the site.

#### Singing Competition at EC Block, Reva University
- *Event:* Duet Performance
- *Description:* Participated in a singing competition held at EC Block, Reva University, showcasing duet performance skills.

#### Classical Competition at Reva University College Fest
- *Event:* Classical Performance
- *Description:* Participated in a classical music competition during the college fest at Reva University, demonstrating proficiency in classical music.

"""



hobbies_content = """
### Hobbies

#### Classical Singing
- *Description:* Trained singer in classical music with completion of Junior Exam in 2018. Actively sing and share performances on public Instagram page.

#### Sketching
- *Description:* Enjoy sketching as a creative hobby.

#### Dancing
- *Description:* Passionate about dancing.

#### Hiking
- *Description:* Enthusiastic hiker with experience in:
  - Sakandagiri
  - Makalidurga
  - Nethravathi 

"""


contact_content = """
### Contact

- *Phone Number:* +91 9513896465
- *Email:* pravallikarajesh773@gmail.com
- *LinkedIn:* [LinkedIn Profile](https://www.linkedin.com/in/pravallika-rajesh-a02a5628a)
- *GitHub:* [GitHub Profile](https://github.com/Pravallikarajeshan)
- *Public Instagram:* [Instagram Profile](https://www.instagram.com/prvk.musicology?igsh=MXZ2N3N2cnE4aWdmNw==)
"""



# Define default selection
DEFAULT_PAGE = "About Me"


# Initialize session state variables
if 'menu_selection' not in st.session_state:
    st.session_state.menu_selection = DEFAULT_PAGE
sidebar_image = "images\imresizer-1718617666502.jpg" # Replace with the actual path to your image file
st.sidebar.image(sidebar_image, caption='Pravallika K.R', width=100, use_column_width=False)
# Sidebar menu with items spaced vertically
st.sidebar.title("Menu")
st.sidebar.markdown("---")  # Horizontal line for separation

# Create buttons for menu selection
button_about_me = st.sidebar.button("About Me")
st.sidebar.markdown("---")  # Add a gap
button_education = st.sidebar.button("Education")
st.sidebar.markdown("---")  # Add a gap
button_projects = st.sidebar.button("Projects")
st.sidebar.markdown("---")  # Add a gap
button_technical_skills = st.sidebar.button("Technical Skills")
st.sidebar.markdown("---")  # Add a gap
button_softskills = st.sidebar.button("SoftSkills")
st.sidebar.markdown("---")  # Add a gap
button_publication = st.sidebar.button("Publication")
st.sidebar.markdown("---")  # Add a gap
button_certifications = st.sidebar.button("Certifications")
st.sidebar.markdown("---")  # Add a gap
button_participations = st.sidebar.button("Participation")
st.sidebar.markdown("---")  # Add a gap
button_hobbies = st.sidebar.button("Hobbies")
st.sidebar.markdown("---")  # Add a gap
button_contact = st.sidebar.button("Contact")

# Determine which button was clicked
if button_about_me:
    st.session_state.menu_selection = "About Me"
elif button_education:
    st.session_state.menu_selection = "Education"
elif button_projects:
    st.session_state.menu_selection = "Projects"
elif button_technical_skills:
    st.session_state.menu_selection = "Technical Skills"
elif button_softskills:
    st.session_state.menu_selection = "SoftSkills"
elif button_publication:
    st.session_state.menu_selection = "Publication"
elif button_certifications:
    st.session_state.menu_selection = "Certifications"
elif button_participations:
    st.session_state.menu_selection = "Participations"
elif button_hobbies:
    st.session_state.menu_selection = "Hobbies"
elif button_contact:
    st.session_state.menu_selection = "Contact"

# Display content based on current selection
if st.session_state.menu_selection == "About Me":
    st.image(profile_image, caption='Pravallika Rajesh ', use_column_width=False, width=150)
    st.markdown(about_me_content)
elif st.session_state.menu_selection == "Education":
    st.markdown(education_content)
elif st.session_state.menu_selection == "Projects":
    for project in projects_content:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(project["image"], use_column_width=True)
        with col2:
            st.markdown(f"#### {project['title']}")
            st.markdown(f"- *Description*: {project['description']}")
            st.markdown(f"- *Technologies*: {project['technologies']}")
elif st.session_state.menu_selection == "Technical Skills":
    st.markdown(technical_skills_content)
elif st.session_state.menu_selection == "SoftSkills":
    st.markdown(softskills_content)
elif st.session_state.menu_selection == "Publication":
    st.markdown(publication_content)
elif st.session_state.menu_selection == "Certifications":
    st.markdown(certifications_content)
elif st.session_state.menu_selection == "Participations":
    st.markdown(participations_content)
elif st.session_state.menu_selection == "Hobbies":
    st.markdown(hobbies_content)
elif st.session_state.menu_selection == "Contact":
    st.markdown(contact_content)
