import os
import nltk

def buid_dict_file():
    word_to_id = {}
    dict_file = 'processed_files/word_to_id.txt'
    file1 = ['dialect.eg', 'dialect.uae']
    for file_item in file1:
        with open(file_item, 'r') as f:
            for item in f:
                item = item.strip()
                word_list = nltk.word_tokenize(item)
                # print(word_list)
                # input("===")
                for word in word_list:
                    word = word.lower()
                    if word not in word_to_id:
                        word_to_id[word] = 0
                    word_to_id[word] += 1
    
    print("Get word_dict success: %d words" % len(word_to_id))
    # write word_to_id to file
    word_dict_list = sorted(word_to_id.items(), key=lambda d: d[1], reverse=True)
    with open(dict_file, 'w') as f:
        f.write("<PAD>\n")
        f.write("<UNK>\n")
        f.write("<BOS>\n")
        f.write("<EOS>\n")
        for ii in word_dict_list:
            f.write("%s\t%d\n" % (str(ii[0]), ii[1]))
            # f.write("%s\n" % str(ii[0]))
    print("build dict finished!")
    return


def build_id_file():
    # load word_dict
    word_dict = {}
    num = 0
    with open('processed_files/word_to_id.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            item = line.strip()
            word = item.split('\t')[0]
            word_dict[word] = num
            num += 1
    print("Load embedding success! Num: %d" % len(word_dict))

    # generate id file
    file1 = ['dialect_dev.eg', 'dialect_dev.uae']

    for file_item in file1:
        id_file_data = []
        with open(file_item, 'r') as f:
            for item in f:
                item = item.strip()
                word_list = nltk.word_tokenize(item)
                # print(word_list)
                # input("===")
                id_list = []
                for word in word_list:
                    word = word.lower()
                    if word in word_dict.keys():
                        id = word_dict[word]
                    else:
                        id = word_dict['<UNK>']
                    id_list.append(id)
                id_file_data.append(id_list)
        # write to file:
        with open("processed_files/%s" % file_item, 'w') as f:
            for item in id_file_data:
                f.write("%s\n" % (' '.join([str(k) for k in item])))

    print('build id file finished!')
    return


if __name__ == '__main__':
    build_id_file()

