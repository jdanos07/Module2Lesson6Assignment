# Write a program that searches through reviews list and looks for 
# keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand 
# out.
#     
# So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

reviews = ["This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]
key_words = ['excellent', 'good', 'average', 'poor','bad']

for review in reviews:
        emphasized_review = review
        for key_word in key_words:
            # key_word = key_word.lower()
            emphatic_key_words = key_word.upper()
            if ((review.lower().find(key_word)) != -1):
                emphasized_review = review.replace(key_word, emphatic_key_words)
                print(emphasized_review)






