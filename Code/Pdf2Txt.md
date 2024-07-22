#### PDF转txt

```python
import fitz, re  # PyMuPDF


# PDF转txt
def extract_and_clean_text(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        # Extract text from the page
        page_text = page.get_text("text")
        if "645 楼" in page_text:
            pass
        # 处理段落
        page_text = clean_text(page_text)
        # Clean text by removing extra whitespace and newlines
        text += page_text + "\n"
    return text.strip()


# 处理字符串：、删除空行、、删除「---」
def clean_text(text):
    # 删除 「@熊熊 chn 2016-03-25 16:05:01」这种字符
    text = re.sub(r"@\S.*?\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}", "", text)
    # 删除「@刮西北风2017-08-19」
    text = re.sub(r"@\S+\d{4}-\d{2}-\d{2}", "", text)
    # 删除 「作者:冻云迷雾」这类字符
    text = re.sub(r"作者:\S+", "", text)
    text = re.sub(r"楼主:\S+", "", text)
    # 删除 「日期:2014-05-01」这类字符
    text = re.sub(r"日期:\d{4}-\d{2}-\d{2}", "", text)
    # 删除 「[img]http://img3.xxx.cn/xxx.png[/img]」「http://news\.xxx\.com\.xxx.shtml」
    text = re.sub(r"\[img\]\S+\[/img\]", "", text)
    text = re.sub(r"http\S+", "", text)
    # 删除多个连字符"-"
    text = re.sub(r"-{2,}", "", text)
    # 删除空格
    text = text.replace(" ", "")
    # 删除 自来 xxx楼
    text = re.sub(r"来自\n\d+楼", "", text)
    # 删除 \n
    text = text.replace("\n", "")
    # 删除每行前面的数字
    # text = re.sub(r"^\d+", "", text, flags=re.MULTILINE)
    return text


# 待处理PDF文件路径
pdf_path = "/Users/jiangsai/Downloads/天涯全集/208-虚拟货币的秘密，兼谈比特币的未来和各国的战略布局.pdf"
final_text = extract_and_clean_text(pdf_path)

# 保存到txt文件
output_txt_path = "/Users/jiangsai/Desktop/1.txt"
with open(output_txt_path, "w", encoding="utf-8") as txt_file:
    txt_file.write(final_text)

```

