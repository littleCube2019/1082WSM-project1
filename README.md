##大概流程：##

1.先用bash Script (CreateDocumentList.sh) 整理成一份有格式的文章
2.makeVec.py吃進去, 用Parser進行前處理 (去詞性、去重複)，並建立word to index的表， 再用raw term frequency 計算 每份文件的tf向量， 同時也統計df向量，以及用nltk判斷哪些詞是動詞名詞，並將他們的Idx值也記下來，然後輸出成pickle檔，節省計算時間
3.main.py使用建立好的pickle檔，依題意算出四種組合輸出

##其中使用的公式、方法:##
+tf-idf
    最普通的raw term frquency 與 idf，base取10
+cos
    使用範例程式util.cosine
+stopword、strmmer、Parser
    使用範例程式Parser
+euclidean distance
    使用numpy.linalg.norm
+分出詞性動詞與名詞
    使用nltk套件


##相關調整討論##
因為一開始不確定誤差大是自己問題還是真實誤差，有做以下調整

###猜測原因1: 標點符號導致字不相同，比如plan: 與 plan被歸為兩個向量
對應方法:清除所有標點符號
<pre><code>
for word in Vocabulary:
    for i in ":!(),?":
        word.replace(i,"")
</code></pre>

###猜測原因2: tf公式不對
對應方法:一一測試課本上所有調整

###猜測原因3: stop word不同 (原本使用nltk)
應對方法:換回原本預設

###猜測原因4: 文章處理有誤
應對方法:檢查文章，發現很多字好像沒有被隔開的很好，比如207587 有 bladeSharp、drillingContoured等等，做分開後發現207587甚至可以衝到第二名
如下圖
![缺圖囉QQ](./img/1.jpg)

***試驗結果最後發現，還是所有都是預設的最貼近作業測資，因此改回所有預設，即使如此，第一題以外的值仍有不知名的誤差(尤其是歐式與pseudo feedback)，但是因為仍有將相關文章爬回，因此判斷應該不太影響排序



