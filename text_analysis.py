from mediawiki import MediaWiki

wikipedia = MediaWiki()


def fetchWikipediaData():
    pages= ["Babson College","Wellesley College","Olin College","Harvard University"]
    data_of_colleges=[]
    for page in range(len(pages)):
        print(pages[page])
        college = wikipedia.page(pages[page])
        data_of_colleges.append(college.content)

    return data_of_colleges

wikipedia_data= fetchWikipediaData()
print(wikipedia_data)

# print(babson.title)
# print(babson.content)