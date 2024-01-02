# 그림체 별 웹툰 추천 및 커뮤니티

## 🐆프로젝트 소개
N사의 요일별웹툰의 썸네일 이미지의 그림체를 활용한 웹툰추천 웹사이트입니다.
<div style="text-align: center;">
  <img src="https://oasis-mouth-2d1.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fa6bbd52d-4565-47e8-8495-06a47f55eada%2F39f46391-919d-48bf-b496-f6c3d3aad1ee%2FUntitled_(3).png?table=block&id=5f1d6270-e5cb-470d-86f6-3a6bcc277a1e&spaceId=a6bbd52d-4565-47e8-8495-06a47f55eada&width=670&userId=&cache=v2" alt="이미지 설명" width=500 height=400 >
</div>

<br>

## 🕙개발기간
* 23.06.01일 - 23.07.01일

<br>

## 👨‍💻역할
> **그림체추출**
- CNN을 활용한 썸네일 이미지 임베딩 추출
- 차원축소 및 군집화
  
<br>

> **웹페이지 배포**
- Django framework를 활용한 웹페이지 구축
- Pass-Ta를 통한 배포
  
  
<br>

## 💻개발도구
- **Model** : ![Apache Kafka](https://img.shields.io/badge/Pytorch-A50034?style=flat-square&logo=&logoColor=white)  
- **Model Deployment** : ![Apache Kafka](https://img.shields.io/badge/Paas_Ta-4285F4?style=flat-square&logo=&logoColor=white) 

<br>



<br>

## 🖼️그림체추출

### 아키텍처
<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/5ae2c4ec-e3cb-47f1-b442-09683b73f6db" alt="이미지 설명" width=650 height=300 >
</div>

<br>

### 이미지 임베딩 추출
> **데이터셋**
> 
> N사의 요일별 웹툰 430여종을 Selenium을 통해 동적 크롤링
> 
> 크롤링 대상은 [웹툰이름, 썸네일경로, 웹툰상세페이지경로, 작가명]
>
> <a href="https://comic.naver.com/webtoon"><img src="https://img.shields.io/badge/N사 요일별웹툰 Link-222222?style=flat-square&logo=&logoColor=white"/></a>

<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/a8d48af9-a799-4487-8a2e-95daf6a40e42" alt="이미지 설명" width=650 height=300 >
</div>

<br>

> **임베딩 차원축소 및 군집화**
>
1. 사전학습된 ![Apache Kafka](https://img.shields.io/badge/ResNet-4285F4?style=flat-square&logo=&logoColor=white)을 사용하여 512차원으로 매핑
<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/4748b16f-6984-41f2-be08-c8f6461d01df" alt="이미지 설명" width=650 height=300 >
</div>

2. ![Apache Kafka](https://img.shields.io/badge/T_SNE-43B02A?style=flat-square&logo=&logoColor=white)를 사용하여, 이미지 임베딩을 2차원으로 매핑

<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/d84b6818-dbb0-4539-82bf-e486dc8eaed6" alt="이미지 설명" width=350 height=300 >
</div>

<br>

3. ![Apache Kafka](https://img.shields.io/badge/K_MEANS-4285F4?style=flat-square&logo=&logoColor=white)를 통해 5가지로 군집화시키고, 라벨로 사용

<div style="text-align: center;">
  <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/4384a0a7-414e-4065-afa3-cbaa2174ba29" alt="이미지 설명" width=350 height=300 >
</div>

### 웹툰 추천
>
> 5가지 군집별 랜덤으로 썸네일 이미지를 사용자에게 보여주고, 특정 이미지 선택시 군집에서 Euclidean거리를 기준으로 10종의 웹툰을 추천 

<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/a14a05b9-87b8-4e45-9318-d82b1a4bfb89" alt="image" style="display: inline-block; width: 70%; height: auto;">
</div>

<br>
<br>

### 웹페이지

### 1. 그림체별 웹툰추천

> **recommend_main.html**
<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/46457812-0d87-432b-8c8e-29479709b616" alt="image" style="display: inline-block; width: 70%; height: auto;">
</div>

<br>
<br>


> **similar_images.html**
<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/a14a05b9-87b8-4e45-9318-d82b1a4bfb89" alt="image" style="display: inline-block; width: 70%; height: auto;">
</div>


### 2. 커뮤니티

> **blog application**

<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/06b54609-b32a-4dcc-9ccd-fa11a5d06a4a" alt="image" style="display: inline-block; width: 70%; height: auto;">
</div>












