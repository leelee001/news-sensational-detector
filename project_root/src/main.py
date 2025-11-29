from feature_extractor import extract_kobert_embedding
from detector import predict_sensationalism

def main():
    title = "예시 제목"
    body = "예시 본문"
    
    # TODO: 벡터 추출
    # title_vec, body_vec = extract_kobert_embedding([title, body])
    
    # TODO: 판별
    # result = predict_sensationalism(...)
    # print(result)
    
if __name__ == "__main__":
    main()
