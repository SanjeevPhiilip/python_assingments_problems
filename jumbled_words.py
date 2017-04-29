import pandas as pd
import itertools
def sort_list(temp_li):
    temp_li.sort()
    temp_li = "".join(temp_li)
    return temp_li
df = pd.read_csv("/usr/share/dict/words",header=None)
df["letters"] = (df[0].str.lower()).apply(list)
df["letters"] = df["letters"].apply(sort_list)
input_text = raw_input('Enter jumbled letters: ')
input_text = input_text.lower()
input_text_list = list(input_text)
all_combo_set = set()
for L in range(1, len(input_text_list)+1):
        for subset in itertools.permutations(input_text_list, L):
                combo = "".join(sorted(subset))
                all_combo_set.add(combo)
for word in all_combo_set:
	if len(df[df["letters"]== word]):
		print((df[df["letters"]== word][0]).tolist())
