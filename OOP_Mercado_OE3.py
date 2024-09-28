class SocialMediaAccount():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        pass
    def post(self):
        pass

class InstagramAccount(SocialMediaAccount):
     def __init__(self,username, password, numberoffollowers):
        super().__init__(username,password)
        self.numberoffollowers = numberoffollowers
        
     def share_story(self):
        pass

class X_Account(SocialMediaAccount):
    def __init__(self,username,password, numberoftweets):
        super().__init__(username,password)
        self.numberoftweets = numberoftweets
    def tweet(self):
        pass