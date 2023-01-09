dummy_data = {
    'id': 1,
    'title':'Title words here',
    'content':{'text':'eilurfbghiquertbngiuebntg'},
    'files':['filerefs'],
    'category':'user defined category tag',
    'type':'application defined type - i.e. idea, project, to-do etc',
    'external_links':['urls'],
    'links':['links to other objects'],#this would be generated from a query to the links table
    'deadline':'datetime',
    'reminders':[{'date':'datetime','text':'reminder-text'}],
    'dependencies':['list of objects required before this can be complete'],#this will be generated from query to dependencies table
    'dependents':['list of objects requiring this one to be complete'],#same as above just other way round
    'active':bool,
    'archived':bool,
    'priority':int,#tbc
    'frontend_id':'unique id of frontend app which created the object'

}

def main():
    pass

if __name__ == '__main__':
    main()