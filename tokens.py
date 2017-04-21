import twitter
consumer_key = 'wBIToKaW13vKwZZU3X4OBnh8s'
consumer_secret = 'pN5JmEgtumQZ5D14dLc8W25WRJoX2YPmatxYLIRJDhhXWWOWln'
access_token_secret = 'Kb1iu9dBJgqUTxMPR8fZEOshIDBgZ2poH6e8LVQNOPAgP'
access_token='1436125748-ZvZT07ouxGfJUU9tqHTTyKFaheetUx6VU2EY1VF' 
api = twitter.Api(consumer_key=[consumer_key],
                  consumer_secret=[consumer_secret],
                  access_token_key=[access_token],
                  access_token_secret=[access_token_secret])

results = api.GetSearch(
    raw_query="https://twitter.com/search?src=typd&q=machakos")
print results