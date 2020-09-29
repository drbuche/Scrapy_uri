import re


def remove_quenbr(lista):  # adaptar para regex
    x = lista.replace('\n', '')
    y = x.replace('\t', '')
    return y


def remove_quenbr_rpvp(lista):  # adaptar para regex
    x = lista.replace('\n', '')
    y = x.replace('\t', '').replace('.', '').replace(',', '.')
    return y


def remove_quenbr_rp(lista):  # adaptar para regex
    x = lista.replace('\n', '')
    y = x.replace('\t', '').replace('.', '')
    return y


def apenas_data(data_suja):
    return re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{1,4}", data_suja)
