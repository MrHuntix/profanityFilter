import re
import math

#A helper class to clean and score a comment
class CommentCleaner:
    def __init__(self,comment):
        self.comment=comment

    #helper function to remove punctuations
    #returns a list of words whithout any special characters, numbers etc.
    def remove_punctuations(self):
        words=re.sub('[^A-Za-z]+',' ', self.comment.lower())
        return words.strip().split(" ")

    #helper function to remove stop words
    #returns a list of words without any stop words
    def remove_stop_words(self):
        stop_words=['a','an','or','the','is','are','ok','and']
        words=self.remove_punctuations()
        words=[word for word in words if word not in stop_words]
        return words

    #a helper function to calculate the profanity percentage in a given comment
    #SCORE=(no. of profanity words in a comment/len. of words)*100
    #returns a tuple containing count of profanity words and the profanity percentage
    def calc_score(self):
        profanity_words=['ass','bitch','idiot','stupid','dumb','shit','rascal']
        profanity_score=0
        words=self.remove_stop_words()
        #print(words)
        for word in words:
            if word in profanity_words:
                profanity_score+=1
        return (profanity_score,math.ceil((profanity_score/len(words))*100))
    

        
