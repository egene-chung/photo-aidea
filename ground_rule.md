# GroundRule.md

- 의사 소통
    - 급한 연락은 카카오톡으로, 주된 연락은 slack으로 한다.
    - 공지사항 등의 중요한 내용에 대해서는 반응 및 답장을 반드시 남기도록 한다.
- 의사 결정
    - 3인 모두가 동의한 것에 대해서만 의견을 확정하도록 한다.
- 피드백
    - 노션 댓글로 피드백을 진행 후 모두 확인하였으면 수정사항 반영 및 댓글을 삭제한다.
- 회의
    - 추가적인 의논 사항이 필요할 때 화요일 11시~12시에 회의를 가진다.
    - 회의 시 항상 존댓말로 상호존중하여 회의를 진행한다.
- 아래의 GitHub Convention을 따르도록 한다.
    
    ### Commit Convention
    
    ---
    
    1. **Commit Policy**
        
        <aside>
        🗣 각 Commit == 하나의 논리적 변경
        
        </aside>
        
        →  하나의 기능 추가 / 삭제 등의 변경이 있을 때 ( commit message description 단위로 )
        
        자주 커밋하면 변경사항을 잘 추적 가능하고 충돌이 났을 경우 해결이 쉽고, 다른 사람의 코드를 파악 용이
        
    2. **Commit Message Convention**
        
        
        | Title | Description |
        | --- | --- |
        | Add | 새로운 기능 / func 추가 |
        | Fix | 버그 / 에러 수정 |
        | Modify | 기존 코드를 변경할 때
        폴더 구조 변경 
        주석의 수정 등
        파일 명을 수정할 경우 |
        | Remove | 파일을 삭제하는 작업
        더 이상 필요하지 않은 코드 삭제 |
        
        ex) Modify: Similarity 코드 수정
        
        - Title은 대문자
        - :뒤에 (space)
    
    ### Pull Request
    
    ---
    
    1. PR Title → Commit Message와 동일하게
        
        ex) Add : util.py 추가
        
    2. *PR을 올린 사람이 직접 Merge*
        
        → Reviewer 가 필요하다면 Reviewer 추가하여 피드백 받기
        
        → PR을 생성했지만, 계속 작업 중인 경우 git push시 pr에 자동 반영되므로
        
    3. `git pull upstream main` 진행하고 pr 날리기 → [Fork한 Repository 에서 작업 과정](https://www.notion.so/Fork-Repository-9dae4d11cf644be3ac6e29c6693f4496?pvs=21) 
    
    ### Branch Convention
    
    ---
    
    우선은 아래와 같이 대문자 없이 hyphen(-)으로 구분 ( 추후 main / dev 구분 - 업데이트 예정 )
    
    - main
    - main-lstm
    - main-spectography
    
    ### Fork한 Repository 에서 작업 과정
    
    ---
    
    1. 작업을 시작하기 전에 `git pull upstream main`을 사용하여 최신 변경 사항을 로컬 저장소로 가져오기
        - 혹은 Github page에서 [ Sync Fork ] 진행(upstream과 내 origin sync)하고
        `git pull origin main`
            
            ![Untitled](GroundRule%20md%206b5c4aabeb344f69b1d0536f9246be15/Untitled.png)
            
    2. Local에서 변경 사항을 작업 후 commit!
    3. 작업한 내용을 나의 fork(origin)에 **`push`**하기 전에 다시 한 번 `git pull upstream main`
        
        → 최신 상태를 반영 
        
        ```
        *Push 하기 전, 원격 저장소의 최신 변경 사항을 로컬 저장소로 가져와, 
        내가 Pull 받은 시점 이후에 다른 사람이 작업한 부분이 내가 작업한 부분과 충돌 가능성이 있기 때문!!*
        ```
        
    4. 충돌하지 않는다면 바로, 충돌이 있다면 해결하고 `git push` → PR 생성!