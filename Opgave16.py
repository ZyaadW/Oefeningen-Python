print("""<svg version="1.1"
    baseProfile="full"
    width="300" height="200"
    xmlns="http://www.w3.org/2000/svg">""")
for i in [0,1,2,3,4,5,6,7,8,9,10] :
    print("""
    <circle cx="150" cy="100" r="80" fill="green" />
    <circle cx="30" cy="30" r="50" fills="red" />
    <circle cx"180" cy"100" r="5" fills="blue" />""")
    
print("</svg>")