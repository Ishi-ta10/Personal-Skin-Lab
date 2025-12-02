import pandas as pd
from typing import Dict, List, Optional
import re
import os

class RecommendationEngine:
    """Core recommendation engine using rule-based NLP and keyword matching"""
    
    def __init__(self):
        """Initialize the recommendation engine with skincare dataset"""
        self.df = self._load_dataset()
        self.concern_keywords = self._build_keyword_map()
    
    def _load_dataset(self) -> pd.DataFrame:
        """Load skincare recommendations from CSV or embedded data"""
        try:
            # Try to load from CSV file first
            csv_path = "skincare_dataset.csv"
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                # Ensure all required columns exist
                required_columns = ['concern', 'skin_type', 'ingredients', 'benefits', 'brands', 'notes']
                if all(col in df.columns for col in required_columns):
                    return df
        except Exception as e:
            print(f"Error loading CSV: {e}")
        
        data = {
            'concern': [
                'acne', 'oily skin', 'dry skin', 'hyperpigmentation', 'blackheads',
                'wrinkles', 'dull skin', 'dark spots', 'enlarged pores', 'sensitivity',
                'redness', 'bumpy skin', 'textured skin', 'rosacea', 'cystic acne',
                'under-eye circles', 'puffy eyes', 'uneven texture', 'sun damage',
                'age spots', 'melasma', 'back acne', 'body acne', 'razor bumps',
                'flaky skin', 'peeling skin', 'makeup irritation', 'damaged skin barrier',
                'large pores', 'clogged pores', 'stress acne', 'hormonal acne',
                'whiteheads', 'blotchiness', 'rough patches', 'itchy skin', 'psoriasis',
                'rosacea', 'seborrheic dermatitis', 'pollution damage', 'tanning damage',
                'inflamed acne', 'deep acne', 'inflammatory acne', 'breakouts',
                'combination skin', 'dehydrated skin', 'mature skin', 'oily t-zone'
            ],
            'skin_type': [
                'oily', 'oily', 'dry', 'combination', 'oily',
                'normal', 'oily', 'combination', 'combination', 'sensitive',
                'combination', 'dry', 'sensitive', 'normal', 'oily',
                'sensitive', 'oily', 'normal', 'sensitive',
                'combination', 'combination', 'oily', 'dry', 'combination',
                'dry', 'dry', 'oily', 'combination',
                'combination', 'sensitive', 'normal', 'combination',
                'combination', 'normal', 'dry', 'combination', 'dry', 'combination',
                'normal', 'normal', 'normal', 'sensitive',
                'combination', 'oily', 'oily', 'normal',
                'combination', 'combination', 'normal', 'combination'
            ],
            'ingredients': [
                'salicylic acid, niacinamide, tea tree oil',
                'niacinamide, glycerin, clay',
                'panthenol, hyaluronic acid, glycerin',
                'niacinamide, vitamin C, azelaic acid',
                'salicylic acid, tea tree oil, benzoyl peroxide',
                'retinol, coenzyme Q10, peptides',
                'vitamin C, AHA, glycolic acid, azelaic acid',
                'arbutin, AHA, kojic acid, vitamin C',
                'panthenol, hyaluronic acid, niacinamide',
                'green tea, allantoin, centella asiatica',
                'centella asiatica, allantoin, green tea',
                'ceramides, colloidal oatmeal, squalane',
                'azelaic acid, benzoyl peroxide, salicylic acid',
                'calendula, allantoin, azelaic acid',
                'tea tree oil, benzoyl peroxide, salicylic acid',
                'coenzyme Q10, retinol, caffeine',
                'caffeine, centella asiatica, peptides',
                'AHA, azelaic acid, vitamin C, kojic acid',
                'AHA, peptides, sunscreen protection',
                'peptides, retinol, age spots treatment',
                'vitamin C, azelaic acid, niacinamide',
                'salicylic acid, benzoyl peroxide, tea tree oil',
                'salicylic acid, azelaic acid, benzoyl peroxide',
                'aloe vera, allantoin, azelaic acid',
                'panthenol, hyaluronic acid, glycerin',
                'glycerin, panthenol, ceramides',
                'allantoin, green tea, calendula',
                'ceramides, lanolin, fatty acids',
                'hyaluronic acid, niacinamide, peptides',
                'benzoyl peroxide, salicylic acid, niacinamide',
                'tea tree oil, salicylic acid, azelaic acid',
                'niacinamide, hormonal support, salicylic acid',
                'benzoyl peroxide, niacinamide, salicylic acid',
                'glycerin, hyaluronic acid, niacinamide',
                'kojic acid, azelaic acid, rough patch treatment',
                'ceramides, cholesterol, lanolin',
                'ceramides, colloidal oatmeal, cholesterol',
                'centella asiatica, calendula, allantoin',
                'ceramides, squalane, antioxidants',
                'arbutin, AHA, kojic acid',
                'kojic acid, azelaic acid, tranexamic acid',
                'azelaic acid, benzoyl peroxide, salicylic acid',
                'tea tree oil, benzoyl peroxide, salicylic acid',
                'niacinamide, salicylic acid, azelaic acid',
                'niacinamide, glycerin, hyaluronic acid',
                'hyaluronic acid, glycerin, ceramides',
                'retinol, peptides, vitamin C',
                'niacinamide, glycerin, salicylic acid'
            ],
            'benefits': [
                'Unclogs pores, kills acne-causing bacteria, reduces acne scars, controls oil',
                'Controls sebum, reduces shine, minimizes pore appearance, prevents congestion',
                'Deep hydration, restores moisture barrier, reduces flaking, soothes skin',
                'Inhibits melanin production, fades dark marks, evens skin tone',
                'Exfoliates, unclogs comedones, antibacterial, prevents future blackheads',
                'Reduces fine lines, boosts collagen production, improves elasticity',
                'Brightens dull complexion, removes dead cells, improves radiance, smooths texture',
                'Fades hyperpigmentation, removes dead skin, promotes cell turnover',
                'Minimizes appearance, hydrates, improves skin texture, refines surface',
                'Calms irritation, reduces sensitivity, strengthens barrier',
                'Reduces inflammation, calms redness, provides antioxidant protection',
                'Smooths texture, repairs barrier, reduces bumpy appearance',
                'Improves uneven surface, reduces congestion, smooths rough areas',
                'Reduces vascular redness, calms inflammation, strengthens barrier',
                'Clears cystic acne, reduces deep inflammation, prevents future breakouts',
                'Brightens under-eye area, reduces puffiness, diminishes circles',
                'Reduces puffiness, depuffs under-eye area, refreshes appearance',
                'Smooths texture, evens tone, improves overall appearance',
                'Reverses UV damage, promotes healing, prevents future damage',
                'Fades age spots, promotes cell renewal, improves skin tone',
                'Targets stubborn melasma, inhibits melanin, fades patches',
                'Clears back acne, prevents bacteria buildup, reduces inflammation',
                'Treats body acne, clears congestion, prevents recurring breakouts',
                'Heals irritation, smooths bumps, prevents ingrown hairs',
                'Restores hydration, removes dead skin, reveals smooth texture',
                'Exfoliates gently, hydrates, reveals fresh skin beneath',
                'Calms irritation, soothes sensitivity, reduces redness',
                'Repairs barrier, restores lipids, strengthens skin protection',
                'Refines pores, hydrates, improves skin smoothness',
                'Unclogs pores, prevents congestion, clears comedones',
                'Manages stress-related breakouts, calms inflammation, reduces redness',
                'Targets hormonal breakouts, regulates sebum, reduces acne',
                'Clears whiteheads, controls oil, prevents new breakouts',
                'Evens tone, improves texture, reduces blotchy appearance',
                'Softens patches, improves texture, calms irritation',
                'Soothes itching, hydrates, calms irritation',
                'Treats psoriasis scales, hydrates, reduces inflammation',
                'Treats rosacea, reduces flushing, calms inflammation',
                'Treats seborrheic dermatitis, reduces flaking, calms scalp',
                'Protects against pollution damage, detoxifies, improves clarity',
                'Reverses tanning damage, brightens tone, restores health',
                'Reduces inflammation, clears acne, prevents scarring',
                'Deep treatment for cystic acne, reduces severe breakouts',
                'Manages inflammatory responses, reduces redness, treats severe acne',
                'Prevents future breakouts, clears existing, maintains clear skin',
                'Balances skin type, manages oil and dry zones, harmonizes skin',
                'Hydrates deeply, restores moisture, plumps skin',
                'Anti-aging treatment, targets mature skin concerns, reduces wrinkles',
                'Controls T-zone oil, hydrates cheeks, balances skin'
            ],
            'brands': [
                'The Ordinary, Cosrx, Paula\'s Choice, Minimalist, Neutrogena',
                'CeraVe, Olay, The Ordinary, Cosrx, Good Molecules',
                'Aveeno, LANEIGE, Tatcha, SK-II, StriVectin',
                'Peach & Lily, Neutrogena, Allies of Skin, The Ordinary, LANEIGE',
                'Olay, First Aid Beauty, Kiehl\'s, Cosrx, The Ordinary',
                'The Ordinary, Vichy, Sunday Riley, Murad, Estee Lauder',
                'Vichy, Ren Clean Skincare, Minimalist, The Ordinary, CeraVe',
                'Krave Beauty, Augustinus Bader, Clarins, The Ordinary, Murad',
                'Estee Lauder, Dermalogica, Drunk Elephant, Tatcha, The Ordinary',
                'Avene, Peter Thomas Roth, Good Molecules, Youth to the People, The Ordinary',
                'Olay, Biossance, Clinique, The Ordinary, Allies of Skin',
                'Ren Clean Skincare, Cosrx, StriVectin, Olay, CeraVe',
                'Obagi, Cosrx, Simple, The Ordinary, Paula\'s Choice',
                'La Roche Posay, CeraVe, Estee Lauder, Krave Beauty, The Ordinary',
                'La Roche Posay, Ren Clean Skincare, Inkey List, Clinique, Paula\'s Choice',
                'Vichy, The Ordinary, Shiseido, Olay, First Aid Beauty',
                'LANEIGE, Olay, Cosrx, The Ordinary, Peach & Lily',
                'Glow Recipe, Allies of Skin, Peter Thomas Roth, The Ordinary, Murad',
                'SK-II, Sunday Riley, Peter Thomas Roth, Glow Recipe, Olay',
                'Biossance, Murad, Dermalogica, Tatcha, Estee Lauder',
                'Naturium, Sunday Riley, SK-II, The Ordinary, Paula\'s Choice',
                'Kiehl\'s, La Roche Posay, Ren Clean Skincare, Cosrx, Paula\'s Choice',
                'Guerlain, Babor, Peter Thomas Roth, The Ordinary, Clinique',
                'Vichy, Dermalogica, Allies of Skin, Aloe-based brands, The Ordinary',
                'Inkey List, Naturium, Aveeno, Tatcha, La Roche Posay',
                'Aveeno, Cetaphil, Drunk Elephant, Farmacy, Simple',
                'First Aid Beauty, Clinique, Youth to the People, The Ordinary, Allantoin-based brands',
                'Versed, StriVectin, Sulwhasoo, SK-II, La Roche Posay',
                'Estee Lauder, Dermalogica, Drunk Elephant, Tatcha, Olay',
                'Youth to the People, Peter Thomas Roth, Sisley Paris, The Ordinary, Cosrx',
                'Inkey List, Babor, Cetaphil, The Ordinary, Ren Clean Skincare',
                'StriVectin, Clinique, Minimalist, The Ordinary, Cosrx',
                'Peach & Lily, Cosrx, La Mer, The Ordinary, Minimalist',
                'Tatcha, Sulwhasoo, Peach & Lily, Farmacy, CeraVe',
                'Sisley Paris, Paula\'s Choice, Youth to the People, The Ordinary, Inkey List',
                'Avene, Inkey List, Sisley Paris, The Ordinary, Naturium',
                'Krave Beauty, LANEIGE, Tatcha, La Roche Posay, CeraVe',
                'La Roche Posay, CeraVe, Estee Lauder, SK-II, The Ordinary',
                'Krave Beauty, LANEIGE, Tatcha, Versed, StriVectin',
                'Biossance, Minimalist, Sulwhasoo, The Ordinary, Vichy',
                'Glow Recipe, Peter Thomas Roth, SK-II, Youth to the People, The Ordinary',
                'Babor, Glow Recipe, Guerlain, The Ordinary, Paula\'s Choice',
                'Inkey List, Ren Clean Skincare, Minimalist, Paula\'s Choice, The Ordinary',
                'Inkey List, Babor, Cetaphil, The Ordinary, Cosrx',
                'Sunday Riley, Minimalist, The Ordinary, CeraVe, Olay',
                'Tatcha, LANEIGE, Sulwhasoo, Peach & Lily, SK-II',
                'Tatcha, Sulwhasoo, Peach & Lily, SK-II, Estee Lauder',
                'Tatcha, The Ordinary, Murad, Sunday Riley, SK-II',
                'The Ordinary, LANEIGE, Cosrx, Olay, CeraVe'
            ],
            'notes': [
                'May cause initial purging. Avoid mixing with vitamin C. Use SPF 30+ daily. Start 1-2x per week.',
                'Suitable for oily skin types. Use SPF 50+ daily. Can cause initial dryness.',
                'Results take 2-3 weeks. Patch test first. Do not skip moisturizer.',
                'Use SPF 50+ during day. Results visible after 4-6 weeks. Avoid direct sun.',
                'Can cause initial dryness. Introduce gradually. Start 2-3x per week.',
                'Use at night 2-3x per week initially. Increases sun sensitivity. Avoid mixing with actives.',
                'Start with once weekly. Build up frequency gradually. Use SPF 50+.',
                'Use with SPF 50+ during day. Avoid direct sun. Results after 4-8 weeks.',
                'Hydrating formula works best. Use daily after cleansing. Pair with moisturizer.',
                'For sensitive skin. Do not combine with strong actives. Patch test.',
                'Calming formula suitable for reactive skin. Use AM and PM. Very gentle.',
                'Moisture-rich ingredients recommended. Use daily. Results in 2-4 weeks.',
                'May cause slight dryness. Start slowly. Use 3-4x per week.',
                'Calming ingredients essential. Avoid hot water. Use gentle products.',
                'Potent formula. Use every 2-3 nights initially. Build tolerance slowly.',
                'Apply around eye area. Use night and morning. Results in 4 weeks.',
                'Apply under eyes. Use morning and night. Refrigerate for extra depuffing.',
                'Use consistently. Results visible after 4-8 weeks. Pair with sun protection.',
                'Essential to use SPF 50+ daily. Results after 8 weeks. Build tolerance.',
                'Use SPF 50+. Results after 6-8 weeks. Use consistently for best results.',
                'Use SPF 50+ daily. Results after 6-8 weeks. Very important for stubborn melasma.',
                'Can cause dryness. Start 1-2x per week. Gradually increase frequency.',
                'Apply to affected areas. Start slowly. May cause initial irritation.',
                'Use post-hair removal. Prevents ingrown hairs. Very soothing.',
                'Use daily AM and PM. Results in 1-2 weeks. Keep skin hydrated.',
                'Use 1-2x per week initially. Can be drying. Follow with rich moisturizer.',
                'Very gentle formula. Use as needed. Good for sensitive skin types.',
                'Essential for damaged barrier. Use 2x daily. Avoid strong actives initially.',
                'Use consistently. Results after 2-4 weeks. Pair with hydrating serum.',
                'Use 2-3x per week. Can cause dryness. Build tolerance gradually.',
                'Manage stress levels. Use consistently. Results after 4 weeks.',
                'Consistency is key. Use 4-8 weeks for results. May regulate after adjustment.',
                'Use 3-4x per week. Can cause dryness. Follow with rich moisturizer.',
                'Use consistently. Results after 4-6 weeks. Avoid strong actives simultaneously.',
                'Use gently. May cause initial dryness. Pair with hydrating serum.',
                'Use with hydrating products. Can cause slight dryness. Very soothing.',
                'Use carefully. May require medical supervision. Consult dermatologist.',
                'Consult dermatologist for proper treatment. Gentle formulas recommended.',
                'Long-term management. Use consistently. Dermatologist guidance helpful.',
                'Use antioxidant products. Pair with sun protection. Prevention is key.',
                'Use SPF 50+. Prevention is important. Reverse damage gradually over time.',
                'Very potent. Start slowly. Can cause initial irritation. Increase gradually.',
                'Requires patience. Results after 6-8 weeks. Professional guidance recommended.',
                'Very effective for severe acne. Start low. Build up concentration.',
                'Consistency is key. Results after 4-8 weeks. Maintain routine.',
                'Balance oil and dry zones. Use targeted products. Customize routine.',
                'Deep hydration essential. Use rich moisturizer. Avoid over-exfoliation.',
                'Use anti-aging routine. Consistent application important. Results after 8 weeks.',
                'Target T-zone with oil control. Hydrate cheeks separately. Customize approach.'
            ]
        }
        
        return pd.DataFrame(data)
    
    def _build_keyword_map(self) -> Dict[str, List[str]]:
        """Build a map of keywords to concern categories"""
        return {
            'acne': ['acne', 'pimple', 'breakout', 'spot', 'blemish', 'congestion'],
            'oily skin': ['oily', 'oil', 'grease', 'shiny', 'shine', 'sebum'],
            'dry skin': ['dry', 'dehydrated', 'flaky', 'peeling', 'tight'],
            'hyperpigmentation': ['hyperpigmentation', 'dark spot', 'dark spots', 'pigmentation', 'uneven tone', 'pigment'],
            'blackheads': ['blackhead', 'comedone', 'pore', 'congested'],
            'wrinkles': ['wrinkle', 'line', 'aging', 'fine line', 'anti-aging', 'mature'],
            'dull skin': ['dull', 'matte', 'tired', 'radiance', 'glow', 'lackluster'],
            'dark spots': ['dark spot', 'spots', 'sun spot', 'age spot', 'freckle'],
            'enlarged pores': ['pore', 'large pore', 'wide pore', 'dilated pore'],
            'sensitivity': ['sensitive', 'sensitivity', 'reactive', 'irritated', 'irritation'],
            'redness': ['red', 'redness', 'flush', 'inflamed', 'inflammation'],
            'bumpy skin': ['bumpy', 'texture', 'rough', 'uneven texture', 'keratosis'],
            'textured skin': ['texture', 'textured', 'bumpy', 'rough patches'],
            'rosacea': ['rosacea', 'persistent redness', 'vascular'],
            'cystic acne': ['cystic', 'cyst', 'nodule', 'deep acne'],
            'under-eye circles': ['under-eye circle', 'dark circles', 'eye puffiness', 'eye bags'],
            'puffy eyes': ['puffy eye', 'eye puffiness', 'eye bag', 'eye swelling'],
            'uneven texture': ['uneven texture', 'rough skin', 'textured skin'],
            'sun damage': ['sun damage', 'photoaging', 'UV damage'],
            'age spots': ['age spot', 'sun spot', 'liver spot'],
            'melasma': ['melasma', 'mask of pregnancy', 'chloasma'],
            'back acne': ['back acne', 'acne on back', 'bacne'],
            'body acne': ['body acne', 'acne on body', 'troubled skin'],
            'razor bumps': ['razor bump', 'pseudofolliculitis barbae', 'ingrown hair'],
            'flaky skin': ['flaky skin', 'scaling skin', 'dry flaky skin'],
            'peeling skin': ['peeling skin', 'exfoliating skin', 'flaking skin'],
            'makeup irritation': ['makeup irritation', 'makeup allergy', 'makeup sensitivity'],
            'damaged skin barrier': ['damaged skin barrier', 'barrier damage', 'skin barrier issues'],
            'large pores': ['large pores', 'wide pores', 'enlarged pores'],
            'clogged pores': ['clogged pores', 'blocked pores', 'congested pores'],
            'stress acne': ['stress acne', 'stress-related acne', 'stress-induced acne'],
            'hormonal acne': ['hormonal acne', 'hormonal breakouts', 'hormonal skin issues'],
            'whiteheads': ['whitehead', 'closed comedone', 'milium'],
            'blotchiness': ['blotchiness', 'skin discoloration', 'uneven skin tone'],
            'rough patches': ['rough patch', 'rough skin', 'uneven texture'],
            'itchy skin': ['itchy skin', 'itching skin', 'irritated skin'],
            'psoriasis': ['psoriasis', 'psoriasis treatment', 'psoriasis skincare'],
            'seborrheic dermatitis': ['seborrheic dermatitis', 'scalp acne', 'scalp irritation'],
            'pollution damage': ['pollution damage', 'city skin', 'urban skin'],
            'tanning damage': ['tanning damage', 'sunburn', 'tan lines'],
            'inflamed acne': ['inflamed acne', 'red acne', 'inflammatory acne'],
            'deep acne': ['deep acne', 'nodular acne', 'cystic acne'],
            'inflammatory acne': ['inflammatory acne', 'red acne', 'papules'],
            'breakouts': ['breakout', 'acne breakout', 'skin breakout'],
            'combination skin': ['combination skin', 'mixed skin', 'oily and dry skin'],
            'dehydrated skin': ['dehydrated skin', 'dry skin', 'water-starved skin'],
            'mature skin': ['mature skin', 'aging skin', 'senior skin'],
            'oily t-zone': ['oily t-zone', 't-zone shine', 't-zone congestion']
        }
    
    def _extract_concerns(self, text: str) -> List[str]:
        """Extract skin concerns from user input using keyword matching"""
        text_lower = text.lower()
        detected_concerns = []
        
        for concern, keywords in self.concern_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    if concern not in detected_concerns:
                        detected_concerns.append(concern)
                    break
        
        return detected_concerns if detected_concerns else ['general skin care']
    
    def get_recommendations(self, user_input: str, skin_type_filter: Optional[str] = None) -> Dict:
        """
        Get personalized skincare recommendations
        
        Args:
            user_input: User's description of skin concerns
            skin_type_filter: Optional skin type filter
        
        Returns:
            Dictionary with recommendations
        """
        # Extract concerns
        concerns = self._extract_concerns(user_input)
        
        # Filter dataset based on detected concerns and skin type
        filtered_df = self.df[self.df['concern'].isin(concerns)]
        
        if skin_type_filter:
            filtered_df = filtered_df[filtered_df['skin_type'] == skin_type_filter.lower()]
        
        if filtered_df.empty:
            # Return default recommendations if no matches
            filtered_df = self.df[self.df['concern'] == 'general skin care']
            if filtered_df.empty:
                filtered_df = self.df.head(1)
        
        # Aggregate recommendations
        all_ingredients = set()
        all_brands = set()
        all_benefits = []
        all_notes = []
        
        for _, row in filtered_df.iterrows():
            ingredients = [ing.strip() for ing in str(row['ingredients']).split(',')]
            all_ingredients.update(ingredients)
            
            brands = [brand.strip() for brand in str(row['brands']).split(',')]
            all_brands.update(brands)
            
            all_benefits.append(row['benefits'])
            all_notes.append(row['notes'])
        
        # Format recommendations
        recommendations = {
            'concerns': concerns,
            'ingredients': sorted(list(all_ingredients)),
            'benefits': ' '.join(set(all_benefits)),
            'brands': ', '.join(sorted(list(all_brands))[:8]),  # Top 8 brands
            'directions': self._generate_directions(list(all_ingredients)),
            'notes': ' | '.join(set(all_notes)),
            'morning_routine': self._generate_morning_routine(list(all_ingredients)),
            'night_routine': self._generate_night_routine(list(all_ingredients))
        }
        
        return recommendations
    
    def _generate_directions(self, ingredients: List[str]) -> str:
        """Generate usage directions based on ingredients"""
        directions = "• **Frequency**: Use as directed on product packaging\n"
        directions += "• **Application**: Apply to cleansed, dry skin\n"
        directions += "• **Layering**: Wait 1-2 minutes between product applications\n"
        directions += "• **SPF**: Always use SPF 30+ during the day\n"
        directions += "• **Patch Test**: Test on small area for 24-48 hours first"
        return directions
    
    def _generate_morning_routine(self, ingredients: List[str]) -> str:
        """Generate morning routine based on ingredients"""
        routine = "1. **Cleanser**: Gentle cleanser suitable for your skin type\n"
        routine += "2. **Toner** (Optional): Hydrating or exfoliating toner\n"
        
        if any(ing in str(ingredients) for ing in ['vitamin c', 'azelaic acid']):
            routine += "3. **Serum**: Vitamin C or brightening serum (2-3 drops)\n"
        else:
            routine += "3. **Serum**: Lightweight serum (2-3 drops)\n"
        
        routine += "4. **Moisturizer**: Suitable for your skin type\n"
        routine += "5. **SPF**: Broad-spectrum SPF 30+ sunscreen"
        return routine
    
    def _generate_night_routine(self, ingredients: List[str]) -> str:
        """Generate night routine based on ingredients"""
        routine = "1. **Cleanser**: Gentle cleanser to remove impurities\n"
        
        if any(ing in str(ingredients) for ing in ['salicylic acid', 'benzoyl peroxide']):
            routine += "2. **Exfoliant**: Salicylic acid or BHA (2-3x per week)\n"
        else:
            routine += "2. **Toner** (Optional): Hydrating or treatment toner\n"
        
        if any(ing in str(ingredients) for ing in ['retinol']):
            routine += "3. **Retinoid**: Start with 1-2x per week, build up gradually\n"
        elif any(ing in str(ingredients) for ing in ['AHA']):
            routine += "3. **AHA**: 2-3x per week for exfoliation\n"
        else:
            routine += "3. **Treatment**: Target serum or treatment (as needed)\n"
        
        routine += "4. **Moisturizer**: Richer formula for overnight hydration"
        return routine
