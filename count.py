import read
import collections
data_hn = read.load_data()
headline = ""
for n in data_hn["headline"]:
    headline = headline + str(n) + " "
headline_wordlist = headline.split(' ')
headline_wordlist = [x.lower() for x in headline_wordlist]
print(collections.Counter(headline_wordlist).most_common(100))
#print(freq_count)