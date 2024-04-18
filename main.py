def gerar_cabecalho(linha, inicio, competencia, num_linhas, num_folhas, campo_Controle, orgao_informacao, orgao_digitacao, CPF_prestador, orgao_destino, M_E, versao, fim):
    #01#BPA#2024020034670000371475                                    00000000000000                                         D03.01
    # campo_Controle = ((int(procedimento) + int(qtde)) % 1111) + 1111
    with open('bpa_i.txt', 'w') as arquivo:
        arquivo.write(f'{linha}') #indicador de linha do Header
        arquivo.write(f'{inicio}') #indicador de início do cabeçalho
        arquivo.write(f'{competencia}') #ano e mês de Processamento da produção. formato AAAAMM
        arquivo.write(f'{num_linhas}') #número de linhas do BPA gravadas.
        arquivo.write(f'{num_folhas}') #quantidades de folhas de BPA gravadas.
        arquivo.write(f'{campo_Controle}') #Campo de controle.DOMÍNIO [1111..2221]
        arquivo.write(f'{orgao_informacao}') #Nome do órgão de origem responsável pela informação.
        arquivo.write(f'{orgao_digitacao}') #Sigla do órgão de origem responsável pela digitação.
        arquivo.write(f'{CPF_prestador}') #CGC/CPF do prestador ou do órgão público responsável pela informação, conforme cadastro na Receita Federal.
        arquivo.write(f'{orgao_destino}') #Nome do órgão de saúde destino do arquivo.
        arquivo.write(f'{M_E}') #Indicador do órgão destino: M/E
        arquivo.write(f'{versao}') #Versão do sistema, informação livre, pode conter qualquer letra e numero.
        arquivo.write(f'{fim}') #Correspondente aos caracteres CR - CHR(13) + LF - CHR(10), do padrão ASCII (.TXT), indicando fim do cabeçalho.



def gerar_bpa_i(linha, cnes, competencia, cns_medico, cbo, data_atendimento, folha, sequencia, procedimento, cns_paciente, sexo, ibge, cid, idade, qtde, cAten, nAutorizacao, origem, nome_paciente, data_nascimento, raca, etnia, nacionalidade, servico, classificacao, seq_equipe, seq_area, cnpj, cep, logradouro, endereco, complemento, numero, bairro, telefone, email, ine):
    with open('bpa_i.txt', 'a') as arquivo:
        #03/9999999/202403/151515151515151/666666/20240307/001/01/9999999999/151515151515151/M/270430/CIDS/066/000002/01/             /BPA/NOME COMPLETO DO PACIENTE     /19570425/01/    /010/333/003/        /    /              /57080000/020/ENDERECO PACIENTE                          /          /999  /BAIRRO                                       /           /                                        /          
        arquivo.write(f'{linha}') #03
        arquivo.write(f'{cnes}') #9999999
        arquivo.write(f'{competencia}') #202404
        arquivo.write(f'{cns_medico}') #151515151515151
        arquivo.write(f'{cbo}') #666666
        arquivo.write(f'{data_atendimento}') #20240407
        arquivo.write(f'{folha}') #001
        arquivo.write(f'{sequencia}') #01
        arquivo.write(f'{procedimento}') #9999999999
        arquivo.write(f'{cns_paciente}') #151515151515151
        arquivo.write(f'{sexo}') #M
        arquivo.write(f'{ibge}') #270430
        arquivo.write(f'{cid}') #CIDS
        arquivo.write(f'{idade}') #066
        arquivo.write(f'{qtde}') #000002
        arquivo.write(f'{cAten}') #01
        arquivo.write(f'{nAutorizacao}') #             /                       SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{origem}') #BPA
        arquivo.write(f'{nome_paciente}') #NOME COMPLETO DO PACIENTE     /     MINIMO DE 30 CARACTERES
        arquivo.write(f'{data_nascimento}') #20000101
        arquivo.write(f'{raca}') #01/                                          01 Branca 02 Preta 03 Parda 04 Amarela 05 Indígena 99 Sem informação
        arquivo.write(f'{etnia}') #    /                                       SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{nacionalidade}') #010
        arquivo.write(f'{servico}') #333
        arquivo.write(f'{classificacao}') #003
        arquivo.write(f'{seq_equipe}') #        /                              SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{seq_area}') #    /                                    SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{cnpj}') #              /                              SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{cep}') #57080000
        arquivo.write(f'{logradouro}') #020
        arquivo.write(f'{endereco}') #ENDERECO PACIENTE                          /          MINIMO DE 30 CARACTERES
        arquivo.write(f'{complemento}') #          /                           SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{numero}') #999  /                                     MINIMO DE 5 CARACTERES
        arquivo.write(f'{bairro}') #BAIRRO                                       /            SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{telefone}') #           /                           SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{email}') #                                        / SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO
        arquivo.write(f'{ine}\n') #          /                                 SE VAZIO, PREENCHER COM ESPAÇOS EM BRANCO

gerar_cabecalho('01', '#BPA#', '202404', '00', '34', '670000371475', '                              ', '      ', '00000000000000', '                                        ', ' ', 'D03.', '01\n')
gerar_bpa_i('03', '9999999', '202404', '151515151515151', '666666', '20240407', '001', '01', '9999999999', '151515151515151', 'M', '270430', 'CIDS', '066', '000002', '01','             ', 'BPA', 'NOME COMPLETO DO PACIENTE     ', '20000101', '01', '    ', '010', '333', '002', '        ', '    ', '              ', '57080000', '020', 'ENDERECO PACIENTE             ', '          ', '999  ', 'BAIRRO                        ', '           ', '                                        ', '          ')
gerar_bpa_i('03', '9999999', '202404', '151515151515151', '666666', '20240408', '001', '02', '9999999999', '151515151515151', 'M', '270430', 'CIDS', '066', '000001', '01','             ', 'BPA', 'NOME COMPLETO DO PACIENTE     ', '20000101', '01', '    ', '010', '333', '002', '        ', '    ', '              ', '57080000', '020', 'ENDERECO PACIENTE             ', '          ', '999  ', 'BAIRRO                        ', '           ', '                                        ', '          ')