data_open = open('/Users/taraghazanfari/Desktop/Week3_BENG181/dataset.txt', 'r')
data_read = data_open.read().splitlines()
k = int(data_read[0])
text = data_read[1]


def stringComposition(k, text):
    final_result = []
    k_mers = []
    for i in range (len(text)-k+1):
        k_mers.append(text[i:i+k])
    if k_mers not in final_result:
        final_result.append(k_mers)
    final_result = sorted(final_result)
    return final_result

for s in stringComposition(k, text):
    print("\n".join(s))
