import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# def load_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# load_css('dark_theme.css')

# Function to draw a heart using matplotlib
def draw_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    
    # Parametric equations for a heart shape
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red', linewidth=3)
    
    # Customizing the plot
    ax.fill(x, y, "r")
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.axis('off')  # Remove axis
    
    # Add text to the heart
    ax.text(0, 1, "I love you Sarina", fontsize=24, color='white', fontweight='bold', ha='center')
    ax.text(0, -8, "From Arash", fontsize=18, color='white', fontweight='bold', ha='center')

    return fig

# Streamlit app setup
# st.title("Heart Drawing")

# Draw the heart
fig = draw_heart()

# Display the heart in Streamlit
st.pyplot(fig)
