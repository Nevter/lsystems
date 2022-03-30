## Generator for L-systems

def generate(axiom, rules, num_gen):
    sentence = axiom
    for i in range(0,num_gen):
        sentence = generate_next(sentence, rules)
    return sentence

def generate_next(sentence, rules):
    new_sentence = ""
    for variable in sentence:
        try:
            new = rules[variable]
        except: 
            new = variable
        new_sentence += new
    return new_sentence        
