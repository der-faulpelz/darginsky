# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:45:33 2018

@author: oleg
"""

import re
import string


HEM = re.compile(r"(([iaeuptšsčcхkχ])ː)", re.I)  # Проверять через finditer
# ABR = re.compile(r'(([kpčtc])1)', re.I)
# PALKA = re.compile(r'(?<=[кпчцхгпт])[I1|l]', re.I)
# LAB = re.compile(r'(([кпчхгтпцъь:])в)', re.I)
# GLOT = re.compile(r'\bъ(?=[аоуеэи])',re.I)
# FAR_ABR = re.compile(r"(((?<=[^aouei]|\w)[iua])ˁ)|(([kpčtc])')", re.I)
FAR = re.compile(r'(((?<=[^aouei]|\w)[iua])ˤ)', re.I)
ABR = re.compile(r"(([qkpčtc])[’'])", re.I)

J_VJ = re.compile(r'j[ua]', re.I)  # контексты, где ja -> я
E = re.compile(r'\be|e(?=[aouei])', re.I)  # контексты, где e -> э

# glot = 'ʔ'


drg_cyr = {'a': 'а',
           'aˤ': 'я',
           'b': 'б',
           'c': 'ц',
           'd': 'д',
           'e': 'е',  # В начале слова и перед гласной это будет э
           'f': 'ф',
           'g': 'г',
           'i': 'и',
           'j': 'й',  # Йоты сделать
           'k': 'к',
           'l': 'л',
           'm': 'м',
           'n': 'н',
           'o': 'о',
           'p': 'п',
           'r': 'р',
           's': 'с',
           't': 'т',
           'u': 'у',
           'w': 'в',
           'ʷ': 'в',
           'z': 'з',
           'č': 'ч',
           'š': 'ш',
           'ž': 'ж',
           'ʁ': 'гъ',
           'ʕ': 'гг',
           'ʡ': 'г1',
           'χ': 'х',
           'q': 'хъ',
           'q:': 'къ',
           'q’': 'кь',
           "q'": 'кь',
           'x': 'хь',
           'ʁ': 'гъ',
           'ʕ': 'гг',
           'ʡ': 'г1',
           'uˤ': 'ю',
           'ħ': 'х1',
           'h': 'гь',
           'aˤ': 'я'}


def transcr(drg_text):
    J = {'ja': 'я',
         'ju': 'ю'}

    digr = ('ь', 'ъ')

    drg_text = J_VJ.sub(lambda match: J[match.group()], drg_text)
    drg_text = E.sub(r'э', drg_text)
    drg_text = FAR.sub(lambda match: drg_cyr.get(match.groups()[0],
                                                 match.group(2) + '1'), drg_text)
    drg_text = ABR.sub(lambda match: drg_cyr.get(match.groups()[0],
                                                 match.group(2) + '1'), drg_text)
    drg_text = HEM.sub(lambda match: drg_cyr[match.group(2)] * 2, drg_text)
    # print(drg_text)
    cyr = ''
    i = 0
    while i < len(drg_text) - 1:
        # extra_artic = False
        s = drg_text[i]
        if (not s.isalpha()) or (s in drg_cyr.values()) or (s in J.values()) or s in digr:
            cyr += drg_text[i]
        else:
            letter = drg_text[i]
            next_letter = drg_text[i + 1]
            if next_letter not in {"'", '’', 'ː', 'ˤ'}:
                next_letter = ''
            else:
                # extra_artic = True
                i += 1
            cyr += drg_cyr[letter + next_letter]
        i += 1
    cyr += drg_cyr.get(drg_text[-1], drg_text[-1]) if drg_text[-1].isalnum() else ''
    # isalnum для случаев типа к1#'
    return cyr


##########################################################################
HEM1 = re.compile(r'(([иаеупткшсчцх]|хь)\2)', re.I)  # Проверять через finditer
ABR1 = re.compile(r'(([кпчтпц])1)', re.I)
PALKA1 = re.compile(r'(?<=[кпчцхгпт])[I1|l]', re.I)
LAB1 = re.compile(r'(([кпчхгтпцъь:])в)', re.I)
# GLOT = re.compile(r'\bъ(?=[аоуеэи])',re.I)
FAR1 = re.compile(r'(?<=[ауэеи])1', re.I)  # Фарингализация незадних - бывает не во всех диалектах

J_VJ1 = re.compile(r'(?<=[аоуеиэюя])[яю]|\b([яю])', re.I)  # контексты, где я -> ja

# glot = 'ʔ'

regular = {HEM1: 'ː',
           ABR1: "’",
           FAR1: 'ˤ',
           LAB1: 'ʷ'}

cyr_drg = {'а': 'a',
           'б': 'b',
           'в': 'w',
           'г': 'g',
           'гъ': 'ʁ',
           'гь': 'h',
           'г1': 'ʡ',
           'гг': 'ʕ',
           'д': 'd',
           'е': 'e',
           'ж': 'ž',
           'з': 'z',
           'и': 'i',
           'й': 'j',
           'к': 'k',
           'къ': 'qː',
           'кь': 'q’',
           'л': 'l',
           'м': 'm',
           'н': 'n',
           'о': 'o',
           'п': 'p',
           'р': 'r',
           'с': 's',
           'т': 't',
           'у': 'u',
           'ф': 'f',
           'х': 'χ',
           'х1': 'ħ',
           'хъ': 'q',
           'хь': 'x',
           'ц': 'c',
           'ч': 'č',
           'ш': 'š',  # фаринг гласных - глсн + 1
           'э': 'e',
           'ю': 'uˤ',  # Встречаются ли ю, ё, есть ли контексты с йотом??? ю редко будет в фарингализации
           'я': 'aˤ'}  # я - фарингализация. Какие гласные фаринг?

J1 = {'я': 'ja',
     'ю': 'ju'}


def transcr_drg(cyr_text):
    cyr_text = PALKA1.sub('1', cyr_text)
    cyr_text = J_VJ1.sub(lambda match: J1[match.group()], cyr_text)
    cyr_text = cyr_text.replace('гг', 'ʕ')  # Не получается хранить в словаре

    for pat in regular.keys():  # Замена в регулярных для фон знаков конетекстах
        fon_znak = regular[pat]
        one = lambda match: match.group(2) + fon_znak
        cyr_text = pat.sub(one, cyr_text)

    drg = ''
    i = 0
    # is_digr = False
    while i < len(cyr_text) - 1:
        # is_digr = False
        s = cyr_text[i]
        if (not s.isalpha()) or (s in cyr_drg.values()) or (s in regular.values()):
            drg += cyr_text[i]
        else:
            letter = cyr_text[i].lower()
            next_letter = cyr_text[i + 1]
            if next_letter not in {'1', 'ъ', 'ь'}:
                next_letter = ''
            else:
                # is_digr = True
                i += 1
            drg += cyr_drg[letter + next_letter]

        i += 1
    drg += cyr_drg.get(cyr_text[-1], cyr_text[-1])
    return drg



cyrillic = re.compile("[а-яА-Я]+")

# print (transcr("ʡaˤpːasi"))

