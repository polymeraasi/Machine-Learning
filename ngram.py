import re
from nltk.util import ngrams
from collections import Counter
"""
Code for the n-gram task:
As preprocessing, you should remove all capitalization, special characters, 
and numbers from the text. In addition, remove the following common words 
(called “stopwords”): [a, an, and, as, at, for, from, in, into, of, on, or, the, to]

After tokenization, remove also tokens with length < 2. 
We perform this step because if e.g. you have in the text words like “sister’s”, 
tokenization will result in meaningless tokens like “s” 
(Note that this might lead to omitting words such as the personal pronoun “I” 
which could be undesirable in practice, but for this exercise it is okay).

Using a word bi-gram language model, what is the probability of the phrase ‘door with’?

Remove the leading zeroes from your answer, and consider the three most significant 
digits of the result as an integer (e.g. if your answer is 0.00010587, consider only 105 from it). 
Divide that integer with 67 and submit the remainder.
"""

stopwords = {'a', 'an', 'and', 'as', 'at', 'for', 'from', 'in', 'into', 'of', 'on', 'or', 'the', 'to'}

# to deal with the file and its special cases:
filename = "TheStoryofAnHour-KateChopin.txt"
with open(filename, mode='r') as file:
    text = file.read()

text = re.sub(r'[^a-zA-Z\s]', '', text.lower())  # remove special characters and numbers
words = [word for word in text.split() if word not in stopwords and len(word) >= 2]  # remove tokens with length < 2


# to deal with bigrams:
bigrams = list(ngrams(words, 2))
count_of_bigrams = Counter(bigrams)
phrase = count_of_bigrams[('door', 'with')]   # numerator for P(wi|wi-1) = P('with'|'door')
denominator = sum(1 for word in words if word == 'door')   # every 'door' word in the corpus

# probability calculus, rounding to percents and returning the remainder of deviation of 67
probability = (phrase / denominator) * (denominator / 798)
print("The probability: ", probability)
remainder = 250 % 67
print("The remainder: ", remainder)



