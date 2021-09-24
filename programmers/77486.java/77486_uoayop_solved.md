## 코드 설명

1. 유저의 이름, 상사 이름, 부하 이름 리스트, 판매 금액을 저장할 클래스 ```user```를 만들어줌

2. [유저의 이름 - 유저 객체] 를 [key-value]로 갖는 HashMap ```map```을 만들어줌

3. 조직에 참여한 순서 enroll, 상사 이름 referral을 이용해 map에 유저를 추가
- 입력 값에서 center는 '-'으로 주어지기 때문에
```map.put("-", new user("-", null));``` 와 같이 임의로 넣어줌

4. 판매원 기록 seller를 순차적으로 처리

4-1. ```map```을 이용해 해당 유저의 정보를 가져옴

4-2. curr_sell을 해당 유저의 판매 금액에 더해줌 : ```curr.addSell(curr_sell);```

- ```amount[i]``` = 해당 유저 판매량
- ```sell``` = 해당 유저가 판매한 금액 = amount[i] * 100
- ```curr_sell``` = 해당 유저가 가져가는 금액 = sell * 0.9
- ```to_boss``` = 상사에게 줘야하는 금액 = sell * 0.1
- ```boss_name``` = 해당 유저의 보스 이름

5. 상사 이름이 null이거나, 금액이 0원이 될 때까지 아래의 내용 반복

- 만약 상사에게 줘야하는 금액 ```to_boss```가 10원 미만이라면, 
현재 상사가 금액을 모두 가져감

- ```to_boss```가 10원 이상이라면<br/>
5-1. ```boss_sell``` = 현재 상사가 가져가는 금액 = to_boss의 90% = to_boss * 0.9<br/>
```boss.addSell(boss_sell);```<br/><br/>
5-2. 현재 상사의 상사에게 보내는 금액 to_boss = to_boss - boss_sell<br/>
5-3. 현재 상사의 상사 이름 = boss_name = boss.boss;<br/>


6. 모든 유저가 판매한 금액을 answer 리스트에 담아 반환
