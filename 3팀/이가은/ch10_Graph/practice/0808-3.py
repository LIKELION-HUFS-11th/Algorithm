'''
경로 압축(Path Compression) 기법을 적용하면 시간 복잡도 개선 가능
    : find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법. (0808-1.py 에서 find 함수만 수정)
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

