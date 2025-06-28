import pandas as pd

# Load necessary data files
try:
    sessions = pd.read_csv('merged_sessions.csv')
    user_features = pd.read_csv('user_segments.csv')
    fallback_top_categories = pd.read_csv('fallback_top_categories.csv')
except FileNotFoundError as e:
    print(f"Error: Data file not found - {e}. Please ensure 'merged_sessions.csv', 'user_segments.csv', and 'fallback_top_categories.csv' exist.")
    exit(1)

# Function to recommend category for new users (from Cold Start Strategy)
def recommend_for_new_user(user_region, user_device=None, user_source=None):
    top_category = fallback_top_categories[fallback_top_categories['region'] == user_region]['category']
    if len(top_category) > 0:
        return top_category.iloc[0]
    else:
        # Fallback to global top category
        return fallback_top_categories['category'].value_counts().idxmax()

# Function to generate landing page content (from Personalization Logic)
def generate_landing_page(user_id=None, user_region=None):
    if user_id:
        user_row = user_features[user_features['user_pseudo_id'] == user_id]
        
        if not user_row.empty:
            segment = user_row['segment'].iloc[0]
            
            # Rule-based mapping for segments
            if segment == 0:
                hero_banner = "Discover New Arrivals"
                product_carousel = "Recommended for You"
                cta = "Sign Up for Exclusive Deals"
            elif segment == 1:
                hero_banner = "Trending Now"
                product_carousel = "Top Picks in Electronics"
                cta = "Complete Your Purchase"
            elif segment == 2:
                hero_banner = "Best Sellers This Week"
                product_carousel = "You Might Also Like"
                cta = "Shop Now"
            else:
                hero_banner = "Deals for You"
                product_carousel = "Popular in Your Region"
                cta = "Start Exploring"
        else:
            # Fallback to cold start if user_id not found
            fallback_category = recommend_for_new_user(user_region if user_region else "DefaultRegion")
            hero_banner = f"Trending in {user_region if user_region else 'DefaultRegion'}: {fallback_category}"
            product_carousel = f"Top {fallback_category} Picks"
            cta = "Start Shopping"
    else:
        # New user, use cold start
        fallback_category = recommend_for_new_user(user_region if user_region else "DefaultRegion")
        hero_banner = f"Trending in {user_region if user_region else 'DefaultRegion'}: {fallback_category}"
        product_carousel = f"Top {fallback_category} Picks"
        cta = "Start Shopping"

    return {
        "Hero_Banner": hero_banner,
        "Product_Carousel": product_carousel,
        "CTA": cta
    }

# Main function for user input and output
def main():
    print("Welcome to the Hyper-Personalized Landing Page Generator!")
    print("Enter 'quit' at any time to exit.")
    
    while True:
        # Get user input
        user_id = input("\nEnter user ID (or press Enter for new user): ").strip()
        if user_id.lower() == 'quit':
            print("Exiting application.")
            break
        
        user_region = input("Enter user region (e.g., California, or press Enter for default): ").strip()
        if user_region.lower() == 'quit':
            print("Exiting application.")
            break

        # Generate personalized landing page
        try:
            if user_id:
                # Convert user_id to appropriate type (string or float based on user_features)
                try:
                    user_id = float(user_id) if user_features['user_pseudo_id'].dtype == 'float64' else user_id
                except ValueError:
                    print("Invalid user ID format. Using region-based fallback.")
                    user_id = None
            result = generate_landing_page(user_id=user_id, user_region=user_region if user_region else None)
            
            # Display output
            print("\n=== Personalized Landing Page ===")
            print(f"Hero Banner: {result['Hero_Banner']}")
            print(f"Product Carousel: {result['Product_Carousel']}")
            print(f"Call to Action: {result['CTA']}")
            print("================================")
        
        except Exception as e:
            print(f"Error generating landing page: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()