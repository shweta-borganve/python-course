def greet(name, language):
    if language == "english":
        greet = "nice to meet you"
    elif language == "klingon":
        greet = "hghhg"
    elif language == "elvish":
        greet = "gi suilon"
    return greet + name
    greet('ben', 'english')