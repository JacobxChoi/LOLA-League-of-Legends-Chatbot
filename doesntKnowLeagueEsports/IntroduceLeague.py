def IntroduceLeague():
    IntroduceLeague = {
        'state': 'IntroduceLeague',
        'score': '0.5',
        '`I\'m sorry, I\'m not very sure about what you want, but I can give you a brief introduction of the '
        'game goal, champion selection, and some advice for improving in-game skills.`': {
            'state': 'InnerIntroduceLeague',

            '[{no, not, dont, nothing}]': {

            },

            '[{sure, yes}]': {
                '`Great! Do you know how to win a League of legends game?`': {
                    'state': 'Directed_Questions',

                    '[{nexus, base, turrets}]': {
                        'state': 'DestroyNexus',
                        'score': '1.0',
                        '`Exactly! League of legends or LoL is a 5 versus 5 MOBA game, where teammates cooperate together to destroy the other team\'s base and, of course, there are many obstacles on the way to final goal.`': {
                            'state': 'Base',
                            '[{what}, {base, nexus}]': {
                                '`The base or nexus is like the \'headquaters\' of a team where waves of minions enter the battlefield from. The game ends if you destroy the nexus on the base of the other team, but you can\'t do this without relying on your minions.`': {
                                    '[{minion, minions}]': {
                                        'score': '1.0',
                                        'state': 'Minions',
                                        '`Where champions are the heroes that individual players control, minions are non-controlled front-line fighters that can rush against the defense of the foe and take the damage from the turret on behalf of the player. Without them, players wouldn\'t be able to enter the base of the other team.`': {
                                            'state': 'minion',
                                            '[{minion, minions, they}, {essential, key, important}]': {
                                                'state': 'MinionImportant',
                                                '`Yeah, the waves of minions that can bear the boat of the victory is the same that swallows it. So, it\'s important to have a sophisticated control of the minions in order to win the game`': {
                                                    '[{explain,know, more},{control}]': {
                                                        'state': 'toMinionWaveControl',
                                                        '`The skill is really learned and honed with thinking in actual practice, but for sure I can give you some hints if you\'d like to know.`': {
                                                            '[#AgreementChecker]': {
                                                                '#IF(#POSITIVE_AGREEMENT) `Wow, it\'s great you have interest in it. I can give you the experience I summarized from playing the game. More is for you to explore`': 'MinionwaveControl',
                                                                '#IF(#NEGATIVE_AGREEMENT) `That\'s alright. I guess it\'s more important for a beginner to find an interest for the game rather than getting overwhelmed with details. What else do you want to know`': 'IntroduceLeague',
                                                                'error': {
                                                                    '`Forgive me for my inability to understand you, but do you know the goal of League of Legends?`': 'Directed_Questions'
                                                                }
                                                            }
                                                        }
                                                    },

                                                    '[{hard, complicated}]': {
                                                        '`Don\'t be overwhelmed by this, with practice, you\'ll definitely become more and more experienced in this! Do you have any other questions?`': 'IntroduceLeague',
                                                    },

                                                    '[{interesting, challenging}]': 'toMinionWaveControl',

                                                    'error': {
                                                        '`(◉◞౪◟◉) Pardon my absent-mindedness just then. Could you say that again?': 'MinionImportant'
                                                    }
                                                }

                                            },

                                            '[{understand, get}]': {
                                                '`ξ( ✿＞◡❛)`': 'MinionImportant'
                                            },

                                            'error': {
                                                '`(◉◞౪◟◉) Pardon my absent-mindedness just then. Could you say that again?': 'minion'
                                            }

                                        }

                                    },

                                    '[turret, turrets, tower]': {
                                        'state': 'turrets',
                                        '`Turrets are the main obstacles on your way to destroy the nexus.They can deal high damage if you hastily enter into their range without your minions by you.`': {
                                            '[{protect}, {own}]': {
                                                '`You really have the talents! Turrets are \'strategic weapons\' that we need to protect in order to protect our base from being attacked.`': {

                                                }
                                            },

                                            '[{not, dont}, {understand, sure, get}]': {
                                                'score': '0.7',
                                                '`You can think those turrets as guardians that protect your base from enemy attacks, so you really want to try hard to protect your own turrets while destroying the enemy turrets alongside your minions.`': {
                                                    '[{how}, {protect}]': {
                                                        '`Good question! Turrets take the most damage from enemy champions, so you want to try to avoid leaving your turrets alone with enemy champions, especially while they have minions in your lane.`': {

                                                        }
                                                    },
                                                    '[{understand, get}]': {
                                                        'score': '0.5',
                                                        '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'

                                                    },

                                                    'error': {
                                                        '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                    }
                                                }

                                            },

                                            '[{understand, get}]': {
                                                'score': '0.5',
                                                '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                            },

                                            'error': {
                                                '`(≧∀≦)ゞ I\'m really sorry for missing that, could you explain what you\'re asking again?`': 'Base'
                                            }

                                        }

                                    },

                                    '[{not, dont},{understand, sure, get}]': {
                                        'score': '0.7',
                                        '#GameGoalAnalogy': {
                                            '[{resources, resource}]': {
                                                'state': 'resource',
                                                '`Enemy champions, neutral monsters, minions, turrets. You gain experience and gold from these, which allows you to build up weapons and armor.`': {
                                                    '[{build, weapon, armor}]': 'buildInfo',
                                                    '[{minions, minion}]': 'Minions',
                                                    '[{turrets}]': 'turrets',
                                                    '[{monsters}]': {
                                                        'state': 'neutralMonsters',
                                                        '`There are many different types of neutral monsters distributed \n nearly symmetrically across the map. You can gain gold, experience, and buffs from defeating them.`': {
                                                            'state': 'MonstersInfo',
                                                            '[{type, different}]': {
                                                                'state': 'TripStart',
                                                                '`Great, I can guide you across the Summoner\'s Rift to \n see the ecology of the monsters. You can always stop me for further information about the monsters such as its origin and power \n and feel free to take off the safari vehicles. We will leave you around the monsters (=^-ω-^=). \n Are you prepared to set out on the journey?`': {
                                                                    'state': 'MonsterTrip',
                                                                    '[{ecology, trip, funny, weird}]': {
                                                                        'score': '1.0',
                                                                        '`I\'m just kidding. So, are you ready to set out on the safari trip around Summoners Rift?`': 'MonsterTrip'
                                                                    },

                                                                    '[#AgreementChecker]': {
                                                                        'score': '0.5',
                                                                        '#IF(#POSITIVE_AGREEMENT) `Welcome to the one and only Summoners Rift Safari Tour! We\'re embarking on a thrilling adventure through the realm of \n epic battles, legendary creatures, and stunning landscapes. Please make sure your seatbelts are fastened \n and your cameras are ready because we\'re about to witness the most gorgeous monsters you\'ve ever laid eyes on! \n Throughout the tour, please don\'t hesitate to ask any questions you may have about the monsters\' origins, powers, or roles in the Rift. \n It\'s not every day that you get to witness such a diverse and fascinating array of creatures, so let\'s make the most \n of this unforgettable adventure!`': {
                                                                            '[{quit,leave}]': {
                                                                                '`No worry, you can always visiting our Summoners Rift Safri Tour, if you call on the name. Do you have other questions regarding to league and league esports`': 'IntroduceLeeague'
                                                                            },

                                                                            'error': {
                                                                                '`Our first stop will be the picturesque Blue Sentinel\'s lair. Be prepared to be amazed by the beautiful and majestic Blue Sentinel, \n an enormous golem adorned with shimmering crystals. Be sure to snap a photo as it lumbers around, but don\'t get too close, \n for it might just smash you with its powerful fists! Do you want to know more about its origin and power, or yo9u want to move to vist another monster?`': {
                                                                                    'state': 'MonsterFirstGlance',
                                                                                    '[{blue, sentinel}]': {
                                                                                        'score': '0.5',
                                                                                        'state': 'blueBuff',
                                                                                        '`It\'s a fearsome monsters guarding the power of energy and mana regeneration, but tempting treasures for greedy, novice hunters.`': 'MonsterFirstGlance'
                                                                                    },

                                                                                    '[{energy, mana}]': {
                                                                                        'score': '0.7',
                                                                                        '`You must be a novice hunter in the rift. Energy or mana is the power champions rely on to use powerful skills and magic`': 'MonsterFirstGlance'
                                                                                    },

                                                                                    '[{cooldown}]': {
                                                                                        'score': '0.7',
                                                                                        '`Even though you may have the energy to release your power, you cannot use it consecutively with no stop, cooldown period is thus the time period between releasing a same skill`': 'MonsterFirstGlance'
                                                                                    },

                                                                                    '[{origin, from, role}]': {
                                                                                        'score': '0.7',
                                                                                        '`Legends say that the Blue Sentinel is a manifestation of the ancient forces that built the Summoners Rift itself. As times going on, it becomes a `': 'MonsterFirstGlance'

                                                                                    },

                                                                                    '[{power, buffs, buff}]': {
                                                                                        'score': '0.7',
                                                                                        '`As an ancient guardian, it holds the Crest of Insight, which bestows the gift of mana regeneration and cooldown reduction upon those brave enough to defeat it. `': 'MonsterFirstGlance'

                                                                                    },

                                                                                    '[{next, continue, move, away}]': {
                                                                                        '`Moving along, we\'ll pass by the fascinating Brambleback family. Observe the captivating Crimson Brambleback, a giant, red-scaled lizard \n with molten rocks protruding from its back, and its two adorable Cinderlings. Make sure to hold onto your hats as they unleash bursts of fire, \n demonstrating their fierce territorial instincts.`': {
                                                                                            'state': 'MonsterSecond',
                                                                                            '[{crimson, brambleback}]': {
                                                                                                'score': '0.5',
                                                                                                '`Dwelling in the dense foliage of the Rift, the Crimson Brambleback is a formidable beast, resembling a cross between a lizard \n and a volcanic rock formation. Its deep, red scales emit an eerie glow, and the molten rocks on its back showcase its fiery temperament. \n  When provoked, this fierce creature can unleash a torrent of flames to defend its territory. The Crimson Brambleback is the guardian of the Red Buff, \n providing the Crest of Cinders to empower the attacks of the champion who bests it in combat.`': 'MonsterSecond',
                                                                                            },

                                                                                            '[{cinderlings, cinderling}]': {
                                                                                                'score': '0.5',
                                                                                                '`The adorable, yet feisty offspring of the Crimson Brambleback, Cinderlings are small, fiery creatures that aid their parent in defending their home. \n With their miniature molten-rock armor and tiny bursts of flame, these little rascals may be small in size, but they are mighty in spirit. \n It is said that a single touch from their flaming breath can set an enemy ablaze.`': 'MonsterSecond',
                                                                                            },

                                                                                            '[{origin, from, role}]': {
                                                                                                'score': '0.7',
                                                                                                '`It is said that these fiery creatures emerged from the volcanic regions of Runeterra, \n born from the union of elemental fire and the earth\'s molten core. Over time, the Crimson Brambleback and its Cinderlings \n found their way to the Summoners Rift, drawn by the latent magic that permeates the land. They now serve as guardians of the Red Buff,\n protecting the powerful Crest of Cinders.`': 'MonsterSecond'

                                                                                            },

                                                                                            '[{power, buff, buffs}]': {
                                                                                                'score': '0.7',
                                                                                                '`The Crimson Brambleback, or you can call it red, is the guardian of the Red Buff, providing the Crest of Cinders to empower \n the attacks of the champion who bests it in combat. `': 'MonsterSecond'

                                                                                            },

                                                                                            '[{next, continue, move, away}]': {
                                                                                                '`As we continue, prepare to feast your eyes on the Rift Scuttler family, or you can call it crabs. These charming crustaceans scuttle across the river, \n serving as peaceful guardians. Their enchanting blue and purple shells sparkle like precious gems. Remember to be gentle with them, \n as they are the only non-aggressive monsters you\'ll find in the Rift.`': {
                                                                                                    'state': 'VisitCrab',

                                                                                                    '[{crab,scuttler}]': {
                                                                                                        'score': '0.5',
                                                                                                        '`The adorable, yet feisty offspring of the Crimson Brambleback, Cinderlings are small, fiery creatures that aid their parent in defending their home. \n With their miniature molten-rock armor and tiny bursts of flame, these little rascals may be small in size, but they are mighty in spirit. \n It is said that a single touch from their flaming breath can set an enemy ablaze.`': 'VisitCrab',
                                                                                                    },

                                                                                                    '[{origin, from, role}]': {
                                                                                                        'score': '0.7',
                                                                                                        '`It is said that these fiery creatures emerged from the volcanic regions of Runeterra, \n born from the union of elemental fire and the earth\'s molten core. Over time, the Crimson Brambleback and its Cinderlings \n found their way to the Summoners Rift, drawn by the latent magic that permeates the land. They now serve as guardians of the Red Buff,\n protecting the powerful Crest of Cinders.`': 'VisitCrab'

                                                                                                    },

                                                                                                    '[{power, buff, buffs}]': {
                                                                                                        'score': '0.7',
                                                                                                        '`The Crimson Brambleback, or you can call it red, is the guardian of the Red Buff, providing the Crest of Cinders to empower \n the attacks of the champion who bests it in combat. `': 'VisitCrab'
                                                                                                    },

                                                                                                    '[{continue, next, move,away}]': {
                                                                                                        '`Next, we venture into the haunting and mysterious Dragon\'s pit. Here, you\'ll witness the breathtaking Elemental Drakes – \n Cloud, Infernal, Ocean, and Mountain – each with its unique powers and mesmerizing appearance. \n Don\'t forget to ask about the mighty Elder Dragon, whose fearsome presence sends chills down the spines of even the most seasoned summoners.`': {
                                                                                                            'state': 'visitDrake',

                                                                                                            '[{drakes,dragon, drake, dragons}]': {
                                                                                                                'score': '0.5',
                                                                                                                'state': 'dragon',
                                                                                                                '`I can guide you to know each of the drakes, which one do you want to visit first`': 'visitDrake',
                                                                                                            },

                                                                                                            '[{cloud}]': {
                                                                                                                'score': '0.7',
                                                                                                                '`An ethereal creature with gossamer wings, the Cloud Drake harnesses the power of wind. Its wispy scales seem to blend with \n the very air around it. When defeated, it grants the victorious team enhanced movement speed, allowing them to swiftly traverse the Rift.`': 'visitDrake'

                                                                                                            },

                                                                                                            '[{infernal}]': {
                                                                                                                'score': '0.7',
                                                                                                                '`A blazing vision of terror and beauty, the Infernal Drake is a dragon of fire and fury. Its scales are a vivid red, \n and plumes of flame billow from its maw. The Infernal Drake bestows increased attack power upon the team that conquers it, \n fueling their destructive potential.`': 'visitDrake'

                                                                                                            },

                                                                                                            '[{ocean}]': {
                                                                                                                'score': '0.7',
                                                                                                                '`A serpentine beast with azure scales, the Ocean Drake embodies the essence of water. Its flowing mane mimics the waves of the deep sea, \n and its gaze can pierce the darkest depths. When vanquished, the Ocean Drake provides enhanced health regeneration \n to the victorious team, allowing them to recover from their battles more quickly.`': 'visitDrake'

                                                                                                            },

                                                                                                            '[{mountain}]': {
                                                                                                                'score': '0.7',
                                                                                                                '`A titan of stone and earth, the Mountain Drake is a force to be reckoned with. Its granite-like scales seem to merge with the very mountains \n that surround it. The Mountain Drake grants increased resistance to damage upon the team that defeats it, \n enabling them to withstand the fiercest assaults.`': 'visitDrake'

                                                                                                            },

                                                                                                            '[{elder}]': {
                                                                                                                'score': '0.7',
                                                                                                                '`Behold the Elder Dragon, a majestic titan of unfathomable power and scale. Its colossal, sinewy body stretches across the horizon, \n adorned with intricate, glowing runes that pulsate with the primal energy of the elements. The Elder Dragon\'s iridescent scales shimmer \n in the faint light, a kaleidoscope of colors that dance and shift with each subtle movement.`': 'visitDrake'

                                                                                                            },


                                                                                                            '[{origin, from, role}]': {
                                                                                                                'score': '0.7',
                                                                                                                '`The Elemental Drakes are said to be the children of the great dragon gods that once ruled the skies of Runeterra. \n Each drake embodies the power and essence of its respective element – wind, fire, water, and earth. Over the centuries, they were drawn to the \n Summoners Rift by the allure of its potent magic, and they have since made the Dragon\'s pit their home.`': 'visitDrake'

                                                                                                            },

                                                                                                            '[{power}]': {
                                                                                                                'score': '0.7',
                                                                                                                '`Those Dragon is not just a creature; it is a force of nature, an embodiment of the untamed wilds of Runeterra.`': 'visitDrake'
                                                                                                            },


                                                                                                            '[{continue, next, move, away}]': {
                                                                                                                '`Finally, we\'ll visit the legendary Baron Nashor, the Rift\'s most fearsome and awe-inspiring beast. This colossal serpent-like creature, with its razor-sharp teeth and piercing tentacles, is the ultimate test for any safari adventurer. But fear not, for we are well-prepared and will safely observe this mighty beast from a distance.`': {
                                                                                                                    'state': 'VisitNashor',

                                                                                                                    '[{nashor, baron}]': {
                                                                                                                        'score': '0.7',
                                                                                                                        'state': 'BaronNashorx',
                                                                                                                        '`The Baron Nashor\'s massive head looms above us, its myriad of razor-sharp teeth and vicious, barbed tentacles casting a \n terrifying shadow. Its eyes burn with a malevolent intelligence, observing our every move as though evaluating our worth as adversaries.`': 'VisitNashor'

                                                                                                                    },

                                                                                                                    '[{origin, from, role}]': {
                                                                                                                        'score': '0.7',
                                                                                                                        '`The origins of the Baron Nashor are steeped in the mythology of the cosmos. Born from the tumultuous battle between the gods of Runeterra, \n it is a living embodiment of chaos and destruction. Drawn to the Summoners Rift by the potent magic that saturates the land, the Baron Nashor \n has made its home in the dark recesses of the Rift, waiting to test the mettle of those who dare to challenge its might.`': 'VisitNashor'

                                                                                                                    },

                                                                                                                    '[{power}]': {
                                                                                                                        'score': '0.7',
                                                                                                                        '`The Baron Nashor\'s primary power lies in the "Hand of Baron" buff it bestows upon the team that manages to defeat it. \n This extraordinary buff greatly empowers the champions and their minions, granting increased attack damage, ability power, and enhanced recall speed. \n It also empowers nearby allied minions, making them more resilient and powerful. The Hand of Baron can completely shift \n the momentum of a battle, enabling a team to siege their opponents\' base with relentless ferocity.`': 'VisitNashor'
                                                                                                                    },

                                                                                                                    '[{continue, leave, move, away, next}]': {
                                                                                                                        '`A sullen imaginative trip ends there, you don\'t understand what the non-sense you\'ve experienced just now. But sanity tells you it\'s the time for asking more questions over the game and its god-know-what esport`': 'InnerIntroduceLeague'
                                                                                                                    },

                                                                                                                    'error': {
                                                                                                                        '#FunTripError': 'VisitNashor'
                                                                                                                    }
                                                                                                                }
                                                                                                            },

                                                                                                            'error': {
                                                                                                                '#FunTripError': 'visitDrake'
                                                                                                            }
                                                                                                        }
                                                                                                    },

                                                                                                    'error': {
                                                                                                        '#FunTripError': 'VisitCrab'
                                                                                                    }
                                                                                                }
                                                                                            },

                                                                                            'error': {
                                                                                                '#FunTripError':  'MonsterSecond'
                                                                                            }
                                                                                        }
                                                                                    },

                                                                                    'error': {
                                                                                        '#FunTripError': 'MonsterFirstGlance'
                                                                                    }
                                                                                }

                                                                            },
                                                                        },
                                                                        '#IF(#NEGATIVE_AGREEMENT)': {
                                                                            '`No worry, the wonderful monster trip will always be there if you call on its name`': 'IntroduceLeague'
                                                                        },
                                                                        'error': {
                                                                            'state': 'suddenFirst',
                                                                            '`Σ(°Д°) Don\t move. A monster is right in front of us. Do you see the large, blue, golem-like creature with a blue crystalline body? That\'s a blue sentinel. Together with its 2 minions, they are fearsome monsters, but tempting treasures for greedy, novice hunters.`': 'MonsterFirstGlance'
                                                                        }

                                                                    },

                                                                    '[{other}]': {
                                                                        'score': '0.7',
                                                                        '`Well, what other questions do you have about League of Legends and League esports?`': 'IntroduceLeague',

                                                                    },

                                                                    'error': {
                                                                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Are prepared for the trip or do you want to switch to other questions?`': 'MonsterTypes',
                                                                    }
                                                                }

                                                            },

                                                            'error': {
                                                                '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'neutralMonsters',
                                                            }

                                                        }
                                                    },
                                                    'error': {
                                                        '`༼ つ◕_◕ ༽つ Do you have other questions about League?`': 'IntroduceLeague',
                                                    }
                                                }

                                            },

                                            '[{what}, {weapon, defense}]': {
                                                'state': 'buildInfo',
                                                '`Appropriate builds include weapons, clothes... , that you can purchase in your base. These can greatly enhance your power and help you gain an edge in combat. For a beginner, you can just follow the recommended items that automatically show when you open the shop.`': {
                                                    '[{purchase, buy}]': {

                                                    },

                                                    'error': {
                                                        '`(≧∀≦)ゞ My apologies, could you explain what you\'re asking a little more please? `': 'IntroduceLeague',

                                                    }
                                                }

                                            },

                                            '[{competitive}]': {

                                            },

                                            '[{why}, {brain}]': {
                                                '`A game is like a dream, where players are forced into sets of absurd rules, and they\'re happy with it. But that\'s off-topic. Do you have other questions about the game goal?`': 'Directed_Questions',
                                            },

                                            '[{understand, get}]': 'understandLeague',
                                            'error': {
                                                '`(*\'ω\')人(\'ω\'*) Cool! do you have other questions about the game?`': 'IntroduceLeague'
                                            }

                                        }

                                    },

                                    '[{understand, get}]': {
                                        'state': 'understandLeague',
                                        'score': '0.5',
                                        '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'

                                    },

                                    'error': {
                                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'DestroyNexus'
                                    }
                                }
                            },
                            '[{played}, {moba}]': {
                                '`Wow, which one did you play? Have you played DOTA 2 or Vain Glory ?`': {
                                    '[dota]': {
                                        'score': '1.0',
                                        '`Then I guess you\'ll get a handle on League of Legends quicker, since DOTA shares a lot of core elements with LoL despite some of its more complex systems.`': {
                                            'state': 'compareWithDOTA',
                                            '[{different, difference}]': {
                                                '`Well, in League of Legends, you can\'t kill your own minions and there aren\'t any courier units. Also, each game takes less time, making it possibly more catered to a fast-paced life.`': {
                                                    '[{understand, get, see}]': {
                                                        '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                    },
                                                    'error': {
                                                        '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                    }
                                                }
                                            },
                                            'error': {
                                                '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'compareWithDOTA'
                                            }
                                        }
                                    },
                                    '[vainglory]': {
                                        'score': '1.0',
                                        '`Then I guess you\'ll be able to transition to League of Legends more smoothly, since the core elements are similar between LoL and Vainglory.`': {
                                            'state': 'compareWithVG',
                                            '[different, difference]': {
                                                '`The key difference is that Vainglory is designed more for iOS and Android, and it supports touchscreen control. LoL is mainly on PC, so the controls and menus are geared around mouse and keyboard input. Also, there are 3 lanes on the map in LoL instead of just 1.`': {
                                                    '[{understand, get, see}]': {
                                                        '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                    },
                                                    'error': {
                                                        '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                                    }
                                                }
                                            },
                                            'error': {
                                                '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'compareWithVG'
                                            }
                                        }
                                    },
                                    '[{played, play, playing}]': {
                                        'score': '0.5',
                                        '`Great! MOBA games all share similar core design, so you\'ll definitely master LoL faster than most people! Do you have any other questions?`': 'IntroduceLeague'
                                    },
                                    'error': {
                                        '`(ゝ∀･) That\'s great! Do you have any other questions?`': 'IntroduceLeague'
                                    }
                                }
                            },
                            '[{what},{moba}]': {
                                '`MOBA is an acronym for Multiplayer Online Battle Arena. In League of Legends, for example, 5 players on each team are working together in the battlefield of Summoner\'s Rift with the shared goal to destroy the other team\'s Nexus.`': {

                                    '[{arena, battlefield}]': 'mapInfo',

                                    '[{understand, get}]': {
                                        '`ξ( ✿＞◡❛) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                    },
                                    'error': {
                                        '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                    }

                                }

                            },
                            '[hindrance, obstacle, obstacles]': 'turrets',

                            '[{how}, {destroy}]': {

                                '`There are no way for you destroy the base unless you destroy all turrets in a lane and two guardian towers in front of the nexus to destroy the base with help from your minions.`': {
                                    '[{tower, turrets}]': 'turrets',
                                    '[{minions}]': 'Minions',
                                    '[{lot, many}]': {
                                        '`I know it sounds like a hard mission, but when you take to the battlefield, enemy turrets will be demolished like piles of sand in the wind.`': 'end'
                                    },
                                    '[{lane}]': 'laneInfo',
                                    'error': {
                                        '`(・ω・) Do you have other questions about League of Legends?`': 'IntroduceLeague'
                                    }
                                }

                            },

                            'error': {
                                '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'Base',
                            }
                        }
                    },
                    '[#AgreementChecker]': {
                        'score': '0.5',
                        '#IF(#POSITIVE_AGREEMENT) `Wow! Could you explain it to me? I guess different people understand it in different ways.`': {
                            'error': {
                                '`Great! It seems like that you already know much about its objectives, do you want to know more about the side missions in the game or monsters in rift`': 'InnerIntroduceLeague'
                            }
                        },
                        '#IF(#NEGATIVE_AGREEMENT)': 'IntroduceObjectives',
                        'error': {
                            '`Forgive me for my inability to understand you, but do you know the goal of a game of League of Legends?`': 'IntroduceObjectives'
                        }
                    },

                    'error': {
                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerIntroduceLeague',
                    }
                }
            },
            '[{game, learn}]': 'IntroduceGame',
            '[{esports, scene}]': 'IntroduceEsports',
            '[{champions, champs, types, champion}]': 'IntroduceChampions',
            '[{objectives, goal, win}]': 'IntroduceObjectives',
            '[{roles, positions, lanes}]': 'laneInfo',
            '[{map, layout}]': 'IntroduceMap',
            '[{roles, team}]': 'laneInfo',
            '[{top}]': 'topLane',
            '[{mid}]': 'midLaneInfo',
            '[{jungle}]':'jungleInfo' ,
            '[{adc, bot, bottom}]': 'botLaneInfo',
            '[{support}]': 'laneInfoSupport',
            '[tank, tanks]': 'laneInfoTank',
            '[duelist, duelists]':  'laneInfoDuelist',
            '[{assassin, assassins}]':'laneInfoAssassin',
            '[{types, categories}]': 'ChampionTypes',
            '[{popular, favorite}]': 'PopularChampions',
            '[{turrets}]': 'TurretsInfo',
            '[{explain, what}{dragons}]': 'dragons',
            '[{explain, what}{Baron, Nashor}]': 'NashorBaron',
            '[{resource, resources}]': 'resource',
            '[{monsters}]': 'neutralMonsters',
            '[{try}]': 'ReadyToTry',
            '[{blue, buff, sentinel}]': 'blueBuff',
            '[{qualify, events}]': 'QualifyCompetitions',
            '[{living}]': 'EsportsLiving',
            '[destroy,{nexus, base, turrets}]': 'DestroyNexus',
            '[{minion, minions}]': 'Minions',
            '[{watching, streaming}]': 'StreamingPlatforms',
            '[{item}]': 'items',
            '[recommend]': 'InnerChampionRecom',
            'error': {
                '`Sorry, I didn\'t catch that, could you say it again?`': 'IntroduceLeague'
            }
        }
    }
    return IntroduceLeague
