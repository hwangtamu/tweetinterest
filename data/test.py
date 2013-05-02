import requests
import json
import sys
import string,re,math,random,copy


#text="Angry Birds, the popular video game that involves catapulting birds at fortresses constructed by enemy pigs, now has a greater purpose than killing time at the checkout line. It&#x2019;s the subject of a 4,485-square-foot exhibit at the Kennedy Space Center Visitor Complex in Florida that is meant to teach children physics.&#xa; &#xa;Though Angry"

#text="While you're watching the dizzily enjoyable documentary divinely quotable . Atwitter before Twitter, she was a fabulous wit who brings to mind Wilde and Warhol even while being inimitably Vreelandesque: ''The best thing about London is Paris.'' ''Fashion is not the same thing as style.'' ''I loathe narcissism, but I approve of vanity.'' Vreeland,"
text="McDonald\u2019s Profit Rises, but Year-Over-Year Sales Fall"

def main():
	f=open('test.txt','w')
	f.write(text)


if __name__ =='__main__':
	main()