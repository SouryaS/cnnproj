import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Set page config with dark theme
st.set_page_config(
    page_title="🐱 vs 🐶 Classifier",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS and JavaScript for enhanced styling and animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');

/* Particle effect container */
.particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    pointer-events: none;
}

/* Glassmorphism effect */
.glass-effect {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}

.stApp {
    max-width: 1000px;
    margin: 0 auto;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    min-height: 100vh;
    color: #fff;
}

.main-header {
    text-align: center;
    padding: 2rem 0;
    background: linear-gradient(120deg, #155799, #159957);
    border-radius: 20px;
    margin: 2rem auto;
    color: white;
    max-width: 90%;
    animation: fadeInDown 1s ease-out;
    position: relative;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}

.main-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transform: rotate(45deg);
    animation: shine 3s infinite;
}

.main-header h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.upload-container {
    background: transparent;
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    margin: 2rem auto;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    border: none;
    max-width: 90%;
    animation: fadeIn 1s ease-out;
}

.upload-container:hover {
    background: rgba(255, 255, 255, 0.05);
    box-shadow: 0 0 20px rgba(21, 153, 87, 0.1);
}

.stFileUploader {
    background: transparent !important;
}

.stFileUploader > div {
    background: transparent !important;
    border: none !important;
}

.stFileUploader > div:hover {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 2px dashed rgba(255, 255, 255, 0.2) !important;
}
    background: rgba(255, 255, 255, 0.1);
    border-color: #159957;
    box-shadow: 0 0 20px rgba(21, 153, 87, 0.1);
}

.stButton>button {
    background: linear-gradient(120deg, #155799, #159957) !important;
    color: white !important;
    border: none !important;
    padding: 0.5rem 2rem !important;
    border-radius: 25px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(21, 153, 87, 0.2);
}

.prediction-container {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 20px;
    margin: 2rem auto;
    text-align: center;
    max-width: 90%;
    animation: fadeInUp 1s ease-out;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

@keyframes shine {
    0% { transform: translateX(-100%) rotate(45deg); }
    100% { transform: translateX(100%) rotate(45deg); }
}

/* Custom animations */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.prediction-result {
    font-size: 2rem;
    font-weight: 600;
    margin: 1rem 0;
    padding: 1rem;
    border-radius: 10px;
    background: rgba(21, 153, 87, 0.1);
}

.stProgress > div > div {
    background-color: #159957 !important;
}

.stImage {
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Initialize particles.js
    particlesJS('particles', {
        particles: {
            number: { value: 80, density: { enable: true, value_area: 800 } },
            color: { value: '#ffffff' },
            shape: { type: 'circle' },
            opacity: { value: 0.5, random: false },
            size: { value: 3, random: true },
            line_linked: {
                enable: true,
                distance: 150,
                color: '#ffffff',
                opacity: 0.4,
                width: 1
            },
            move: {
                enable: true,
                speed: 2,
                direction: 'none',
                random: false,
                straight: false,
                out_mode: 'out',
                bounce: false
            }
        },
        interactivity: {
            detect_on: 'canvas',
            events: {
                onhover: { enable: true, mode: 'repulse' },
                onclick: { enable: true, mode: 'push' },
                resize: true
            }
        },
        retina_detect: true
    });
});
</script>
""", unsafe_allow_html=True)

# Add particles container
st.markdown('<div id="particles" class="particles"></div>', unsafe_allow_html=True)

# Title and description with enhanced styling
st.markdown('<div class="main-header glass-effect"><h1 class="animate__animated animate__fadeIn">🐱 vs 🐶 Classifier</h1><p class="animate__animated animate__fadeIn animate__delay-1s">Upload an image of a cat or dog and let our AI model classify it!</p></div>', unsafe_allow_html=True)
st.markdown("""<div style='text-align: center; color: #666;'>
Built with ❤️ using TensorFlow and Streamlit
</div>""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('trained_model.h5')
    return model

def preprocess_image(image):
    img = image.resize((64, 64))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def main():
    try:
        model = load_model()
        
        # File uploader with custom container
        st.markdown('<div class="upload-container">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Drop your image here or click to browse", 
            type=["jpg", "jpeg", "png"],
            help="Upload a cat or dog image for classification"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        if uploaded_file is not None:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_container_width=True)
            
            # Add a prediction button
            if st.button('Predict'):
                with st.spinner('Analyzing image...'):
                    # Preprocess the image
                    processed_image = preprocess_image(image)
                    
                    # Make prediction
                    prediction = model.predict(processed_image)
                    confidence = prediction[0][0]
                    
                    # Display results in a styled container
                    st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
                    st.markdown('### 🎯 Prediction Results')
                    
                    if confidence > 0.5:
                        result = f"🐶 It's a Dog!"
                        conf_text = f"Confidence: {confidence:.2%}"
                    else:
                        result = f"🐱 It's a Cat!"
                        conf_text = f"Confidence: {(1-confidence):.2%}"
                    
                    st.markdown(f'<div class="prediction-result">{result}</div>', unsafe_allow_html=True)
                    st.markdown(f'<p style="color: #666;">{conf_text}</p>', unsafe_allow_html=True)
                    
                    # Display confidence bar with animation
                    st.markdown('<div style="padding: 1rem;">', unsafe_allow_html=True)
                    st.progress(float(confidence if confidence > 0.5 else 1-confidence))
                    st.markdown('</div></div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.info("Please make sure the model file 'trained_model.h5' exists in the project directory.")

if __name__ == "__main__":
    main()