def casual():
    casual = {
        'state': 'casual', #at this point, they don't have a favorite professional player. They have a favorite region, but are not watching any games currently
        '`I\'ll share some of my favorite teams. Jojopyun is my favorite player, but my favorite team is Edward Gaming. They\'re fun to watch`': { #user will ask questions
            '{[like, too]}':{#I like them too!
                '`Awesome! What do you like about Edward Gaming?`':'end'
            },
            '[{like}]':{ #What do you like about them?
                '`I like how they\'re very aggressive. They hardly make mistakes, and they\'re really fun to watch.`':'end'
            },
            '{[favorite, team]}':{ #my favorite team is
                '`What do you like about your favorite team?`':'end'
            },
            '{[favorite, player]}':{ #my favorite player, though, is ...
                '`What do you like about them?`':'end'
            },
            '{[think]}':{  #I think this team is better, though
                '`What do you like about this team?`':'end'
            },
            'error':'end'
        }
    }
    return casual