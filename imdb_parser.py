import HTMLParser

"""
The IMDBParser class is used to parse the HTML received from IMDB in order to
find the movie title, the movie storyline, and the movie poster.

attributes:
    title - title of the movie
    storyline - storyline of the movie
    poster_url - URL of the movie poster
"""
class IMDBParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.title = ""
        self.storyline = ""
        self.poster_url = ""
        self.in_storyline_div = False
        self.in_storyline_p = False
        self.in_title_overview = False
        
    def handle_starttag(self, tag, attrs):
        # Get the title
        if (tag == 'meta') and (('property', 'og:title') in attrs):
            self.title = (a for a in attrs if a[0]=='content').next()[1]
        # Enter the div element that will contain the storyline
        elif (tag == 'div') and (('id', 'titleStoryLine') in attrs):
            self.in_storyline_div = True
        # Enter the p element instead the stroyline div element
        elif self.in_storyline_div and (tag == 'p'):
            self.in_storyline_p = True
        # Enter the div element that will contain the poster URL
        elif (tag == 'div') and (('id', 'title-overview-widget') in attrs):
            self.in_title_overview = True
        # Get the poster URL
        elif self.in_title_overview and (tag == 'img'):
            self.poster_url = (a for a in attrs if a[0]=='src').next()[1]
            self.in_title_overview = False

    def handle_data(self, data):
        # Get the storyline from the storyline p element
        if self.in_storyline_p:
            self.storyline = data
            self.in_storyline_p = False
            self.in_storyline_div = False
            
