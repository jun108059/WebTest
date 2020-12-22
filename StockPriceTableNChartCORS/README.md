# Report#3 & Report#4

## Report#3 StockPriceTableNChartCORS 보완(1)

> Due Date 2020-12-13(일)

[Sample Project](https://github.com/chomskim/Web-Programming/tree/master/WP2020/StockProject/StockPriceTableNChart) 의 Chart CORS를 보완한다.

CORS를 사용할 수 있도록 코드를 설정

- response.headers['Access-Control-Allow-Origin'] = '*'
- Request의 headers에 포함
- Origin에서 Cross Origin의 Resource를 사용할 수 있도록 함
- `Origin` : 5001, `Cross Origin` : 5005

1. Stock Price Table을 과제 1번처럼 보기 좋게 한다.
2. 과제2와 같은 Footer를 준다.

### Result#3

![img](/img/Result04.png)

---

## Report#4 StockPriceTableNChartCORS 보완(2)

> Due Date 2020-12-22(화)

Report#3에 이어 Responsive Column을 추가하고, Delete 기능을 구현한다.

1. Chart와 Table(여러개 나오게 함)을 2개의 Column에 만든다.
   - Responsive로 화면이 줄어들면 1 Column으로 표시
2. Delete Chart와 Delete Table 기능(마지막 추가 된 Element 삭제)추가

- svg 파일을 만들기 위해서 temp 폴더를 static 아래에 추가

### Result#4

![img](/img/Result04.gif)
