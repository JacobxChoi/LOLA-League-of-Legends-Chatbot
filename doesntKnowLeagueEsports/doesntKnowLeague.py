from .IntroduceLeague import IntroduceLeague
from .laneInfo import laneInfo

IntroduceLeague = IntroduceLeague()
laneInfo = laneInfo()

def doesntKnowLeague():
    doesntKnowLeague = {
        'state': 'doesntKnowLeagueEsports',
        '`Have you ever played League of Legends?`': {
            'state': 'playedLOL',
            '[{yes, yeah, yup}]': {
                'state': 'familiarity',
                '`Who\'s your favorite champion?`': {
                    'state':'userPicksChamp',
                    '#UserChamp': {
                        # ontology for favorite champion. Does not unfortunately handle cases where user has no favorite champion
                        '$FAV_CHAMP `is fun to play! Why do you like playing them?`': {
                            'error': {
                                '`I agree! By the way,` $PLAYER_RECOMMEND `is a pro player who happens to play` $FAV_CHAMP `really well. Are you interested in learning about esports?`': {
                                    'state':'learnEsports',
                                    '[{yes, yeah, do, learn, know, sure, ok, okay}]': {
                                        '`Okay, nice!`': 'casual'
                                    },
                                    '[{no, dont, not, nah, nope}]':{
                                        '`No worries! What do you like about league?`': {
                                            'error': {
                                                '`That\'s dope. I got good pretty fast after watching a lot of esports players and teams, and`': 'casual'
                                            }
                                        }
                                    },
                                    'error':{
                                        'My bad, I didn\'t quite get that. Are you still interested in learning about esports?': 'learnEsports'
                                    }
                                }
                            }
                        }
                    },
                    '[{dont, no, not}]': {
                        '`All good. My favorite champion is Irelia. I like playing aggressively and getting kills, so I find playing Irelia pretty fun. Just curious`': 'knowsLeague'
                    },
                    'error': {
                        '`I\'m sorry, I don\'t think I know that champion. Do you have another champion in mind?`': 'userPicksChamp'
                    }
                }
            },
            '[{heard, [video game]}]': {
                '`Yeah, it\'s actually one of the most popular video games in the world! It\'s a competitive, team-based game that\'s played by millions of people, and it has a thriving esports scene. Would you like to learn more about the game or the esports scene?`': {
                    '[{game, learn}]': 'IntroduceGame',
                    '[{esports, scene}]': 'IntroduceEsports',
                    'error': 'IntroduceGame'
                }
            },
            '[{no, nope, not, dont, never, barely, little bit}]': {
                'state': 'transit',
                # Casual questions to collect related infos
                '#GATE `By the way, what\'s your favorite video game?`': {
                    'score': '0.8',
                    'state': 'favGame',
                    '[#FAV_GAMETYPE]': {
                        '`Wow, I tried other` #GET_FAV_GAME `like` $OtherGame `before, but haven\'t touched` $GameName `yet. May I know why you love it?`': {
                            'error': {
                                '`Great! I heard that` #GET_REASON_FAV_GAME` That is definitely amazing! Do you have any tips for a new player?`': {
                                    'error': {
                                        '`Thank you so much, I\'ll definitely keep that in mind! Besides, what do you think of League of Legends`': {
                                            'error': 'transit'
                                        }
                                    }
                                }
                            }
                        }

                    },
                    'error': {
                        '`Cool`': 'transit'
                    }
                },

                '#GATE `May I know why are you interested in knowing more about League esports?`': {
                    'score': '1.0',
                    'state': 'interest',
                    '[{friend, friends, social, community, peers, group}]': {
                        '`Yeah, a shared interest in games connects friends together. What do you typically do with friends in your free time?`': {
                            '[#ACTIVITY_WITH_FRIENDS]': {
                                '`Definitely, I wish I would have the chance to` #GET_ACTIVITY_FRIEND `with my friends too.`': 'transit'
                            },
                        }
                    },
                    '[{fun, challenging, exciting, interesting}]': {
                        '`For sure! After all, the adrenaline rush after watching an exciting matches is true. Do you enjoy the watching other sports events as well?`': {
                            '[#SportEvents]': {
                                '`(^ρ^)/, Wow,I love` #GET_SportsEvent `too. My emotions get quickly driven by the players, and I love that feeling !`': {
                                    'state': 'SportEvents',
                                    '[{too, [as well], yeah, sure, true, definitely}]': {
                                        'score': '0.5',
                                        '`Yeah, the feeling of being is definitely fun, even it\'s online. `': {

                                            '[{yeah,well,true,too,similar}]': {
                                                '`What do you think of esport event then`': {
                                                    'state': 'esportAttitude',
                                                    '[{#ESportAttitudeChecker}]': {
                                                        '#ESportAttitudeResponse': 'transit'
                                                    },

                                                }

                                            },
                                            'error': {
                                                '`Cool, in this case what do you think about the esport event of virtual games?`': 'esportAttitude',
                                            }

                                        }
                                    },
                                    'error': {
                                        '`Cool, in this case what do you think about the esport event of virtual games?`': 'esportAttitude',
                                    }
                                },

                                'error': {
                                    '`Cool, in this case what do you think about the esports event of virtual games?`': 'esportAttitude'
                                }

                            }
                        }
                    },

                    '[{waste, time}]': {
                        '`Ha, sounds like you\'ve fallen into the trap of modernism. I guess there are better ways to use your time.`': 'transit'
                    },

                    '[$FAV_PLAYER=#ONT(leagues)]': {
                        '#IF($FAV_PLAYER = keria) `Agree! Keria is my favorite player too.`': 'transit',
                        '`I like` $FAV_PLAYER `too`': 'transit',
                        'error': 'loveLeague',
                    },
                    '[{not, not really, no, dont, nothing}]': {
                        '`Oh ok, so I guess you just want to get some info on the subject.`': 'transit'
                    },
                    '[{bye, exit}]': {
                        'state': 'quit',
                        '`Adieu, hope to see you again.`': 'end'
                    },
                    'error': {
                        'state': 'loveLeague',
                        '`Cool, I also love to watch league e-sports with friends. The exciting performance of the '
                        'players always fascinates me`': 'transit'
                    },
                },

                '`Let me give you a brief introduction to League of Legends. It\'s actually one of the most popular video games in the world! \n It\'s a competitive, team-based game played by millions of people, and it has a thriving esports scene. \n Do you want to know more about the game mechanics? \n (Remember just say Bye, if you want to quit the bot)`': {
                    'score': '0.5',
                    '[{sure, yes, definitely, ok, okey}]': {
                        '`So do you want to know more about the game mechanics?`': {
                            '[#AgreementChecker]': {
                                'score': '0.5',
                                '#IF(#POSITIVE_AGREEMENT) `For sure,`': 'IntroduceGame',
                                '#IF(#NEGATIVE_AGREEMENT)': {
                                    '`How about the esport scene, I can give you a brief introduction to how league esports work and where to find the exiciting scens!`': 'IntroduceLeague',
                                },
                                'error': {
                                    '`Forgive me for my inability to understand you, but do you know the goal of a game of League of Legends?`': 'Directed_Questions'
                                }
                            },
                        }
                    },
                    '[{game, learn}]': 'IntroduceGame',
                    '[{esports, scene, esport}]': 'IntroduceEsports',
                    'error': 'IntroduceGame'
                }

            },

            'error': {
                '` (￣ε(#￣)☆, Sorry, I didn\'t catch that, could you say it again? ξ( ✿＞◡❛)`': 'playedLOL'
            },

        },

    }

    IntroduceGame = {
        'state': 'IntroduceGame',
        '`In League of Legends, there are five main roles: Top, Jungle, Mid, AD Carry, and Support. Each role has specific responsibilities and champion types. Damage dealers focus on dealing damage to enemy champions, tanks absorb damage and protect their teammates, and supports provide utility to their team through healing, crowd control, and vision control. The map is divided into three lanes and a jungle area. Players must work together, communicate, and strategize to secure objectives and outplay their opponents. Do you want to know how people win a game or the basic info about each lane, or the description for champions`': {
            '[{champions, types}]': 'IntroduceChampions',
            '[{objectives, goal, win}]': 'IntroduceObjectives',
            '[{lane, lanes, roles, positions}]': 'laneInfo',
            '[{items, item}]': 'items',
            '[{no, nothing, fine}]': 'EndIntroduceGame',
            '[{complicated}]': {
                '`It can be at first, but once you get the hang of it, it\'s really fun. You choose a champion to play as, and each one has unique abilities and playstyles.`': 'IntroduceLeague',
            },
            '[{require,need},{coordination}]': {
                '`Absolutely, but that\'s what makes it so much fun! You get to work with your friends to take down the enemy team and claim victory.`': 'IntroduceLeague',
            },
            'error': {
                'state': 'IntroduceGameRepeat',
                '`I\'m sorry, I didn\'t quite understand your question. Would you like to know more about the different types of champions, in-game objectives, roles in the game, or monsters in the rift?`': {
                    '[{champions, types}]': 'IntroduceChampions',
                    '[{objective, ingame, goal, win}]': 'IntroduceObjectives',
                    '[{roles, positions, lanes}]': 'laneInfo',
                    '[{no, nothing, fine}]': {
                        'state': 'EndIntroduceGame',
                        '`Feel free to ask me, if you have another questions!ヽ( ° ▽°)ノ`': 'InnerIntroduceLeague',
                    },
                    '[{monsters, monster}]': 'neutralMonsters',
                    'error': 'IntroduceLeague',
                }
            }
        }
    }

    ChampionRoles = {
        'state': 'ChampionRoles',
        '`In a team, champions play specific roles based on their strengths and abilities. The roles are Top, Jungle, Mid, ADC, and Support. Each role contributes to the overall success of the team. Which role sounds interesting to you?`': 'laneInfo'
        }

    IntroduceObjectives = {
        'state': 'IntroduceObjectives',
        '#GameGoalAnalogy': {
            'state': 'InnerObjectives',
            '[{obstacles, hindrance, barrier, barricade, block}]': {
                'state': 'obstacles',
                '`There are turrets for both teams in each lane to block our road to enemies\'s base. The enemy champions will also try to beat us down to block our attack`': {
                    '[{turret}]': 'turrets',
                    '[{lane}]': 'laneInfo',
                    '[{side mission, side}]': 'sideMissions',
                    'error':{
                        '`If you have any question over any confusing term in my explanation. Just let me know`': 'IntroduceLeague'
                    }

                }

            },

            '[{side mission, side}]':{
                'state': 'sideMissions',
                '`To gain advantages over the enemy champions, we can beat neural monsters, like dragons and Baron Nashor, on the map to gain more golds and buffs`': {
                    '[{monsters, comp}]': 'neutralMonsters',
                    '[{dragons}]': 'dragons',
                    '[{Baron, Nashor}]': 'NashorBaron',

                }

            },

            '[{resource, resources}]': 'resource',
            '[{monsters}]': 'neutralMonsters',
            '[{turrets}]': 'turrets',
            '[{dragons, drakes, dragon, drake}]': {
                'state': 'dragons',
                '`Dragons or drakes are one of the powerful neutral monsters. Do you want to know more about the cretures with an virtual safari trip ?`': {
                    '[#AgreementChecker]': {
                        '#IF(#POSITIVE_AGREEMENT)': 'TripStart',
                        '#IF(#NEGATIVE_AGREEMENT)': 'dragon',

                        'error': 'neutralMonsters',

                    }
                }
            },
            '[{Baron Nashor}]': {
                'state': 'NashorBaron',
                '`Baron Nashor is one of the powerful neutral monster. Do you want to know more about the cretures with an virtual safari trip ? `': {
                    '[#AgreementChecker]': {
                        '#IF(#POSITIVE_AGREEMENT)': 'TripStart',
                        '#IF(#NEGATIVE_AGREEMENT)': 'BaronNashorx',

                        'error': 'neutralMonsters',

                    }
                }
            },
            '[{esports, scene}]': 'IntroduceEsports',
            '[{try, game}]': 'ReadyToTry',
            'error': 'IntroduceLeague',

        }
    }

    IntroduceChampions = {
        'state': 'IntroduceChampions',
        '`By the way, League of Legends has over 150 unique champions, each with their own abilities and playstyle! It\'s so diverse and exciting. (ゝ∀･)b`': {
            'state': 'InnerIntroduceChampions',
            '[{recommend}]': 'RecommendChampions',
            '[{roles, team}]': 'ChampionRoles',
            '[{types, categories}]': 'ChampionTypes',
            '[{popular, favorite}]': 'PopularChampions',
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you have any questions about champions, feel free to ask!`': 'InnerIntroduceChampions'
            }
        }
    }

    ChampionTypes = {
        'state': 'ChampionTypes',
        '`Champions are grouped into six main classes: assassins, fighters, mages, marksmen, supports, and tanks. Each class offers a unique playstyle. Is there a specific class you\'d like to know more about?`': {
            'state': 'InnerChampionTypes',
            '[{assassins, jungle}]': {
                'state': 'AssassinsInfo',
                '`Assassins are like ninjas - fast, sneaky, and deadly! They excel at picking off high-value targets. Popular assassins include Zed, Katarina, and Fizz. Feel free to ask about other champion types or anything else about the game!`': {
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': 'IntroduceLeague'
                }
            },
            '[{fighters, top}]': {
                'state': 'FightersInfo',
                '`Fighters are like brawlers - strong and resilient! They excel in close combat and can take a beating while dishing out damage. Popular fighters include Darius, Garen, and Illaoi. Feel free to ask about other champion types or anything else about the game!`': {
                    'state': 'InnerFighters',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{mages, mid}]': {
                'state': 'MagesInfo',
                '`Mages are the spellcasters of the game, wielding powerful magic to obliterate their enemies. Popular mages include Lux, Veigar, and Annie. Curious about other champion types or any other aspect of the game? Just ask!`': {
                    'state': 'InnerMage',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{marksmen, ad}]': {
                'state': 'MarksmenInfo',
                '`Marksmen are the sharpshooters of the game, dealing consistent damage from a distance. Popular marksmen include Ashe, Miss Fortune, and Jhin. Feel free to ask about other champion types or anything else about the game!`': {
                    'state': 'InnerMarksmen',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{supports, support}]': {
                'state': 'SupportsInfo',
                '`Supports are the unsung heroes of the game, providing utility, protection, and vision for their team. Popular supports include Soraka, Thresh, and Lulu. Feel free to ask about other champion types or anything else about the game!`': {
                    'state': 'InnerSupports',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{tanks}]': {
                'state': 'TanksInfo',
                '`Tanks are the juggernauts of the game, soaking up damage and protecting their allies. Popular tanks include Malphite, Ornn, and Sion. Feel free to ask about other champion types or anything else about the game!`': {
                    'state':'InnerTanks',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerIntroduceLeague'
                    }
                }
            },
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerIntroduceLeague'
            }
        }
    }

    PopularChampions = {
        'state': 'PopularChampions',
        '`Some popular champions among players include Ahri, Yasuo, and Lux. They all have unique abilities that make them stand out. Do you want to know more about any specific champion?`': {
            '[{Ahri}]': {
                'state': 'AhriInfo',
                '`Ahri is a charming mage-assassin. With her quick dashes and mesmerizing abilities, she can leave enemies dazed and confused. Think you might want to give her a try? Or maybe learn about other champions?`': {
                    'state': 'InnerAhri',
                    '[{yes, try, play}]': {
                        'state': 'GiveAhriTry',
                        '`Great! Have fun mastering Ahri\'s abilities and charming your way to victory! Remember, practice makes perfect. If you have any questions or want to learn about other aspects of the game, just let me know!`': 'InnerIntroduceLeague'
                    },
                    '[{other champions, more champions}]': 'PopularChampions',
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{Yasuo}]': {
                'state': 'YasuoInfo',
                '`Yasuo is a skilled swordsman who can cut through enemies like a whirlwind! His high mobility and damage make him a thrilling champion to play. Interested in giving him a shot or exploring other champions?`': {
                    'state': 'InnerYasuo',
                    '[{yes, try, play}]': {
                        'state': 'GiveYasuoTry',
                        '`Awesome! Enjoy mastering Yasuo\'s swift moves and sharp skills. Just like Yasuo, stay focused and you\'ll soon become a force to be reckoned with! If you need help or want to learn more about the game, I\'m here to help!`': 'InnerIntroduceLeague'
                    },
                    '[{other champions, more champions}]': 'PopularChampions',
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{Lux}]': {
                'state': 'LuxInfo',
                '`Lux is a light-wielding mage who brightens up the battlefield! Her abilities include a snare, an area-of-effect damage spell, a shield, and a long-range laser for her ultimate. She\'s not just great at dealing damage but also has utility to support her team. Do you want to know about other champions, or maybe ask about roles, objectives, or anything else related to League of Legends?`': {
                    'state': 'InnerLux',
                    '[{other champions, champions}]': 'PopularChampions',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    '[{champion types, types}]': 'ChampionTypes',
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{another, other}]': 'AnotherChampion',
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about the champions, just let me know!`': 'InnerChampionTypes'
            }
        }
    }

    RecommendChampions = {
        'state': 'RecommendChampions',
        '`Here\' s a list of easy - to - learn champions for each role: \n🌟Top: Garen, Malphite, Darius \n- Jungle: Warwick, Amumu, Vi \n- Mid: Annie, Lux, Veigar \n- ADC: Ashe, Miss Fortune, Sivir \n- Support: Soraka, Leona, Morgana.\nTry them out and find the ones that fit your playstyle best! ε(*´･∀･｀)зﾞDo you wan to know more about any of those champions`': {
            'state': 'InnerChampionRecom',
            '#GetChampion': {
                '#RecommendChampion': 'InnerIntroduceLeague',
            },

            '[{yes, sure, okey}]': {
                '`Which champion do you want to know more about`': {
                    '[$FAN_CHAMP=#ONT(top), champion]': {
                        '`My apologies, could you repeat the champion name again?` $FAN_CHAMP': {
                            '#RecommendChampion': 'InnerIntroduceLeague',
                        }
                    },
                }
            },

            'error':{
                '`I\'m sorry, I didn\'t catch that. If you want to know more about champions, just let me know!`': 'InnerIntroduceLeague'
            }
        }
    }


    IntroduceEsports = {
        'state': 'IntroduceEsports',
        '`Oh man, the esports scene is huge. The two biggest international events are the Mid-Season Invitational and the League of Legends World Championship.`': {
            '[{teams, team}]': 'SpecificTeams',
            '[{players, player}]': 'SpecificPlayers',
            '[{game, event, works}]': 'IntroduceChampions',
            '[{qualify}]': 'QualifyCompetitions',
            '[{professional}]': {
                'state': 'ProTeamsInfo',
                '`In the LoL e-sports scene, teams usually have coaches, analysts, and support staff to help them prepare for matches. They practice together, work on strategies, and scout their opponents to find weaknesses they can exploit. Most regions have their own professional leagues, like the LEC in Europe, LCS in North America, and LCK in Korea. Are you interested in major international competitions or how teams qualify for them?`': {
                    'state': 'InnerProTeams',
                    '[{international, competitions}]': {
                        'state': 'InternationalCompetitions',
                        '`The two biggest international events are the Mid-Season Invitational (MSI) and the League of Legends World Championship, or just Worlds. MSI happens around the middle of the year, while Worlds takes place in the fall. Would you like to learn more about how teams qualify for these events or how players make a living from e-sports?`': {
                            'state': 'InnerInternationalCompetitions',
                            '[{qualify, earn, award}]': 'QualifyCompetitions',
                            '[{living}]': 'EsportsLiving',
                            'error': {
                                '`I\'m sorry, I didn\'t catch that. If you want to know more about how teams qualify for events or how players make a living from e-sports, just let me know!`': 'InnerIntroduceLeague'
                            }
                        }
                    },
                    '[{how, qualify}]': {
                        'state': 'QualifyCompetitions',
                        '`Teams earn championship points throughout the year based on their performance in regional leagues and the MSI. The teams with the most points at the end of the season qualify for Worlds, with additional spots awarded through regional playoffs and a last-chance qualifier. Are you curious about the financial aspect of e-sports or how to start watching LoL e-sports?`': {
                            'state': 'InnerQualification',
                            '[{financial, aspect}]': {
                                'state': 'EsportsLiving',
                                '`Many pro LoL players make a good living from salaries, sponsorships, and prize money. Some of the top players are even considered celebrities in their home countries. The e-sports industry is growing rapidly, and there are more opportunities than ever for talented players.`': {
                                    'state': 'InnerEsportLiving',
                                    '[{watching, streaming}]': {
                                        'state': 'StreamingPlatforms',
                                        '`Streaming platforms like Twitch and YouTube are essential for the growth and popularity of e-sports. Fans can watch live matches, replays, and highlights, as well as follow their favorite players and teams. Some pro players even stream their own gameplay and interact with fans during their downtime. Do you want to know how to start watching League of Legends e-sports or how to start playing the game yourself?`': {
                                            'state': 'InnerStreamingPlatforms',
                                            '[{watch, watching}]': 'StartWatching',
                                            '[{play, playing}]': 'StartPlaying',
                                            'error': {
                                                '`I\'m sorry, I didn\'t catch that. If you want to know more about how to start watching League of Legends e-sports or how to start playing the game, just let me know!`': 'InnerIntroduceLeague'
                                            }
                                        }
                                    },
                                    '[{playing, game}]': 'StartPlaying',
                                    '[{lot, large, huge}]': {
                                        '`Yeah, it\'s worth it. The pro players make a good living from salaries, sponsorships, and prize money, and some of the top players are even considered celebrities in their home countries.`': 'InnerIntroduceLeague'
                                    },
                                    'error': {
                                        '`I\'m sorry, I didn\'t catch that. If you want to know more about watching e-sports on streaming platforms or how to get into playing the game, just let me know!`': 'InnerIntroduceLeague'
                                    }
                                }
                            },
                            '[{watching, esports}]': 'StartWatching',
                            'error': {
                                '`I\'m sorry, I didn\'t catch that. If you want to know more about the financial aspect of e-sports or how to start watching LoL e-sports, just let me know!`': 'InnerIntroduceLeague'
                            }
                        }
                    },
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about international competitions or how teams qualify for them, just let me know!`': 'InnerIntroduceLeague'
                    }
                }
            },
            '[{no, not now, later}]': {
                'state': 'EndEsports',
                '`That\'s totally fine! If you ever want to learn more about the esports scene or anything else related to League of Legends, feel free to ask.Have a great time playing the game!`': 'InnerIntroduceLeague'
            },
            'error': 'IntroduceLeague',
        }
    }

    SpecificTeams = {
        'state': 'SpecificTeams',
        '`Some of the most famous and successful teams in League of Legends history include T1 (formerly SK Telecom T1) from Korea, Fnatic and G2 Esports from Europe, and Team SoloMid and Cloud9 from North America. These teams have consistently performed well in their regional leagues and at international events. Are you interested in learning about specific players?`': {
            '[{yes, players, specific}]': 'SpecificPlayers',
            '[{no, not now, later}]': {
                'state': 'EndPlayers',
                '`Okay! If you ever want to know more about specific players or anything else related to League of Legends, just let me know. Enjoy your journey into the world of League of Legends!`': 'end'
            },
            'error': 'InnerIntroduceLeague'
        }
    }

    SpecificPlayers = {
        'state': 'SpecificPlayers',
        '`Some legendary players in the history of League of Legends esports are Faker (mid laner for T1), Uzi (former ADC for Royal Never Give Up), Caps (mid laner for G2 Esports), and Doublelift (former ADC for Team SoloMid and Team Liquid). These players have had successful careers and have made a significant impact on the esports scene. I can also share some of my favorite players and teams if you\'re interested.`': {
            '[{yes, know}]': { #yes, I'd like to know about your favorite teams/players as well
                'state': 'ReadyToTry',
                '`Great!`': 'casual'
            },
            '[{no, not now, later}]': {
                'state': 'EndReadyToTry',
                '`No worries! If you ever decide to give League of Legends a try, or if you have any more questions, feel free to ask. Have a great day!`': 'end'
            },
            'error': 'InnerIntroduceLeague'
        }
    }

    StartWatching = {
        'state': 'StartWatching',
        '`I\'d recommend starting with the regional leagues, like the LEC, LCS, or LCK. This will give you a good introduction to the teams and players, as well as the overall competitive landscape. From there, you can move on to international events like MSI and Worlds. If you\'re interested in playing the game, it\'s free and there are plenty of resources available to help you learn!`': {
            'state': 'InnerStartWatching',
            '[you, {watch, enjoy}]': {
                '`Absolutely! It\'s a big part of the experience. Fans can watch live matches, replays, and highlights, as well as follow their favorite players and teams. Some pro players even stream their own gameplay and interact with fans during their downtime.`': 'IntroduceLeague',
            },
            '[{playing, game}]': 'StartPlaying',
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about playing the game, just let me know!`': 'InnerIntroduceLeague'
            }
        }
    }

    StartPlaying = {
        'state': 'StartPlaying',
        '`While there is a learning curve, the game is free to play, and there are plenty of resources available to help you learn. You can find guides, tutorials, and community forums online to help you improve your skills. Plus, playing with friends can make the experience more enjoyable. If you ever have any questions or want to play together, just let me know! Lastly, would you happen to be interested in learning a bit about the esports scene as well? I can introduce my favorite players and teams too!`': {
            'state': 'InnerStartPlaying',
            '[{yes, ready}]':{
                '`Cool!`':'casual'
            },
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about playing the game or anything else related to League of Legends, just let me know!`': 'InnerIntroduceLeague'
            }
        }
    }

    items = {
        'state': 'items',
        '`Items are intimidating at first glance, but they\'re actually pretty simple. Items are purchased from the '
        'store in your base, and they provide positive effects to you. Most items provide stat bonuses, but some grant '
        'a passive ability, and some are consumables that have some effect when used. Do you want me to explain any '
        'of that in more depth?`': {
            'state': 'itemQuestions',
            '[{how}, {buy, purchase}, {money, gold}]': {
                '`You buy items with gold, which you earn passively throughout the game. You can also get more '
                'gold by defeating minions, enemy champs, or jungle monsters, or by destroying enemy structures. Any '
                'other item questions?`': {
                    '[{-think, no, nope}]': {
                        '`Great, any other general League questions?`': 'IntroduceGame'
                    },
                    'error': {
                        '`I\'m sorry, I didn\'t understand that. Can you say it again please?`': 'itemQuestions'
                    }
                }
            },
            '[{stat, bonus}]': {
                '`Some examples of stat boosting items are the Mercury Treads, which increase your magic resistance and movements speed, and the Bramble Vest, which increases your defense and harms enemies that hit you. Any other item questions?`': {
                    '[{-think, no, nope}]': {
                        '`Great, any other general League questions?`': 'IntroduceGame'
                    },
                    'error': {
                        '`I\'m sorry, I didn\'t understand that. Can you say it again please?`': 'itemQuestions'
                    }
                }
            },
            '[{consumable}]': {
                '`Some consumables restore health and mana, like the Corrupting potion, and some grant temporary stat boosts, like the Elixir of Iron and the Elixir of Sorcery. Another consumable item is the Control Ward, which you can place on the map to gain vision around where the ward is placed. Any other item questions?`': {
                    '[{-think, no, nope}]': {
                        '`Great, any other general League questions?`': 'IntroduceGame'
                    },
                    'error': {
                        '`I\'m sorry, I didn\'t understand that. Can you say it again please?`': 'itemQuestions'
                    }
                }
            },
            '[{passive, ability}]': {
                '`One example is the Spirit Visage, which increases all healing and shielding received from items or abilities by 25%. Another example is the Staff of Flowing Water, which boosts a teammate\'s magic power and reduces their cooldowns if you shield them. Any other item questions?`': {
                    '[{-think, no, nope}]': {
                        '`Great, any other general League questions?`': 'IntroduceGame'
                    },
                    'error': {
                        '`I\'m sorry, I didn\'t understand that. Can you say it again please?`': 'itemQuestions'
                    }
                }
            },
            '[{yeah, yes, yup, yep, sure, ok}]': {
                '`Sure, what would you like to hear about?`': 'itemQuestions'
            },
            '[{-think, no, nah, not really, nope}]': {
                '`Great, any other general League questions?`': 'IntroduceGame'
            },
            'error': {
                '`I\'m sorry, I didn\'t understand that. Can you say it again please?`': 'itemQuestions'
            }
        }
    }

    base = {
        'state': 'base',
        '`Each team has their base at opposite corners of the map. The base is where players respawn after getting '
        'killed, as well as where they can heal their HP and buy items. The nexus is in the center of the base, '
        'protected by 2 turrets which do massive damage to champions in their range. Once one team destroys their '
        'opponents nexus, they win the game.`': 'end'
    }

    return doesntKnowLeague, items, base, laneInfo, IntroduceLeague, IntroduceGame, IntroduceChampions, IntroduceEsports, IntroduceObjectives, ChampionRoles, SpecificTeams, SpecificPlayers, RecommendChampions, PopularChampions, ChampionTypes,ChampionRoles, StartPlaying, StartWatching
