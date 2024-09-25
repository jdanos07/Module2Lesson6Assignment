# Implement a script that takes the first 30 characters of a review and appends
# "…" to create a summary. Ensure that the summary does not cut off in the middle 
# of a word.

reviews = ["This amazing product is really good. I'm impressed with its awesome quality.", 
           "The performance of this product is excellent. Highly recommended!", 
           "I had a bad experience with this product. It was disappointing.", 
           "Poor quality product. Wouldn't recommend it to anyone.", 
           "The product was average. Nothing extraordinary about it."]

for review in reviews:
    slice_review = slice(0,31)
    snapshot_review = review[slice_review]
    print(f"\"{snapshot_review}...\"")

    # need to implement some sort of if statement to have the word complete before 
    # cutting off