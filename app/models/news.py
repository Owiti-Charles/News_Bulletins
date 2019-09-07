
class Articles:
    """ 
    Articles class to define Article Objects
    
    """
    def __init__(self, source, author, title, description, url, image_url, publish_time):

        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.publish_time = publish_time

class Sources:
    '''
    Sources class that defines each source object
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
