# %%
from anagram import words_with_anagrams

if __name__ == '__main__':
	list1 = ["spot", "tops", "dad", "simple", "dine", "cats"]
	list2 = ["pots", "add", "simple", "dined", "acts", "cast"]
	ans = {"cats", "dad", "simple", "spot", "tops"}
	solution = words_with_anagrams(list1, list2)
	print("Example from assignment: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = ["wrench", "insurance", "careful", "dues", "dam", "null"]
	list2 = ["mad", "mint", "outrageous", "butter", "used"]
	ans = {"dues", "dam"}
	solution = words_with_anagrams(list1, list2)
	print("Test 1: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = ["duster", "drapes", "dose", "song", "ball"]
	list2 = ["deserted", "rudest", "balk", "rusted", "smart", "padres", "does", "soil"]
	ans = {"duster", "drapes", "dose"}
	solution = words_with_anagrams(list1, list2)
	print("Test 2: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = ["bible", "scribble", "a", "gentil", "preach"]
	list2 = ["lighten", "a", "libbers", "eparch", "motorcycle"]
	ans = {"preach", "a"}
	solution = words_with_anagrams(list1, list2)
	print("Test 3: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = ["sir", "ears", "raise", "serai", "air", "aes", "sea", "situation"]
	list2 = ["arise", "seria", "ser"]
	ans = {"raise", "serai"}
	solution = words_with_anagrams(list1, list2)
	print("Test 4: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = []
	list2 = ["word", "morewords", "if", "crash", "program", "then", "noob"]
	ans = set()
	solution = words_with_anagrams(list1, list2)
	print("Test 5: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = ["words", "for", "da", "test", "im", "hungry"]
	list2 = []
	ans = set()
	solution = words_with_anagrams(list1, list2)
	print("Test 6: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = ["padres", "parsed", "rasped", "spared", "spread", "enlist"]
	list2 = ["tinsel", "drapes", "silent", "listen", "inlets"]
	ans = {"padres", "parsed", "rasped", "spared", "spread", "enlist"}
	solution = words_with_anagrams(list1, list2)
	print("Test 7: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	list1 = []
	list2 = []
	ans = set()
	solution = words_with_anagrams(list1, list2)
	print("Test 8: " + str(set(solution) == ans and len(set(solution)) == len(solution)))

	# Empty strings might or might not need to be considered, someone asked on Ed, waiting for response
	list1 = ["introduces", "decanter", "", "drawer", "redraw", "daters"]
	list2 = ["dowry", "reductions", "stared", "", "recanted", "trades"]
	ans = {"", "decanter", "introduces", "daters"}
	solution = words_with_anagrams(list1, list2)
	print("Test 9: " + str(set(solution) == ans and len(set(solution)) == len(solution)))
# %%
