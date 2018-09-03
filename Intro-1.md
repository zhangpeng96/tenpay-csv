# 抓包数据分析



抓包得到的数据大致如下

```json
{
    "ret_code":0,
    "ret_msg":"OK",
    "statistic":Array[1],
    "record":Array[*],
    "total":*,
    "last_bill_id":"1aa*************",
    "last_bill_type":1,
    "last_trans_id":"10000*******************",
    "last_create_time":153********,
    "is_over":false
}
```



`statistic`中分析了特定月份的“收入”、“支出”的金额

![](D:\mycode\python\tenpay-csv\image\image-1-2.png)



`record`中记录了各条账单的详细信息（顺便吐槽一下 Tencent 的英文水平：`negtive`）

![](D:\mycode\python\tenpay-csv\image\image-1-3.png)

