import streamlit as st
from model import RecommendationEngine
from ingredients_db import INGREDIENT_GLOSSARY, BRAND_INFO

st.set_page_config(page_title="SkinCare Genius", page_icon="💆", layout="wide")

@st.cache_resource
def load_engine():
    return RecommendationEngine()

st.markdown("<style>p, li { color: #4a5568; } .tag { display: inline-block; background: #f0f4ff; color: #4c51bf; padding: 4px 12px; border-radius: 16px; margin: 4px; font-size: 12px; }</style>", unsafe_allow_html=True)

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
