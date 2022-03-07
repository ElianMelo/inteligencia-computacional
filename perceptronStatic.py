b = 1
taxa = 1 #int(input("taxa: "))
limiar = 0.2 #int(input("limiar: "))
geracoes = 10
# entradas = int(input("entradas: "))
# linhas = int(input("linhas: "))

def calculoPesos():

    pesoParado = 0

    geracao = 1

    x = [[]]
    w = [
        [0, 0, 0]
    ]

    # AND 2 entradas e alvos bipolares

    scene = [
        [1, 1, 1],
        [1, -1, 1],
        [-1, 1, 1],
        [-1, -1, 1],
    ]

    target = [1, -1, -1, -1]    

    # AND 2 entradas binárias e alvos bipolares

    # scene = [
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [0, 1, 1],
    #     [0, 0, 1],
    # ]

    # target = [1, -1, -1, -1]

    # XOR 2 entradas binárias e alvos bipolares

    # scene = [
    #     [1, 1, 0],
    #     [1, 0, 1],
    #     [0, 1, 1],
    #     [0, 0, 0],
    # ]

    # target = [1, -1, -1, -1]

    # OR 2 entradas e alvo binários

    # scene = [
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [0, 1, 1],
    #     [0, 0, 1],
    # ]

    # target = [1, 1, 1, 0]

    for g in range(0, geracoes):
        if g == 0:
            w = [
                [0, 0, 0]
            ]
        else:
            oldW = w[len(w)-1]
            globalOldW = oldW
            newW = []
            newW.append(oldW)
            w = newW
        
        for i in range(0, len(scene)):
            yent = 0
            for j in range(0, len(scene[i])):
                yent += (scene[i][j] * w[i][j])

            if yent > limiar:
                fYent = 1
            elif yent < (limiar * -1):
                fYent = -1
            else:
                fYent = 0
                            
            # print("yent: " + str(yent))
            # print("fYent: " + str(fYent))
            # print("target: " + str(target[i]))
            # print()
            
            w.append([])

            pesoParadoNow = 0
            # print("------------------------")
            for k in range(0, len(scene[i])):
                if fYent != target[i]:
                    pesoParadoNow = 0
                    deltaW = taxa * (target[i] - fYent) * scene[i][k]
                    # print("DeltaW" + str(k) + ": " + str(deltaW))
                    pesoAnt = w[i][k]
                    w[i+1].append(deltaW + pesoAnt)
                else:
                    pesoParadoNow += 1
                    w[i+1].append(w[i][k])
            # print(w[i+1])
            # print("------------------------")
            if pesoParadoNow >= len(scene[i]):
                pesoParado += 1
            else:
                pesoParado = 0
            # teste de peso                
            result = 0
            if pesoParado >= len(scene):
                # print("Nova verificação")
                for o in range(0, len(scene)):
                    # print("------------ Verificação Peso -------------")
                    yentPeso = 0
                    for p in range(0, len(scene[o])):
                        # print("valor" + str(p) + ": " + str(scene[o][p]))
                        # print("peso" + str(p) + ": " + str(w[i+1][p]))
                        yentPeso += scene[o][p] * w[i+1][p]
                    
                    if yentPeso > limiar:
                        fYentPeso = 1
                    elif yentPeso < (limiar * -1):
                        fYentPeso = -1
                    else:
                        fYentPeso = 0
                    
                    # print("Yent: " + str(yentPeso))
                    # print("fYent: " + str(fYentPeso))
                    # print("target: " + str(target[o]))
                    
                    if fYentPeso == target[o]:
                        result += 1
                if result == len(scene):
                    print("Resultado encontrado !")
                    print(w[i+1])
                    print("Geracao: " + str(geracao))
                    return
                else:
                    print("Resultado não encontrado !")
                    print(w[i+1])
                    print("Geracao: " + str(geracao))
                    return
            
            
        print("---------------------------------------")
        print("Geração: " + str(geracao))
        print("Ultimos pesos: " + str(w[len(w)-1]))
        print("---------------------------------------")
        geracao += 1
            
calculoPesos()
