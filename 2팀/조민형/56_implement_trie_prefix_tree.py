# 노드용 클래스 생성. 딕셔너리로 여러 개의 노드 관리
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    # 빈 루트노트 만들기
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root #루트 설정
        for i in word: #계속해서 트리 탐색
            if i not in root.children: #해당되는 알파벳 없으면 추가
                root.children[i] = TrieNode()
            root = root.children[i] #트리 다음 노드로 들어가기
        root.word = True #해당되는 단어로 생성되었는지 추가. prefix와 구분
        

    def search(self, word: str) -> bool: #해당되는 단어 찾기. 알파벳이 끝까지 탐색되어야 함
        root = self.root
        for i in word: #트리 내려가면서 탐색
            if i not in root.children: #만약 없는 경우가 나올 경우 바로 false 리턴
                return False
            root = root.children[i] #해당되는 알파벳 자식노드가 있을 경우 계속 탐색
        return root.word #해당되는 단어가 있는지 구분한 word를 내보내서 prefix정도인지 완전히 일치한 단어인지 찾기
        
    def startsWith(self, prefix: str) -> bool: #prefix 찾기
        root = self.root
        for i in prefix: #똑같이 탐색
            if i not in root.children:
                return False
            root = root.children[i]
        return True #이건 해당되는 글자까지만 탐색되면 단어가 있든없든 상관없음


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)