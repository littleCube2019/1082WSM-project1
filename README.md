大概流程：

先用bash Script (CreateVocabulary.sh) 輸出所有字入Vocabulary 檔案
再讓main.py吃進去,用Parser進行前處理  （stop word 使用nltk的）

接著用 CreateDocumentList 存所有文章到 DocumentList

