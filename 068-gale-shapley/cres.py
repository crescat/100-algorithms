# Day 68: Gale-Shapley

def stable_match(men, women):
    free_men = list(men.keys())
    engaged = {key: None for key in list(women.keys())}
    while free_men:
        boy = free_men.pop(0)
        for pref_girl in men[boy]:
            girl_pref = women[pref_girl].index(boy)
            fiance = engaged[pref_girl]

            if fiance:
                girl_pref_boy = women[pref_girl].index(boy)
                girl_pref_fiance = women[pref_girl].index(fiance)
                if girl_pref_boy < girl_pref_fiance:
                    engaged[pref_girl] = boy
                    free_men.append(fiance)
                    break
            else:
                engaged[pref_girl] = boy
                break
    return [(boy, girl) for girl, boy in engaged.items()]


men = {
    'adam': ['diana', 'alice', 'betty', 'claire'],
    'bob': ['betty', 'claire', 'alice', 'diana'],
    'charlie': ['betty', 'diana', 'claire', 'alice'],
    'david': ['claire', 'alice', 'diana', 'betty'],
}
women = {
    'alice': ['david', 'adam', 'charlie', 'bob'],
    'betty': ['adam', 'charlie', 'bob', 'david'],
    'claire': ['adam', 'bob', 'charlie', 'david'],
    'diana': ['david', 'adam', 'charlie', 'bob'],
}

print(stable_match(men, women))

# result:
# [('david', 'alice'),
# ('charlie', 'betty'),
# ('bob', 'claire'),
# ('adam', 'diana')]
