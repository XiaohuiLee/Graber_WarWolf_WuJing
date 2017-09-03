# Grab-Application-Data
This is a grabber for grabbing the data for the BIG heat movie in China this year: 《War Wolf》. Basically this is about extracting its comment on douban.com

The basic url is https://movie.douban.com/subject/26363254/comments?start=0
While we change the “start” parameter in the url which is using GET method, we are allowed to re-load the url of each comment page, which makes our recursive codes runs perfectly well.

Using python libs:
1\requests
2\re
3\pandas

One thing worth to mention is that the cookie should be handled properly as login to douban.com is required and in order to not be forbidden to grab in douban.com. A bid generator is set up to generate different bid which is contained in cookies to pass different bid to douban —— which is a little tricky treat to "fraud" douban.




