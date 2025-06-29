def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    hmap = {}
    skip = False
    for lettre in text:
        lettre = lettre.lower()
        if lettre in hmap:
            hmap[lettre] += 1
        else:
            hmap[lettre] = 1
    
    return hmap

def sort_on(items):
    return items["num"]

def list_dict(hmap):
    ans = []
    while hmap:
        big = (None, 0)
        for key, val in hmap.items():
            if val > big[1]:
                big = (key, val)
        ans.append({"char": big[0], "num": big[1]})
        del hmap[big[0]]
        
    ans.sort(reverse=True, key=sort_on)
    return ans

if __name__ == "__main__":
    dic = {'t': 29492, 'h': 19175, 'e': 44537, ' ': 70479}
    caca = list_dict(dic)
    caca.sort(reverse=True, key=sort_on)
    print(caca)