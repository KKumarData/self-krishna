# import re
# 
# # Open the bookmark file
# with open("C:\\Users\\krish\\Documents\\GitHub\\self-krishna\\bookmarks_1_3_23.html","r" ) as f:
#     bookmark_html = f.read()
# 
# # Use a regular expression to find all of the HTTP links in the file
# http_links = re.findall(r'<A HREF="(http[^"]+)', bookmark_html)
# 
# # Print the links
# print(http_links)


print("Hi")

import re

with open("C:\\Users\\krish\\Documents\\GitHub\\self-krishna\\bookmarks_1_3_23.html", "r", encoding='utf-8') as f:
    with open("C:\\Users\\krish\\Documents\\GitHub\\self-krishna\\links.txt", "w", encoding='utf-8') as f_w:
        for i in f.readlines():
            bookmark_links = re.findall(r'<H3[^>]*>(.*?)</H3>', i)
            if bookmark_links:
                f_w.write(f"\n{''.join(bookmark_links)}")                     
            http_links = re.findall(r'<A HREF="(http[^"]+)', i)
            if http_links:                
                f_w.write(f"\n\t{''.join(http_links)}")     
                
                