# Time: O(w*nlog(n) + n*wlog(w))
# Space: O(w + n)

def main(words):
    sorted_words = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sorted_words[x])

    result = []
    current_group = []
    current_anagram = sorted_words[indices[0]]

    for i in indices:
        word = words[i]
        sorted_word = sorted_words[i]

        if sorted_word == current_anagram:
            current_group.append(word)
            continue


        result.append(current_group)
        current_anagram = sorted_words
        current_group = [word]

    return result
