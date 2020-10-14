import re


def apenas_data(data_suja):
    return re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{1,4}", data_suja)


def apenas_pontos_float(pontos):
    return ''.join(re.findall(r"[\d\\.]+", pontos))


def apenas_pontos(pontos):
    return ''.join(re.findall(r"[\d]+", pontos))


def apenas_sigla_pais(pais):
    return (re.findall(r"-([a-zA-z]+)", pais))[0].upper()
