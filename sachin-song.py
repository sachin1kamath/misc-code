import random

transitions = {}
starting_words_list = [("we", "we")]
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
        while word == current_state:
            word = random.choices(words, weights=weights, k=1)[0]

        if i == length - 1:
            print(word + ".")
        else:
            print(word + " ", end="")

        current_state = (current_state[1], word)

enhanced_text = "We can work, then we know we can do it together. We're the team! We can work the team together to work out with all our powers we have. We know how to fix things, and we know how to build things. Beep, beep, beep, we know the beep-up. We know how to fix the beep-up away. We know how things go away, we know how things go away, and we know how things go away. We know how things can work. We don't know how to thing... things, things, things that have to work. We know how to do things. We know how to fix things. We know how to fix things! We know how to fix things! We know how to fix things, oh standard fix things. We know how to fix things. How to fix things, we are engineers. We know how to fix things. We are, my engineer, know how to fix things. They know how to do things that they need to do. We know how the power works. How, how power works, and we know how the power works. We know how the power works!"

make_sentence(
    make_transitions(enhanced_text, transitions), 
    starting_words, 25
)