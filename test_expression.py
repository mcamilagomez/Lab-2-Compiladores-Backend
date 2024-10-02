import pandas as pd
def test(df, regex):
    #Case the regex is &, check if regex support &
    if regex == '':
        row= df[df['states']== 'A']
        if row['values'].values[0] == '->*':
            return True, [('A','','&')]
        else: return False, [('A','','&')]
    else:
        i=0
        transitions=[]
        #Initial state
        find = 'A'
        while i<len(regex):
            chart = regex[i]
            #If chart it's in alphabet
            if chart in df.columns:
                #Find the state
                row= df[df['states']== find]
                if not row.empty:
                    #Find the transition
                    result= row[chart].values[0]
                    if result != '':
                        #When has a transition
                        transitions.append((find, result, chart))
                        find=result
                    else:
                        #When the transition is ''
                        transitions.append((find, '', chart))
                        return False, transitions
            else:
                #When the chart is not in the alphabert
                transitions.append((find, '', chart))
                return False, transitions
            if (i == len(regex)-1):
                #If it is in the last chart check if the state is a final state
                state = df[df['states']== result]
                if state['values'].values[0] == '*' or state['values'].values[0] == '->*':
                    return True, transitions
            i+=1
    return False, transitions
        
