def word_freq_str(st):
    seen = {}
    for word in st.split():
        word = word.lower()
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1
    return seen
print(word_freq_str("i am best in the world and the world is best"))
