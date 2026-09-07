"""
Author: [Navneet DAS]
Course: Coding for AI
Assignment: Problem Set 5.2 - The AI Social Media Auditor

Description: 
This script performs text normalisation to accurately count word frequencies 
(Task 1) and utilizes set operations to deduplicate and compare follower lists 
across two different social media platforms (Task 2).
"""
import string

text="""AI is changing the world. ai is powering new tools, and AI
is helping researchers learn faster. The world loves AI, and the world depends on it more each year."""

word_count={}
for raw_words in text.split( ):
    cleaned_word = raw_words.lower().strip(string.punctuation)
    if not cleaned_word:
        continue
    word_count.setdefault(cleaned_word,0)
    word_count[cleaned_word] += 1
    
print(word_count)

platform_a_followers=["u101","u102","u103","u104","u105"]
platform_b_followers=["u103","u104","u106","u107"]


platform_a_followers = set(platform_a_followers)
platform_b_followers = set(platform_b_followers)

print(f"Follower of both platform(&) :{platform_a_followers & platform_b_followers}")
print(f"Unique to Platform A(-) {platform_a_followers - platform_b_followers}")
print(f"Unique to Platform B(-) {platform_b_followers - platform_a_followers}")
print(f"Unique to exactly one platform ^ {platform_a_followers ^ platform_b_followers}")
