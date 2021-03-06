#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == "__main__":
     # 크롤링을 하려는 URL
     targetUrl = "http://aqicn.org/city/seoul/kr/"
     # 웹페이지를 읽어온다.
     html = urlopen(targetUrl).read()
     # beautifulsoup 으로 파싱
     soupData = BeautifulSoup(html,'html.parser')
     # 지역 정보를 읽어 오고.
     titleData = soupData.find('a', id='aqiwgttitle1')
     print(titleData.string)
     # 미세먼지 수집 시간도 읽고
     timeData = soupData.find('span', id='aqiwgtutime')
     print(timeData.string)
     # 마지막으로 미세먼지 수치를 읽는다.
     aqiData = soupData.find('div', id='aqiwgtvalue')
     print(aqiData.get('title'))
     print(aqiData.string)