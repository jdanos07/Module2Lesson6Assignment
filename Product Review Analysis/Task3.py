# Implement a script that takes the first 30 characters of a review and appends
# "…" to create a summary. Ensure that the summary does not cut off in the middle 
# of a word.

reviews = ["This amazing product is really good. I'm impressed with its awesome quality.", 
           "The performance of this product is excellent. Highly recommended!", 
           "I had a bad experience with this product. It was disappointing.", 
           "Poor quality product. Wouldn't recommend it to anyone.", 
           "The product was average. Nothing extraordinary about it."]

for review in reviews:
    snapshot_review = review[:30]
    if review[30].isalnum():
        cut_off = -1
        for i in range(30):
            if snapshot_review[i] == ' ':
                cut_off = i
        if cut_off != -1:
            snapshot_review = snapshot_review[:cut_off]
    print(f"\"{snapshot_review}...\"")
  