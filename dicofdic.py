user={
    'csk':{
        'first':'sai',
        'last':'kumar',
        'place':'tirupati'
        },
    'josh':{
        'first':'joshi',
        'last':'tha',
        'place':'atp'
        }    
}
for k,v in user.items():
    print('\n''username:{}'.format(k))
    full=('{} {}'.format(v['first'],v['last']))
    location=v['place']
    print('\t''full_name:{}'.format(full.title()))
    print('\t''from:{}'.format(location.upper()))


