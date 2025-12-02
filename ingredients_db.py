"""
Comprehensive Skincare Ingredients Database and Product Information
"""

INGREDIENT_GLOSSARY = {
    # Exfoliants
    'Salicylic Acid': 'BHA that exfoliates pores and reduces acne; ideal for oily, congested skin',
    'AHA': 'Alpha Hydroxy Acid; chemical exfoliant that removes dead skin cells; improves texture',
    'Glycolic Acid': 'Type of AHA; gentle exfoliation; brightens and smooths skin',
    'Azelaic Acid': 'Treats acne, rosacea, and hyperpigmentation; antibacterial and anti-inflammatory',
    'Benzoyl Peroxide': 'Kills acne-causing bacteria; reduces inflammation; use cautiously as it can be drying',
    
    # Hydration & Moisture
    'Hyaluronic Acid': 'Humectant that holds 1000x its weight in water; deeply hydrates skin',
    'Glycerin': 'Draws moisture to skin; humectant; suitable for all skin types',
    'Panthenol': 'Provitamin B5; soothes irritation; strengthens skin barrier',
    'Squalane': 'Lightweight oil; mimics skin\'s natural oils; non-comedogenic',
    'Ceramides': 'Lipids that repair skin barrier; essential for dry skin',
    'Cholesterol': 'Barrier-repairing lipid; strengthens skin barrier; reduces irritation',
    
    # Brightening & Antioxidants
    'Vitamin C': 'Antioxidant; boosts collagen; brightens skin and fades dark spots',
    'Niacinamide': 'Vitamin B3; controls oil; reduces redness; strengthens skin barrier',
    'Kojic Acid': 'Natural brightener; inhibits melanin; fades dark spots and hyperpigmentation',
    'Arbutin': 'Plant-derived ingredient; inhibits tyrosinase; fades hyperpigmentation',
    'Vitamin E': 'Antioxidant; protects against environmental damage; moisturizes',
    'Green Tea': 'Antioxidant; calms inflammation; reduces sebum production',
    
    # Anti-Aging & Retinoids
    'Retinol': 'Vitamin A derivative; stimulates collagen; reduces wrinkles and fine lines',
    'Retinoid': 'Family of vitamin A compounds; powerful anti-aging; requires gradual introduction',
    'Coenzyme Q10': 'Antioxidant; boosts energy in cells; reduces fine lines',
    'Peptides': 'Amino acid chains; stimulate collagen; improve skin firmness',
    'Collagen': 'Protein; plumps skin; improves elasticity; large molecules (stays on surface)',
    
    # Soothing & Calming
    'Centella Asiatica': 'Cica; heals skin; reduces redness; strengthens barrier',
    'Allantoin': 'Soothes irritation; promotes healing; calms reactive skin',
    'Aloe Vera': 'Cooling; hydrating; reduces inflammation; soothes burns',
    'Calendula': 'Promotes healing; reduces inflammation; suitable for sensitive skin',
    'Tea Tree Oil': 'Antibacterial; antifungal; acne-fighting; use cautiously to avoid irritation',
    
    # Barrier & Repair
    'Colloidal Oatmeal': 'Soothes itching; repairs barrier; gentle exfoliation',
    'Lanolin': 'Emollient; deeply moisturizing; occlusive; may cause irritation in some',
    'Fatty Acids': 'Essential for barrier function; deeply nourishing; anti-inflammatory',
    
    # Specialized
    'Tranexamic Acid': 'Reduces redness; prevents vascular dilation; brightens skin',
    'Licorice Root': 'Brightens skin; reduces irritation; calms redness',
}

PRODUCT_IMAGES = {
    'The Ordinary': '/placeholder.svg?height=200&width=200',
    'CeraVe': '/placeholder.svg?height=200&width=200',
    'Cosrx': '/placeholder.svg?height=200&width=200',
    'Paula\'s Choice': '/placeholder.svg?height=200&width=200',
    'Olay': '/placeholder.svg?height=200&width=200',
    'Neutrogena': '/placeholder.svg?height=200&width=200',
    'Tatcha': '/placeholder.svg?height=200&width=200',
    'Kiehl\'s': '/placeholder.svg?height=200&width=200',
    'Estee Lauder': '/placeholder.svg?height=200&width=200',
    'SK-II': '/placeholder.svg?height=200&width=200',
}

# Comprehensive mapping of skin concerns to recommended ingredients
CONCERN_INGREDIENT_MAP = {
    'acne': ['salicylic acid', 'benzoyl peroxide', 'niacinamide', 'tea tree oil'],
    'oily skin': ['niacinamide', 'salicylic acid', 'glycerin', 'clay'],
    'dry skin': ['hyaluronic acid', 'glycerin', 'ceramides', 'panthenol'],
    'hyperpigmentation': ['vitamin c', 'niacinamide', 'kojic acid', 'arbutin'],
    'sensitivity': ['centella asiatica', 'allantoin', 'green tea', 'panthenol'],
    'aging': ['retinol', 'vitamin c', 'peptides', 'coenzyme q10'],
    'dull skin': ['vitamin c', 'aha', 'glycolic acid', 'niacinamide'],
}

BRAND_INFO = {
    'The Ordinary': {
        'price_range': '$',
        'specialty': 'Affordable, science-backed formulations',
        'best_for': 'Budget-conscious users seeking effective actives'
    },
    'CeraVe': {
        'price_range': '$',
        'specialty': 'Barrier repair, ceramides, hypoallergenic',
        'best_for': 'Sensitive and dry skin types'
    },
    'Cosrx': {
        'price_range': '$$',
        'specialty': 'Korean skincare, gentle formulations',
        'best_for': 'Sensitive and acne-prone skin'
    },
    'Paula\'s Choice': {
        'price_range': '$$',
        'specialty': 'Dermatologist-founded, research-based',
        'best_for': 'Acne and rosacea'
    },
    'Tatcha': {
        'price_range': '$$$',
        'specialty': 'Japanese beauty, premium ingredients',
        'best_for': 'Luxury skincare seekers'
    },
}
