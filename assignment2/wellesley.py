from mediawiki import MediaWiki
import string
wikipedia = MediaWiki()




def wellesley_college():
    wellesley = wikipedia.page("Wellesley College")
    
    return wellesley.content
    return wellesley.title

print(wellesley_college())
