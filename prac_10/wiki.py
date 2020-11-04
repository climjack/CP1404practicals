import wikipedia

search_input = input("Enter page title or search phrase: ")
while input != "":
    suggested_results = wikipedia.search(search_input, results=3)
    i = 0
    print("Did you mean:")
    for result in suggested_results:
        i += 1
        print(f"{i}. {result}")
    print(f"{i + 1}. *None of the above*")
    selection_input = input("Enter selection: ")
    if selection_input != "4":
        print(wikipedia.summary(suggested_results[int(selection_input) - 1]))
        search_input = input("Enter page title or search phrase: ")