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
    length = 0
    r = []
    while l:
        words = []
        while sum([len(w) for w in words]) <= width:
            words.append(l.pop() + " ")
        while sum([len(w) for w in words]) < width:
            for i in range(len(words) - 1):
                if words[i].count(" ") <= words[i + 1].count(""):
                    words[i] += words[i] + " "
                    break
        r.append("".join(words))
    return "\n".join(r)


if __name__ == "__main__":
    soln = justify(
        "Lorem  ipsum  dolor  sit amet,consectetur  adipiscing  elit. Vestibulum    sagittis   dolor mauris,  at  elementum  ligula tempor  eget.  In quis rhoncus nunc,  at  aliquet orci. Fusce at   dolor   sit   amet  felis suscipit   tristique.   Nam  a imperdiet   tellus.  Nulla  eu vestibulum    urna.    Vivamus tincidunt  suscipit  enim, nec ultrices   nisi  volutpat  ac. Maecenas   sit   amet  lacinia arcu,  non dictum justo. Donec sed  quam  vel  risus faucibus euismod.  Suspendisse  rhoncus rhoncus  felis  at  fermentum. Donec lorem magna, ultricies a nunc    sit    amet,   blandit fringilla  nunc. In vestibulum velit    ac    felis   rhoncus pellentesque. Mauris at tellus enim.  Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi    sit   amet   hendrerit fringilla,   ante  odio  porta lacus,   ut   elementum  justonulla et dolor.", 30)
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
    print(answer == soln)

