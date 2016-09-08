def justify(text, width):
    """
    justify the text with a given width.
    use spaces to separate words and each line ends with a word not a space
    last line no need to justify.
    more spaces are in front less spaces are in back.
    :param text: unjustified text
    :type text: str
    :param width: the width limit
    :type width: int
    :return: justified text
    :rtype: str
    """
    l = text.split()
    l.reverse()
    r = []
    while l:
        words = []
        while l and sum([len(w) for w in words]) + len(l[-1]) + 1 <= width:
            words.append(l.pop() + " ")
        words[-1] = words[-1].rstrip()
        if len(words) == 1:
            break
        # Todo: spacing between words
        print(words)
        while sum([len(w) for w in words]) < width:
            for i in range(len(words) - 1):
                if words[i].count(" ") < words[i + 1].count(""):
                    words[i] += " "
                    break
        r.append("".join(words))
    r[-1] = " ".join(r[-1].split())
    return "\n".join(r)

    # soln:
    # length = text.rfind(' ', 0, width+1)
    # if length == -1 or len(text) <= width: return text
    # line = text[:length]
    # spaces = line.count(' ')
    # if spaces != 0:
    #     expand = (width - length) / spaces + 1
    #     extra = (width - length) % spaces
    #     line = line.replace(' ', ' '*expand)
    #     line = line.replace(' '*expand, ' '*(expand+1), extra)
    # return line + '\n' + justify(text[length+1:], width)


if __name__ == "__main__":
    soln = justify(
        "Lorem  ipsum  dolor  sit amet, consectetur  adipiscing  elit. "
        "Vestibulum    sagittis   dolor mauris,  at  elementum  ligula tempor"
        "  eget.  In quis rhoncus nunc,  at  aliquet orci. Fusce at   dolor   "
        "sit   amet  felis suscipit   tristique.   Nam  a imperdiet   tellus. "
        " Nulla  eu vestibulum    urna.    Vivamus tincidunt  suscipit  enim, "
        "nec ultrices   nisi  volutpat  ac. Maecenas   sit   amet  lacinia"
        " arcu,  non dictum justo. Donec sed  quam  vel  risus faucibus"
        " euismod.  Suspendisse  rhoncus rhoncus  felis  at  fermentum."
        " Donec lorem magna, ultricies a nunc    sit    amet,   blandit"
        " fringilla  nunc. In vestibulum velit    ac    felis   rhoncus "
        "pellentesque. Mauris at tellus enim.  Aliquam eleifend tempus "
        "dapibus. Pellentesque commodo, nisi    sit   amet   hendrerit "
        "fringilla,   ante  odio  porta lacus,   ut   elementum  justonulla"
        " et dolor.", 30)
    # print(soln)

    answer = """Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor."""
