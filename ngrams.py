# Building an ngram algorithm for NLP analysis

class ngrams:
    # text = the text body you want to create ngrams
    # n = number of ngrams desired
  
    def ngram(text, n):
        tokens = text.split()
        bucket = {}
        if n < 1:
            print("Any number equal or less than 0 is not an ngram.\nPlease add a positive integer number greater than 0 as a valid ngram number.")
        elif n > len(tokens):
            print("The number of ngrams is larger than the text body length.\nPlease add a ngram number smaller than your text body length.")
        else:
            if len(tokens) < 1:
                print("empty string is not valid")
            else:
                for i in range(len(tokens) - n + 1):
                    gram = ' '.join(tokens[i:i+n])
                    if gram in bucket:
                        bucket[gram] += 1
                    else:
                        bucket[gram] = 1
        return bucket
