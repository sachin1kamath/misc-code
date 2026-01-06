import random

transitions = {}
starting_words_list = [("the", "the"), ("an", "an"), ("a", "a"), ("this", "this"), ("that", "that"), ("every", "every")]
starting_words = random.choice(starting_words_list)

def make_transitions(text, transition_list):
    text = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "").lower()
    text_list = text.split()
    
    if len(text_list) < 2:
        return transition_list

    for i in range(len(text_list) - 2):
        state_key = (text_list[i], text_list[i + 1])
        next_word = text_list[i + 2] 

        if state_key not in transition_list:
            transition_list[state_key] = {}
        
        if next_word not in transition_list[state_key]:
            transition_list[state_key][next_word] = 1
        else:
            transition_list[state_key][next_word] += 1
    
    return transition_list

def make_sentence(transition_list, starting_words, length):
    
    current_state = starting_words
    
    if current_state not in transition_list:
        first_word_match = [k for k in transition_list.keys() if k[0] == starting_words[0]]
        
        if first_word_match:
            current_state = random.choice(first_word_match)
        else:
            print("\nError: Starting word not found in any sequence.\n")
            return
            
    print("\n" + current_state[0].capitalize() + " ", end="")
    
    for i in range(length):
        
        if current_state not in transition_list:
             print(".\n\n", end="")
             break
             
        next_word_counts = transition_list[current_state] 

        words = list(next_word_counts.keys())
        weights = list(next_word_counts.values())

        word = random.choices(words, weights=weights, k=1)[0]

        if i == length - 1:
            print(word + ".")
        else:
            print(word + " ", end="")

        current_state = (current_state[1], word)

enhanced_text = "The beautiful morning brought with it a great opportunity. This moment is the best moment, and every person should cherish it. A dog is a loyal friend, and a cat is an independent companion. That simple truth guides every decision we make. The road ahead is long, but that challenge makes the journey worthwhile. An apple a day keeps the doctor away, and this common phrase highlights a universal lesson. The sun rose over the hills, casting a golden light. Every time we learn, that knowledge helps us grow. This whole effort is designed to be a successful and rewarding project."

make_sentence(
    make_transitions(enhanced_text, transitions), 
    starting_words, 25
)