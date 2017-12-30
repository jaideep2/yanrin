'''
TODO:
-1. Apply tfidf beforehand?
0. fix model by removing common words and united states instead of united_states
1. save/load models from file. Can do 1k at a time. So to get 150k do it 150 times.
model.save(fname)
model = lm.load(fname)
2. Save to models db
3. Work on summarization!
4. use faster phraser class
5. Named entitiy recorgnition into:
World,US/Domestic,Politics,State,Business,Opinion,Tech/Science,Health,Sports,Arts/Style,Food/Travel,Real Estate

500
LSI: 0.294878790851
LDA: 0.292729157768
HDP: 0.267182858046
lda+lsi model
round,top_topics[0][1]: 1 0.375660617905
round,top_topics[0][1]: 2 0.369877080454

1k
LSI: 0.294880618713
LDA: 0.289098235675
HDP: 0.246033253161
lda+lsi model
round  1 : 0.328287996563
round  2 : 0.327601096944
LDA+LSI: 0.317157425822

5k
LSI: 0.322105074121
LDA: 0.289542197103
HDP: 0.237900436668
slowwwwwwww

10k
LSI: 0.340836582348
LDA: 0.321519038949
HDP: 0.200997114764
lda+lsi model
round  1 : 0.374080759731
round  2 : 0.339413562568
round  3 : 0.361010216812
final: 0.374080759731
LDA+LSI: 0.364769981546
real	11m35.892s
user	21m51.778s
sys	0m26.949s

50k

100k

500k

'''

list_of_countries_and_capitals = [
    'United States',
    'Afghanistan',
    'Albania',
    'Algeria',
    'American Samoa',
    'Andorra',
    'Angola',
    'Anguilla',
    'Antarctica',
    'Antigua And Barbuda',
    'Argentina',
    'Armenia',
    'Aruba',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda',
    'Bhutan',
    'Bolivia',
    'Bosnia And Herzegowina',
    'Botswana',
    'Bouvet Island',
    'Brazil',
    'Brunei Darussalam',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Cayman Islands',
    'Central African Rep',
    'Chad',
    'Chile',
    'China',
    'Christmas Island',
    'Cocos Islands',
    'Colombia',
    'Comoros',
    'Congo',
    'Cook Islands',
    'Costa Rica',
    'Cote D`ivoire',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Falkland Islands (Malvinas',
    'Faroe Islands',
    'Fiji',
    'Finland',
    'France',
    'French Guiana',
    'French Polynesia',
    'French S. Territories',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Gibraltar',
    'Greece',
    'Greenland',
    'Grenada',
    'Guadeloupe',
    'Guam',
    'Guatemala',
    'Guinea',
    'Guinea-bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hong Kong',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea (North',
    'Korea (South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macau',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Martinique',
    'Mauritania',
    'Mauritius',
    'Mayotte',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montserrat',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'Netherlands Antilles',
    'New Caledonia',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'Norfolk Island',
    'Northern Mariana Islands',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Pitcairn',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'Reunion',
    'Romania',
    'Russian Federation',
    'Rwanda',
    'Saint Kitts And Nevis',
    'Saint Lucia',
    'St Vincent/Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome',
    'Saudi Arabia',
    'Senegal',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'St. Helena',
    'St.Pierre',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syrian Arab Republic',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tokelau',
    'Tonga',
    'Trinidad And Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City State',
    'Venezuela',
    'Viet Nam',
    'Virgin Islands (British',
    'Virgin Islands (U.S.',
    'Western Sahara',
    'Yemen',
    'Yugoslavia',
    'Zaire',
    'Zambia',
    'Zimbabwe'
]
list_of_us_states = []
list_of_us_cities = []
list_of_sports = []

topic_labels = ['World','Local','National','International',
                'US',
                'Domestic','Metropolitan',
                'Politics','Police','Crime',
                'State',
                'Local',
                'Business','Finance','Economy',
                'Opinion',
                'Tech','Science','Technology','Computers','Computers','Automobiles',
                'Health','Medicine',
                'Sports',
                'Weather',
                'Classified','Employment',
                'Interviews',
                'Letters',
                'Opinion','Editorial',
                'Religion','Culture','Literature','Society',
                'Arts','Style','Entertainment','Comics','Crossword','Puzzle','Horoscopes','Television','Books',
                'Food','Travel','Events','Movies','Tourism','People','Fashion','Cooking','Cuisine','Nutrition',
                'Home','Decoration','Family','Kids','Youth','Music','Decoration',
                'Real Estate','Sale']

topic_labels += list_of_countries_and_capitals