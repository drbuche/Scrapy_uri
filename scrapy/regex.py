# import re

def remove_quenbr(lista):
    x = lista.replace('\n', '')
    y = x.replace('\t', '')
    return y


def remove_quenbr_rpvp(lista):
    x = lista.replace('\n', '')
    y = x.replace('\t', '').replace('.', '').replace(',', '.')
    return y


def remove_quenbr_rp(lista):
    x = lista.replace('\n', '')
    y = x.replace('\t', '').replace('.', '')
    return y
