import random
RM_PUNCT = u"'\"”„+-—:;()"
class markov:
    def __init__(self, file_name=None):
        if file_name:
            with open(file_name, 'r') as f:
                pass
        else:
            self.mc = {}

    def triples(self, words):
        if len(words) < 3:
            return
        for i in range(len(words)-2):
            yield (words[i], words[i+1], words[i+2])

    def train(self, words):
        for w1, w2, w3 in self.triples(words):
            key = w1 + '+' + w2
            if key not in self.mc:
                self.mc[key] = []
            self.mc[key].append(w3)

    def train_from_text(self, text, remove=RM_PUNCT):
        text = text.replace('.', ' . ').replace(',', ' , ')
        word_seq = text.strip().split()
        print(word_seq)
        word_seq = [word.strip(remove) for word in word_seq 
                    if len(word.strip(remove)) != 0]
        self.train(word_seq)

    def choose_start_words(self, first_word=None, second_word=None):
        if second_word != None:
            return first_word, second_word
        elif first_word != None:
            if len(self.mc['.' + '+' + first_word]) != 0:
                second_word = random.choice(self.mc['.' + '+' + first_word])
            elif len(self.mc['.' + '+' + first_word.capitalize()]) != 0: 
                second_word = random.choice(self.mc['.' + '+' + first_word.capitalize()])
            else:
                return self.choose_start_words(None, None)
            return first_word, second_word
        else:
            first_word = random.choice(self.mc[random.choice(list(self.mc.keys()))])
            return self.choose_start_words(first_word, second_word)
        
    def generate_text(self, first_word=None, second_word=None, size=10):
        w1, w2 = self.choose_start_words(first_word, second_word)
        gen_words = [w1.capitalize()]
        while not (len(gen_words) > size and w2 == '.'):
            gen_words.append(w2.capitalize() if (w1 == '.') else w2)
            w1, w2 = w2, random.choice(self.mc[w1 + '+' + w2])
        gen_words.append(w2)
        text = ' '.join(gen_words)
        text = text.replace(' ,', ',').replace(' .', '.')
        return text
