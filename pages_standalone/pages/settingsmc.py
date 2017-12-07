import json

settings_mailchimp = json.dumps([
#    {'type': 'title',
#     'title': 'MailChimp'},
#    {'type': 'bool',
#     'title': 'A boolean setting',
#     'desc': 'Boolean description text',
#     'section': 'example',
#     'key': 'boolexample'},
#    {'type': 'numeric',
#     'title': 'A numeric setting',
#     'desc': 'Numeric description text',
#     'section': 'example',
#     'key': 'numericexample'},
#    {'type': 'options',
#     'title': 'An options setting',
#     'desc': 'Options description text',
#     'section': 'example',
#     'key': 'optionsexample',
#     'options': ['option1', 'option2', 'option3']},
    {'type': 'string',
     'title': 'User Name',
     'desc': 'The user name to connect to MailChimp with.',
     'section': 'API',
     'key': 'mc_user'},
    {'type': 'string',
     'title': 'API Key',
     'desc': 'The MailChimp apikey for the user.',
     'section': 'API',
     'key': 'mc_key'}
#    {'type': 'path',
#     'title': 'A path setting',
#     'desc': 'Path description text',
#     'section': 'example',
#     'key': 'pathexample'}
    ])

  
