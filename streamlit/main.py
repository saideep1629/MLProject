import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("alzheimer.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(256,256))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    confidence = round(100 * (np.max(predictions)), 2)
    return np.argmax(predictions), confidence #return index of max element



#Sidebar
st.sidebar.title("Alzheimer's Predictor")
app_mode = st.sidebar.selectbox("Options",["Home","About","Alzheimer Prediction","Prevention"])

st.markdown(
    """
    <style>
    /* CSS for sidebar title */
    .sidebar .sidebar-content .sidebar-section div[data-testid="stSidebar"] div[role="heading"] {
        color: blue; /* Set text color to blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)



#Main Page
if(app_mode=="Home"):
    st.header("ALZHEIMER DISEASE PREDICTION")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_760599_1696326718990377.jpg");
    background-repeat: no repeat;
    backgground-size: cover;
    }
    
     [data-testid="stSidebar"] {
      background-image: url("https://wallpapers.com/images/hd/light-orange-background-l9joxufvtdllqp3v.jpg");
     background-repeat: no repeat;
    backgground-size: cover;
     }
     
     [data-testid="stSidebar"] {
     .sidebar.sidebar-section {
        background-color: #000080; /* Semi-transparent white background for content */
        padding: 10px; /* Add padding for better readability */
    }
    .sidebar.sidebar-content {
        color:#000080; /* Set text color to white */
    }
     }

     [data-testid="stHeader"] {
     background-color: rgba(0,0,0,0);
     }
    </style>

""" 

    st.markdown(page_bg_img, unsafe_allow_html=True)
    image_path = "home.jpg"
    
    #st.markdown(image_path,use_column_width=True)

    st.markdown(
    """
    <style>
    .bullet {
        list-style-type: disc;
        margin-left: 10px;
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.markdown(
    """
    <ul class="bullet">
        <li>Alzheimer's disease is a progressive neurological disorder that causes memory loss, cognitive decline, and behavioral changes.</li>
        <br>
        <li>It is the most common cause of dementia, accounting for 60-80% of dementia cases.</li> <br>
        <li>Alzheimer's primarily affects older adults, typically starting after the age of 65, although early-onset Alzheimer's can occur in individuals as young as their 30s or 40s.</li> <br>
        
    </ul>
    """,
    unsafe_allow_html=True
)
    st.video('https://www.youtube.com/watch?v=wfLP8fFrOp0')


#About Project
elif(app_mode=="About"):
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_760599_1696326718990377.jpg");
    background-repeat: no repeat;
    backgground-size: cover;
    }
    
     [data-testid="stSidebar"] {
     background-image: url("https://wallpapers.com/images/hd/light-orange-background-l9joxufvtdllqp3v.jpg");
     background-repeat: no repeat;
    backgground-size: cover;
     }

     [data-testid="stHeader"] {
     background-color: rgba(0,0,0,0);
     }
    </style>

""" 

    st.markdown(page_bg_img, unsafe_allow_html=True)



    col1, col2, col3 = st.columns(3)

    with col1:
     st.header("Early-stage Alzheimer's (mild)")
     st.image("photos/early.png")

    with col2:
        st.header("Middle-stage Alzheimer's (moderate)")
        st.image("photos/middle.png")

    with col3:
        st.header("Late-stage Alzheimer's (severe)")
        st.image("photos/final.png")

    st.title("Symptoms")
    st.markdown(
    """
    <ul class="bullet">
        <li>Forgetting things or recent events</li>
        <li>Losing or misplacing things</li>
        <li>Getting lost when walking or driving</li>
        <li>Being confused, even in familiar places</li>
        <li>Losing track of time</li>
        <li>Difficulties solving problems or making decisions</li>
        <li>Problems following conversations or trouble finding words</li>
        <li>Difficulties performing familiar tasks</li>
        <li>Misjudging distances to objects visually.</li>
        
    </ul>
    """,
    unsafe_allow_html=True
)

    

           

#Prediction Page
elif(app_mode=="Alzheimer Prediction"): 
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_760599_1696326718990377.jpg");
    background-repeat: no repeat;
    backgground-size: cover;
    }
    
     [data-testid="stSidebar"] {
     background-image: url("https://wallpapers.com/images/hd/light-orange-background-l9joxufvtdllqp3v.jpg");
     background-repeat: no repeat;
    backgground-size: cover;
     }

     [data-testid="stHeader"] {
     background-color: rgba(0,0,0,0);
     }
    </style>

""" 

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.header("Alzheimer Disease Prediction")
    test_image = st.file_uploader("Please upload an image:", type=["jpg","jpeg","png"])
    if test_image is not None:
        file_extension = test_image.name.split(".")[-1].lower()
        if file_extension not in ["jpg"]:
           st.error("Please upload valid image.")
        else:
           if st.button("Show Image"):
              st.image(test_image, width=400, use_column_width=True)
           if st.button("Predict"):
                st.write("Our Prediction")
                result_index, confidence = model_prediction(test_image)
                # Reading Labels
                class_name = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
                st.success(f"The result is {class_name[result_index]} with confidence {confidence}.")
    else:
        st.write("upload image for prediction")
    

elif(app_mode=="Prevention"):
    st.header("Preventions")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_760599_1696326718990377.jpg");
    background-repeat: no repeat;
    backgground-size: cover;
    }
    
     [data-testid="stSidebar"] {
     background-image: url("https://wallpapers.com/images/hd/light-orange-background-l9joxufvtdllqp3v.jpg");
     background-repeat: no repeat;
    backgground-size: cover;
     }

     [data-testid="stHeader"] {
     background-color: rgba(0,0,0,0);
     }
    </style>

""" 

    st.markdown(page_bg_img, unsafe_allow_html=True)

# List of image paths and corresponding sentences
    images_and_sentences = [
    {'path': 'photos/blood.jpg', 'sentence': 'Prevent and manage high blood pressure. '},
    {'path': 'photos/sugar.webp', 'sentence': 'Manage blood sugar.'},
    {'path': 'photos/weight.jpeg', 'sentence': 'Maintain a healthy weight.'},
    {'path': 'photos/active.jpg', 'sentence': 'Be physically active.'}
    ]

# Display images and sentences in rows with two images per row
    for i in range(0, len(images_and_sentences), 2):
       col1, col2 = st.columns(2)  # Create two columns
       with col1:
         st.image(images_and_sentences[i]['path'], use_column_width=True)  # Display first image
         st.write(images_and_sentences[i]['sentence'])  # Display sentence below the first image
       with col2:
          if i + 1 < len(images_and_sentences):
            st.image(images_and_sentences[i + 1]['path'], use_column_width=True)  # Display second image
            st.write(images_and_sentences[i + 1]['sentence'])  # Display sentence below the second image
    
    st.video('https://www.youtube.com/watch?v=EdrfZYs3uuc')
    
    
     
