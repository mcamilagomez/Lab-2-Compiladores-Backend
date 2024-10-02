import json

def transitions_to_json(sussefull, transitions):

    result = {
        'sussefull': sussefull,
        'transitions': [
            {
                'node1': t[0],  
                'node2': t[1],  
                'chart': t[2]   
            } for t in transitions
        ]
    }
    
    return json.dumps(result, indent=4)