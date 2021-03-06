# Day44 (2022/03/17)

## 노트

### Gradient Centralization

> https://arxiv.org/pdf/2004.01461.pdf

평균을 계산해서 빼 준다는 매우 간단한 방법으로 gradient의 평균을 0으로 만드는 작업만 해 주면 generalization 성능이 개선된다는 것이 매우 인상적이었다.

### Explanation & Evaluation Methods for CNN

#### Task Definition

  * Evaluating reliability of attribution
    * Evaluating quality of saliency map
      * Model dependency
      * Dataset dependency
      * Robustness of saliency map itself
    * Boosting performance of generating saliency map

#### Qualitative Evaluation Methods

  * Coherence check
  * Discriminativity check
  * Human study

#### Quantitative Evaluation Methods

  * Completeness check with gradient
    * Maximizing sensitivity
    * Minimizing implementation variance
  * Minimizing infidelity
    * Noisy baseline method
    * Square removal test
  * Other quantitative evaluation methods
    * Localization error check
    * Sanity check: Weight initialization
    * Selectivity check: Heatmap penalty
    * ROAR: Remove & retain method

#### Remaining Tasks

  * Reducing computation cost of evaluation methods
  * Evaluating reliability of dataset itself

## 일지

### Daily scrum (10:00-10:10)

### 과제 수행 (10:10-12:00)

  * [과제] Computer Vision Basics & Research Trends
    * Human Pose Estimation Using Hourglass Network

### Time off (13:00-14:00)

  * nCov2019 신속항원검사 진행

### Mentoring (14:00-15:00)

> https://arxiv.org/pdf/1904.02868.pdf

  * Gradient centralization 소개
  * Explanation & evaluation methods for CNN 소개

### 과제 정답 확인 및 비교 (15:00-16:00)

### Peer session (16:00-17:00)

  * CLIP 성능 이야기
  * VoxelNet 소개
  * 취업 관련 이야기
    * 공인영어시험 이야기
    * 대기업 공채 소식 공유
    * 취업 직전 여행 계획 이야기
  * 인턴 경험 공유
  * 다음 peer session 준비
    * 주간 회고 양식 작성해 오기

### Office hour (17:00-18:00)

  * 과제 해설

### 과제 수행 (18:00-20:30)

  * [과제] Computer Vision Basics & Research Trends
    * Human Pose Estimation Using Hourglass Network
