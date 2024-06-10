with open("input.txt","r") as f:
    content = f.read()

upper_content = content.upper()

with open("output.txt","w") as f:
    f.write(upper_content)
    
