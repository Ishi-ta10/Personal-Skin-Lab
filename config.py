"""
Configuration and constants for SkinCare Genius app
"""

# App configuration
APP_NAME = "SkinCare Genius"
APP_TAGLINE = "Personalized Skincare Recommendations Powered by AI"
APP_DESCRIPTION = "Get expert-backed skincare recommendations based on your unique skin concerns"

# Supported skin types
SKIN_TYPES = ["Any", "Dry", "Oily", "Normal", "Sensitive", "Combination"]

# Recommendation confidence settings
MIN_CONCERN_KEYWORDS = 1
CONFIDENCE_THRESHOLD = 0.5

# UI/UX settings
CARD_SHADOW = "0 2px 8px rgba(0,0,0,0.08)"
HOVER_SHADOW = "0 4px 16px rgba(0,0,0,0.12)"
BORDER_RADIUS = "12px"

# Color palette
COLORS = {
    'primary': '#8B5CF6',
    'secondary': '#EC4899',
    'accent': '#06B6D4',
    'success': '#10B981',
    'warning': '#F59E0B',
    'danger': '#EF4444',
    'light_bg': '#F8FAFC',
    'dark_bg': '#1E293B',
    'card_bg': '#FFFFFF',
}

# Feature flags
ENABLE_DARK_MODE = True
ENABLE_SAMPLE_DATA = True
SHOW_BRAND_INFO = True
SHOW_ROUTINE_GENERATION = True

# Sample inputs for demonstration
SAMPLE_INPUTS = [
    "I have oily, acne-prone skin with blackheads and enlarged pores",
    "My skin is dry, sensitive, and gets irritated easily with rough patches",
    "I have combination skin - oily T-zone but dry cheeks with dark spots",
    "I'm concerned about wrinkles, fine lines, and aging on my mature skin",
    "I have hyperpigmentation and dark spots from sun damage",
]
