# vowelfinder.py

def find_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text if char in vowels]

if __name__ == "__main__":
    sample_text = (
        "Bidirectional encoder representations from transformers (BERT) is a language model "
        "introduced in October 2018 by researchers at Google. It learns to represent text as a "
        "sequence of vectors using self-supervised learning. It uses the encoder-only transformer "
        "architecture. BERT dramatically improved the state-of-the-art for large language models. "
        "As of 2020, BERT is a ubiquitous baseline in natural language processing (NLP) experiments."
    )
    vowels_found = find_vowels(sample_text)
    print("Vowels found:", vowels_found)
    print("Total number of vowels:", len(vowels_found))