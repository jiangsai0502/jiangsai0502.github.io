### Mac txt乱码问题

1. cd [文件所在目录]

2. iconv -c -f GB2312 -t UTF-8 [你要看的文件] >> [新文件的名称]

   ```bash
   iconv -c -f GB2312 -t UTF-8 凡人修仙转.txt >> 凡人修仙转2.txt
   //GB2312是常用中文编码，其他还有gbk等，UTF-8是mac能够识别的编码
   ```

   

