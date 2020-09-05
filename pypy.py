
def search_link_google(inp):
    inp=inp.split(" ")
    query=inp[0]
    for i in range(1,len(inp)):
        query+="+"+inp[i]
    return "https://www.google.com/search?q="+query+"&client=ubuntu&sourceid=chrome&ie=UTF-8"
while True:
    print(search_link_google(input("input: ")))
