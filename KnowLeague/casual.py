def casual():
    casual = {
        'state': 'casual', #at this point, they don't have a favorite professional player. They have a favorite region, but are not watching any games currently
        '#GATE`I\'ll share some of my favorite teams. Jojopyun is my favorite player, but my favorite team is Edward Gaming. They\'re fun to watch`': { #user will ask questions
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
        },
        '#GATE `Are there any games or tournaments that you watched this year?`':{ #user didn't watch Lola suggested games, but perhaps they still watched a game this year
            '[{yes, yeah, watched, watch}]':{ #yeah! this year, I watched a game between team1 and team2
                '`That\'s cool! Who was the highlight of the game?`' :{

                },
                '`Nice! Who won the game? Was it close?`':{
                    '[{yes, yeah, close}]':{ #yeah, it was a really close game!
                        '`awesome!`':'end'
                    },
                    '[{no, not}]':{ #no, the game wasnt really close
                        '`Dang. I\'m not a fan of one-sided games either.`':'end'
                    }
                }
            },
            '[{no, did not, didnt}]':{
                '`no worries!`':'end'
            },
            'error':'end'
        } #TODO: add another conversation so that gate is not stuck
    }
    return casual