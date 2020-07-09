import color


def colored(true, predict):
    true = true.split('\n')
    predict = predict.split('\n')

    for t, p in zip(true, predict):
        if t == p == '':
            print()
            continue

        t_word, t_kp = t.split('\t')
        p_word, p_kp = p.split('\t')

        if t_word != p_word:
            raise Exception('word is different! %s, %s' % (t_word, p_word))

        color.coloring(t_word, t_kp, p_kp)


with open('data/true.tsv', 'r') as f:
    true = f.read()
with open('data/sci-prediction.tsv', 'r') as f:
    sci_prediction = f.read()
with open('data/bert-prediction.tsv', 'r') as f:
    bert_prediction = f.read()

print('scibert')
print('-'*80)
print(colored(true, sci_prediction))
print()

print('bert')
print('-'*80)
print(colored(true, bert_prediction))
