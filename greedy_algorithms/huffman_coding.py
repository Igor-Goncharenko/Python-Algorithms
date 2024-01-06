def encode_huffman(input_str: str) -> tuple[str, dict]:
    """"""
    # count symbols
    counter = {}
    for l in input_str:
        if l in counter:
            counter[l] += 1
        else:
            counter[l] = 1
    # create codes for letters
    codes = {k: "" for k in counter}
    queue = sorted(counter.items(), key=lambda x: x[1])

    while len(queue) > 1:
        el1 = queue.pop(0)
        el2 = queue.pop(0)

        if len(el1[0]) == 1:
            codes[el1[0]] = "0" + codes[el1[0]]
        else:
            for lt in el1[0]:
                codes[lt] = "0" + codes[lt]

        if len(el2[0]) == 1:
            codes[el2[0]] = "1" + codes[el2[0]]
        else:
            for lt in el2[0]:
                codes[lt] = "1" + codes[lt]

        queue.append((el1[0] + el2[0], el1[1] + el2[1]))
        queue = sorted(queue, key=lambda x: x[1])

    # encode input string
    result = ""
    for s in input_str:
        result += codes[s]

    return result, codes


def decode_huffman(input_str: str, codes: dict) -> str:
    """"""
    flipped_codes = {v: k for k, v in codes.items()}
    input_str = list(input_str)
    output = ""
    temp = ""
    while input_str:
        temp += input_str.pop(0)
        if not any(map(lambda x: x.startswith(temp + "0"), flipped_codes.keys())):
            output += flipped_codes[temp]
            temp = ""

    return output


if __name__ == '__main__':
    test_str = "EEEEEEEEEENNNNYSSOFFFTTTT"
    enc, cd = encode_huffman(test_str)
    print(cd)
    print(enc)
    dec = decode_huffman(enc, cd)
    print(dec)
    print(f"Encoded bits: {len(enc)}")
    print(f"String bits: {len(test_str) * 8}\n")

    text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. " \
           "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, " \
           "ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, " \
           "fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, " \
           "venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. " \
           "Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, " \
           "consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, " \
           "tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam " \
           "ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas " \
           "tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. " \
           "Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt " \
           "tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros " \
           "faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed " \
           "consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce " \
           "vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam " \
           "accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in " \
           "faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam " \
           "pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed " \
           "aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent " \
           "adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium " \
           "libero. Cras id dui. Aenean ut."
    enc, cd = encode_huffman(text)
    print(cd)
    print(enc)
    dec = decode_huffman(enc, cd)
    print(dec)
    print(f"Encoded bits: {len(enc)}")
    print(f"String bits: {len(text) * 8}")
