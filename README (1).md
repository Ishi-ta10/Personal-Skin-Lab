# SkinCare Genius - AI-Powered Skincare Recommendation App

A sophisticated Streamlit-based application that uses natural language processing to analyze skin concerns and provide personalized, dermatology-backed skincare recommendations.

## Features

### Core Functionality
- **Natural Language Input**: Describe your skin concerns in plain English
- **Smart NLP Analysis**: Detects multiple skin concerns simultaneously (acne, dryness, hyperpigmentation, etc.)
- **Personalized Recommendations**: Intelligent mapping of concerns to recommended ingredients and products
- **Multi-label Classification**: Handles complex skin profiles with multiple overlapping concerns
- **Brand Suggestions**: Curated recommendations from 50+ premium skincare brands

### User Experience
- **Modern, Beautiful Interface**: Clean design with color-coded cards and intuitive navigation
- **Theme Support**: Light and dark mode options
- **Sidebar Navigation**: Quick access to ingredient glossary, disclaimers, brand info, and tips
- **Visual Organization**: Separate sections for concerns, ingredients, routines, and safety notes
- **Interactive Cards**: Hover effects and gradient styling for enhanced engagement

### Content & Recommendations
- **Ingredient Glossary**: 40+ skincare ingredients with detailed explanations
- **Directions for Use**: Step-by-step guidance on application and frequency
- **Morning & Night Routines**: Generated routines tailored to your concerns
- **Safety Information**: Important cautions and patch test recommendations
- **Brand Information**: Price ranges and specialties of featured brands
- **50+ Skin Concerns**: Comprehensive coverage from acne to anti-aging

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or Download the Repository**
   \`\`\`bash
   git clone <repository-url>
   cd skincare-genius
   \`\`\`

2. **Create a Virtual Environment (Recommended)**
   \`\`\`bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   \`\`\`

3. **Install Dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run the Application**
   \`\`\`bash
   streamlit run app.py
   \`\`\`

5. **Access the App**
   - The app will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

## Usage

### Getting Recommendations

1. **Describe Your Skin Concerns**
   - Use the text area in the main section to describe your skin
   - Be specific about multiple concerns if applicable
   - Example: "I have oily, acne-prone skin with dark spots and enlarged pores"

2. **Filter by Skin Type (Optional)**
   - Select your skin type from the dropdown menu
   - Options: Any, Dry, Oily, Normal, Sensitive, Combination

3. **Click Analyze**
   - The app processes your input using NLP keyword matching
   - Returns personalized recommendations within seconds

4. **Review Recommendations**
   - **Detected Concerns**: Your identified skin issues
   - **Recommended Ingredients**: Active ingredients to address your concerns
   - **Benefits**: Explanations of how ingredients help
   - **Directions**: How and when to use products
   - **Brands**: Suggested brands categorized by price range
   - **Daily Routine**: Morning and night skincare routine
   - **Safety Notes**: Important precautions

### Sidebar Features

- **About Section**: Learn about the app and how it works
- **Ingredient Glossary**: Search 40+ ingredients with descriptions
- **Disclaimers**: Important medical and safety information
- **Brand Information**: Details on featured skincare brands
- **Pro Tips**: Best practices for skincare routine success
- **Theme Toggle**: Switch between light and dark modes

## Sample Inputs & Expected Outputs

### Example 1: Acne-Prone & Oily Skin
**Input:** "I have oily, acne-prone skin with blackheads"

**Expected Output:**
- Concerns: Acne, Oily Skin, Blackheads
- Ingredients: Salicylic Acid, Niacinamide, Benzoyl Peroxide, Tea Tree Oil
- Brands: The Ordinary, Cosrx, Paula's Choice, Minimalist
- Morning Routine: Cleanser → Serum → Moisturizer → SPF
- Night Routine: Cleanser → Salicylic Acid Exfoliant → Moisturizer

### Example 2: Dry & Sensitive Skin
**Input:** "My skin is dry, sensitive, and gets irritated easily"

**Expected Output:**
- Concerns: Dry Skin, Sensitivity, Redness
- Ingredients: Hyaluronic Acid, Glycerin, Ceramides, Centella Asiatica
- Brands: CeraVe, Tatcha, La Roche Posay, LANEIGE
- Morning Routine: Gentle Cleanser → Hydrating Serum → Rich Moisturizer → SPF
- Night Routine: Gentle Cleanser → Calming Toner → Night Moisturizer

### Example 3: Hyperpigmentation & Dark Spots
**Input:** "I have dark spots and hyperpigmentation from sun damage"

**Expected Output:**
- Concerns: Hyperpigmentation, Dark Spots, Sun Damage
- Ingredients: Vitamin C, Niacinamide, Kojic Acid, Arbutin
- Brands: LANEIGE, Peach & Lily, Sunday Riley
- Morning Routine: Brightening Serum with SPF 50+
- Night Routine: Treatment with SPF Protection During Day

## Project Structure

\`\`\`
skincare-genius/
├── app.py                 # Main Streamlit application
├── model.py              # NLP recommendation engine
├── ingredients_db.py     # Ingredient and brand database
├── utils.py              # Utility functions and helpers
├── config.py             # Configuration constants
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── skincare_dataset.csv  # Optional: CSV data source
\`\`\`

## Technical Details

### NLP Processing
- **Algorithm**: Rule-based keyword matching with multi-label classification
- **Database**: 50+ skin concerns, 40+ ingredients, 50+ brand mappings
- **Accuracy**: High precision for common concerns, fallback to general recommendations

### Data Structure
- CSV-based ingredient and concern database
- Fallback embedded database for reliability
- Modular design for easy updates

### Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: Pandas, NumPy
- **NLP**: Custom keyword-matching engine

## Features in Detail

### 1. Smart Recommendation Engine
- Parses natural language input
- Identifies multiple simultaneous skin concerns
- Maps concerns to optimal ingredients
- Ranks recommendations by relevance

### 2. Comprehensive Database
- **50+ Skin Concerns**: Acne, dryness, aging, hyperpigmentation, etc.
- **40+ Ingredients**: From salicylic acid to retinol
- **50+ Brands**: Budget to luxury options

### 3. Personalized Routines
- Morning routine generation based on concerns
- Night routine with appropriate actives
- Frequency recommendations
- Layering instructions

### 4. Safety & Disclaimers
- Patch test recommendations
- Ingredient interaction warnings
- Medical condition disclaimers
- Professional consultation prompts

## Important Disclaimers

⚠️ **IMPORTANT**: This tool is for informational purposes only. It is NOT a substitute for professional medical advice.

- Always consult a dermatologist for:
  - Persistent or severe skin conditions
  - Allergic reactions or sensitivity
  - Medical skin disorders (eczema, psoriasis, etc.)
  - Before starting new treatment regimens

- **Patch Testing**: Always test new products on a small area for 24-48 hours first
- **Individual Variation**: Results vary based on genetics, climate, and lifestyle
- **Consistency**: Most results appear after 4-8 weeks of consistent use

## Troubleshooting

### Issue: App won't start
**Solution**: Ensure all dependencies are installed with `pip install -r requirements.txt`

### Issue: No recommendations found
**Solution**: Try describing your concerns differently or include more details

### Issue: App runs slowly
**Solution**: The app is fully functional even with slow internet; no API calls required

## Future Enhancements

- Machine learning model training on skincare reviews
- Product price comparison features
- Integration with skincare e-commerce platforms
- User accounts for personalized history
- Before/after progress tracking
- Video tutorials on proper application
- Multi-language support

## Contributing

Contributions are welcome! Areas for improvement:
- Additional skincare concerns and ingredients
- Brand database expansion
- UI/UX enhancements
- Multilingual support
- Performance optimizations

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions:
1. Check the FAQ section in the sidebar
2. Review the ingredient glossary for ingredient-specific info
3. Ensure you've read all safety disclaimers

## Acknowledgments

- Built with Streamlit for fast, interactive development
- Dermatological knowledge base from established skincare research
- Brand information from official brand sources
- Community feedback and suggestions

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Production Ready
