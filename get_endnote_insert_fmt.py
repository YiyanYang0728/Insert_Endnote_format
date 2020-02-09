# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:36:06 2020

@author: LucasTsubasaYang
"""

"""get Endnote insert format"""

import re

def get_Endnote_insert_format(endnote_file, paper_ref_file, outfile):
    endnote_ref = {}
    endnote_file = r'F:\add_ref_by_program\AOA.txt'
    f = open(endnote_file, 'r', encoding='utf-8')
    items_in_need = ['Author','Year','Title']
    for line in f:
        if line.startswith('Record Number'):
            rec_no = line.strip().split(': ')[1]
    #        print(rec_no)
            endnote_ref[rec_no] = {'Author':'NULL','Year':'NULL','Title':'NULL'}
        for key in items_in_need:
            if line.startswith(key+': '):
                content = line.strip().split(': ',1)[1]
                endnote_ref[rec_no][key] = content
    f.close()
    #print(endnote_ref['428'])
#    recno = '80'
#    print(endnote_ref[recno]['Title'][:30], endnote_ref[recno]['Year'], endnote_ref[recno]['Author'].split(',')[0])
#    print(len(endnote_ref))
    #partitionfinder 2: new methods 2016 Lanfear
    #PartitionFinder 2: New Methods 2017 Lanfear
    
    paper_ref_file = r'F:\add_ref_by_program\my_word_refs.txt'
    paper_ref = {}
    f = open(paper_ref_file, 'r')
    for line in f:
        No = line.split('\t')[0].split('.')[0]
        ref = line.split('\t')[1]
        lst = [i.strip() for i in re.split('\(|\)', ref, maxsplit=2)]
        author, year, title = lst[:3]
        title = title.split('. ')[0]
        paper_ref[No] = [author, year, title]
    f.close()
    
    g = open(outfile, 'w')
    for i in range(1, len(paper_ref)+1):
        No = str(i)
        print(No)
        if No not in paper_ref:
            print('This No. not exist!')
            continue
        for rec_no in endnote_ref:
            query_title = paper_ref[No][2].lower()[:30]
            query_year = paper_ref[No][1]
            query_author = ' '.join(re.split('\,|\&', paper_ref[No][0])[0].split()[:-1])
            if endnote_ref[rec_no]['Title'][:30].lower() == query_title \
            and endnote_ref[rec_no]['Year'] == query_year \
            and endnote_ref[rec_no]['Author'].split(',')[0] == query_author:
                #FORMAT ex: {Betts, 2018 #83}
                year = query_year
                author_last_name = query_author
                print(query_title, query_year, query_author)
                insert_format = '{'+author_last_name+', '+year+' #'+rec_no+'}'
                print(insert_format)
                g.write(No+'. '+'|'.join([query_title, query_year, query_author])+'\n')
                g.write(No+'. '+insert_format+'\n')
                break
        else:
            print(No, paper_ref[No])
            print('Not find!!!!!!!!!!!!!')
            print(paper_ref[No][2].lower()[:30], paper_ref[No][1], paper_ref[No][0].split(',')[0].split()[0])
    g.close()

if __name__ == '__main__':
    endnote_file = r'Example_input_exported_endnote_style.txt'
    paper_ref_file = r'Example_input_Paper_reference_list.txt'
    outfile = r'Example_output_Insert_format.txt'
    get_Endnote_insert_format(endnote_file, paper_ref_file, outfile)
    
