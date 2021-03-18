from mediawiki import MediaWiki
import string
wikipedia = MediaWiki()




def babson_college():
    babson = wikipedia.page("Babson College")
    
    return babson.content

print(babson_college())
