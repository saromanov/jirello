from trello import TrelloClient

class Trello:
    '''
        main object for trello manipulation
        it supports getting cards, boards, etc
    '''
    def __init__(self, key, secret, oauth_key, oauth_token_secret):
        self._client = TrelloClient(api_key=key,api_secret=secret,token=oauth_key,token_secret=oauth_token_secret)
    
    def get_boards(self):
        '''
        return list of boards
        '''
        return self._client.list_boards()
    
    def get_last_activity(self):
        '''
        return last activity on the board
        '''
        return self._client.get_last_activity()