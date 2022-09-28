def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

path = 'in.txt'
in_ = open(path,'r')
text = ''.join(in_)
enc_val = rle_encode(text)
in_.close()

out_ = open('out.txt', 'w')
out_.writelines(enc_val)
out_.close()

path_o='out.txt'
out_1 = open(path_o,'r+',encoding='utf-8-sig')
text_out = ''.join(out_1)
decode_val = rle_decode(text_out)

decode_ = open('decode.txt','w')
decode_.writelines(decode_val)




