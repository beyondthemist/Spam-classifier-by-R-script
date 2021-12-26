# 데이터셋 준비
1. enron.zip 압축 해제
2. check.py 실행
3. dataset.py 실행


### enron.zip
http://nlp.cs.aueb.gr/software_and_datasets/Enron-Spam/index.html
에서 구한 파일의 압축본.


###check.py
데이터셋에 포함된 파일들 중 인코딩이 UTF-8이 아닌 파일 삭제

###dataset.py
Kaggle에서 구한 데이터셋인 spam_ham_dataset.xlsx과 enron.zip의 데이터를 하나의 엑셀 파일로 합친 후,  
training set과 test set으로 나눈다.  
이 때 각 dataset의 spam:ham 비율은 일치시킨다.
