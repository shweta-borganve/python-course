def greet(name, language):
    if language == "english":
        greet = "nice to meet you: "
    elif language == "klingon":
        greet = "hghhg: "
    elif language == "elvish":
        greet = "gi suilon : "
    return greet + name
    
print(greet('ben', 'english'))
print(greet('Raj', 'klingon'))
print(greet('John', 'elvish'))

