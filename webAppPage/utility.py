import pandas as pd
from webAppPage import utility
import streamlit as st


def getEmotionsCount(dataframeToCount):
    emotionCount = {}
    for i in dataframeToCount.index:
        emotions = dataframeToCount["labels"][i]
        if emotions in emotionCount:
            emotionCount[emotions] += 1
        else:
            emotionCount[emotions] = 1
    return dict(sorted(emotionCount.items(), key=lambda x: x[0]))

# uncomment this to run only when function call
# def getToCountDF():
#     savee, saveeDf = "Savee", pd.read_excel("E:/EM/individualTestOfDatasets/features_S_great.xlsx")
#
#     ravdess, ravdessDf = "Ravdess", pd.read_excel("E:/EM/individualTestOfDatasets/features_R_great.xlsx")
#     crema, cremaDf = "CremaD", pd.read_excel("E:/EM/individualTestOfDatasets/features_C_73.xlsx")
#     tess, tessDf = "Tess", pd.read_excel("E:/EM/individualTestOfDatasets/features_T.xlsx")
#     saveeEmotionList = utility.getEmotionsCount(saveeDf)
#     ravdessEmotionList = utility.getEmotionsCount(ravdessDf)
#     cremaEmotionList = utility.getEmotionsCount(cremaDf)
#     tessEmotionList = utility.getEmotionsCount(tessDf)
#
#     ds = {ravdess: [ravdessEmotionList, ravdessDf], crema: [cremaEmotionList, cremaDf], tess: [tessEmotionList, tessDf],
#           savee: [saveeEmotionList, saveeDf]}
#     # ds = {savee: [saveeEmotionList, saveeDf]}
#     return ds


savee, saveeDf = "Savee", pd.read_excel("E:/EM/individualTestOfDatasets/features_S_great.xlsx")
saveeEmotionList = utility.getEmotionsCount(saveeDf)

# Uncomment this when universal call
ravdess, ravdessDf = "Ravdess", pd.read_excel("E:/EM/individualTestOfDatasets/features_R_great.xlsx")
crema, cremaDf = "CremaD", pd.read_excel("E:/EM/individualTestOfDatasets/features_C_73.xlsx")
tess, tessDf = "Tess", pd.read_excel("E:/EM/individualTestOfDatasets/features_T.xlsx")
ravdessEmotionList = utility.getEmotionsCount(ravdessDf)
cremaEmotionList = utility.getEmotionsCount(cremaDf)
tessEmotionList = utility.getEmotionsCount(tessDf)

ds = {ravdess: [ravdessEmotionList, ravdessDf], crema: [cremaEmotionList, cremaDf], tess: [tessEmotionList, tessDf],
      savee: [saveeEmotionList, saveeDf]}
# ds = {savee: [saveeEmotionList, saveeDf]}


def getEmotionsFromEachDS_Dict():
    # uncomment this when function call
    # ds = utility.getToCountDF()
    col = st.columns(len(ds))
    for key, i in zip(ds.keys(), range(len(ds))):
        with col[i]:
            st.write(f"""##### <div style = "text-align:center">{key} Dataset</div>""",
                     unsafe_allow_html=True)
            st.write(ds[key][0])
            st.write(ds[key][1])
