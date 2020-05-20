arr = [('con cho', 0.05913243875864445), ('thanh oc con', 0.0790262557081126), ('thanh', 0.11984314898676356),
       ('cho la con', 0.12748048004056906), ('con', 0.14323823713631006), ('cho', 0.19488865479360015)]
array = []
for i in arr:
    r = {}
    r['word'] = i[0]
    r['score'] = i[1]
    array.append(r)
print(array)
