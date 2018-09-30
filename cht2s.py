class TraditionalToSimplified:
    def __init__(self, traditional_file, simplified_file):
        def __read_chars(filename):
            f = open(filename, encoding='utf-8')
            line = next(f)
            f.close()
            return line

        chars_t = __read_chars(traditional_file)
        chars_s = __read_chars(simplified_file)

        self.t2s_dict = {cht: chs for cht, chs in zip(chars_t, chars_s)}

    def to_simplified(self, text):
        text_new = ''
        for ch in text:
            chs = self.t2s_dict.get(ch, ch)
            text_new += chs
        return text_new
