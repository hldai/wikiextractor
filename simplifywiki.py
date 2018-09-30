from cht2s import TraditionalToSimplified

cht_file = 'd:/data/res/ch-traditional.txt'
chs_file = 'd:/data/res/ch-simplified.txt'
tts = TraditionalToSimplified(cht_file, chs_file)

f = open('d:/data/res/wiki-text.txt', encoding='utf-8')
fout = open('d:/data/res/wiki-text-simplified.txt', 'w', encoding='utf-8')
for i, line in enumerate(f):
    line = tts.to_simplified(line)
    fout.write(line)
    if i % 100000 == 0:
        print(i)
f.close()
fout.close()
