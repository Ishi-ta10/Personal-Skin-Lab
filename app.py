import streamlit as st
import pandas as pd
from model import RecommendationEngine
from ingredients_db import INGREDIENT_GLOSSARY, PRODUCT_IMAGES, BRAND_INFO
import json

# Page configuration
st.set_page_config(
    page_title="SkinCare Genius",
    page_icon="💆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cache the engine initialization
@st.cache_resource
def load_engine():
    return RecommendationEngine()

st.markdown("""
<style>
    /* Minimal, Modern Design */
    * {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    body, .main {
        background-color: #FAFBFC;
        color: #1a202c;
    }
    
    /* Typography */
    h1 {
        color: #1a202c;
        font-weight: 800;
        font-size: 2.8rem;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.02em;
    }
    
    h2 {
        color: #1a202c;
        font-weight: 700;
        font-size: 1.3rem;
        margin: 2rem 0 1rem 0;
        letter-spacing: -0.01em;
    }
    
    h3 {
        color: #1a202c;
        font-weight: 600;
        font-size: 1rem;
        margin: 0;
    }
    
    h4 {
        color: #1a202c;
        font-weight: 600;
        font-size: 0.9rem;
        margin: 0.5rem 0 0.25rem 0;
    }
    
    p, li, span {
        color: #4a5568;
        line-height: 1.6;
    }
    
    /* Cards - Minimal style */
    .card-container {
        background: white;
        border: none;
        border-radius: 12px;
        padding: 1.25rem;
        margin: 0.75rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        color: #1a202c;
        transition: box-shadow 0.2s ease;
    }
    
    .card-container:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    
    .card-container p, .card-container h4, .card-container h5 {
        color: #2d3748;
        margin: 0.5rem 0;
    }
    
    .card-container ul, .card-container ol {
        color: #4a5568;
        padding-left: 1.5rem;
    }
    
    .card-container li {
        color: #4a5568;
        margin: 0.35rem 0;
    }
    
    /* Ingredient tags */
    .ingredient-tag {
        display: inline-block;
        background: #f0f4ff;
        color: #4c51bf;
        padding: 0.35rem 0.75rem;
        border-radius: 16px;
        margin: 0.25rem 0.25rem 0.25rem 0;
        font-size: 0.8rem;
        font-weight: 500;
        border: 1px solid #e0e7ff;
    }
    
    /* Brand badges */
    .brand-badge {
        display: inline-block;
        background: #f3f4f6;
        color: #374151;
        padding: 0.35rem 0.75rem;
        border-radius: 16px;
        margin: 0.25rem 0.25rem 0.25rem 0;
        font-size: 0.8rem;
        font-weight: 500;
        border: 1px solid #e5e7eb;
    }
    
    /* Morning routine */
    .morning-routine {
        background: #fffbeb;
        border-left: 3px solid #f59e0b;
        border-radius: 12px;
        padding: 1.25rem;
        color: #5a3a0a;
    }
    
    .morning-routine h4, .morning-routine p, .morning-routine li {
        color: #5a3a0a;
    }
    
    /* Night routine */
    .night-routine {
        background: #f5f3ff;
        border-left: 3px solid #8b5cf6;
        border-radius: 12px;
        padding: 1.25rem;
        color: #4a1d7a;
    }
    
    .night-routine h4, .night-routine p, .night-routine li {
        color: #4a1d7a;
    }
    
    /* Safety note */
    .safety-note {
        background: #fef2f2;
        border-left: 3px solid #ef4444;
        border-radius: 12px;
        padding: 1.25rem;
        margin: 1rem 0;
        color: #7f1d1d;
    }
    
    .safety-note h3, .safety-note p, .safety-note li, .safety-note strong {
        color: #7f1d1d;
    }
    
    /* Success badge */
    .success-badge {
        background: #f0fdf4;
        border-left: 3px solid #22c55e;
        border-radius: 12px;
        padding: 1.25rem;
        margin: 1rem 0;
        color: #166534;
    }
    
    .success-badge h3, .success-badge p {
        color: #166534;
    }
    
    /* Input section */
    .input-section {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        color: #1a202c;
    }
    
    /* Header */
    .header-main {
        background: white;
        color: #1a202c;
        padding: 2.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        border-bottom: 2px solid #4c51bf;
    }
    
    .header-main h1 {
        color: #1a202c;
        margin: 0;
        font-size: 2.8rem;
    }
    
    .header-main p {
        color: #718096;
        margin: 0.75rem 0 0 0;
        font-size: 0.95rem;
        font-weight: 400;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'engine' not in st.session_state:
    st.session_state.engine = load_engine()

if 'last_recommendation' not in st.session_state:
    st.session_state.last_recommendation = None

# Sidebar
with st.sidebar:
    st.title("💆 SkinCare Genius")
    st.markdown("Your personal skin advisor")
    st.divider()
    
    with st.expander("📖 How to Use"):
        st.markdown("""
        1. Describe your skin concerns naturally
        2. Select your skin type (optional)
        3. Click "Analyze"
        4. Get personalized recommendations
        """)
    
    with st.expander("📚 Ingredients"):
        search = st.text_input("Search ingredients:", placeholder="e.g., Retinol")
        ingredient_list = [(k, v) for k, v in INGREDIENT_GLOSSARY.items() if search.lower() in k.lower()]
        
        if ingredient_list:
            for name, desc in ingredient_list[:8]:
                st.markdown(f"**{name}**")
                st.caption(desc)
        else:
            st.info("No ingredients found")
    
    with st.expander("⚠️ Disclaimer"):
        st.markdown("""
        This tool provides general guidance only. 
        
        **See a dermatologist for:**
        - Persistent skin issues
        - Severe reactions
        - Medical conditions
        """)
    
    st.divider()
    st.caption("Always patch test new products before full use")

# Header
st.markdown('<div class="header-main"><h1>💆 SkinCare Genius</h1><p>Get personalized skincare recommendations</p></div>', unsafe_allow_html=True)

# Input section
st.markdown('<div class="input-section">', unsafe_allow_html=True)

col1, col2 = st.columns([2.5, 1])

with col1:
    user_input = st.text_area(
        "Describe your skin",
        placeholder="E.g., oily, acne-prone skin with dark spots",
        height=90,
        label_visibility="collapsed"
    )

with col2:
    st.markdown("")
    skin_type = st.selectbox(
        "Skin Type",
        ["Any", "Dry", "Oily", "Normal", "Sensitive", "Combination"],
        label_visibility="collapsed"
    )
    st.markdown("")
    st.markdown("")
    submit_button = st.button("Analyze", use_container_width=True, type="primary")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

# Results
if submit_button and user_input.strip():
    with st.spinner("Analyzing..."):
        results = st.session_state.engine.get_recommendations(
            user_input, 
            skin_type if skin_type != "Any" else None
        )
        st.session_state.last_recommendation = results
    
    if results:
        st.markdown('<div class="success-badge">✅ Analysis Complete</div>', unsafe_allow_html=True)
        
        st.markdown("")
        
        # Detected concerns
        st.markdown("**Your Skin Concerns**")
        concern_text = ", ".join([c.title() for c in results['concerns']])
        st.info(concern_text)
        
        st.markdown("")
        
        # Ingredients
        st.markdown("**Recommended Ingredients**")
        ingredient_html = ""
        for ing in results['ingredients'][:12]:
            ingredient_html += f'<span class="ingredient-tag">{ing.title()}</span>'
        st.markdown(ingredient_html, unsafe_allow_html=True)
        
        st.markdown("")
        
        # Benefits and Directions
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Why These Ingredients**")
            st.markdown(f'<div class="card-container">{results["benefits"]}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown("**How to Use**")
            st.markdown(f'<div class="card-container">{results["directions"]}</div>', unsafe_allow_html=True)
        
        st.markdown("")
        
        # Brands
        st.markdown("**Recommended Brands**")
        brand_html = ""
        for brand in results['brands'].split(", ")[:8]:
            brand_html += f'<span class="brand-badge">{brand.strip()}</span>'
        st.markdown(brand_html, unsafe_allow_html=True)
        
        st.markdown("")
        
        # Routines
        st.markdown("**Your Daily Routine**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div class="morning-routine"><h4>🌅 Morning</h4>{results.get("morning_routine", "")}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="night-routine"><h4>🌙 Night</h4>{results.get("night_routine", "")}</div>', unsafe_allow_html=True)
        
        st.markdown("")
        
        # Safety
        if results.get('notes'):
            st.markdown("**Safety Notes**")
            st.markdown(f'<div class="safety-note">{results["notes"]}</div>', unsafe_allow_html=True)
        
        st.divider()
        st.markdown("""
        **Tips for Best Results**
        - 🧪 Patch test first (24-48 hours)
        - ⏱️ Introduce one product at a time  
        - ⏳ Results take 4-8 weeks
        - ☀️ Always use SPF 30+
        - 💧 Stay hydrated
        """)
    else:
        st.warning("No recommendations found. Try describing your concerns differently.")

# Footer
st.divider()
st.markdown("""
<div class="safety-note">
<strong>⚠️ Medical Disclaimer:</strong> This tool is for general guidance only. See a dermatologist for persistent issues, severe reactions, or medical conditions.
</div>
""", unsafe_allow_html=True)
st.caption("© 2024 SkinCare Genius")
