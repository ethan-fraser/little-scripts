import webbrowser

link = input("Enter link:\n")

link = link.split(".")

print(link)

for x in link:
    if x == "reddit":
        link[link.index(x)] = "removeddit"

".".join(link)

print(link)
webbrowser.open_new_tab(link)
