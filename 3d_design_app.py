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

# Add introduction with picture under the title
col1, col2 = st.columns([1, 3])
with col1:
    st.image("myself.jpeg", width=250)
with col2:
    st.markdown("""
    ### About Me
    Hello! My name is Tyler Liao. I am a student with a strong passion for engineering, particularly mechanical engineering, and a deep interest in solving real-world problems through design and innovation. I enjoy transforming ideas into practical solutions by combining creativity with precision, testing, and persistence.

    My interest in engineering has grown through hands-on projects, from designing and 3D-printing custom solutions for everyday challenges to repairing and assembling complex systems. One of my most meaningful projects was designing and building a fully functional 3D-printed camera from scratch using CAD, which taught me the importance of adaptability, iterative problem-solving, and attention to detail.

    I am especially motivated by collaborative learning and structured design processes, as I believe the best engineering solutions emerge from teamwork and diverse perspectives. I aspire to further develop my technical foundation through rigorous, college-level engineering experiences and hands-on projects that reflect real engineering practice.

    Ultimately, my goal is to pursue a career in mechanical engineering, where I can continue to innovate, challenge myself, and create solutions that make a meaningful impact.
    """)

st.header("Gallery")

st.markdown("#### My 3D Design Gallery")
gallery_images = [
    ("1.Camera.jpeg", "3D-Printed Camera"),
    ("2.MugInsert.jpeg", "Mug Insert"),
    ("4.PencilHolder.jpeg", "Pencil Holder")
]
cols = st.columns(3)
for idx, (img, caption) in enumerate(gallery_images):
    with cols[idx]:
        st.image(img, caption=caption)

st.markdown("---")

st.header("Project Stories & Collaboration")
st.write("Share your design process, tips, and connect with other creators!")

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
