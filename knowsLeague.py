
def knowsLeague():
    favoriteTeam = {
        'state': 'favTeam',
        '`Do you have a favorite professional player?`': {
            '[{yes, yeah}]':{
                'state':'whichFavoritePlayer',
                '`Who is this player?`': {
                    '[{faker}]':{
                        'state':'teamCondition',
                        '`What do you think about how they\'ve been doing lately?`':'end' #continue conversation
                    },
                    'error': {
                        '`I don\'t think I know this player`': 'whichFavoritePlayer'
                    }
                }
            },
            '[{faker}]':'teamCondition',
            'error':'favRegion'
        }
    }
    favoriteRegion = {
        'state':'favRegion',
        '`What\'s your favorite region to watch?`':{
            '[favorite region]':{
                '`What are your thoughts on that particular tournament?`':'end' #leads to open ended response
            },
            'error':'end'
        }
    }
    return favoriteTeam, favoriteRegion