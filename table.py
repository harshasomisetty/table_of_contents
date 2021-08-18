def format_as_title(title):
    chapter = title.split(" ", 1)[0]
    rest = title.split(" ", 1)[1]
    name = rest.rsplit(" ", 1)[0]
    page = rest.rsplit(" ", 1)[-1]
    return "BookmarkBegin\nBookmarkTitle: {0}\nBookmarkLevel: 1\nBookmarkPageNumber: {1}"\
            .format(name, page)

def format_as_subtitle(title):
    name = title.rsplit(" ", 1)[0]
    page = title.rsplit(" ", 1)[-1]
    return "BookmarkBegin\nBookmarkTitle: {0}\nBookmarkLevel: 2\nBookmarkPageNumber: {1}"\
            .format(name, page)

def get_titles(file_loc):
    sections = []
    with open(file_loc, "r") as file:
        lines = [line.rstrip() for line in file if line.rstrip()]
        titles, subtitles = [], []
        for line in lines:
            if line[0] is " ":
                sections.append(format_as_subtitle(line.strip()))
            elif line[0:2] is not "\n":
                sections.append(format_as_title(line.strip()))
    return sections

file = "number_toc.txt"
sections = get_titles(file)
for i in sections:
    print(i)
# for title in titles[:5]:
#     formatted = format_as_title(title)
#     print(formatted)

# for title in subtitles[:5]:
#     formatted = format_as_subtitle(title)
#     print(formatted)

