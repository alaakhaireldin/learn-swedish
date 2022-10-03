swedish_sentences = []
swedish_sentences_translation = []
new_list = []
import csv
with open("sentences_source.txt", "r") as text:
    new_line = ''
    lines = text.readlines()
    for i in range(len(lines)-1):
        if i % 5 == 0:
            swedish_sentences.append(lines[i].rstrip())
        elif i % 5 == 1:
            swedish_sentences_translation.append(lines[i].rstrip())
#
for i in range(len(swedish_sentences)):
    new_list.append([swedish_sentences[i], swedish_sentences_translation[i]])

print(swedish_sentences[0])

Details = ['Swedish', 'English']
# new_list
with open('to_learn.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(Details)
    write.writerows(new_list)
