#1052

#지민이는 N개의 물병을 가지고 있다. 각 물병에는 물을 무한대로 부을 수 있다. 처음에 모든 물병에는 물이 1리터씩 들어있다. 지민이는 이 물병을 또 다른 장소로 옮기려고 한다. 지민이는 한 번에 K개의 물병을 옮길 수 있다. 하지만, 지민이는 물을 낭비하기는 싫고, 이동을 한 번보다 많이 하기는 싫다. 따라서, 지민이는 물병의 물을 적절히 재분배해서, K개를 넘지 않는 비어있지 않은 물병을 만들려고 한다.
#물은 다음과 같이 재분배 한다.
#먼저 같은 양의 물이 들어있는 물병 두 개를 고른다. 그 다음에 한 개의 물병에 다른 한 쪽에 있는 물을 모두 붓는다. 이 방법을 필요한 만큼 계속 한다.
#이런 제약 때문에, N개로 K개를 넘지않는 비어있지 않은 물병을 만드는 것이 불가능할 수도 있다. 다행히도, 새로운 물병을 살 수 있다. 상점에서 사는 물병은 물이 1리터 들어있다.
#예를 들어, N=3이고, K=1일 때를 보면, 물병 3개로 1개를 만드는 것이 불가능하다. 한 병을 또다른 병에 부으면, 2리터가 들어있는 물병 하나와, 1리터가 들어있는 물병 하나가 남는다. 만약 상점에서 한 개의 물병을 산다면, 2리터가 들어있는 물병 두 개를 만들 수 있고, 마지막으로 4리터가 들어있는 물병 한 개를 만들 수 있다.

##첫째 줄에 N과 K가 주어진다. N은 107보다 작거나 같은 자연수이고, K는 1,000보다 작거나 같은 자연수이다.
##첫째 줄에 상점에서 사야하는 물병의 최솟값을 출력한다. 만약 정답이 없을 경우에는 -1을 출력한다.

n,k=map(int,input().split())
c=n
while c.bit_count()>k: #이진수는 1,2,4,8,...리터의 물이 든 물병의 개수를 나타낸다.
  c+=1 #물병 수+=1
print(c-n) #구매한 물병수

###이진수

####숏코딩 3위
n,k=map(int,input().split())
c=n
while c.bit_count()>k:c+=1
print(c-n)
