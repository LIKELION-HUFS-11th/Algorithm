from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        text = paragraph.replace(",", " ")
        text = text.replace(".", "")
        text = text.replace("\'", "")
        text = text.replace("\"", "")
        text = text.replace("!", "")
        text = text.replace("?", "")
        text = text.replace(";", "")
        text = text.lower()
        splited_text = text.split()

        wordsdict = collections.Counter(splited_text)

        for i in wordsdict.most_common():
            if i[0] not in banned:
                return i[0]
                break
