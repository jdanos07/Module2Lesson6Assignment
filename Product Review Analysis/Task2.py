# Develop a function that tallies the number of positive and negative words in
# each review.  The function should return the total count of positive and 
# negative words.


reviews = ["This amazing product is really good. I'm impressed with its awesome quality.", 
           "The performance of this product is excellent. Highly recommended!", 
           "I had a bad experience with this product. It was disappointing.", 
           "Poor quality product. Wouldn't recommend it to anyone.", 
           "The product was average. Nothing extraordinary about it."]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing"]


def without_punc(reviews):
    punc_swept_reviews = []
    for review in reviews:
        swept_review = ''
        for trm in review:
            if str(trm).isalnum() or str(trm).isspace():
                swept_review += trm
        punc_swept_reviews.append(swept_review)
    return punc_swept_reviews

swept_reviews = without_punc(reviews)


def getting_the_vibe():
    for i, review in enumerate(swept_reviews, 1):
        good_vibe = 0
        bad_vibe = 0
        word_search = str(review).lower().split()
        for positive_word in positive_words:
            good_vibe += word_search.count(positive_word)
        for negative_word in negative_words:
            bad_vibe += word_search.count(negative_word)
        print(f"Review {i}: Positive sentiments = {good_vibe}, Negative sentiments = {bad_vibe}") 
     
getting_the_vibe()

