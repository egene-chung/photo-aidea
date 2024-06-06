# 포토 AI디어

이화여자대학교 소프트웨어학부 컴퓨터공학전공 캡스톤디자인과창업프로젝트 19팀 우엉

작업기간: 2024.03 ~

## 팀원 소개

| 손윤지                                       | 정이진                                         | 정지은                                             |
| -------------------------------------------- | ---------------------------------------------- | -------------------------------------------------- |
| [@yunjeee](https://github.com/yunjeee)                                 | [@egene-chung](https://github.com/egene-chung) | [@stopsilver123](https://github.com/stopsilver123) |
| 프론트엔드                                   | AI                                             | 백엔드                                             |
| 이화여자대학교 소프트웨어학부 컴퓨터공학전공 | 이화여자대학교 소프트웨어학부 컴퓨터공학전공   | 이화여자대학교 소프트웨어학부 컴퓨터공학전공       |

## 프로젝트 소개

포토AI디어란 인물 전신에 대해 실시간으로 사진 각도, 구도 촬영 가이드를 제공하는 서비스입니다.

실시간으로 사진 촬영 가이드를 제공하여 따로 촬영 꿀팁을 찾거나 촬영 후 사진을 보정하는 번거로움을 없애고자 합니다.

또, 현재 기본 카메라 앱에서 제공하는 수평수직선, 기울기 바가 아니라 구도, 각도를 기반으로 더 세밀한 가이드를 제공하고자 합니다.

## 주요 기능

1.  실시간 피드백 제공

    - 카메라 화면에서 실시간으로 피드백을 제공합니다.

2.  5가지 클래스별 가이드 제공

    - Small_Figure : 전신의 크기가 이미지의 높이의 30프로 미만일 때 분류되는 Class
    - Large_Figure : 전신의 크기가 이미지의 높이의 70프로 보다 클 때 분류되는 Class
    - Excessive_Floor : 바닥의 비율이 이미지 높이의 30프로 보다 클 때 분류되는 Class
    - Limited_Floor : 바닥의 비율이 너무 적거나, 발이 잘렸을 때 분류되는 Class
    - Off_Center_Figure : 전신의 위치가 지나치게 치우쳐진 경우 분류되는 Class

3.  개인별 필터 기능

    - 피드백을 원하는, 원하지 않는 부분을 선택할 수 있습니다.
      - 예) 발끝 잘림 감지 X 체크 → 발끝이 잘린 구도여도 피드백을 제공하지 않음

## 기술 검증 링크

### 학습 모델 적용

repository : [https://github.com/egene-chung/photo-aidea](https://github.com/egene-chung/photo-aidea)

1. /models 폴더 다운로드 또는 git clone
2. /models/evaluate_model.py에서 folder_path = “데이터 경로”

   “데이터 경로”에 모델을 돌리고 싶은 **데이터가 있는 폴더의 경로**로 수정

3. python evaluate_mode.py 로 실행하여 학습시킨 CNN 모델 적용

전체 코드 : [https://github.com/egene-chung/photo-aidea/blob/dev/photo_aidea_final.ipynb](https://github.com/egene-chung/photo-aidea/blob/dev/photo_aidea_final.ipynb)

Documentation : https://egenechung.tistory.com/4
## Stacks

### Development

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black">

<img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white"> <img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white"> <img src="https://img.shields.io/badge/springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
