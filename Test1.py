import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import folium
import pydeck as pdk
import plotly.express as px
import openpyxl

st.set_page_config(layout="wide")



# Define functions for each page
def home():
   
    st.markdown("<h1 style='text-align: center;'>Welcome!</h1>", unsafe_allow_html=True)
    username = st.text_input("Please enter your Name:")
    if username:
        st.session_state.username = username
        ethics_description = """
        <p style='text-align: Center; font-size: 18px;'>
        <i>Welcome to our website dedicated to ethics education! 🌟
        <br>Explore real-life case studies and captivating videos to deepen
         your understanding of ethical dilemmas. 
         <br>Test your knowledge with
          interactive quizzes on every page, and track your progress with
           the cumulative score displayed in the sidebar.
        <br>Join us on a journey of critical thinking and ethical reflection.
         Let's navigate the complexities of today's world together, armed with
          knowledge and ethical insight. Welcome! 🚀</i>
    </p>
    """
        st.balloons()
        st.markdown(f"<h4 style='text-align: center;'>Hello {username}!</h1>", unsafe_allow_html=True)
        st.markdown(f"{ethics_description}" ,unsafe_allow_html=True)
    

##############################################################  WHAT IS ETHICS ###################################################################

def what_is_ethics():
    

    st.markdown("<h2 style='text-align: center;'>What is <span style='color: orange;'>Ethics</span>?</h>", unsafe_allow_html=True)
    ethics_description = """
        <p style='text-align: justify; font-size: 18px;'>
        "<i>Ethics is a branch of philosophy that deals with
        the study of moral principles and values that govern
        human behavior. It helps individuals and organizations
        determine what is right or wrong, good or bad, and
        how to act in various situations. Ethics provides a
        framework for making decisions that align with moral
        standards and values</i>"
    </p>
    """
    st.markdown(ethics_description, unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")
    st.write("   ")

    

    # Define column widths
    column_widths = [10,1,10]  # Column 1 will be twice as wide as Column 2

    # Create columns with specified widths
    col1, col2 , col3 = st.columns(column_widths)

    with col1:

        st.markdown("<h3 style='text-align: center;'>Importance of <span style='color: orange;'>Ethics</span></h3>", unsafe_allow_html=True)
        Importance = """
            <p style='text-align: justify; font-size: 17px;'>
            <br><br><span style='color: orange;'><strong>Make principled decisions:</strong></span></h3> Ethics guides decision-making processes by providing a moral compass and a set of principles to follow.
            <br><br><span style='color: orange;'><strong>Build trust and credibility:</strong></span></h3> Adhering to ethical principles fosters trust among stakeholders, customers, and the public, enhancing reputation and credibility.
            <br><br><span style='color: orange;'><strong>Create a positive work environment:</strong></span></h3> Ethical behavior in the workplace promotes respect, fairness, and a sense of purpose, leading to a positive and productive work culture.
            <br><br><span style='color: orange;'><strong>Ensure compliance:</strong></span></h3> Many industries and professions have established ethical codes and guidelines that must be followed to maintain compliance and avoid legal consequences.
            <br><br><span style='color: orange;'><strong>Promote social responsibility:</strong></span></h3> Ethics encourages individuals and organizations to consider the wider implications of their actions and to contribute positively to society.
        </p>
        """

        st.markdown(Importance, unsafe_allow_html=True)

    with col3:
        st.markdown("<h3 style='text-align: center;'>Branches of <span style='color: orange;'>Ethics</span></h3>", unsafe_allow_html=True)
        Branch = """
            <p style='text-align: justify; font-size: 17px;'>
            <br><br><span style='color: orange;'><strong>Normative Ethics:</strong></span></h3> This branch deals with the development and evaluation of moral standards, principles, and theories that determine right or wrong conduct. It includes ethical frameworks such as utilitarianism, deontology, and virtue ethics.
            <br><br><span style='color: orange;'><strong>Applied Ethics:</strong></span></h3> This branch focuses on the practical application of ethical principles to specific situations or contexts, such as business ethics, bioethics, environmental ethics, and computer ethics.
            <br><br><span style='color: orange;'><strong>Meta-Ethics:</strong></span></h3> This branch examines the fundamental nature of ethical concepts and judgments, including the meaning of moral terms, the validity of moral reasoning, and the objectivity or subjectivity of moral values.
        </p>
        """
        st.markdown(Branch, unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")

    st.markdown("<h3 style='text-align: center;'><span style='color: orange;'>Ethics</span></h3>", unsafe_allow_html=True)

    video_url = 'https://www.youtube.com/embed/u399XmkjeXo'
    video_html = f'<div style="display: flex; justify-content: center;"><iframe width="640" height="360" src="{video_url}" frameborder="0" allowfullscreen></iframe></div>'
    st.markdown(video_html, unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")

    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)

    questions = [
    {
        "question": "What is the primary focus of ethics?",
        "options": ["Determining what is legal", "Studying moral principles and values", "Maximizing personal gain", "Analyzing scientific theories"],
        "answer": "Studying moral principles and values"
    },
    {
        "question": "Which branch of ethics deals with the practical application of ethical principles to specific situations or contexts?",
        "options": ["Normative Ethics", "Applied Ethics", "Meta-Ethics", "Virtue Ethics"],
        "answer": "Applied Ethics"
    },
    {
        "question": "According to utilitarianism, the most ethical choice is the one that:",
        "options": ["Follows established moral rules", "Develops virtuous character traits", "Maximizes overall happiness and well-being", "Arises from an implicit social contract"],
        "answer": "Maximizes overall happiness and well-being"
    },
    {
        "question": "Deontology, developed by Immanuel Kant, emphasizes the importance of:",
        "options": ["Compassion and empathy", "Duty, moral rules, and respect for persons", "Cooperating for mutual benefit", "Maximizing happiness for the greatest number"],
        "answer": "Duty, moral rules, and respect for persons"
    },
    {
        "question": "Which ethical theory highlights the significance of attentiveness in moral decision-making, particularly in interpersonal relationships and caregiving contexts?",
        "options": ["Utilitarianism", "Deontology", "Virtue Ethics", "Care Ethics"],
        "answer": "Care Ethics"
    }
 ]

    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken' not in st.session_state:
            st.session_state['quiz_taken'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Key ethical considerations in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")
        

##############################################################  TYPE OF ETHICS ###################################################################

def key_aspects():
    

    st.markdown("<h2 style='text-align: center;'>Key aspects of <span style='color: orange;'>ethics</span> in data analytics</h2>", unsafe_allow_html=True)

    

    key_aspects = """
        <p style='text-align: justify; font-size: 17px;'>
        <strong>Ethics in context of Analytics:</strong>  Building Trust, Responsibility, and Fairness In the world of data analytics, ethics isn't just a buzzword – it's the moral compass guiding every step of the journey. Imagine it as a guardian angel, ensuring that every move made with data respects people's privacy, plays fair, and is held accountable.
    <br><br>Firstly, let's talk about privacy. It's like protecting someone's secret diary; you wouldn't want it to fall into the wrong hands. Similarly, in data analytics, we must safeguard personal information and follow the rules laid out by privacy laws.
    <br><br>Transparency and accountability are like the trust between friends. Organizations need to be open about how they handle data, just like friends are honest with each other. And when something goes wrong, accountability means owning up to it and making it right.
    <br><br>Lastly, fairness is the golden rule. Just as you wouldn't want someone to play favorites, data analytics should strive to treat everyone equally. It means recognizing and correcting biases so that everyone gets a fair shot.
    </p>
    """

    st.markdown(key_aspects, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("<h2 style='text-align: center;'><span style='color: orange;'>Ethical</span> Considerations in Data Collection</h2>", unsafe_allow_html=True)

    st.image(r"C:\Users\edwin\Downloads\photo1.png", use_column_width=True)

    Ethical_considerations = """
        <p style='text-align: justify; font-size: 17px;'>
        <strong><span style='color: orange;'>Data Privacy:</span></strong>  Protecting individuals' personal information by obtaining proper consent, storing data securely, and adhering to privacy regulations. It's about respecting people's privacy rights and ensuring data is used responsibly.
    <br><br><strong><span style='color: orange;'>Bias and Fairness:</span></strong>  Recognizing and addressing biases in data or algorithms to ensure fairness and equity. By mitigating biases, we strive to avoid discriminatory outcomes and promote inclusivity in data analysis.
    <br><br><strong><span style='color: orange;'>Data Privacy:</span></strong>  Being open about data analytics processes, methodologies, and sources. It allows for better understanding and scrutiny, fostering trust and enabling stakeholders to comprehend how decisions are made.
    <br><br><strong><span style='color: orange;'>Accountability and Responsibility:</span></strong>  Holding individuals and organizations accountable for their actions and decisions in data analytics. It involves taking responsibility for the outcomes of data practices, including addressing any unintended consequences or harms.
    <br><br><strong><span style='color: orange;'>Data Security and Vulnerability:</span></strong>  Implementing robust security measures to protect data from unauthorized access, breaches, and vulnerabilities. It's about safeguarding data integrity and confidentiality to prevent data misuse or exploitation.
    </p>
        """
    st.markdown(Ethical_considerations, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)

    questions = [
    {
        "question": "What does data privacy in the context of analytics involve?",
        "options": [
            "Using data for personal gain without consent",
            "Protecting personal information by obtaining proper consent and adhering to privacy regulations",
            "Selling personal data to third-party companies",
            "Sharing personal information without informing individuals"
        ],
        "answer": "Protecting personal information by obtaining proper consent and adhering to privacy regulations"
    },
    {
        "question": "What is the significance of transparency and explainability in data analytics?",
        "options": [
            "Concealing data practices to maintain confidentiality",
            "Being open about data processes, fostering trust, and enabling scrutiny",
            "Limiting access to data to a select group of individuals",
            "Refusing to disclose information about data sources and methodologies"
        ],
        "answer": "Being open about data processes, fostering trust, and enabling scrutiny"
    },
    {
        "question": "Why is addressing bias and promoting fairness essential in data analytics?",
        "options": [
            "To exclude certain groups from accessing data",
            "To ensure everyone gets a fair opportunity and avoid discriminatory outcomes",
            "To manipulate data for personal gain",
            "To prioritize certain individuals' interests over others"
        ],
        "answer": "To ensure everyone gets a fair opportunity and avoid discriminatory outcomes"
    }
    ]


    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken2' not in st.session_state:
            st.session_state['quiz_taken2'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken2:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Data Privacy in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken2 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")


##############################################################  DATA PRIVACY ###################################################################


def data_privacy():
    

    st.markdown("<h2 style='text-align: Center;'>Data Privacy</h2>", unsafe_allow_html=True)

    data_privacy = """
        <p style='text-align: justify; font-size: 17px;'>
        <span style='color: orange;'><strong>Data privacy</span></strong> is the concept of ensuring the proper
         handling, protection, and responsible use of personal
          data. It involves maintaining an individual's right
           to control how their personal information is collected,
            processed, stored, and shared. With the increasing
             digitization of information and the growing reliance
              on data-driven technologies, data privacy has become
               a critical concern for individuals, organizations,
                and governments worldwide.
    </p>
    """

    st.markdown(data_privacy, unsafe_allow_html=True)

    

    st.write("")
    st.write("")
    st.write("")

    st.markdown("<h3 style='text-align: Center;'>Importance</h3>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns([2,10,2])

    with col2:
        st.image(r"C:\Users\edwin\Downloads\photo2.png", use_column_width=True)

    importance = """
        <p style='text-align: justify; font-size: 17px;'>
    <br><strong><span style='color: orange;'>Individual Rights:</span></strong> Data privacy is essential for individuals to control their personal information, enabling informed choices about its collection, use, and sharing.
    <br><br><strong><span style='color: orange;'>Trust and Confidence:</span></strong> Respecting data privacy builds trust between organizations and users, fostering stronger relationships and increased loyalty.
    <br><br><strong><span style='color: orange;'>Regulatory Compliance:</span></strong> Adhering to data privacy regulations like GDPR and CCPA is a legal requirement, essential for avoiding penalties and maintaining business operations.
    <br><br><strong><span style='color: orange;'>Security:</span></strong> Protecting data privacy is vital for preventing unauthorized access, identity theft, fraud, and other security breaches.
    <br><br><strong><span style='color: orange;'>Ethical Considerations:</span></strong> Respecting data privacy aligns with principles of fairness, respect, and transparency, demonstrating a commitment to treating individuals with dignity and upholding their rights.
    </p>
    """

    st.markdown(importance, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Best Practices</span> for Data Privacy Compliance</h3>", unsafe_allow_html=True)

    best_practices = """
        <p style='text-align: justify; font-size: 17px;'>
    <br><strong><span style='color: orange;'>Data Mapping and Inventory:</span></strong> Conduct a comprehensive data mapping exercise to identify all the personal data your organization collects, processes, stores, and shares. Maintain an up-to-date inventory of this data.
    <br><br><strong><span style='color: orange;'>Data Protection Impact Assessments (DPIAs):</span></strong> Perform DPIAs before implementing new data processing activities, systems, or technologies to assess potential privacy risks and identify appropriate mitigation measures.
    <br><br><strong><span style='color: orange;'>Privacy Policies and Notices:</span></strong> Develop clear and transparent privacy policies and notices that inform individuals about your data processing practices, their rights, and how to exercise them.
    <br><br><strong><span style='color: orange;'>Consent Management:</span></strong> Implement robust consent management processes to obtain valid and documented consent from individuals for processing their personal data, where required.
    <br><br><strong><span style='color: orange;'>Access Controls and Encryption:</span></strong> Implement appropriate access controls and encryption techniques to protect personal data from unauthorized access, disclosure, or misuse.
    </p>
    """

    st.markdown(best_practices, unsafe_allow_html=True)

    st.write("")
    st.write("")

    video_url = 'https://www.youtube.com/embed/bmgPd0rIrKw'
    video_html = f'<div style="display: flex; justify-content: center;"><iframe width="640" height="360" src="{video_url}" frameborder="0" allowfullscreen></iframe></div>'
    st.markdown(video_html, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Define the data
    # Data
    # Data
    data = {
        'country': ['United States', 'European Union', 'Canada', 'United Kingdom', 'Australia',
                    'Brazil', 'China', 'South Korea', 'Malaysia', 'Singapore', 'Japan', 'India',
                    'United States', 'United States', 'Thailand'],
        'law': ['California Consumer Privacy Act (CCPA)', 'General Data Protection Regulation (GDPR)',
                'Personal Information Protection and Electronic Documents Act (PIPEDA)', 'Data Protection Act 2018',
                'Privacy Act 1988', 'Data Protection Law (Lei Geral de Proteção de Dados - LGPD)',
                'Personal Information Protection Law (PIPL)', 'Personal Information Protection Act (PIPA)',
                'Personal Data Protection Act (PDPA)', 'Personal Data Protection Act (PDPA)',
                'Data Protection Directive', 'Digital Personal Data Protection Act, 2023',
                'Privacy Act of 1974', 'Children\'s Online Privacy Protection Act (COPPA)',
                'Personal Data Protection Act (PDPA)'],
        'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Values for coloring countries
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Streamlit app
    st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Data Protection Laws</span> Across Countries</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 10, 1])

    with col2:
        # Select theme
        st.markdown("""
        <style>
            body {
                color: white;
                background-color: #0E1117;
            }
        </style>
        """, unsafe_allow_html=True)

        fig = px.choropleth(df, 
                        locations="country", 
                        color="value",
                        hover_name="country",
                        hover_data={"value": False, "law": True},
                        locationmode='country names',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        labels={'law': 'Law'},
                        template='plotly_dark')

        fig.update_layout(
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font=dict(
                color="white"
            ),
            geo=dict(
                showframe=False,  # Hide frame around map
                projection_type='natural earth'  # Choose projection
            ),
            coloraxis_colorbar=dict(
                title="",
                tickvals=[]  # Hide tick values
            )
        )

        st.plotly_chart(fig)







    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)


    questions = [
    {
        "question": "Which of the following laws protects data privacy in Brazil?",
        "options": [
            "Personal Data Protection Act (PDPA)",
            "Privacy Act of 1974 (United States)",
            "Data Protection Law (Lei Geral de Proteção de Dados - LGPD)",
            "Personal Information Protection and Electronic Documents Act (PIPEDA)"
        ],
        "answer": "Data Protection Law (Lei Geral de Proteção de Dados - LGPD)"
    },
    {
        "question": "What is a Data Protection Impact Assessment (DPIA) used for?",
        "options": [
            "Assessing the impact of data breaches on individuals' privacy.",
            "Analyzing the potential risks to data security during storage.",
            "Evaluating potential privacy risks before implementing new data processing activities.",
            "Monitoring compliance with data privacy laws and regulations."
        ],
        "answer": "Evaluating potential privacy risks before implementing new data processing activities."
    },
    {
        "question": "Which of the following is NOT a recommended best practice for data privacy compliance?",
        "options": [
            "Implementing robust consent management processes.",
            "Developing clear and transparent privacy policies.",
            "Selling personal data to third-party companies without consent.",
            "Using appropriate access controls and encryption techniques."
        ],
        "answer": "Selling personal data to third-party companies without consent."
    }
    ]



    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken3' not in st.session_state:
            st.session_state['quiz_taken3'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken3:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Case Studies in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken3 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")


    

















    ########################  CASE STUDIES ##################################

##############################################################  CASE STUDY ###################################################################

def case_study_1():
    
    st.markdown("<h2 style='text-align: Center;'><span style='color: orange;'>Target's Holiday Havoc: </span>The 2013 Data Breach Debacle</span></h2>", unsafe_allow_html=True)


    #Background section
    st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Background</span></h3>", unsafe_allow_html=True)
    background_content = """
    <p style='text-align: justify; font-size: 16px;'>
    In 2013, Target, a prominent US retail chain, experienced a significant data breach during the holiday season. 
    Hackers gained access to Target's payment system, compromising the credit and debit card information of over 40 million customers. 
    Additionally, personal data such as names, addresses, and phone numbers of approximately 70 million individuals were exposed.
    </p>
    """
    st.markdown(background_content, unsafe_allow_html=True)


    col1,col2 = st.columns([2,2])

    with col1:

        # Ethical Issues section
        st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Ethical Issues</span></h3>", unsafe_allow_html=True)
        ethical_issues_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The breach raised ethical concerns regarding data security, transparency, and consumer trust. 
        Target's failure to adequately secure its payment system and promptly disclose the breach to affected customers 
        violated consumer trust and privacy expectations.
        </p>
        """
        st.markdown(ethical_issues_content, unsafe_allow_html=True)

    with col2:

        # Consequences section
        st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Consequences</span></h3>", unsafe_allow_html=True)
        consequences_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The breach resulted in substantial financial losses, legal actions, and reputational damage for Target. 
        The company faced numerous lawsuits, regulatory fines, and a decline in consumer trust and loyalty. 
        The incident highlighted the importance of robust cybersecurity measures, transparency, and communication 
        in safeguarding consumer data and maintaining trust.
        </p>
        """
        st.markdown(consequences_content, unsafe_allow_html=True)

    # Lessons Learned section
    st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Lessons Learned</span></h3>", unsafe_allow_html=True)
    lessons_learned_content = """
    <p style='text-align: justify; font-size: 16px;'>
    Companies must prioritize investment in cybersecurity, transparency, and communication 
    to protect consumer data and mitigate the impact of data breaches on their brand reputation and financial stability.
    </p>
    """
    st.markdown(lessons_learned_content, unsafe_allow_html=True)


    col1,col2,col3 = st.columns([2,10,2])

    with col2:
        # Embed YouTube video
        st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Video</span></h3>", unsafe_allow_html=True)
        video_link = "https://www.youtube.com/embed/tGXV-ZRwcUM"
        st.markdown(f'<iframe width="560" height="315" src="{video_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)


def case_study_2():
    # Background section
    st.markdown("<h2 style='text-align: Center;'><span style='color: orange;'>Background</span></h2>", unsafe_allow_html=True)
    background_content = """
    <p style='text-align: justify; font-size: 16px;'>
    Between 2013 and 2016, Yahoo suffered two massive data breaches compromising over 1.5 billion user accounts. 
    The breaches exposed personal data, including names, email addresses, and hashed passwords. 
    However, Yahoo did not disclose the breaches publicly until 2016, raising concerns about its security practices and transparency.
    </p>
    """
    st.markdown(background_content, unsafe_allow_html=True)

    # Ethical Issues section
    st.markdown("<h2 style='text-align: Center;'><span style='color: orange;'>Ethical Issues</span></h2>", unsafe_allow_html=True)
    ethical_issues_content = """
    <p style='text-align: justify; font-size: 16px;'>
    Yahoo's failure to adequately protect user data, timely disclose the breaches, and obtain user consent 
    violated ethical principles of data protection, transparency, and user privacy.
    </p>
    """
    st.markdown(ethical_issues_content, unsafe_allow_html=True)

    # Consequences section
    st.markdown("<h2 style='text-align: Center;'><span style='color: orange;'>Consequences</span></h2>", unsafe_allow_html=True)
    consequences_content = """
    <p style='text-align: justify; font-size: 16px;'>
    The breaches resulted in a loss of user trust, regulatory scrutiny, and a negative impact on Yahoo's acquisition deal with Verizon Communications. 
    Yahoo faced legal and financial repercussions, highlighting the importance of transparency, accountability, and regulatory compliance 
    in data breach response efforts.
    </p>
    """
    st.markdown(consequences_content, unsafe_allow_html=True)

    # Lessons Learned section
    st.markdown("<h2 style='text-align: Center;'><span style='color: orange;'>Lessons Learned</span></h2>", unsafe_allow_html=True)
    lessons_learned_content = """
    <p style='text-align: justify; font-size: 16px;'>
    Companies must prioritize transparency, accountability, and regulatory compliance 
    in disclosing data breaches promptly, protecting user data, and maintaining trust with stakeholders.
    </p>
    """
    st.markdown(lessons_learned_content, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([2,10,2])

    with col2:

        # Embed YouTube video
        st.markdown("<h3 style='text-align: Center;'><span style='color: orange;'>Video</span></h3>", unsafe_allow_html=True)
        video_link = "https://www.youtube.com/embed/zRQTTQpCbUo"
        st.markdown(f'<iframe width="560" height="315" src="{video_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

def case_study_3():
    st.header("Case Study 3")
    # Add your content for Case Study 3 here
    st.write("This is the content for Case Study 3.")

def case_study_4():
    st.header("Case Study 4")
    # Add your content for Case Study 4 here
    st.write("This is the content for Case Study 4.")


def case_study_5():
    st.header("Case Study 5")
    # Add your content for Case Study 5 here
    st.write("This is the content for Case Study 5.")



    ############################################## MAIN #############################################################

def leaderboard():
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>Leader<span style='color: orange;'>board</Span></h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    # Read the leaderboard data from the Excel file
    leaderboard_df = pd.read_excel(r"C:\Users\edwin\Downloads\leaderboard.xlsx", engine='openpyxl')

    # Sort the leaderboard in descending order of scores
    leaderboard_df = leaderboard_df.sort_values(by='Score', ascending=False)

    # Add a Rank column
    leaderboard_df['Rank'] = leaderboard_df['Score'].rank(ascending=False, method='dense').astype(int)

    # Style the table
    table_html = leaderboard_df[['Rank', 'Username', 'Score']].style.format({
        "Score": "{:.2f}",
        "Rank": "{:d}"
    }).set_table_styles([
        {"selector": "th", "props": [("text-align", "center"), ("font-weight", "bold"), ("background-color", "#2a2a2a"), ("color", "#ffffff"), ("padding", "12px")]},
        {"selector": "td", "props": [("text-align", "center"), ("color", "#ffffff"), ("padding", "12px")]},
        {"selector": "tr:nth-child(even)", "props": [("background-color", "#333333")]},
        {"selector": "tr:hover", "props": [("background-color", "#444444")]},
        {"selector": "table", "props": [("margin", "0 auto"), ("width", "auto"), ("max-width", "100%")]},  # Added this line
    ]).set_table_attributes('border="1" class="dataframe"').to_html()



    col1,col2,col3 = st.columns([5,3,6])

    with col2:
        # Display the leaderboard table
        st.markdown(table_html, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Display the current user's rank
    if 'username' in st.session_state and st.session_state.username:
        current_user_score = leaderboard_df[leaderboard_df['Username'] == st.session_state.username]
        if not current_user_score.empty:
            rank = current_user_score['Rank'].values[0]
            st.markdown(f"<h3 style='text-align: center; color: #ffffff;'>YOUR <span style='color: orange;'>RANK</span>: {int(rank)}</h3>", unsafe_allow_html=True)


# Define the sidebar navigation menu
def main():
    with st.sidebar:
        if 'username' in st.session_state:
            menu_title = f"{st.session_state.username}"

            
        else:
            menu_title = None
        selected = option_menu(
            menu_title=menu_title,
            options=["Home", "What is Ethics?", "Key Aspects", "Data Privacy", "Case Studies","Leaderboard"],
            icons=["house", "book", "list-task", "lock", "highlighter","trophy"],
            default_index=0,
        )

        if 'score' in st.session_state:
            score_html = f"""
            <div style="background-color: #121212; color: #FFFFFF; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.1), 0 6px 20px 0 rgba(255, 255, 255, 0.07); text-align: center;">
                <p style="font-weight: bold; font-size: 16px; margin-bottom: 10px;">Score</p>
                <p style="font-size: 24px; color: #4CAF50; margin: 0;">{st.session_state.score}</p>
            </div>
            """
            st.markdown(score_html, unsafe_allow_html=True)

            st.write("")
            st.write("")
            
            col1,col2,col3 = st.columns([1,2,1])

            with col2:

                if st.button("Submit Score") and not st.session_state.get('score_submitted', False):

                    leaderboard_df = pd.read_excel(r"C:\Users\edwin\Downloads\leaderboard.xlsx", engine='openpyxl')
                    new_entry = pd.DataFrame({'Username': [st.session_state.username], 'Score': [st.session_state.score]})
                    leaderboard_df = pd.concat([leaderboard_df, new_entry], ignore_index=True)
                    leaderboard_df.to_excel(r"C:\Users\edwin\Downloads\leaderboard.xlsx", index=False, engine='openpyxl')
                    st.session_state.score_submitted = True  # Set score_submitted to True
                    st.success(f"Score submitted successfully! Your score: {st.session_state.score}")
                elif st.session_state.get('score_submitted', False):
                    st.warning("Score already submitted!")
        else:
            st.session_state.score = 0

            

    if selected == "Home":
         home()
    elif selected == "What is Ethics?":
         what_is_ethics()
    elif selected == "Key Aspects":
        key_aspects()
    elif selected == "Data Privacy":
        data_privacy()
    elif selected == "Case Studies":
            case_study_submenu = st.selectbox("Select a Case Study", ["Case 1", "Case 2", "Case 3", "Case 4", "Case 5"])
            if case_study_submenu == "Case 1":
                case_study_1()
            elif case_study_submenu == "Case 2":
                case_study_2()
            elif case_study_submenu == "Case 3":
                case_study_3()
            elif case_study_submenu == "Case 4":
                case_study_4()
            elif case_study_submenu == "Case 5":
                case_study_5()
    elif selected  == "Leaderboard":
        leaderboard()



if __name__ == "__main__":
    main()