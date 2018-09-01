from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import re


def home(request):
    return render(request,'home.html')

def count(request):
    user_text = request.GET['text']
    user_text1 = request.GET['text']
    user_text = re.findall('[\u4e00-\u9fa5]', user_text, re.S)
    total_count=len(user_text)

    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1

        else:
            word_dict[word] += 1

    dataframe = pd.DataFrame(list(word_dict.keys()), columns=['字'])
    dataframe['频次'] = pd.DataFrame(list(word_dict.values()))
    dataframe.sort_values('频次', inplace=True, ascending=False)
    old_width = pd.get_option('display.max_colwidth')
    pd.set_option('display.max_colwidth', -1)
    dataframe = dataframe.to_html(escape=False, index=False, sparsify=True, border=0, index_names=False, header=False)
    pd.set_option('display.max_colwidth', old_width)

    return render(request , 'count.html',{'count':total_count , 'text':user_text1,'dict':dataframe})

#def dataframe():
    #count().da

if __name__ == '__main__':
    home()
    count()