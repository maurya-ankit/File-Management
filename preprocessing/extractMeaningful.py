from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# nltk.download('stopwords')
# nltk.download('punkt')


def extract_meaningful(input_text: str):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_text)

    filtered_text = [w for w in word_tokens if not w in stop_words]

    # print(filtered_text)

    return filtered_text
