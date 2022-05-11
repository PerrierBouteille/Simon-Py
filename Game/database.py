import yaml


def Database(name,score):
    print("[Logs] (DataBase) > Pseudo: ", name)
    print("[Logs] (DataBase) > Score: ",score)
    #DB = [{ name : score }]
    #with open('database.yaml', 'w') as f:
    #    print()
    #    data = yaml.dump(DB, f)
    #return print(DB)

    data = "Game/database.yaml"

    with open('Game/none.yaml') as f:
        old = yaml.dump(yaml.load(f, Loader=yaml.SafeLoader), default_flow_style=False)

    with open(data) as f:
        new = yaml.load(f, Loader=yaml.SafeLoader)

    print(new)
    new[name] = {"score" : str(score)}

    with open(data, "w") as f:
        yaml.dump(new, f)

def load():
    with open('Game/database.yaml') as f:
        
        docs = yaml.load_all(f, Loader=yaml.SafeLoader)

        for doc in docs:
            
            for k, v in doc.items():
                print(k, "->", v)
                Player = []
                ScorePlayer = []

                Player.append(k)
                ScorePlayer.append(v)

                Player.sort()
                ScorePlayer.sort()
