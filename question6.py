#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
#“I am a teacher and I love to inspire and teach people”
teacher_sentence = "I am a teacher and I love to inspire and teach people"
sentence_words = teacher_sentence.split()
unique_words = set(sentence_words)
print("Unique words are",len(unique_words))
print("Unique words =",unique_words)