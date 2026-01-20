import streamlit as st

st.set_page_config(page_title="3D Design Project", layout="wide")

# Add custom CSS for a modern look
st.markdown('''
    <style>
        .main {
            background: linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%);
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
        }
        h1, h2, h3, h4 {
            color: #2d3a4a;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            border-radius: 18px;
            background: #fff;
            box-shadow: 0 4px 24px 0 rgba(60,72,88,0.08);
        }
        .stImage > img {
            border-radius: 16px;
            box-shadow: 0 2px 12px 0 rgba(60,72,88,0.10);
        }
        .stMarkdown, .stText, .stInfo {
            font-size: 1.1rem;
        }
        .st-bb, .st-cq, .st-cv {
            background: #f1f5fa !important;
            border-radius: 12px;
        }
    </style>
''', unsafe_allow_html=True)

# Replace fireworks animation with 'Printing in Progress' banner
st.markdown('<div style="text-align:center; font-size:2rem; font-weight:bold; color:#ff6600; margin-top:30px; margin-bottom:10px;">🖨️ Printing in Progress...</div>', unsafe_allow_html=True)

st.title("3D Design Project Showcase")

st.markdown("---")

st.markdown("""
Welcome to the 3D Design Project page!
""")

# Add introduction with picture under the title (use st.image for compatibility)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("myself.jpeg", width=260)
with col2:
    st.markdown("""
    ### About Me
    Hello! My name is Tyler Liao. I am a student with a strong passion for engineering, particularly mechanical engineering, and a deep interest in solving real-world problems through design and innovation. I enjoy transforming ideas into practical solutions by combining creativity with precision, testing, and persistence.

    My interest in engineering has grown through hands-on projects, from designing and 3D-printing custom solutions for everyday challenges to repairing and assembling complex systems. One of my most meaningful projects was designing and building a fully functional 3D-printed camera from scratch using CAD, which taught me the importance of adaptability, iterative problem-solving, and attention to detail.

    I am especially motivated by collaborative learning and structured design processes, as I believe the best engineering solutions emerge from teamwork and diverse perspectives. I aspire to further develop my technical foundation through rigorous, college-level engineering experiences and hands-on projects that reflect real engineering practice.

    Ultimately, my goal is to pursue a career in mechanical engineering, where I can continue to innovate, challenge myself, and create solutions that make a meaningful impact.
    """)

st.header("Gallery")

# Define projects with their stories
projects = [
    {
        "img": "1.Camera.jpeg",
        "title": "3D-Printed Camera",
        "date": "Dec. 15, 2025",
        "story": """I designed and built a functional 3D-printed film camera as a hands-on engineering project. My original plan was to reuse parts from an existing camera, but when that wasn’t practical, I adapted by designing more components myself using CAD. Throughout the process, I faced challenges with 3D-printing limitations, including poor tolerances, weak parts, thread fitting issues, and light leaks that affected exposure. I addressed these problems through repeated redesigns, testing, and simple solutions like adjusting part thicknesses and sealing gaps with electrical tape. The project taught me the value of flexibility, simplifying designs, and learning through trial and error. It reflects my problem-solving mindset, persistence, and ability to work with limited resources to turn a complex idea into a working prototype."""
    },
    {
        "img": "2.MugInsert.jpeg",
        "title": "Mug Insert",
        "date": "Nov. 10, 2025",
        "story": "I designed a custom 3D-printed insert for my mom’s mug when it didn’t fit in her car’s cup holder. I carefully measured the dimensions of both the mug and the holder, then created a solution that allowed the mug to fit securely. Now, she can enjoy her favorite mug on her daily commute, making a small but meaningful improvement to her everyday routine."
    },
    {
        "img": "4.PencilHolder.jpeg",
        "title": "Pencil Holder",
        "date": "Oct. 05, 2025",
        "story": "A geometric workspace organizer. I focused on clean lines and stability, experimenting with varying wall thicknesses to optimize print time and strength."
    },
    {
        "img": "5.BrushHolder.jpeg",
        "title": "Brush Holder",
        "date": "Jan. 19, 2026",
        "story": """
        I designed a compact brush holder to solve a space limitation at a school Chinese calligraphy event organized by my mother. With limited table space, my goal was to create a sturdy, space-saving design that also attracted students’ attention.

        I measured the brushes to determine proper dimensions and structural requirements, ensuring stability and balance. I incorporated traditional Chinese festival patterns to enhance visual appeal. 
        
        During prototyping, I discovered issues with joint smoothness, which I corrected through sanding and reinforcing the connections. This process taught me the importance of precision and iteration in mechanical design.

        In future versions, I plan to redesign the joints with a twist-lock mechanism to improve strength and ease of assembly. This project strengthened my interest in 3D printing and mechanical engineering.
        """
    }
]

# Initialize session state for selected project
if 'selected_project_index' not in st.session_state:
    st.session_state.selected_project_index = 3  # Default to Brush Holder

st.markdown("#### Click 'View Story' under an image to see the project details below!")

cols = st.columns(len(projects))
for idx, project in enumerate(projects):
    with cols[idx]:
        st.image(project["img"], caption=project["title"])
        if st.button("View Story", key=f"btn_{idx}"):
            st.session_state.selected_project_index = idx

st.markdown("---")

st.header("Project Stories")

# Display the selected project story
current_project = projects[st.session_state.selected_project_index]

st.subheader(f"Project Spotlight: {current_project['title']}")
story_col1, story_col2 = st.columns([1, 2])
with story_col1:
    st.image(current_project["img"], caption=current_project["title"])
with story_col2:
    st.markdown(f"**Created Date:** {current_project['date']}")
    st.markdown(current_project["story"])

# Contact Form
st.markdown("---")
st.subheader("Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        if name and email and message:
            st.success("Thank you for reaching out! I'll get back to you soon.")
        else:
            st.error("Please fill in all fields before submitting.")
