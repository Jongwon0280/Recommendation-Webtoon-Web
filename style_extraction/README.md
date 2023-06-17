### Style Extraction
크롤링한 웹툰의 상세정보들을 토대로 특성추출과 차원축소 및 군집화를 진행하였다.

<br>

> ### 사용기술
 <table border="1"  align = "center">
  <th>구분</th>
   <th>사용기술</th>
	<tr><!-- 첫번째 줄 시작 -->
	    <td> 특성추출 </td>
	    <td>  pytorch </td>
	</tr><!-- 첫번째 줄 끝 -->
  	<tr><!-- 첫번째 줄 시작 -->
	    <td> 차원축소 </td>
	    <td> sklearn.tsne </td>
	</tr><!-- 첫번째 줄 끝 -->	<tr><!-- 첫번째 줄 시작 -->
	    <td> 군집화 </td>
	    <td> sklearn.kmeans </td>
	
  </table>



<br>

> ### 1. 아키텍처

<br>

<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/a49bea13-0797-4fa0-a9cc-3d6591441b07" alt="image" style="display: inline-block; width: 80%; height: auto;">
</div>


<br>
<br>


> ### 2. 특성추출
스타일 추출을 위한 이미지 사이즈 및 정규화를 수행하고, CNN 중 ResNet을 사용하여 FNN전의 Max Pooling Layer의 Output의 벡터를 가져오도록 모델을 수정하여 웹툰당 512개의 feature를 얻었다.

<br>

<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/d5b4b1c9-ca1c-486e-8f93-b731a3156f41" alt="image" style="display: inline-block; width: 60%; height: auto;">

<br>
<br>
<br>

> ### 3. 차원축소 및 군집화
매니폴드 차원축소 기법인 T-SNE를 활용하여 512개의 feature를 2차원으로 줄였으며, 계층적군집화 기법인 Kmeans를 수행하여 라벨링을 수행하였다.

<br>

<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/1daebdda-b25a-49a6-9072-1520d4cbf5de" alt="image" style="display: inline-block; width: 60%; height: auto;">
</div>

<br>
<br>
<br>

> ### 4. 시각화 결과 및 최종산출물

<br>

**1. Kmeans(K=5) 시각화**

<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/a5a24115-9e93-4925-bc8a-a51e2db51edf" alt="image" style="display: inline-block; width: 60%; height: auto;">
</div>

<br>
<br>


**2. 최종 CSV**

<div style="text-align: center;">
    <img src="https://github.com/Jongwon0280/Recommendation-Webtoon-Web/assets/56438131/a014d81c-6f73-4152-8c08-a5e1748c737f" alt="image" style="display: inline-block; width: 60%; height: auto;">












