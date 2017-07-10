import json
string_1 = r"""[{'copyright': 'Copyright (c) 2017 Pro Publica Inc. All Rights Reserved.',
 					'results': [{'actions': [{'datetime': '2017-03-30 00:00:00 UTC',
                           'description': 'Presented to President.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'Motion to reconsider laid on the '
                                          'table Agreed to without objection.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'On passage Passed by the Yeas and '
                                          'Nays: 215 - 205 (Roll no. 202).'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'Considered as unfinished business.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'POSTPONED PROCEEDINGS - At the '
                                          'conclusion of debate on S.J.Res. '
                                          '34, the Chair put the question on '
                                          'passage and by voice vote, '
                                          'announced that the ayes had '
                                          'prevailed. Mr. Doyle demanded the '
                                          'yeas and nays and the Chair '
                                          'postponed further proceedings on '
                                          'the question of passage until a '
                                          'time to be announced.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'The previous question was ordered '
                                          'pursuant to the rule.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'DEBATE - The House proceeded with '
                                          'one hour of debate on S.J. Res. '
                                          '34.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'Rule provides for consideration of '
                                          'S.J. Res. 34 with 1 hour of general '
                                          'debate. Previous question shall be '
                                          'considered as ordered without '
                                          'intervening motions except motion '
                                          'to recommit with or without '
                                          'instructions. Measure will be '
                                          'considered read. Bill is closed to '
                                          'amendments.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'Considered under the provisions of '
                                          'rule H. Res. 230.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'Rule H. Res. 230 passed House.'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'On passage Passed by the Yeas and '
                                          'Nays: 215 - 205 (Roll no. 202). '
                                          '(text: CR H2489)'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'Considered as unfinished business. '
                                          '(consideration: CR H2503-2504)'},
                          {'datetime': '2017-03-28 00:00:00 UTC',
                           'description': 'Considered under the provisions of '
                                          'rule H. Res. 230. (consideration: '
                                          'CR H2489-2501)'},
                          {'datetime': '2017-03-27 00:00:00 UTC',
                           'description': 'Rules Committee Resolution H. Res. '
                                          '230 Reported to House. Rule '
                                          'provides for consideration of S.J. '
                                          'Res. 34 with 1 hour of general '
                                          'debate. Previous question shall be '
                                          'considered as ordered without '
                                          'intervening motions except motion '
                                          'to recommit with or without '
                                          'instructions. Measure will be '
                                          'considered read. Bill is closed to '
                                          'amendments.'},
                          {'datetime': '2017-03-23 00:00:00 UTC',
                           'description': 'Held at the desk.'},
                          {'datetime': '2017-03-23 00:00:00 UTC',
                           'description': 'Received in the House.'},
                          {'datetime': '2017-03-23 00:00:00 UTC',
                           'description': 'Message on Senate action sent to '
                                          'the House.'},
                          {'datetime': '2017-03-23 00:00:00 UTC',
                           'description': 'Passed Senate without amendment by '
                                          'Yea-Nay Vote. 50 - 48. Record Vote '
                                          'Number: 94.'},
                          {'datetime': '2017-03-23 00:00:00 UTC',
                           'description': 'Considered by Senate.'},
                          {'datetime': '2017-03-23 00:00:00 UTC',
                           'description': 'Passed Senate without amendment by '
                                          'Yea-Nay Vote. 50 - 48. Record Vote '
                                          'Number: 94. (text: CR S1955)'},
                          {'datetime': '2017-03-23 00:00:00 UTC',
                           'description': 'Considered by Senate. '
                                          '(consideration: CR S1942-1955)'},
                          {'datetime': '2017-03-22 00:00:00 UTC',
                           'description': 'Measure laid before Senate by '
                                          'motion.'},
                          {'datetime': '2017-03-22 00:00:00 UTC',
                           'description': 'Motion to proceed to consideration '
                                          'of measure agreed to in Senate by '
                                          'Voice Vote.'},
                          {'datetime': '2017-03-22 00:00:00 UTC',
                           'description': 'Measure laid before Senate by '
                                          'motion. (consideration: CR '
                                          'S1925-1929, S1935-1940)'},
                          {'datetime': '2017-03-22 00:00:00 UTC',
                           'description': 'Motion to proceed to consideration '
                                          'of measure agreed to in Senate by '
                                          'Voice Vote. (consideration: CR '
                                          'S1925)'},
                          {'datetime': '2017-03-15 00:00:00 UTC',
                           'description': 'Placed on Senate Legislative '
                                          'Calendar under General Orders. '
                                          'Calendar No. 16.'},
                          {'datetime': '2017-03-15 00:00:00 UTC',
                           'description': 'Senate Committee on Commerce, '
                                          'Science, and Transportation '
                                          'discharged by petition pursuant to '
                                          '5 U.S.C. 802 (c).'},
                          {'datetime': '2017-03-15 00:00:00 UTC',
                           'description': 'Senate Committee on Commerce, '
                                          'Science, and Transportation '
                                          'discharged by petition pursuant to '
                                          '5 U.S.C. 802(c).'},
                          {'datetime': '2017-03-07 00:00:00 UTC',
                           'description': 'Read twice and referred to the '
                                          'Committee on Commerce, Science, and '
                                          'Transportation.'}],
              'active': 'true',
              'bill': 'S.J.RES.34',
              'bill_id': 'sjres34-115',
              'bill_type': 'sjres',
              'bill_uri': 'https://api.propublica.org/congress/v1/115/bills/sjres34.json',
              'committees': 'Senate Commerce, Science, and Transportation '
                            'Committee',
              'congress': '115',
              'congressdotgov_url': 'https://www.congress.gov/bill/115th-congress/senate-joint-resolution/34',
              'cosponsors': '24',
              'enacted': '2017-03-30',
              'govtrack_url': 'https://www.govtrack.us/congress/bills/115/sjres34',
              'gpo_pdf_uri': 'https://www.gpo.gov/fdsys/pkg/BILLS-115sjres34pcs/pdf/BILLS-115sjres34pcs.pdf',
              'house_passage': '2017-03-28',
              'house_passage_vote': '2017-03-28',
              'introduced_date': '2017-03-07',
              'last_vote_date': '2017-03-28',
              'latest_major_action': 'Presented to President.',
              'latest_major_action_date': '2017-03-30',
              'number': 'S.J.RES.34',
              'primary_subject': 'Science, Technology, Communications',
              'senate_passage': '2017-03-23',
              'senate_passage_vote': '2017-03-23',
              'sponsor': 'Jeff Flake',
              'sponsor_id': 'F000444',
              'sponsor_party': 'R',
              'sponsor_state': 'AZ',
              'sponsor_uri': 'https://api.propublica.org/congress/v1/members/F000444.json',
              'summary': '(This measure has not been amended since it was '
                         'introduced. The summary of that version is repeated '
                         'here.) This joint resolution nullifies the rule '
                         'submitted by the Federal Communications Commission '
                         'entitled "Protecting the Privacy of Customers of '
                         'Broadband and Other Telecommunications Services." '
                         'The rule published on December 2, 2016: (1) applies '
                         'the customer privacy requirements of the '
                         'Communications Act of 1934 to broadband Internet '
                         'access service and other telecommunications '
                         'services, (2) requires telecommunications carriers '
                         'to inform customers about rights to opt in or opt '
                         'out of the use or the sharing of their confidential '
                         'information, (3) adopts data security and\xa0breach '
                         'notification requirements, (4) prohibits broadband '
                         'service offerings that are contingent on '
                         'surrendering privacy rights, and (5)\xa0requires '
                         'disclosures and affirmative consent\xa0when a '
                         'broadband provider offers customers financial '
                         "incentives in exchange for\xa0the provider's right "
                         "to use a customer's\xa0confidential information.",
              'summary_short': '(This measure has not been amended since it '
                               'was introduced. The summary of that version is '
                               'repeated here.) This joint resolution '
                               'nullifies the rule submitted by the Federal '
                               'Communications Commission entitled '
                               '&quot;Protecting the Privacy of Customers of '
                               'Broadband and Other Telecommunications '
                               'Services.&quot; The rule published on December '
                               '2, 2016: (1) applies the customer privacy '
                               'requirements of the Communications Act of 1934 '
                               'to broadband Internet access service and other '
                               'telecommunications services, (2)...',
              'title': 'A joint resolution providing for congressional '
                       'disapproval under chapter 8 of title 5, United States '
                       'Code, of the rule submitted by the Federal '
                       "Communications Commission relating to 'Protecting the "
                       'Privacy of Customers of Broadband and Other '
                       "Telecommunications Services'.",
              'versions': [],
              'vetoed': '',
              'votes': [{'api_url': 'https://api.propublica.org/congress/v1/115/house/sessions/1/votes/202.json',
                         'chamber': 'House',
                         'date': '2017-03-28',
                         'question': 'On Passage',
                         'result': 'Passed',
                         'roll_call': '202',
                         'time': '17:56',
                         'total_no': '205',
                         'total_not_voting': '9',
                         'total_yes': '215'},
                        {'api_url': 'https://api.propublica.org/congress/v1/115/senate/sessions/1/votes/94.json',
                         'chamber': 'Senate',
                         'date': '2017-03-23',
                         'question': 'On the Joint Resolution',
                         'result': 'Joint Resolution Passed',
                         'roll_call': '94',
                         'time': '12:25',
                         'total_no': '48',
                         'total_not_voting': '2',
                         'total_yes': '50'}],
              'withdrawn_cosponsors': '0'}],
 'status': 'OK'}"""

b = json.dumps(string_1)
c = json.loads(b)
# break down by dictionary keys
