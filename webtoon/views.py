from django.shortcuts import render
from django.conf import settings

import pandas as pd
import os
import numpy as np
import random

webtoon_df = pd.DataFrame()

def select_random_images(df, num_images):
    # 해당 군집 라벨에 해당하는 웹툰 이미지들을 필터링합니다.

    selected_webtoons = []
    for i in range(num_images):
        filtered_webtoons = df[df['집단'] == i]
        # 랜덤으로 이미지를 선택합니다.
        selected_webtoon = random.sample(filtered_webtoons.index.tolist(), 1)
        selected_webtoons.extend(selected_webtoon)

    # 선택된 이미지들의 상세 정보를 반환합니다.
    return df.loc[selected_webtoons]

def home(request):
    # 웹툰 데이터프레임 로드
    global webtoon_df
    csv_file_path = os.path.join(settings.STATIC_ROOT, 'webtoon', 'webtoon0607.csv')
    webtoon_df = pd.read_csv(csv_file_path)

    # 군집별로 랜덤 이미지 선택
    random_images = select_random_images(webtoon_df , 5)


    # 렌더링할 HTML 페이지에 데이터 전달
    context = {'random_images': random_images}
    return render(request, 'webtoon/recommend_main.html', context)
def compute_distance(x1, y1, x2, y2):
    # Compute the Euclidean distance between two points (x1, y1) and (x2, y2)
    distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def find(label,selected_x, selected_y, webtoon_df):
    # 근접한 이미지 찾기
    similarity_threshold = 5  # 근접도 임계값 설정
    similar_images = []
    cnt=0
    for _, image in webtoon_df.iterrows():
        if cnt ==10:
            break
        distance = compute_distance(selected_x, selected_y, image['x'], image['y'])
        if distance < similarity_threshold and label == image['집단']:
            if distance == 0.0 :
                continue
            similar_images.append(image)

            cnt+=1

    return similar_images

def find_similar_images(request, selected_image_id):
    global webtoon_df
    # 선택한 이미지의 t-sne x, y 값 가져오기
    selected_image = webtoon_df.iloc[int(selected_image_id)]
    selected_x = selected_image['x']
    selected_y = selected_image['y']

    similar_images = find(selected_image['집단'],selected_x, selected_y, webtoon_df)

    # 렌더링할 HTML 페이지에 데이터 전달
    context = {'selected_image': selected_image, 'similar_images': similar_images}
    return render(request, 'webtoon/similar_images.html', context)


