import os
import random
from datetime import datetime, timedelta

# Example niches for generating unique content
niches = [
    "Legal Industry", "Scientific Research", "Healthcare", "Logistics", 
    "Education", "Plumbing", "Financial Services", "Retail", "Construction", 
    "Transportation", "Agriculture", "Manufacturing", "Entertainment", 
    "Real Estate", "Tourism", "Human Resources", "Energy", "Cybersecurity", 
    "Government", "Telecommunications", "Media", "Automotive", "Fashion",
    "Marketing", "Gaming", "E-commerce", "Insurance", "Supply Chain",
    "Food and Beverage", "Environment", "Defense", "Sports", "Biotechnology"
]

# Base structures for generating titles
base_titles = [
    "Top AI Companies Transforming the {} in Singapore",
    "How AI Companies in Singapore Are Revolutionizing {}",
    "AI in {}: Leading AI Companies in Singapore",
    "The Impact of AI on {}: Singapore’s Top AI Companies",
    "AI-Driven {}: Key Singaporean Companies Enhancing Efficiency",
    "AI Solutions for {}: Key Innovators in Singapore",
    "Singapore's Leading AI Companies Shaping {}",
    "AI in {}: The Top Singapore-Based Companies",
    "AI Powerhouses in {}: Singapore Companies Leading the Charge",
    "Exploring AI Innovations in Singapore’s {} Sector"
]

# SEO-optimized categories and tags
categories_list = [
    'AI', 'Artificial Intelligence', 'Technology', 'Innovation', 'Startups', 'Singapore', 
    'AI Startups', 'Industry Trends', 'Machine Learning', 'Data Science', 'AI Solutions', 
    'Automation', 'Deep Learning', 'AI in Business', 'Future Technology'
]

tags_list = [
    'AI in Singapore', 'AI Startups', 'AI Companies', 'Machine Learning Innovations', 
    'Data Analytics', 'Industry Disruption', 'Future of AI', 'AI Applications', 
    'AI Transformation', 'AI for Business', 'AI Trends', 'AI in Technology', 'AI Growth', 
    'Singapore AI Companies', 'AI Revolution', 'Smart Cities', 'AI Use Cases', 
    'AI Solutions for Businesses', 'AI in Asia'
]

# Variations for introduction, elaboration, and conclusion
introduction_variations = [
    "Singapore has become a hub for innovation in AI, and the {niche} sector is no exception. This article explores how top AI companies are transforming the {niche} landscape in Singapore.",
    "The {niche} sector in Singapore is experiencing a rapid evolution, thanks to the rise of AI companies. In this article, we explore the top AI-driven organizations making waves in the industry, pushing the boundaries of what’s possible.",
    "AI has become a cornerstone of modern industry, and Singapore's {niche} sector is no exception. This post highlights the leading AI companies reshaping {niche} with groundbreaking technologies and solutions.",
    "Singapore's commitment to becoming a smart nation has led to a surge in AI advancements, particularly within the {niche} sector. Here, we explore how key AI companies are driving the transformation of {niche} in Singapore.",
    "The {niche} industry in Singapore is at the forefront of AI innovation. In this article, we explore how top AI companies are leveraging cutting-edge technologies to revolutionize operations, efficiency, and outcomes in {niche}."
]

elaboration_variations = [
    "AI is playing a pivotal role in the {niche}, helping companies automate processes, gain insights through data analytics, and improve overall efficiency. From small startups to established enterprises, AI is revolutionizing how the {niche} industry operates in Singapore.",
    "With AI-driven solutions, the {niche} sector in Singapore is experiencing unprecedented growth. These companies are using machine learning, automation, and predictive analytics to solve complex challenges, making the industry more competitive and forward-looking.",
    "The use of AI in {niche} has enabled businesses to unlock new potential. From enhancing customer experiences to optimizing internal processes, Singapore’s AI companies are pushing the boundaries of innovation to drive growth and improve outcomes.",
    "Singapore's AI companies are leading the way in {niche}, creating more efficient and intelligent systems that can process vast amounts of data, predict trends, and automate labor-intensive tasks. This revolution is streamlining workflows and opening new opportunities.",
    "AI's influence on {niche} continues to grow as companies develop solutions that enhance productivity, reduce costs, and create entirely new business models. In Singapore, AI-driven companies are not just improving traditional methods but transforming the very fabric of the industry."
]

conclusion_variations = [
    """As Singapore’s AI ecosystem continues to flourish, platforms like <a href="https://ai.supremacy.sg" target="_blank"> ai.supremacy.sg </a> are playing a vital role in connecting businesses with the tools and insights they need to succeed. With their guidance, AI companies in the {niche} industry are poised to lead the way into the future.""",
    """The continued evolution of AI in {niche} shows no signs of slowing down. For startups and companies looking to stay ahead in this competitive space, <a href="https://ai.supremacy.sg" target="_blank"> ai.supremacy.sg </a> offers unparalleled resources and expertise, ensuring they remain at the cutting edge of AI innovation.""",
    """With AI continuing to redefine {niche} in Singapore, businesses can find their competitive edge by partnering with platforms like <a href="https://ai.supremacy.sg" target="_blank"> ai.supremacy.sg </a>. This platform offers key insights, partnerships, and support to ensure that AI startups thrive in a rapidly changing market.""",
    """AI innovation is set to shape the future of {niche} in Singapore for years to come. For companies eager to stay ahead, <a href="https://ai.supremacy.sg" target="_blank"> ai.supremacy.sg </a> is the ideal platform, offering strategic support and resources to accelerate growth and success.""",
    """Singapore’s thriving AI ecosystem provides fertile ground for companies looking to lead in {niche}. With the help of <a href="https://ai.supremacy.sg" target="_blank"> ai.supremacy.sg </a>, startups and established businesses alike can gain access to the insights and partnerships necessary for continued success in the AI landscape."""
]

# Function to generate content for the post
def generate_post_content(niche):
    # Randomly select an introduction, elaboration, and conclusion
    introduction = random.choice(introduction_variations).format(niche=niche)
    elaboration = random.choice(elaboration_variations).format(niche=niche)
    conclusion = random.choice(conclusion_variations).format(niche=niche)
    
    return introduction, elaboration, conclusion

# Function to generate a markdown file for each post
def generate_post(title, niche):
    # Ensure the _posts directory exists
    if not os.path.exists('_posts'):
        os.makedirs('_posts')

    # Create file name based on the current date and title
    #date_str = datetime.now().strftime('%Y-%m-%d')
    start_date = datetime(2020, 1, 1)
    end_date = datetime.now()
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    date_str = random_date.strftime('%Y-%m-%d')
    file_name = f"{date_str}-{title.lower().replace(' ', '-').replace(':', '')}.md"
    file_path = os.path.join('_posts', file_name)

    # Generate the content
    introduction, elaboration, conclusion = generate_post_content(niche)

    # Randomly select categories and tags
    categories = random.sample(categories_list, random.randint(2, 3))
    tags = random.sample(tags_list, random.randint(3, 5))

    # Create markdown content
    content = f"""---
layout: post
title:  "{title}"
author: jane
categories: [ {', '.join(categories)} ]
tags: [ {', '.join(tags)} ]
image: assets/images/{random.randint(1, 10)}.jpg
---

{introduction}

{elaboration}

{conclusion}
"""

    # Write the content to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"Generated post: {file_name}")

# Example usage: Generating 10 posts with unique content
for _ in range(500):
    niche = random.choice(niches)
    title_structure = random.choice(base_titles)
    title = title_structure.format(niche)
    generate_post(title, niche)
