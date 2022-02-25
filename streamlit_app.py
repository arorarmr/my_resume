import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Rahul Arora, Data Scientist
##### *Resume* 
''')

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Software Developer, Researcher, Machine Learning Engineer and Trainer with almost ten years of experience in software development industry. 
- Strong verbal and written communication skills and passionate to solve challenging problems with machine learning.
- Filed 5 patents, 1 research paper and 1 research poster.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">Rahul Arora</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#recognitions">Recognitions</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#personal-projects">Personal Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b, c):
  col1, col2 = st.columns([5,1])
  with col1:
    st.markdown(a)
    st.markdown(b)
  with col2:
    st.markdown(c)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1,3,1])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
    
def txt5(a, b):
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

#####################
st.markdown('''
## Education
''')

txt('**PG Diploma in Advanced Computing**, C-DAC Bangalore',
'2011-2012')
st.markdown('''
- Percentage: `73`
''')

txt('**B.Tech in Computer Science**, United College of Engineering, Greater Noida',
'2007-2011')
st.markdown('''
- Percentage: `72.4`
''')

txt('**Intermediate (12th)** Harmilap Mission School, Kanpur',
'2006-2007')
st.markdown('''
- Percentage: `77`
''')

txt('**Higher Secondary (10th)** Harmilap Mission School, Kanpur',
'2004-2005')
st.markdown('''
- Percentage: `83`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Bixby Voice Assistant Analytics**, "Data Scientist, Samsung Research, Bangalore, India",
'2020-Present')
st.markdown('''

- Created text classifiers to identify gibberish text with 90% accuracy for different languages using state-of-the-art models (BERT, ULMFit)
- Worked on sentence rephrasing (reformulation) problem to handle contextual user utterances using encoder decoder architecture
- Used Back-Translation and EDA methods for creating augmented text datasets
- Optimized BERT model in production for faster inference time reducing cost to the company
- Conducted several organizational and team level trainings on data structures for internal coding challenges
''')

txt('**Non-Invasive Glucose Monitoring**, "Data Scientist, Samsung Research, Bangalore, India",
'2018-2020')
st.markdown('''
- Developed several algorithms for predicting glucose information from NIR and PPG signals
- Used various signal processing methods such as MSC, E-MSC and Wavelet Transform
- Worked on Linear Regression, SVR, Ensemble Method, Cross Validation and Feature Selection
- Filed patents and papers based on the algorithms developed
''')

txt('**OpenCL APIs Implementation For GPU**, "Lead Software Developer, Samsung Research, Bangalore, India",
'2016-2018')
st.markdown('''
- Implemented OpenCL APIs for Samsung GPU according to OpenCL 1.2 specification by Khronos
- Worked on APIs such as clDeviceType, clCommandQueue, clProgram and clRelease
- Fixed several bugs for already implemented API’s using C++ language
''')

txt('**Performance Improvement using OpenCL and OpenGL**, "Senior Software Developer, Samsung Research, Bangalore, India",
'2014-2016')
st.markdown('''
- Created OpenCL kernels for SKIA API’s (2D graphics library for android), Low-Light Imaging and Kids-Mode Application. The solution worked for both MALI and QCOM GPUs
- Fish eye images were converted and stitched together using OpenGL framework to create a single 360 images for Samsung camera devices
''')

txt('**Crypt Analysis using hybrid computing**, "Software Developer, C-DAC R&D, Bangalore, India",
'2012-2014')
st.markdown('''
- Retrieved metadata information from encrypted files such as Winzip and MS Word files
- Generated keyboard patterns dictionaries serving as passwords for encrypted files
- Modified POCL API’s (open source OpenCL code) to add support for FPGA devices.
- Some kernel functions were built for specific algorithms to run on FPGA and GPU devices
''')


#####################
st.markdown('''
## Recognitions
''')
txt4('Patent','A drift, noise and motion artifact correction method for photoplethysmogram (PPG) signal', 'https://patents.google.com/patent/US20200323493A1/en')
txt4('Patent','Method and apparatus for pre-processing PPG signal', 'https://patents.google.com/patent/US20200237312A1/en')
txt4('Patent','Method and systems for performing universal calibration to non-invasively determine blood glucose concentration','https://patents.google.com/patent/US20200022627A1/en')
txt4('Patent','Method of preprocessing near infrared (NIR) spectroscopy data for non-invasive glucose monitoring and apparatus thereof','https://patents.google.com/patent/US20200352517A1/en')
txt4('Patent','Method and system for predicting blood compound concentration of a target','https://patents.google.com/patent/US20210247304A1/en')

txt4('Research Paper','Motion artifact correction for photoplethysmogram (PPG) using advanced wavelet-based method','https://ieeexplore.ieee.org/abstract/document/8857131')
txt4('Research Poster','Motion artifact removal method for photoplethysmogram (PPG) signal','EMBC 2019')

txt5('Award','Spot Award for relentless effort and contribution in glucose monitoring project')
txt5('Award','Employee of the Month Award for quick learning and fast project delivery')
txt5('Award','C-DAC Best Student Award for best performance among all students')


#####################
st.markdown('''
## Personal Projects
''')

txt('**NLP Based Projects**','')
st.markdown('''

- Fake and real news classification using Bi-Directional LSTM model (implemented from scratch)
- Image captioning using LSTM and pre-trained VGG-16 model on Flicker Dataset from Kaggle
- German to English machine translation using SeqToSeq model (implemented from scratch)
- Fake and real disaster tweet classification using BERT (with pre-trained huggingface model)
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`C`, `C++`, `Python`')
txt3('Data Processing/Wrangling', '`Pandas`, `Numpy`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`Pytorch, Torchtext`')
txt3('Tools', '`MLflow`,`Visual Studio`, `JIRA`, `Source Insight`, `Perforce`,')
txt3('Work Areas', '`Software Development`, `Machine Learning`, `Deep Learning`, `Hiring Committee`, `Technical Trainer`')


#####################
st.markdown('''
## Contact
''')
txt2('Phone', '+918095518050')
txt2('Email', 'arora.rmr@gmail.com')
txt2('LinkedIn', 'https://www.linkedin.com/in/rahularora16')
txt2('Google Scholar', 'https://scholar.google.com/citations?user=vZVLuyQAAAAJ&hl=en')
