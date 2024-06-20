# Словарь для перевода латиницы в кириллицу
latin_to_cyrillic = {
    'A': 'Ф',
    'B': 'И',
    'C': 'С',
    'D': 'В',
    'E': 'У',
    'F': 'А',
    'J': 'О',
    'H': 'Р',
    'I': 'Ш',
    'G': 'П',
    'K': 'Л',
    'L': 'Д',
    'M': 'Ь',
    'N': 'Т',
    'O': 'Щ',
    'P': 'З',
    'Q': 'Й',
    'R': 'К',
    'S': 'Ы',
    'T': 'Е',
    'U': 'Г',
    'V': 'М',
    'W': 'Ц',
    'X': 'Ч',
    'Y': 'Н',
    'Z': 'Я',
    'a': 'ф', 'b': 'и', 'c': 'с', 'd': 'в', 'e': 'у', 'f': 'а', 'g': 'п',
    'h': 'р', 'i': 'ш', 'j': 'о', 'k': 'л', 'l': 'д', 'm': 'ь', 'n': 'т',
    'o': 'щ', 'p': 'з', 'q': 'й', 'r': 'к', 's': 'ы', 't': 'е', 'u': 'г',
    'v': 'м', 'w': 'ц', 'x': 'ч', 'y': 'н', 'z': 'я', '[': 'х', ']': 'ъ',
    ';': 'ж', '\'': 'э', ',': 'б', '.': 'ю', '/': '.'
}


class Decoder:
    @staticmethod
    def decryption(encrypted_dict: list):
        """ Функция декодирования """
        decrypt_dict = []

        for doc in encrypted_dict:

            text = Decoder.latin_to_cyrillic_conversion(doc['question'])
            print(text)
            answers = [Decoder.latin_to_cyrillic_conversion(answer) for answer in doc['answers']]

            decrypt_dict.append({
                'order': doc['order'],
                'question': text,
                'answers': answers,
                'correct_answer': doc['correct_answer']
            })
        return decrypt_dict

    @staticmethod
    def latin_to_cyrillic_conversion(text):
        """ Функция для перевода латиницы в кириллицу """
        cyrillic_text = ""
        i = 0
        while i < len(text):
            if i + 2 < len(text) and text[i:i+3] in latin_to_cyrillic:
                cyrillic_text += latin_to_cyrillic[text[i:i+3]]
                i += 3
            elif i + 1 < len(text) and text[i:i+2] in latin_to_cyrillic:
                cyrillic_text += latin_to_cyrillic[text[i:i+2]]
                i += 2
            else:
                cyrillic_text += latin_to_cyrillic.get(text[i], text[i])
                i += 1
        return Decoder.caesar_decrypt(cyrillic_text, 7)

    # Функция для декодирования методом Цезаря
    @staticmethod
    def caesar_decrypt(ciphertext, shift):
        decrypted_text = ""
        for char in ciphertext:
            if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
                decrypted_char = chr((ord(char) - shift - ord('а')) % 32 + ord('а')) if char.islower() else chr((ord(char) - shift - ord('А')) % 32 + ord('А'))
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

# # Пример использования
# latin_text = "Wvxqp; k[nr[ix[.ap; xpb[op Kpegxp — lo[:"  # Ваш зашифрованный текст
# shift = 7  # Предположим, что сдвиг Цезаря равен 7
#
# # Шаг 1: Перевод текста с латиницы на кириллицу
# cyrillic_text = latin_to_cyrillic_conversion(latin_text.lower())
#
# # Шаг 2: Декодирование текста методом Цезаря
# decrypted_text = caesar_decrypt(cyrillic_text, shift)
#
# print("Расшифрованный текст:", decrypted_text)

encrypted_dict = [
    {
        "order": 1,
        "text": "Kn; ap.pnp wx[qvxge oq[t gao]g'gt. Q[wx[i: Kpegx] ivh.pi…",
        "answers": {
            "1": "24 r[kgcp",
            "2": "r[kgc[",
            "3": "28 r[kgc[q",
            "4": "32 r[kgcp"
        }
    },
    {
        "order": 5,
        "text": "Wvxqp; k[nr[ix[.ap; xpb[op Kpegxp — lo[:",
        "answers": {
            "1": "qvxiopnufgc HTML / CSS / JS. {kage [ivaage kave [ka[rx]wwagc Kpegxp wxvkn[ygn ve] w[e[.u i xpb[o[h \\u2014 w[qvxiopou iphod. Ap o[o e[evao Kpegx avea[r[ japn HTML g CSS, g vr[ wxga;ng q c[epak] gj 3 .vn[qvc, rkv [a g jpxpb[opn iq[g wvxqdv cx[qadv kvavycg",
            "2": "oxvavx w[ b[ci]. Q e[n[k[iog Kpegx ivxuvja[ jpagepni; iw[xo[e, p gevaa[ \\u2014 b[ci[e, g q iq[b[ka[v qxve; oxvagx[qpn e[n[kvyu ap w[niopqcg q [ka[e gj b[civxicgm cn]b[q Cgvqp",
            "3": "c[wgxphovx. Kpegx xpb[opn ap gaovxavo-gjkpagg: wgipn iopoug [ cxgwo[qpntopm, oxvhkgarv g gaqviog'g;m g avwn[m[ jpxpbpodqpn, cpc kn; io]kvaop 2-3 c]xip",
            "4": ""
        }
    },
    {
        "order": 6,
        "text": "Kpegx] c]wgng c[ewutovx, c[rkp ve] bdn[:",
        "answers": {
            "1": "6 nvo. Igioveadh bn[c apw[egapn [rx[ea]t bvn]t egcx[q[na[qc], p lcxpa \\u2014 b[nuz]t c[x[bc] i qdw]cnde e[ago[x[e",
            "2": "q 12 nvo. Lo[ bdn .vxadh igioveadh bn[c i .vxade wn[icge LED-lcxpa[e q 21 kthe. Gevaa[ ap ave Kpegx w[n].gn wvxqdh [wdo wx[rxpeegx[qpag;",
            "3": "k[ 17 nvo ] Kpegxp av bdn[ c[ewutovxp. Wvxqdh c[ew [a qj;n cxvkgo gj iq[gm .vioa[ jpxpb[opaadm kvavr",
            "4": ""
        }
    },
    {
        "order": 7,
        "text": "Kpegx apwgipn iq[h wvxqdh index.html, c[rkp ve] bdn[:",
        "answers": {
            "1": "ap wvxq[e c]xiv ]agqvxigovop; kx]r w[cpjpn av o[nuc[ HTML, a[ g CSS\\u2026 G kpyv JS g jQuery, c[o[xdv bdng [.vau w[w]n;xad ap o[ qxve;",
            "2": "q 17 nvo, c[rkp kx]r w[cpjpn ve], .o[ opc[v HTML. Kpegx jpr[xvni;, g gevaa[ lo[ i[bdogv iopn[ w[q[x[oade q vr[ ygjag \\u2014 [a xvzgn w[io]wgou q ]agqvxigovo ap wx[rxpeegiop",
            "3": "12 nvo, c[rkp in].pha[ apoca]ni; ap ipho i bviwnpoade [b].vagve HTML g CSS\\",
            "4": ""
        }
    },
    {
        "order": 5,
        "text": "Wvxqp; k[nr[ix[.ap; xpb[op Kpegxp — lo[:",
        "answers": {
            "1": "qvxiopnufgc HTML / CSS / JS. {kage [ivaage kave [ka[rx]wwagc Kpegxp wxvkn[ygn ve] w[e[.u i xpb[o[h \\u2014 w[qvxiopou iphod. Ap o[o e[evao Kpegx avea[r[ japn HTML g CSS, g vr[ wxga;ng q c[epak] gj 3 .vn[qvc, rkv [a g jpxpb[opn iq[g wvxqdv cx[qadv kvavycg",
            "2": "oxvavx w[ b[ci]. Q e[n[k[iog Kpegx ivxuvja[ jpagepni; iw[xo[e, p gevaa[ \\u2014 b[ci[e, g q iq[b[ka[v qxve; oxvagx[qpn e[n[kvyu ap w[niopqcg q [ka[e gj b[civxicgm cn]b[q Cgvqp",
            "3": "c[wgxphovx. Kpegx xpb[opn ap gaovxavo-gjkpagg: wgipn iopoug [ cxgwo[qpntopm, oxvhkgarv g gaqviog'g;m g avwn[m[ jpxpbpodqpn, cpc kn; io]kvaop 2-3 c]xip",
            "4": ""
        }
    },
    {
        "order": 9,
        "text": "K[ xpb[od ].govnve Kpegx ievagn wx[sviigh g w[bdqpn ap xpjadm xpb[.gm eviopm:",
        "answers": {
            "1": "7 xpjadm wx[sviigh, 8 xpb[.gm evio",
            "2": "6 xpjadm wx[sviigh, 12 xpb[.gm evio",
            "3": "3 xpjadm wx[sviigg, 5 xpb[.gm evio",
            "4": ""
        }
    },
    {
        "order": 3,
        "text": "Kpegx jpc[a.gn zc[n] cpc:",
        "answers": {
            "1": "cx]rndh [ong.agc i j[n[o[h evkpnut",
            "2": "[ong.agc",
            "3": "m[x[zgio",
            "4": ""
        }
    },
    {
        "order": 10,
        "text": "Iq[b[ka[v qxve; Kpegx q [ia[qa[e wx[q[kgo:",
        "answers": {
            "1": "wgzvo e]jdc] g grxpvo ap rgopxv. Jq]cg iox]a .pio[ qq[k;o Kpegxp q oxpai, q c[o[x[e ve] wxgm[k;o a[qdv gkvg w[ c]xi]",
            "2": "q cx]r] kx]jvh g bngjcgm. Xpjr[q[xd w[ k]zpe w[e[rpto Kpegx] m[x[z[ q[iiopapqngqpoui; w[inv xpb[.vh avkvng",
            "3": "Kpegx [bd.a[ [okdmpvo [kga, [b;jpovnua[ \\u2014 ap wxgx[kv. Q k]zv [a \\u2014 w]ovzvioqvaagc, opc .o[ q iq[b[ka[v qxve; [a av igkgo ap eviov. Wxgx[kp n].zv qivr[ q[iiopapqngqpvo vr[ k]zvqadh w[c[h",
            "4": ""
        }
    },
    {
        "order": 4,
        "text": "Kpegx w[io]wgn q ]agqvxigovo:",
        "answers": {
            "1": "ixpj] w[inv zc[nd. {a ikpn JA{ (ivh.pi apjdqpvoi; AEO) ap qdi[cgh bpnn g bvj wx[bnve w[io]wgn o]kp, c]kp g m[ovn",
            "2": "Ap ]kgqnvagv qivm Kpegx AV ikpqpn JA{, jpbgn ap qiv g w[zvn xpb[opou ap E{HC}. {a w[io]wgo q ]agqvxigovo o[nuc[ ap invk]tfvh r[k, c[rkp w[hevo: e[hcp g x[ka[h r[x[k \\u2014 lo[ av wxvkvn vr[ ev.opagh\\u2026",
            "3": "{bp qpxgpaop qdk]epad",
            "4": ""
        }
    },
    {
        "order": 1,
        "text": "Kn; ap.pnp wx[qvxge oq[t gao]g'gt. Q[wx[i: Kpegx] ivh.pi…",
        "answers": {
            "1": "24 r[kgcp",
            "2": "r[kgc[",
            "3": "28 r[kgc[q",
            "4": "32 r[kgcp"
        }
    },
    {
        "order": 6,
        "text": "Kpegx] c]wgng c[ewutovx, c[rkp ve] bdn[:",
        "answers": {
            "1": "6 nvo. Igioveadh bn[c apw[egapn [rx[ea]t bvn]t egcx[q[na[qc], p lcxpa \\u2014 b[nuz]t c[x[bc] i qdw]cnde e[ago[x[e",
            "2": "q 12 nvo. Lo[ bdn .vxadh igioveadh bn[c i .vxade wn[icge LED-lcxpa[e q 21 kthe. Gevaa[ ap ave Kpegx w[n].gn wvxqdh [wdo wx[rxpeegx[qpag;",
            "3": "k[ 17 nvo ] Kpegxp av bdn[ c[ewutovxp. Wvxqdh c[ew [a qj;n cxvkgo gj iq[gm .vioa[ jpxpb[opaadm kvavr",
            "4": ""
        }
    },
    {
        "order": 8,
        "text": "Ag [kag ivxuvjadv [oa[zvag; Kpegxp av kpng ve] o[n.[c kn; ng.a[ioa[r[ x[iop:",
        "answers": {
            "1": "av wxpqkp. {oa[zvag; qivrkp xpiogng Kpegxp g kvnpng vr[ n].zv",
            "2": "wxpqkp. Ap x[io Kpegxp o[ncpng b[nu, [bgkp g xpj[.px[qpagv q ntk;m",
            "3": "vx]akp w[nap; \\u2014 ] Kpegxp yv agc[rkp av bdn[ ivxuvjadm [oa[zvagh! g CSS",
            "4": ""
        }
    },
    {
        "order": 4,
        "text": "Kpegx w[io]wgn q ]agqvxigovo:",
        "answers": {
            "1": "ixpj] w[inv zc[nd. {a ikpn JA{ (ivh.pi apjdqpvoi; AEO) ap qdi[cgh bpnn g bvj wx[bnve w[io]wgn o]kp, c]kp g m[ovn",
            "2": "Ap ]kgqnvagv qivm Kpegx AV ikpqpn JA{, jpbgn ap qiv g w[zvn xpb[opou ap E{HC}. {a w[io]wgo q ]agqvxigovo o[nuc[ ap invk]tfvh r[k, c[rkp w[hevo: e[hcp g x[ka[h r[x[k \\u2014 lo[ av wxvkvn vr[ ev.opagh\\u2026",
            "3": "{bp qpxgpaop qdk]epad",
            "4": ""
        }
    },
    {
        "order": 10,
        "text": "Iq[b[ka[v qxve; Kpegx q [ia[qa[e wx[q[kgo:",
        "answers": {
            "1": "wgzvo e]jdc] g grxpvo ap rgopxv. Jq]cg iox]a .pio[ qq[k;o Kpegxp q oxpai, q c[o[x[e ve] wxgm[k;o a[qdv gkvg w[ c]xi]",
            "2": "q cx]r] kx]jvh g bngjcgm. Xpjr[q[xd w[ k]zpe w[e[rpto Kpegx] m[x[z[ q[iiopapqngqpoui; w[inv xpb[.vh avkvng",
            "3": "Kpegx [bd.a[ [okdmpvo [kga, [b;jpovnua[ \\u2014 ap wxgx[kv. Q k]zv [a \\u2014 w]ovzvioqvaagc, opc .o[ q iq[b[ka[v qxve; [a av igkgo ap eviov. Wxgx[kp n].zv qivr[ q[iiopapqngqpvo vr[ k]zvqadh w[c[h",
            "4": ""
        }
    }
]

# Decoder.decryption(encrypted_dict)
