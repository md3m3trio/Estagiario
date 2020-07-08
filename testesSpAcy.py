##
import spacy
nlp = spacy.load('pt_core_news_sm')
##

f1 = nlp(u'estagiário, mapeia o limite!')
f2 = nlp(u'estagiário mapear o limite')
f3 = nlp(u'estagiário mapeamento do limite')
f4 = nlp(u'estagiário mapear limites')

## # No obj nlp a LC separa as palavras, virgulas, sinais etc...
[palavra for palavra in f1]
##  # Com .orth_ nlp a LC separa como uma lista de str
[palavra.orth_ for palavra in f1]
## # Com com este if traz as palavras como str
[palavra.orth_ for palavra in f1 if palavra.is_alpha]
## #compara similaridade das palavras, no exemplo mapeia -> mapear
f1[2].similarity(f3[1])
## #Traz a palavra(orth_) e a classe gramatical(pos_)
[(palavra.orth_, palavra.pos_) for palavra in f3 if palavra.is_alpha]
## #separa oq é verbo
[palavra.orth_ for palavra in f1 if palavra.pos_=='VERB']
## #Relação da dependencia sintatica das palavras
[palavra.dep_ for palavra in f1 if palavra.is_alpha]
## #Transforma em verbo
[palavra.lemma_ for palavra in f1 if palavra.is_alpha]
## #limpa a frase e deixa apenas o comando

f1_cmd = ' '.join([palavra.orth_ for palavra in f1 if palavra.is_alpha and (palavra.dep_ =='ROOT' or palavra.dep_ =='obj')])
f2_cmd = ' '.join([palavra.orth_ for palavra in f2 if palavra.is_alpha and (palavra.dep_ =='ROOT' or palavra.dep_ =='obj')])
f3_cmd = ' '.join([palavra.orth_ for palavra in f3 if palavra.is_alpha and (palavra.dep_ =='ROOT' or palavra.dep_ =='obj')])
f4_cmd = ' '.join([palavra.lemma_ for palavra in f4 if palavra.is_alpha and (palavra.dep_ =='ROOT' or palavra.dep_ =='obj')])

## #Tenta descobrir o nivel de similaridade
nlp(f1_cmd).similarity(nlp(f4_cmd))

nlp(nlp(nlp(f1_cmd)[0].lemma_)[0].lemma_)[0].lemma_