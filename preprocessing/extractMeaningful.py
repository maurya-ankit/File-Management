from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# nltk.download('stopwords')
# nltk.download('punkt')


def extract_meaningful(input_text: str):
    stop_words = set(stopwords.words('english'))
    additional_stopwords = {"dot","one"}
    stop_words = stop_words.union(additional_stopwords)
    word_tokens = word_tokenize(input_text)

    filtered_text = [w for w in word_tokens if not w in stop_words]

    # print(filtered_text)

    return filtered_text

if __name__ =="__main__":
    query = input("Enter:")
    print(extract_meaningful(query))
