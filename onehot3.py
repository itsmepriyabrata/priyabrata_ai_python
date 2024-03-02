class OneHotEncoder:
    def _init_(self):
        self.word_to_index = {}
        self.index_to_word = {}

    def fit(self, sentence):
        words = sentence.split()
        unique_words = set(words)
        for i, word in enumerate(unique_words):
            self.word_to_index[word] = i
            self.index_to_word[i] = word

    def encode(self, sentence):
        words = sentence.split()
        encoding = []
        for word in words:
            one_hot_vector = [0] * len(self.word_to_index)
            index = self.word_to_index[word]
            one_hot_vector[index] = 1
            encoding.append(one_hot_vector)
        return encoding

    def decode(self, encoding):
        decoded_sentence = []
        for one_hot_vector in encoding:
            index = one_hot_vector.index(1)
            word = self.index_to_word[index]
            decoded_sentence.append(word)
        return ' '.join(decoded_sentence)


# Example usage:
encoder = OneHotEncoder()
sentence = "The quick brown fox jumps over the lazy dog."
encoder.fit(sentence)
encoded_sentence = encoder.encode(sentence)
decoded_sentence = encoder.decode(encoded_sentence)

print("Encoded sentence:")
for word, encoding in zip(sentence.split(), encoded_sentence):
    print(f"{word}: {encoding}")

print("\nDecoded sentence:", decoded_sentence)
