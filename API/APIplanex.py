import json
from flask import Flask, jsonify
from itertools import combinations
from itertools import combinations
import numpy as np
from pandas import DataFrame
from IPython.display import display
from statistics import variance
from scipy.stats import t, f, norm
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/matrix/<fatores>/<replicadas>',methods=['GET'])
def matrix(fatores,replicadas):
    alfa = 0.05
    mult = 2
    fatores = int(fatores)
    replicadas = int(replicadas)
    mult = 2
    combvariaveis = list()
    for aux1 in range(2,fatores + 1):
        combinacoes = list()
        for aux2 in range(1, fatores + 1):
            combinacoes.append(aux2)
        combvariaveis.append(list(combinations(combinacoes, aux1)))
    
    ind_comb1 = 0
    ind_comb2 = 0
    cont_comb = 0
    
    lim_comb = combvariaveis[ind_comb2].__len__()
    linx = 2 ** fatores + replicadas
    colx = 2 ** fatores
    matx = np.ones((linx, colx), dtype=int)

    # Preenchimento da Matriz X (Replicatas, Coluna 2, Última Coluna e Variáveis)
    for coluna in range(1, colx):
        # Necessário para Colunas das variáveis
        imparpar = 0
        for linha in range(0, linx):

            # 'Replicatas do ponto central'
            if linha >= linx - replicadas:
                matx[linha, coluna] = 0

            # Coluna 2
            elif coluna == 1 and linha % 2 == 0:
                matx[linha, coluna] = -1

            # Colunas das variáveis
            elif coluna <= fatores and coluna != 1:
                if linha % mult == 0:
                    imparpar += 1
                    #print('Linha:', linha, '\n', 'Mult: ', mult, '\n', 'O valor do imparpar: ', imparpar, '\n')
                if imparpar % 2 == 1:
                    matx[linha, coluna] = -1

            # Última Coluna
            elif coluna == colx - 1:
                ultcol = 0
                for ind_ultcol in range(1, fatores + 1):
                    if matx[linha, ind_ultcol] == -1:
                        ultcol += 1
                if ultcol % 2 != 0:
                    matx[linha, coluna] = -1

            # Combinação das Variáveis
            elif coluna > fatores:
                if coluna - fatores <= lim_comb:
                    if cont_comb < 2 ** fatores:
                        cont_comb += 1
                        comb = combvariaveis[ind_comb2][ind_comb1]
                    else:
                        ind_comb1 += 1
                        cont_comb = 1
                        comb = combvariaveis[ind_comb2][ind_comb1]
                else:
                    ind_comb2 += 1
                    ind_comb1 = 0
                    cont_comb = 1
                    lim_comb += combvariaveis[ind_comb2].__len__()
                    comb = combvariaveis[ind_comb2][ind_comb1]
                valormult = 1
                for indcomb in range(0, comb.__len__()):
                    valormult *= matx[linha, comb[indcomb]]
                # print('A multiplicação da combinação:', comb, 'na linha', linha, 'é', valormult)
                matx[linha, coluna] = valormult

        # Necessário para a Coluna das Variáveis
        if coluna <= fatores and coluna != 1:
            mult *= 2

    print('=-=' * 30, '\n')
    # Informando o tamanho da Matriz X
    print('A matriz X possui', linx, 'linhas e ', colx, 'colunas.\n')
    return jsonify(matx.tolist())

@app.route('/matriTesteT/<fatores>/<replicadas>/<maty>',methods=['GET'])
def testT(fatores,replicadas, maty):
    alfa = 0.05
    mult = 2
    fatores = int(fatores)
    replicadas = int(replicadas)
    maty = np.array(json.loads(maty))
    #maty = json.loads(maty)

    fatores = int(fatores)
    replicadas = int(replicadas)
    mult = 2
    combvariaveis = list()
    for aux1 in range(2,fatores + 1):
        combinacoes = list()
        for aux2 in range(1, fatores + 1):
            combinacoes.append(aux2)
        combvariaveis.append(list(combinations(combinacoes, aux1)))
    
    ind_comb1 = 0
    ind_comb2 = 0
    cont_comb = 0
    
    lim_comb = combvariaveis[ind_comb2].__len__()
    linx = 2 ** fatores + replicadas
    colx = 2 ** fatores
    matx = np.ones((linx, colx), dtype=int)

    # Preenchimento da Matriz X (Replicatas, Coluna 2, Última Coluna e Variáveis)
    for coluna in range(1, colx):
        # Necessário para Colunas das variáveis
        imparpar = 0
        for linha in range(0, linx):

            # 'Replicatas do ponto central'
            if linha >= linx - replicadas:
                matx[linha, coluna] = 0

            # Coluna 2
            elif coluna == 1 and linha % 2 == 0:
                matx[linha, coluna] = -1

            # Colunas das variáveis
            elif coluna <= fatores and coluna != 1:
                if linha % mult == 0:
                    imparpar += 1
                    #print('Linha:', linha, '\n', 'Mult: ', mult, '\n', 'O valor do imparpar: ', imparpar, '\n')
                if imparpar % 2 == 1:
                    matx[linha, coluna] = -1

            # Última Coluna
            elif coluna == colx - 1:
                ultcol = 0
                for ind_ultcol in range(1, fatores + 1):
                    if matx[linha, ind_ultcol] == -1:
                        ultcol += 1
                if ultcol % 2 != 0:
                    matx[linha, coluna] = -1

            # Combinação das Variáveis
            elif coluna > fatores:
                if coluna - fatores <= lim_comb:
                    if cont_comb < 2 ** fatores:
                        cont_comb += 1
                        comb = combvariaveis[ind_comb2][ind_comb1]
                    else:
                        ind_comb1 += 1
                        cont_comb = 1
                        comb = combvariaveis[ind_comb2][ind_comb1]
                else:
                    ind_comb2 += 1
                    ind_comb1 = 0
                    cont_comb = 1
                    lim_comb += combvariaveis[ind_comb2].__len__()
                    comb = combvariaveis[ind_comb2][ind_comb1]
                valormult = 1
                for indcomb in range(0, comb.__len__()):
                    valormult *= matx[linha, comb[indcomb]]
                # print('A multiplicação da combinação:', comb, 'na linha', linha, 'é', valormult)
                matx[linha, coluna] = valormult

        # Necessário para a Coluna das Variáveis
        if coluna <= fatores and coluna != 1:
            mult *= 2

    # Continuidade do Programa

    # Matriz Transposta
    matxtranp = np.transpose(matx)
    tamanho = matxtranp.shape
    '''
    print("\nA Matriz X transposta possui", tamanho[0], "linhas e", tamanho[1],'colunas')
    for linha in range(0, tamanho[0]):
        for coluna in range(0, tamanho[1]):
            print(f'[{matxtranp[linha, coluna]:^3}]', end='')
        print()
    '''

    # Matriz X^t*X
    matx_t_x = np.matmul(matxtranp, matx)
    tamanho = matx_t_x.shape
    '''
    print("\nA Matriz X_t * X possui", tamanho[0], "linhas e", tamanho[1], 'colunas')
    for linha in range(0, tamanho[0]):
        for coluna in range(0, tamanho[1]):
            print(f'[{matx_t_x[linha, coluna]:^3}]', end='')
        print()
    '''

    # Matriz X^t*X a -1
    matx_t_xinv = matx_t_x.astype(float)
    tamanho = matx_t_xinv.shape
    for linha in range(0, tamanho[0]):
        for coluna in range(0, tamanho[1]):
            if linha == coluna:
                matx_t_xinv[linha][coluna] = 1 / (matx_t_x[linha][coluna])
    '''
    print("\nA Matriz X_t*X-¹ possui", tamanho[0], "linhas e", tamanho[1], 'colunas')
    for linha in range(0, tamanho[0]):
        for coluna in range(0, tamanho[1]):
            print(f'[{round(matx_t_xinv[linha, coluna], 5):^7}]', end='')
            #print(f'[{matx_t_xinv[linha, coluna]:^10}]', end='')
        print()
    '''
    
    # Cálculo da Matriz X^t * Y
    matx_t_y = np.matmul(matxtranp, maty)

    # Cálculo dos Betas
    matbetas = np.matmul(matx_t_xinv, matx_t_y)
    #print('\nMatriz BETA:\n', matbetas)

    # Matriz Beta^t
    matbetas_t = np.transpose(matbetas)

    # Valor de Beta^t * X^t * Y
    matbetas_t_x_t_y = np.matmul(matbetas_t, matx_t_y)
    #print('\n \n', matbetas_t_x_t_y)

    # Calculo da variância dos pontos centrais
    pntcentrais = []
    for i in range(colx, linx):
        pntcentrais.append(maty[i, 0])

    varian = np.sqrt(variance(pntcentrais) * matx_t_xinv)
    #print(varian)

    er = []
    for lin in range(tamanho[0]):
        for col in range(tamanho[1]):
            if lin == col:
                er.append(varian[lin][col])
    #print(er)

    # Montagem da Tabela de Significância dos Betas
    matb = matbetas.ravel()
    tam_matb = matb.size
    tcalc = (matb - 0) / er
    tintervalo = t.interval(1 - alfa, linx - tam_matb)
    tcrit = tintervalo[1]

    t_pvalor_bc = []
    for i in range(tam_matb):
        if matb[i] >= 0:
            t_pvalor_bc.append(2 * t.sf(tcalc[i], tam_matb - 1))
        else:
            t_pvalor_bc.append(2 * t.cdf(tcalc[i], tam_matb - 1))

    t_aceitacao = []
    for i in range(tam_matb):
        if t_pvalor_bc[i] < alfa:
            t_aceitacao.append("Aceita-se H0")
        else:
            t_aceitacao.append("Rejeita-se H0")

    tab_signbeta = DataFrame(
        {
            'B   ': matb,
            'er   ': er,
            'H0': 0,
            '     t[(B - H0)/er]': tcalc,
            't crítico': tcrit,
            '  Análise da Hipótese': t_aceitacao,
            'p-valor': t_pvalor_bc
        }
    )
    
    # print('\nTABELA DE SIGNIFICÂNCIA DOS BETAS\n', '=-=' * 30)
    # display('\n', tab_signbeta)


    #return jsonify(tab_signbeta)
    return tab_signbeta.to_json(orient="table")


app.run()