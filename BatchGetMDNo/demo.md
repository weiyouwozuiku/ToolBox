---
title: Acwing刷题记录
author: 不二
mathjax: true
date: 2021-03-23 02:35:22
tags: 
- Cpp
img: https://cdn.jsdelivr.net/gh/weiyouwozuiku/weiyouwozuiku.github.io@src/source/_posts/PageImg/algorithm2.jpg
categories: 算法
---

## 前言

本文记录本人刷Acwing过程的收获和代码。语言选择C++。

## 1~1000

### 1~500

#### 1~100

[1.](https://www.acwing.com/problem/content/)



```cpp
```

[2.](https://www.acwing.com/problem/content/)



```cpp
```

[3.](https://www.acwing.com/problem/content/)



```cpp
```

[4.](https://www.acwing.com/problem/content/)



```cpp
```

[5.](https://www.acwing.com/problem/content/)



```cpp
```

[6.](https://www.acwing.com/problem/content/)



```cpp
```

[7.](https://www.acwing.com/problem/content/)



```cpp
```

[8.](https://www.acwing.com/problem/content/)



```cpp
```

[9.](https://www.acwing.com/problem/content/)



```cpp
```

[10.](https://www.acwing.com/problem/content/)



```cpp
```

[11.](https://www.acwing.com/problem/content/)



```cpp
```

[12.](https://www.acwing.com/problem/content/)



```cpp
```

[13.](https://www.acwing.com/problem/content/)



```cpp
```

[14.](https://www.acwing.com/problem/content/)



```cpp
```

[15.](https://www.acwing.com/problem/content/)



```cpp
```

[16.](https://www.acwing.com/problem/content/)



```cpp
```

[17.](https://www.acwing.com/problem/content/)



```cpp
```

[18.](https://www.acwing.com/problem/content/)



```cpp
```

[19. 二叉树的下一个节点](https://www.acwing.com/problem/content/31/)

这题主要想法就是判断当前节点是否拥有右节点。如果拥有右节点，则中序遍历的后一个节点为右节点子树的最左的节点。即，通过右节点循环找到子树的最左的节点；如果没有右节点，则中序遍历的后一个节点为该节点父节点的拐点。即上一次子树的根节点。

```cpp
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* p) {
        if(!p) return nullptr;
        //有右节点的情况
        if(p->right){
            p=p->right;
            while(p->left)
                p=p->left;
            return p;
        }else{
            //没有右节点的情况
            while(p->father&&p->father->right==p) p=p->father;
            return p->father;
        }
    }
};
```

[20.](https://www.acwing.com/problem/content/)



```cpp
```

[21.](https://www.acwing.com/problem/content/)



```cpp
```

[22.](https://www.acwing.com/problem/content/)



```cpp
```

[23.](https://www.acwing.com/problem/content/)



```cpp
```

[24.](https://www.acwing.com/problem/content/)



```cpp
```

[25.](https://www.acwing.com/problem/content/)



```cpp
```

[26. 二进制中1的个数](https://www.acwing.com/problem/content/25/)

```cpp
class Solution {
public:
    int NumberOf1(int n) {
        int res=0;
        while(n) n-=n&-n,res+=1;
        return res;
    }
};
```

[27.](https://www.acwing.com/problem/content/)



```cpp
```

[28.](https://www.acwing.com/problem/content/)



```cpp
```

[29.](https://www.acwing.com/problem/content/)



```cpp
```

[30.](https://www.acwing.com/problem/content/)



```cpp
```

[31.](https://www.acwing.com/problem/content/)



```cpp
```

[32.](https://www.acwing.com/problem/content/)



```cpp
```

[33. 链表中倒数第k个节点](https://www.acwing.com/problem/content/32/)

本题解题分为两步：

1. 计算当前链表长度
2. 通过n-k循环找到返回的节点

```cpp
class Solution {
public:
    ListNode* findKthToTail(ListNode* pListHead, int k) {
        if(!pListHead) return NULL;
        int len=0;
        for(auto p=pListHead;p;p=p->next) len+=1;
        if(k>len)return NULL;
        else{
            auto p=pListHead;
            for(int i=0;i<len-k;i++) p=p->next;
            return p;
        }
    }
};
```

[34.](https://www.acwing.com/problem/content/)



```cpp
```

[35. 反转链表](https://www.acwing.com/problem/content/33/)

此题有两个版本，一个迭代，一个递归。

迭代版：

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //如果没有节点或者只有一个节点
        if(head==NULL||head->next==NULL) return head;
        auto current=head;
        ListNode* pre=NULL;
        while(current){
            auto next=current->next;
            current->next=pre;
            pre=current;
            current=next;
        }
        return pre;
    }
};
```

递归版：

```cpp

```

[36.](https://www.acwing.com/problem/content/)



```cpp
```

[37.](https://www.acwing.com/problem/content/)



```cpp
```

[38.](https://www.acwing.com/problem/content/)



```cpp
```

[39.](https://www.acwing.com/problem/content/)



```cpp
```

[40.](https://www.acwing.com/problem/content/)



```cpp
```

[41.](https://www.acwing.com/problem/content/)



```cpp
```

[42.](https://www.acwing.com/problem/content/)



```cpp
```

[43.](https://www.acwing.com/problem/content/)



```cpp
```

[44.](https://www.acwing.com/problem/content/)



```cpp
```

[45.](https://www.acwing.com/problem/content/)



```cpp
```

[46.](https://www.acwing.com/problem/content/)



```cpp
```

[47.](https://www.acwing.com/problem/content/)



```cpp
```

[48.](https://www.acwing.com/problem/content/)



```cpp
```

[49.](https://www.acwing.com/problem/content/)



```cpp
```

[50.](https://www.acwing.com/problem/content/)



```cpp
```

[51.](https://www.acwing.com/problem/content/)



```cpp
```

[52.](https://www.acwing.com/problem/content/)



```cpp
```

[53.](https://www.acwing.com/problem/content/)



```cpp
```

[54.](https://www.acwing.com/problem/content/)



```cpp
```

[55.](https://www.acwing.com/problem/content/)



```cpp
```

[56.](https://www.acwing.com/problem/content/)



```cpp
```

[57.](https://www.acwing.com/problem/content/)



```cpp
```

[58.](https://www.acwing.com/problem/content/)



```cpp
```

[59.](https://www.acwing.com/problem/content/)



```cpp
```

[60.](https://www.acwing.com/problem/content/)



```cpp
```

[61.](https://www.acwing.com/problem/content/)



```cpp
```

[62.](https://www.acwing.com/problem/content/)



```cpp
```

[63.](https://www.acwing.com/problem/content/)



```cpp
```

[64.](https://www.acwing.com/problem/content/)



```cpp
```

[65.](https://www.acwing.com/problem/content/)



```cpp
```

[66.](https://www.acwing.com/problem/content/)



```cpp
```

[67.](https://www.acwing.com/problem/content/)



```cpp
```

[68.](https://www.acwing.com/problem/content/)



```cpp
```

[69.](https://www.acwing.com/problem/content/)



```cpp
```

[70.](https://www.acwing.com/problem/content/)



```cpp
```

[71.](https://www.acwing.com/problem/content/)



```cpp
```

[72.](https://www.acwing.com/problem/content/)



```cpp
```

[73.](https://www.acwing.com/problem/content/)



```cpp
```

[74.](https://www.acwing.com/problem/content/)



```cpp
```

[75.](https://www.acwing.com/problem/content/)



```cpp
```

[76.](https://www.acwing.com/problem/content/)



```cpp
```

[77.翻转单词顺序](https://www.acwing.com/problem/content/73/)

本题分为二步：

1. 首先将整个字符串进行翻转
2. 将每个字母进行翻转。此处用双指针算法，设置j获取当前字母长度，进行翻转

```cpp
class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(),s.end());
        for(int i=0;i<s.size();i++){
            int j=i+1;
            while(s[j]!=' '&&j<s.size()) j++;
            reverse(s.begin()+i,s.begin()+j);
            i=j;
        }
        return s;
    }
};
```

[78.](https://www.acwing.com/problem/content/)



```cpp
```

[79.](https://www.acwing.com/problem/content/)



```cpp
```

[80.](https://www.acwing.com/problem/content/)



```cpp
```

[81.](https://www.acwing.com/problem/content/)



```cpp
```

[82.](https://www.acwing.com/problem/content/)



```cpp
```

[83.](https://www.acwing.com/problem/content/)



```cpp
```

[84.](https://www.acwing.com/problem/content/)



```cpp
```

[85.](https://www.acwing.com/problem/content/)



```cpp
```

[86.](https://www.acwing.com/problem/content/)



```cpp
```

[87.](https://www.acwing.com/problem/content/)



```cpp
```

[88.](https://www.acwing.com/problem/content/)



```cpp
```

[89.](https://www.acwing.com/problem/content/)



```cpp
```

[90.](https://www.acwing.com/problem/content/)



```cpp
```

[91.](https://www.acwing.com/problem/content/)



```cpp
```

[92.](https://www.acwing.com/problem/content/)



```cpp
```

[93.](https://www.acwing.com/problem/content/)



```cpp
```

[94.](https://www.acwing.com/problem/content/)



```cpp
```

[95.](https://www.acwing.com/problem/content/)



```cpp
```

[96.](https://www.acwing.com/problem/content/)



```cpp
```

[97.](https://www.acwing.com/problem/content/)



```cpp
```

[98.](https://www.acwing.com/problem/content/)



```cpp
```

[99.](https://www.acwing.com/problem/content/)



```cpp
```

[100.](https://www.acwing.com/problem/content/)



```cpp
```

#### 101~200

[101.](https://www.acwing.com/problem/content/)



```cpp
```

[102.](https://www.acwing.com/problem/content/)



```cpp
```

[103.](https://www.acwing.com/problem/content/)



```cpp
```

[104.](https://www.acwing.com/problem/content/)



```cpp
```

[105.](https://www.acwing.com/problem/content/)



```cpp
```

[106.](https://www.acwing.com/problem/content/)



```cpp
```

[107.](https://www.acwing.com/problem/content/)



```cpp
```

[108.](https://www.acwing.com/problem/content/)



```cpp
```

[109.](https://www.acwing.com/problem/content/)



```cpp
```

[110.](https://www.acwing.com/problem/content/)



```cpp
```

[111.](https://www.acwing.com/problem/content/)



```cpp
```

[112.](https://www.acwing.com/problem/content/)



```cpp
```

[113.](https://www.acwing.com/problem/content/)



```cpp
```

[114.](https://www.acwing.com/problem/content/)



```cpp
```

[115.](https://www.acwing.com/problem/content/)



```cpp
```

[116.](https://www.acwing.com/problem/content/)



```cpp
```

[117.](https://www.acwing.com/problem/content/)



```cpp
```

[118.](https://www.acwing.com/problem/content/)



```cpp
```

[119.](https://www.acwing.com/problem/content/)



```cpp
```

[120.](https://www.acwing.com/problem/content/)



```cpp
```

[121.](https://www.acwing.com/problem/content/)



```cpp
```

[122.](https://www.acwing.com/problem/content/)



```cpp
```

[123.](https://www.acwing.com/problem/content/)



```cpp
```

[124.](https://www.acwing.com/problem/content/)



```cpp
```

[125.](https://www.acwing.com/problem/content/)



```cpp
```

[126.](https://www.acwing.com/problem/content/)



```cpp
```

[127.](https://www.acwing.com/problem/content/)



```cpp
```

[128.](https://www.acwing.com/problem/content/)



```cpp
```

[129.](https://www.acwing.com/problem/content/)



```cpp
```

[130.](https://www.acwing.com/problem/content/)



```cpp
```

[131.](https://www.acwing.com/problem/content/)



```cpp
```

[132.](https://www.acwing.com/problem/content/)



```cpp
```

[133.](https://www.acwing.com/problem/content/)



```cpp
```

[134.](https://www.acwing.com/problem/content/)



```cpp
```

[135.](https://www.acwing.com/problem/content/)



```cpp
```

[136.](https://www.acwing.com/problem/content/)



```cpp
```

[137.](https://www.acwing.com/problem/content/)



```cpp
```

[138.](https://www.acwing.com/problem/content/)



```cpp
```

[139.](https://www.acwing.com/problem/content/)



```cpp
```

[140.](https://www.acwing.com/problem/content/)



```cpp
```

[141.](https://www.acwing.com/problem/content/)



```cpp
```

[142.](https://www.acwing.com/problem/content/)



```cpp
```

[143.](https://www.acwing.com/problem/content/)



```cpp
```

[144.](https://www.acwing.com/problem/content/)



```cpp
```

[145.](https://www.acwing.com/problem/content/)



```cpp
```

[146.](https://www.acwing.com/problem/content/)



```cpp
```

[147.](https://www.acwing.com/problem/content/)



```cpp
```

[148.](https://www.acwing.com/problem/content/)



```cpp
```

[149.](https://www.acwing.com/problem/content/)



```cpp
```

[150.](https://www.acwing.com/problem/content/)



```cpp
```

[151.](https://www.acwing.com/problem/content/)



```cpp
```

[152.](https://www.acwing.com/problem/content/)



```cpp
```

[153.](https://www.acwing.com/problem/content/)



```cpp
```

[154.滑动窗口](https://www.acwing.com/problem/content/156/)

本题利用了结果本身的单调性。因为滑动窗口的长度限制，所以使用单调队列而非单调栈。当新元素入队的时候，元素从队尾移除。当新入队元素小于(或大于)等于队尾元素时，将相应元素从队尾出队。生成的单调队列具有单调性，其最值即为队尾或队首元素。

```cpp
#include <iostream>
using namespace std;
const int N = 1e6 + 10;
//q数组负责记录提供的数据，s数组负责记录q数组对应元素的索引
int q[N], s[N];
//hh表示单调队列的头部，tt表示单调队列的尾部
int hh = 0, tt = -1;

int main() {
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) scanf("%d", &q[i]);
    for (int i = 0; i < n; ++i) {
        //检查队头是否出队列
        if (hh <= tt && i - k + 1 > s[hh]) ++hh;
        //检查单调队列队尾元素是否大于等于新入队元素
        while (hh <= tt && q[s[tt]] >= q[i]) --tt;
        //新元素入队
        s[++tt] = i;
        if (i >= k - 1) printf("%d ", q[s[hh]]);
    }
    printf("\n");
    //重新初始化
    hh = 0, tt = -1;
    for (int i = 0; i < n; ++i) {
        //检查队头是否出队列
        if (hh <= tt && i - k + 1 > s[hh]) ++hh;
        //检查单调队列队尾元素是否小于等于新入队元素
        while (hh <= tt && q[s[tt]] <= q[i]) --tt;
        //新元素入队
        s[++tt] = i;
        if (i >= k - 1) printf("%d ", q[s[hh]]);
    }
    return 0;
}
```

[155.](https://www.acwing.com/problem/content/)



```cpp
```

[156.](https://www.acwing.com/problem/content/)



```cpp
```

[157.](https://www.acwing.com/problem/content/)



```cpp
```

[158.](https://www.acwing.com/problem/content/)



```cpp
```

[159.](https://www.acwing.com/problem/content/)



```cpp
```

[160.](https://www.acwing.com/problem/content/)



```cpp
```

[161.](https://www.acwing.com/problem/content/)



```cpp
```

[162.](https://www.acwing.com/problem/content/)



```cpp
```

[163.](https://www.acwing.com/problem/content/)



```cpp
```

[164.](https://www.acwing.com/problem/content/)



```cpp
```

[165.](https://www.acwing.com/problem/content/)



```cpp
```

[166.](https://www.acwing.com/problem/content/)



```cpp
```

[167.](https://www.acwing.com/problem/content/)



```cpp
```

[168.](https://www.acwing.com/problem/content/)



```cpp
```

[169.](https://www.acwing.com/problem/content/)



```cpp
```

[170.](https://www.acwing.com/problem/content/)



```cpp
```

[171.](https://www.acwing.com/problem/content/)



```cpp
```

[172.](https://www.acwing.com/problem/content/)



```cpp
```

[173.](https://www.acwing.com/problem/content/)



```cpp
```

[174.](https://www.acwing.com/problem/content/)



```cpp
```

[175.](https://www.acwing.com/problem/content/)



```cpp
```

[176.](https://www.acwing.com/problem/content/)



```cpp
```

[177.](https://www.acwing.com/problem/content/)



```cpp
```

[178.](https://www.acwing.com/problem/content/)



```cpp
```

[179.](https://www.acwing.com/problem/content/)



```cpp
```

[180.](https://www.acwing.com/problem/content/)



```cpp
```

[181.](https://www.acwing.com/problem/content/)



```cpp
```

[182.](https://www.acwing.com/problem/content/)



```cpp
```

[183.](https://www.acwing.com/problem/content/)



```cpp
```

[184.](https://www.acwing.com/problem/content/)



```cpp
```

[185.](https://www.acwing.com/problem/content/)



```cpp
```

[186.](https://www.acwing.com/problem/content/)



```cpp
```

[187.](https://www.acwing.com/problem/content/)



```cpp
```

[188.](https://www.acwing.com/problem/content/)



```cpp
```

[189.](https://www.acwing.com/problem/content/)



```cpp
```

[190.](https://www.acwing.com/problem/content/)



```cpp
```

[191.](https://www.acwing.com/problem/content/)



```cpp
```

[192.](https://www.acwing.com/problem/content/)



```cpp
```

[193.](https://www.acwing.com/problem/content/)



```cpp
```

[194.](https://www.acwing.com/problem/content/)



```cpp
```

[195.](https://www.acwing.com/problem/content/)



```cpp
```

[196.](https://www.acwing.com/problem/content/)



```cpp
```

[197. 阶乘分解](https://www.acwing.com/problem/content/description/199/)

质数定理：不超过x的质数的个数近似为$\frac{x}{ln(x)}$。

底数为10时，对数可简写为$lg(x)$。

底数为e时，对数可简写为$ln(x)$。

[198.](https://www.acwing.com/problem/content/)



```cpp
```

[199.](https://www.acwing.com/problem/content/)



```cpp
```

[200.](https://www.acwing.com/problem/content/)



```cpp
```

#### 201~300

[201.](https://www.acwing.com/problem/content/)



```cpp
```

[202.](https://www.acwing.com/problem/content/)



```cpp
```

[203.](https://www.acwing.com/problem/content/)



```cpp
```

[204.](https://www.acwing.com/problem/content/)



```cpp
```

[205.](https://www.acwing.com/problem/content/)



```cpp
```

[206.](https://www.acwing.com/problem/content/)



```cpp
```

[207.](https://www.acwing.com/problem/content/)



```cpp
```

[208.](https://www.acwing.com/problem/content/)



```cpp
```

[209.](https://www.acwing.com/problem/content/)



```cpp
```

[210.](https://www.acwing.com/problem/content/)



```cpp
```

[211.](https://www.acwing.com/problem/content/)



```cpp
```

[212.](https://www.acwing.com/problem/content/)



```cpp
```

[213.](https://www.acwing.com/problem/content/)



```cpp
```

[214.](https://www.acwing.com/problem/content/)



```cpp
```

[215.](https://www.acwing.com/problem/content/)



```cpp
```

[216.](https://www.acwing.com/problem/content/)



```cpp
```

[217.](https://www.acwing.com/problem/content/)



```cpp
```

[218.](https://www.acwing.com/problem/content/)



```cpp
```

[219.](https://www.acwing.com/problem/content/)



```cpp
```

[220.](https://www.acwing.com/problem/content/)



```cpp
```

[221.](https://www.acwing.com/problem/content/)



```cpp
```

[222.](https://www.acwing.com/problem/content/)



```cpp
```

[223.](https://www.acwing.com/problem/content/)



```cpp
```

[224.](https://www.acwing.com/problem/content/)



```cpp
```

[225.](https://www.acwing.com/problem/content/)



```cpp
```

[226.](https://www.acwing.com/problem/content/)



```cpp
```

[227.](https://www.acwing.com/problem/content/)



```cpp
```

[228.](https://www.acwing.com/problem/content/)



```cpp
```

[229.](https://www.acwing.com/problem/content/)



```cpp
```

[230.](https://www.acwing.com/problem/content/)



```cpp
```

[231.](https://www.acwing.com/problem/content/)



```cpp
```

[232.](https://www.acwing.com/problem/content/)



```cpp
```

[233.](https://www.acwing.com/problem/content/)



```cpp
```

[234.](https://www.acwing.com/problem/content/)



```cpp
```

[235.](https://www.acwing.com/problem/content/)



```cpp
```

[236.](https://www.acwing.com/problem/content/)



```cpp
```

[237.](https://www.acwing.com/problem/content/)



```cpp
```

[238.](https://www.acwing.com/problem/content/)



```cpp
```

[239.](https://www.acwing.com/problem/content/)



```cpp
```

[240.](https://www.acwing.com/problem/content/)



```cpp
```

[241.](https://www.acwing.com/problem/content/)



```cpp
```

[242.](https://www.acwing.com/problem/content/)



```cpp
```

[243.](https://www.acwing.com/problem/content/)



```cpp
```

[244.](https://www.acwing.com/problem/content/)



```cpp
```

[245.](https://www.acwing.com/problem/content/)



```cpp
```

[246.](https://www.acwing.com/problem/content/)



```cpp
```

[247.](https://www.acwing.com/problem/content/)



```cpp
```

[248.](https://www.acwing.com/problem/content/)



```cpp
```

[249.](https://www.acwing.com/problem/content/)



```cpp
```

[250.](https://www.acwing.com/problem/content/)



```cpp
```

[251.](https://www.acwing.com/problem/content/)



```cpp
```

[252.](https://www.acwing.com/problem/content/)



```cpp
```

[253.](https://www.acwing.com/problem/content/)



```cpp
```

[254.](https://www.acwing.com/problem/content/)



```cpp
```

[255.](https://www.acwing.com/problem/content/)



```cpp
```

[256.](https://www.acwing.com/problem/content/)



```cpp
```

[257.](https://www.acwing.com/problem/content/)



```cpp
```

[258.](https://www.acwing.com/problem/content/)



```cpp
```

[259.](https://www.acwing.com/problem/content/)



```cpp
```

[260.](https://www.acwing.com/problem/content/)



```cpp
```

[261.](https://www.acwing.com/problem/content/)



```cpp
```

[262.](https://www.acwing.com/problem/content/)



```cpp
```

[263.](https://www.acwing.com/problem/content/)



```cpp
```

[264.](https://www.acwing.com/problem/content/)



```cpp
```

[265.](https://www.acwing.com/problem/content/)



```cpp
```

[266.](https://www.acwing.com/problem/content/)



```cpp
```

[267.](https://www.acwing.com/problem/content/)



```cpp
```

[268.](https://www.acwing.com/problem/content/)



```cpp
```

[269.](https://www.acwing.com/problem/content/)



```cpp
```

[270.](https://www.acwing.com/problem/content/)



```cpp
```

[271.](https://www.acwing.com/problem/content/)



```cpp
```

[272.](https://www.acwing.com/problem/content/)



```cpp
```

[273.](https://www.acwing.com/problem/content/)



```cpp
```

[274.](https://www.acwing.com/problem/content/)



```cpp
```

[275.](https://www.acwing.com/problem/content/)



```cpp
```

[276.](https://www.acwing.com/problem/content/)



```cpp
```

[277.](https://www.acwing.com/problem/content/)



```cpp
```

[278.](https://www.acwing.com/problem/content/)



```cpp
```

[279.](https://www.acwing.com/problem/content/)



```cpp
```

[280.](https://www.acwing.com/problem/content/)



```cpp
```

[281.](https://www.acwing.com/problem/content/)



```cpp
```

[282.](https://www.acwing.com/problem/content/)



```cpp
```

[283.](https://www.acwing.com/problem/content/)



```cpp
```

[284.](https://www.acwing.com/problem/content/)



```cpp
```

[285.](https://www.acwing.com/problem/content/)



```cpp
```

[286.](https://www.acwing.com/problem/content/)



```cpp
```

[287.](https://www.acwing.com/problem/content/)



```cpp
```

[288.](https://www.acwing.com/problem/content/)



```cpp
```

[289.](https://www.acwing.com/problem/content/)



```cpp
```

[290.](https://www.acwing.com/problem/content/)



```cpp
```

[291.](https://www.acwing.com/problem/content/)



```cpp
```

[292.](https://www.acwing.com/problem/content/)



```cpp
```

[293.](https://www.acwing.com/problem/content/)



```cpp
```

[294.](https://www.acwing.com/problem/content/)



```cpp
```

[295.](https://www.acwing.com/problem/content/)



```cpp
```

[296.](https://www.acwing.com/problem/content/)



```cpp
```

[297.](https://www.acwing.com/problem/content/)



```cpp
```

[298.](https://www.acwing.com/problem/content/)



```cpp
```

[299.](https://www.acwing.com/problem/content/)



```cpp
```

[300.](https://www.acwing.com/problem/content/)



```cpp
```

#### 301~400

[301.](https://www.acwing.com/problem/content/)



```cpp
```

[302.](https://www.acwing.com/problem/content/)



```cpp
```

[303.](https://www.acwing.com/problem/content/)



```cpp
```

[304.](https://www.acwing.com/problem/content/)



```cpp
```

[305.](https://www.acwing.com/problem/content/)



```cpp
```

[306.](https://www.acwing.com/problem/content/)



```cpp
```

[307.](https://www.acwing.com/problem/content/)



```cpp
```

[308.](https://www.acwing.com/problem/content/)



```cpp
```

[309.](https://www.acwing.com/problem/content/)



```cpp
```

[310.](https://www.acwing.com/problem/content/)



```cpp
```

[311.](https://www.acwing.com/problem/content/)



```cpp
```

[312.](https://www.acwing.com/problem/content/)



```cpp
```

[313.](https://www.acwing.com/problem/content/)



```cpp
```

[314.](https://www.acwing.com/problem/content/)



```cpp
```

[315.](https://www.acwing.com/problem/content/)



```cpp
```

[316.](https://www.acwing.com/problem/content/)



```cpp
```

[317.](https://www.acwing.com/problem/content/)



```cpp
```

[318.](https://www.acwing.com/problem/content/)



```cpp
```

[319.](https://www.acwing.com/problem/content/)



```cpp
```

[320.](https://www.acwing.com/problem/content/)



```cpp
```

[321.](https://www.acwing.com/problem/content/)



```cpp
```

[322.](https://www.acwing.com/problem/content/)



```cpp
```

[323.](https://www.acwing.com/problem/content/)



```cpp
```

[324.](https://www.acwing.com/problem/content/)



```cpp
```

[325.](https://www.acwing.com/problem/content/)



```cpp
```

[326.](https://www.acwing.com/problem/content/)



```cpp
```

[327.](https://www.acwing.com/problem/content/)



```cpp
```

[328.](https://www.acwing.com/problem/content/)



```cpp
```

[329.](https://www.acwing.com/problem/content/)



```cpp
```

[330.](https://www.acwing.com/problem/content/)



```cpp
```

[331.](https://www.acwing.com/problem/content/)



```cpp
```

[332.](https://www.acwing.com/problem/content/)



```cpp
```

[333.](https://www.acwing.com/problem/content/)



```cpp
```

[334.](https://www.acwing.com/problem/content/)



```cpp
```

[335.](https://www.acwing.com/problem/content/)



```cpp
```

[336.](https://www.acwing.com/problem/content/)



```cpp
```

[337.](https://www.acwing.com/problem/content/)



```cpp
```

[338.](https://www.acwing.com/problem/content/)



```cpp
```

[339.](https://www.acwing.com/problem/content/)



```cpp
```

[340.](https://www.acwing.com/problem/content/)



```cpp
```

[341.](https://www.acwing.com/problem/content/)



```cpp
```

[342.](https://www.acwing.com/problem/content/)



```cpp
```

[343.](https://www.acwing.com/problem/content/)



```cpp
```

[344.](https://www.acwing.com/problem/content/)



```cpp
```

[345.](https://www.acwing.com/problem/content/)



```cpp
```

[346.](https://www.acwing.com/problem/content/)



```cpp
```

[347.](https://www.acwing.com/problem/content/)



```cpp
```

[348.](https://www.acwing.com/problem/content/)



```cpp
```

[349.](https://www.acwing.com/problem/content/)



```cpp
```

[350.](https://www.acwing.com/problem/content/)



```cpp
```

[351.](https://www.acwing.com/problem/content/)



```cpp
```

[352.](https://www.acwing.com/problem/content/)



```cpp
```

[353.](https://www.acwing.com/problem/content/)



```cpp
```

[354.](https://www.acwing.com/problem/content/)



```cpp
```

[355.](https://www.acwing.com/problem/content/)



```cpp
```

[356.](https://www.acwing.com/problem/content/)



```cpp
```

[357.](https://www.acwing.com/problem/content/)



```cpp
```

[358.](https://www.acwing.com/problem/content/)



```cpp
```

[359.](https://www.acwing.com/problem/content/)



```cpp
```

[360.](https://www.acwing.com/problem/content/)



```cpp
```

[361.](https://www.acwing.com/problem/content/)



```cpp
```

[362.](https://www.acwing.com/problem/content/)



```cpp
```

[363.](https://www.acwing.com/problem/content/)



```cpp
```

[364.](https://www.acwing.com/problem/content/)



```cpp
```

[365.](https://www.acwing.com/problem/content/)



```cpp
```

[366.](https://www.acwing.com/problem/content/)



```cpp
```

[367.](https://www.acwing.com/problem/content/)



```cpp
```

[368.](https://www.acwing.com/problem/content/)



```cpp
```

[369.](https://www.acwing.com/problem/content/)



```cpp
```

[370.](https://www.acwing.com/problem/content/)



```cpp
```

[371.](https://www.acwing.com/problem/content/)



```cpp
```

[372.](https://www.acwing.com/problem/content/)



```cpp
```

[373.](https://www.acwing.com/problem/content/)



```cpp
```

[374.](https://www.acwing.com/problem/content/)



```cpp
```

[375.](https://www.acwing.com/problem/content/)



```cpp
```

[376.](https://www.acwing.com/problem/content/)



```cpp
```

[377.](https://www.acwing.com/problem/content/)



```cpp
```

[378.](https://www.acwing.com/problem/content/)



```cpp
```

[379.](https://www.acwing.com/problem/content/)



```cpp
```

[380.](https://www.acwing.com/problem/content/)



```cpp
```

[381.](https://www.acwing.com/problem/content/)



```cpp
```

[382.](https://www.acwing.com/problem/content/)



```cpp
```

[383.](https://www.acwing.com/problem/content/)



```cpp
```

[384.](https://www.acwing.com/problem/content/)



```cpp
```

[385.](https://www.acwing.com/problem/content/)



```cpp
```

[386.](https://www.acwing.com/problem/content/)



```cpp
```

[387.](https://www.acwing.com/problem/content/)



```cpp
```

[388.](https://www.acwing.com/problem/content/)



```cpp
```

[389.](https://www.acwing.com/problem/content/)



```cpp
```

[390.](https://www.acwing.com/problem/content/)



```cpp
```

[391.](https://www.acwing.com/problem/content/)



```cpp
```

[392.](https://www.acwing.com/problem/content/)



```cpp
```

[393.](https://www.acwing.com/problem/content/)



```cpp
```

[394.](https://www.acwing.com/problem/content/)



```cpp
```

[395.](https://www.acwing.com/problem/content/)



```cpp
```

[396.](https://www.acwing.com/problem/content/)



```cpp
```

[397.](https://www.acwing.com/problem/content/)



```cpp
```

[398.](https://www.acwing.com/problem/content/)



```cpp
```

[399.](https://www.acwing.com/problem/content/)



```cpp
```

[400.](https://www.acwing.com/problem/content/)



```cpp
```

#### 401~500

[401.](https://www.acwing.com/problem/content/)



```cpp
```

[402.](https://www.acwing.com/problem/content/)



```cpp
```

[403.](https://www.acwing.com/problem/content/)



```cpp
```

[404.](https://www.acwing.com/problem/content/)



```cpp
```

[405.](https://www.acwing.com/problem/content/)



```cpp
```

[406.](https://www.acwing.com/problem/content/)



```cpp
```

[407.](https://www.acwing.com/problem/content/)



```cpp
```

[408.](https://www.acwing.com/problem/content/)



```cpp
```

[409.](https://www.acwing.com/problem/content/)



```cpp
```

[410.](https://www.acwing.com/problem/content/)



```cpp
```

[411.](https://www.acwing.com/problem/content/)



```cpp
```

[412.](https://www.acwing.com/problem/content/)



```cpp
```

[413.](https://www.acwing.com/problem/content/)



```cpp
```

[414.](https://www.acwing.com/problem/content/)



```cpp
```

[415.](https://www.acwing.com/problem/content/)



```cpp
```

[416.](https://www.acwing.com/problem/content/)



```cpp
```

[417.](https://www.acwing.com/problem/content/)



```cpp
```

[418.](https://www.acwing.com/problem/content/)



```cpp
```

[419.](https://www.acwing.com/problem/content/)



```cpp
```

[420.](https://www.acwing.com/problem/content/)



```cpp
```

[421.](https://www.acwing.com/problem/content/)



```cpp
```

[422.](https://www.acwing.com/problem/content/)



```cpp
```

[423.](https://www.acwing.com/problem/content/)



```cpp
```

[424.](https://www.acwing.com/problem/content/)



```cpp
```

[425.](https://www.acwing.com/problem/content/)



```cpp
```

[426.](https://www.acwing.com/problem/content/)



```cpp
```

[427.](https://www.acwing.com/problem/content/)



```cpp
```

[428.](https://www.acwing.com/problem/content/)



```cpp
```

[429.](https://www.acwing.com/problem/content/)



```cpp
```

[430.](https://www.acwing.com/problem/content/)



```cpp
```

[431.](https://www.acwing.com/problem/content/)



```cpp
```

[432.](https://www.acwing.com/problem/content/)



```cpp
```

[433.](https://www.acwing.com/problem/content/)



```cpp
```

[434.](https://www.acwing.com/problem/content/)



```cpp
```

[435.](https://www.acwing.com/problem/content/)



```cpp
```

[436.](https://www.acwing.com/problem/content/)



```cpp
```

[437.](https://www.acwing.com/problem/content/)



```cpp
```

[438.](https://www.acwing.com/problem/content/)



```cpp
```

[439.](https://www.acwing.com/problem/content/)



```cpp
```

[440.](https://www.acwing.com/problem/content/)



```cpp
```

[441.](https://www.acwing.com/problem/content/)



```cpp
```

[442.](https://www.acwing.com/problem/content/)



```cpp
```

[443.](https://www.acwing.com/problem/content/)



```cpp
```

[444.](https://www.acwing.com/problem/content/)



```cpp
```

[445.](https://www.acwing.com/problem/content/)



```cpp
```

[446.](https://www.acwing.com/problem/content/)



```cpp
```

[447.](https://www.acwing.com/problem/content/)



```cpp
```

[448.](https://www.acwing.com/problem/content/)



```cpp
```

[449.](https://www.acwing.com/problem/content/)



```cpp
```

[450.](https://www.acwing.com/problem/content/)



```cpp
```

[451.](https://www.acwing.com/problem/content/)



```cpp
```

[452.](https://www.acwing.com/problem/content/)



```cpp
```

[453.](https://www.acwing.com/problem/content/)



```cpp
```

[454.](https://www.acwing.com/problem/content/)



```cpp
```

[455.](https://www.acwing.com/problem/content/)



```cpp
```

[456.](https://www.acwing.com/problem/content/)



```cpp
```

[457.](https://www.acwing.com/problem/content/)



```cpp
```

[458.](https://www.acwing.com/problem/content/)



```cpp
```

[459.](https://www.acwing.com/problem/content/)



```cpp
```

[460.](https://www.acwing.com/problem/content/)



```cpp
```

[461.](https://www.acwing.com/problem/content/)



```cpp
```

[462.](https://www.acwing.com/problem/content/)



```cpp
```

[463.](https://www.acwing.com/problem/content/)



```cpp
```

[464.](https://www.acwing.com/problem/content/)



```cpp
```

[465.](https://www.acwing.com/problem/content/)



```cpp
```

[466.](https://www.acwing.com/problem/content/)



```cpp
```

[467.](https://www.acwing.com/problem/content/)



```cpp
```

[468.](https://www.acwing.com/problem/content/)



```cpp
```

[469.](https://www.acwing.com/problem/content/)



```cpp
```

[470.](https://www.acwing.com/problem/content/)



```cpp
```

[471.](https://www.acwing.com/problem/content/)



```cpp
```

[472.](https://www.acwing.com/problem/content/)



```cpp
```

[473.](https://www.acwing.com/problem/content/)



```cpp
```

[474.](https://www.acwing.com/problem/content/)



```cpp
```

[475.](https://www.acwing.com/problem/content/)



```cpp
```

[476.](https://www.acwing.com/problem/content/)



```cpp
```

[477.](https://www.acwing.com/problem/content/)



```cpp
```

[478.](https://www.acwing.com/problem/content/)



```cpp
```

[479.](https://www.acwing.com/problem/content/)



```cpp
```

[480.](https://www.acwing.com/problem/content/)



```cpp
```

[481.](https://www.acwing.com/problem/content/)



```cpp
```

[482.](https://www.acwing.com/problem/content/)



```cpp
```

[483.](https://www.acwing.com/problem/content/)



```cpp
```

[484.](https://www.acwing.com/problem/content/)



```cpp
```

[485.](https://www.acwing.com/problem/content/)



```cpp
```

[486.](https://www.acwing.com/problem/content/)



```cpp
```

[487.](https://www.acwing.com/problem/content/)



```cpp
```

[488.](https://www.acwing.com/problem/content/)



```cpp
```

[489.](https://www.acwing.com/problem/content/)



```cpp
```

[490.](https://www.acwing.com/problem/content/)



```cpp
```

[491.](https://www.acwing.com/problem/content/)



```cpp
```

[492.](https://www.acwing.com/problem/content/)



```cpp
```

[493.](https://www.acwing.com/problem/content/)



```cpp
```

[494.](https://www.acwing.com/problem/content/)



```cpp
```

[495.](https://www.acwing.com/problem/content/)



```cpp
```

[496.](https://www.acwing.com/problem/content/)



```cpp
```

[497.](https://www.acwing.com/problem/content/)



```cpp
```

[498.](https://www.acwing.com/problem/content/)



```cpp
```

[499.](https://www.acwing.com/problem/content/)



```cpp
```

[500.](https://www.acwing.com/problem/content/)



```cpp
```

### 501~1000

#### 501~600

[501.](https://www.acwing.com/problem/content/)



```cpp
```

[502.](https://www.acwing.com/problem/content/)



```cpp
```

[503.](https://www.acwing.com/problem/content/)



```cpp
```

[504.](https://www.acwing.com/problem/content/)



```cpp
```

[505.](https://www.acwing.com/problem/content/)



```cpp
```

[506.](https://www.acwing.com/problem/content/)



```cpp
```

[507.](https://www.acwing.com/problem/content/)



```cpp
```

[508.](https://www.acwing.com/problem/content/)



```cpp
```

[509.](https://www.acwing.com/problem/content/)



```cpp
```

[510.](https://www.acwing.com/problem/content/)



```cpp
```

[511.](https://www.acwing.com/problem/content/)



```cpp
```

[512.](https://www.acwing.com/problem/content/)



```cpp
```

[513.](https://www.acwing.com/problem/content/)



```cpp
```

[514.](https://www.acwing.com/problem/content/)



```cpp
```

[515.](https://www.acwing.com/problem/content/)



```cpp
```

[516.](https://www.acwing.com/problem/content/)



```cpp
```

[517.](https://www.acwing.com/problem/content/)



```cpp
```

[518.](https://www.acwing.com/problem/content/)



```cpp
```

[519.](https://www.acwing.com/problem/content/)



```cpp
```

[520.](https://www.acwing.com/problem/content/)



```cpp
```

[521.](https://www.acwing.com/problem/content/)



```cpp
```

[522.](https://www.acwing.com/problem/content/)



```cpp
```

[523.](https://www.acwing.com/problem/content/)



```cpp
```

[524.](https://www.acwing.com/problem/content/)



```cpp
```

[525.](https://www.acwing.com/problem/content/)



```cpp
```

[526.](https://www.acwing.com/problem/content/)



```cpp
```

[527.](https://www.acwing.com/problem/content/)



```cpp
```

[528.](https://www.acwing.com/problem/content/)



```cpp
```

[529.](https://www.acwing.com/problem/content/)



```cpp
```

[530.](https://www.acwing.com/problem/content/)



```cpp
```

[531.](https://www.acwing.com/problem/content/)



```cpp
```

[532.](https://www.acwing.com/problem/content/)



```cpp
```

[533.](https://www.acwing.com/problem/content/)



```cpp
```

[534.](https://www.acwing.com/problem/content/)



```cpp
```

[535.](https://www.acwing.com/problem/content/)



```cpp
```

[536.](https://www.acwing.com/problem/content/)



```cpp
```

[537.](https://www.acwing.com/problem/content/)



```cpp
```

[538.](https://www.acwing.com/problem/content/)



```cpp
```

[539.](https://www.acwing.com/problem/content/)



```cpp
```

[540.](https://www.acwing.com/problem/content/)



```cpp
```

[541.](https://www.acwing.com/problem/content/)



```cpp
```

[542.](https://www.acwing.com/problem/content/)



```cpp
```

[543.](https://www.acwing.com/problem/content/)



```cpp
```

[544.](https://www.acwing.com/problem/content/)



```cpp
```

[545.](https://www.acwing.com/problem/content/)



```cpp
```

[546.](https://www.acwing.com/problem/content/)



```cpp
```

[547.](https://www.acwing.com/problem/content/)



```cpp
```

[548.](https://www.acwing.com/problem/content/)



```cpp
```

[549.](https://www.acwing.com/problem/content/)



```cpp
```

[550.](https://www.acwing.com/problem/content/)



```cpp
```

[551.](https://www.acwing.com/problem/content/)



```cpp
```

[552.](https://www.acwing.com/problem/content/)



```cpp
```

[553.](https://www.acwing.com/problem/content/)



```cpp
```

[554.](https://www.acwing.com/problem/content/)



```cpp
```

[555.](https://www.acwing.com/problem/content/)



```cpp
```

[556.](https://www.acwing.com/problem/content/)



```cpp
```

[557.](https://www.acwing.com/problem/content/)



```cpp
```

[558.](https://www.acwing.com/problem/content/)



```cpp
```

[559.](https://www.acwing.com/problem/content/)



```cpp
```

[560.](https://www.acwing.com/problem/content/)



```cpp
```

[561.](https://www.acwing.com/problem/content/)



```cpp
```

[562.](https://www.acwing.com/problem/content/)



```cpp
```

[563.](https://www.acwing.com/problem/content/)



```cpp
```

[564.](https://www.acwing.com/problem/content/)



```cpp
```

[565.](https://www.acwing.com/problem/content/)



```cpp
```

[566.](https://www.acwing.com/problem/content/)



```cpp
```

[567.](https://www.acwing.com/problem/content/)



```cpp
```

[568.](https://www.acwing.com/problem/content/)



```cpp
```

[569.](https://www.acwing.com/problem/content/)



```cpp
```

[570.](https://www.acwing.com/problem/content/)



```cpp
```

[571.](https://www.acwing.com/problem/content/)



```cpp
```

[572.](https://www.acwing.com/problem/content/)



```cpp
```

[573.](https://www.acwing.com/problem/content/)



```cpp
```

[574.](https://www.acwing.com/problem/content/)



```cpp
```

[575.](https://www.acwing.com/problem/content/)



```cpp
```

[576.](https://www.acwing.com/problem/content/)



```cpp
```

[577.](https://www.acwing.com/problem/content/)



```cpp
```

[578.](https://www.acwing.com/problem/content/)



```cpp
```

[579.](https://www.acwing.com/problem/content/)



```cpp
```

[580.](https://www.acwing.com/problem/content/)



```cpp
```

[581.](https://www.acwing.com/problem/content/)



```cpp
```

[582.](https://www.acwing.com/problem/content/)



```cpp
```

[583.](https://www.acwing.com/problem/content/)



```cpp
```

[584.](https://www.acwing.com/problem/content/)



```cpp
```

[585.](https://www.acwing.com/problem/content/)



```cpp
```

[586.](https://www.acwing.com/problem/content/)



```cpp
```

[587.](https://www.acwing.com/problem/content/)



```cpp
```

[588.](https://www.acwing.com/problem/content/)



```cpp
```

[589.](https://www.acwing.com/problem/content/)



```cpp
```

[590.](https://www.acwing.com/problem/content/)



```cpp
```

[591.](https://www.acwing.com/problem/content/)



```cpp
```

[592.](https://www.acwing.com/problem/content/)



```cpp
```

[593.](https://www.acwing.com/problem/content/)



```cpp
```

[594.](https://www.acwing.com/problem/content/)



```cpp
```

[595.](https://www.acwing.com/problem/content/)



```cpp
```

[596.](https://www.acwing.com/problem/content/)



```cpp
```

[597.](https://www.acwing.com/problem/content/)



```cpp
```

[598.](https://www.acwing.com/problem/content/)



```cpp
```

[599.](https://www.acwing.com/problem/content/)



```cpp
```

[600.](https://www.acwing.com/problem/content/)



```cpp
```

#### 601~700

[601.](https://www.acwing.com/problem/content/)



```cpp
```

[602.](https://www.acwing.com/problem/content/)



```cpp
```

[603.](https://www.acwing.com/problem/content/)



```cpp
```

[604.](https://www.acwing.com/problem/content/)



```cpp
```

[605.](https://www.acwing.com/problem/content/)



```cpp
```

[606.](https://www.acwing.com/problem/content/)



```cpp
```

[607.](https://www.acwing.com/problem/content/)



```cpp
```

[608.](https://www.acwing.com/problem/content/)



```cpp
```

[609.](https://www.acwing.com/problem/content/)



```cpp
```

[610.](https://www.acwing.com/problem/content/)



```cpp
```

[611.](https://www.acwing.com/problem/content/)



```cpp
```

[612.](https://www.acwing.com/problem/content/)



```cpp
```

[613.](https://www.acwing.com/problem/content/)



```cpp
```

[614.](https://www.acwing.com/problem/content/)



```cpp
```

[615.](https://www.acwing.com/problem/content/)



```cpp
```

[616.](https://www.acwing.com/problem/content/)



```cpp
```

[617.](https://www.acwing.com/problem/content/)



```cpp
```

[618.](https://www.acwing.com/problem/content/)



```cpp
```

[619.](https://www.acwing.com/problem/content/)



```cpp
```

[620.](https://www.acwing.com/problem/content/)



```cpp
```

[621.](https://www.acwing.com/problem/content/)



```cpp
```

[622.](https://www.acwing.com/problem/content/)



```cpp
```

[623.](https://www.acwing.com/problem/content/)



```cpp
```

[624.](https://www.acwing.com/problem/content/)



```cpp
```

[625.](https://www.acwing.com/problem/content/)



```cpp
```

[626.](https://www.acwing.com/problem/content/)



```cpp
```

[627.](https://www.acwing.com/problem/content/)



```cpp
```

[628.](https://www.acwing.com/problem/content/)



```cpp
```

[629.](https://www.acwing.com/problem/content/)



```cpp
```

[630.](https://www.acwing.com/problem/content/)



```cpp
```

[631.](https://www.acwing.com/problem/content/)



```cpp
```

[632.](https://www.acwing.com/problem/content/)



```cpp
```

[633.](https://www.acwing.com/problem/content/)



```cpp
```

[634.](https://www.acwing.com/problem/content/)



```cpp
```

[635.](https://www.acwing.com/problem/content/)



```cpp
```

[636.](https://www.acwing.com/problem/content/)



```cpp
```

[637.](https://www.acwing.com/problem/content/)



```cpp
```

[638.](https://www.acwing.com/problem/content/)



```cpp
```

[639.](https://www.acwing.com/problem/content/)



```cpp
```

[640.](https://www.acwing.com/problem/content/)



```cpp
```

[641.](https://www.acwing.com/problem/content/)



```cpp
```

[642.](https://www.acwing.com/problem/content/)



```cpp
```

[643.](https://www.acwing.com/problem/content/)



```cpp
```

[644.](https://www.acwing.com/problem/content/)



```cpp
```

[645.](https://www.acwing.com/problem/content/)



```cpp
```

[646.](https://www.acwing.com/problem/content/)



```cpp
```

[647.](https://www.acwing.com/problem/content/)



```cpp
```

[648.](https://www.acwing.com/problem/content/)



```cpp
```

[649.](https://www.acwing.com/problem/content/)



```cpp
```

[650.](https://www.acwing.com/problem/content/)



```cpp
```

[651.](https://www.acwing.com/problem/content/)



```cpp
```

[652.](https://www.acwing.com/problem/content/)



```cpp
```

[653.](https://www.acwing.com/problem/content/)



```cpp
```

[654.](https://www.acwing.com/problem/content/)



```cpp
```

[655.](https://www.acwing.com/problem/content/)



```cpp
```

[656.](https://www.acwing.com/problem/content/)



```cpp
```

[657.](https://www.acwing.com/problem/content/)



```cpp
```

[658.](https://www.acwing.com/problem/content/)



```cpp
```

[659.](https://www.acwing.com/problem/content/)



```cpp
```

[660.](https://www.acwing.com/problem/content/)



```cpp
```

[661.](https://www.acwing.com/problem/content/)



```cpp
```

[662.](https://www.acwing.com/problem/content/)



```cpp
```

[663.](https://www.acwing.com/problem/content/)



```cpp
```

[664.](https://www.acwing.com/problem/content/)



```cpp
```

[665.](https://www.acwing.com/problem/content/)



```cpp
```

[666.](https://www.acwing.com/problem/content/)



```cpp
```

[667.](https://www.acwing.com/problem/content/)



```cpp
```

[668.](https://www.acwing.com/problem/content/)



```cpp
```

[669.](https://www.acwing.com/problem/content/)



```cpp
```

[670.](https://www.acwing.com/problem/content/)



```cpp
```

[671.](https://www.acwing.com/problem/content/)



```cpp
```

[672.](https://www.acwing.com/problem/content/)



```cpp
```

[673.](https://www.acwing.com/problem/content/)



```cpp
```

[674.](https://www.acwing.com/problem/content/)



```cpp
```

[675.](https://www.acwing.com/problem/content/)



```cpp
```

[676.](https://www.acwing.com/problem/content/)



```cpp
```

[677.](https://www.acwing.com/problem/content/)



```cpp
```

[678.](https://www.acwing.com/problem/content/)



```cpp
```

[679.](https://www.acwing.com/problem/content/)



```cpp
```

[680.](https://www.acwing.com/problem/content/)



```cpp
```

[681.](https://www.acwing.com/problem/content/)



```cpp
```

[682.](https://www.acwing.com/problem/content/)



```cpp
```

[683.](https://www.acwing.com/problem/content/)



```cpp
```

[684.](https://www.acwing.com/problem/content/)



```cpp
```

[685.](https://www.acwing.com/problem/content/)



```cpp
```

[686.](https://www.acwing.com/problem/content/)



```cpp
```

[687.](https://www.acwing.com/problem/content/)



```cpp
```

[688.](https://www.acwing.com/problem/content/)



```cpp
```

[689.](https://www.acwing.com/problem/content/)



```cpp
```

[690.](https://www.acwing.com/problem/content/)



```cpp
```

[691.](https://www.acwing.com/problem/content/)



```cpp
```

[692.](https://www.acwing.com/problem/content/)



```cpp
```

[693.](https://www.acwing.com/problem/content/)



```cpp
```

[694.](https://www.acwing.com/problem/content/)



```cpp
```

[695.](https://www.acwing.com/problem/content/)



```cpp
```

[696.](https://www.acwing.com/problem/content/)



```cpp
```

[697.](https://www.acwing.com/problem/content/)



```cpp
```

[698.](https://www.acwing.com/problem/content/)



```cpp
```

[699.](https://www.acwing.com/problem/content/)



```cpp
```

[700.](https://www.acwing.com/problem/content/)



```cpp
```

#### 701~800

[701.](https://www.acwing.com/problem/content/)



```cpp
```

[702.](https://www.acwing.com/problem/content/)



```cpp
```

[703.](https://www.acwing.com/problem/content/)



```cpp
```

[704.](https://www.acwing.com/problem/content/)



```cpp
```

[705.](https://www.acwing.com/problem/content/)



```cpp
```

[706.](https://www.acwing.com/problem/content/)



```cpp
```

[707.](https://www.acwing.com/problem/content/)



```cpp
```

[708.](https://www.acwing.com/problem/content/)



```cpp
```

[709.](https://www.acwing.com/problem/content/)



```cpp
```

[710.](https://www.acwing.com/problem/content/)



```cpp
```

[711.](https://www.acwing.com/problem/content/)



```cpp
```

[712.](https://www.acwing.com/problem/content/)



```cpp
```

[713.](https://www.acwing.com/problem/content/)



```cpp
```

[714.](https://www.acwing.com/problem/content/)



```cpp
```

[715.](https://www.acwing.com/problem/content/)



```cpp
```

[716.](https://www.acwing.com/problem/content/)



```cpp
```

[717.](https://www.acwing.com/problem/content/)



```cpp
```

[718.](https://www.acwing.com/problem/content/)



```cpp
```

[719.](https://www.acwing.com/problem/content/)



```cpp
```

[720.](https://www.acwing.com/problem/content/)



```cpp
```

[721.](https://www.acwing.com/problem/content/)



```cpp
```

[722.](https://www.acwing.com/problem/content/)



```cpp
```

[723.](https://www.acwing.com/problem/content/)



```cpp
```

[724.](https://www.acwing.com/problem/content/)



```cpp
```

[725.](https://www.acwing.com/problem/content/)



```cpp
```

[726.](https://www.acwing.com/problem/content/)



```cpp
```

[727.](https://www.acwing.com/problem/content/)



```cpp
```

[728.](https://www.acwing.com/problem/content/)



```cpp
```

[729.](https://www.acwing.com/problem/content/)



```cpp
```

[730.](https://www.acwing.com/problem/content/)



```cpp
```

[731.](https://www.acwing.com/problem/content/)



```cpp
```

[732.](https://www.acwing.com/problem/content/)



```cpp
```

[733.](https://www.acwing.com/problem/content/)



```cpp
```

[734.](https://www.acwing.com/problem/content/)



```cpp
```

[735.](https://www.acwing.com/problem/content/)



```cpp
```

[736.](https://www.acwing.com/problem/content/)



```cpp
```

[737.](https://www.acwing.com/problem/content/)



```cpp
```

[738.](https://www.acwing.com/problem/content/)



```cpp
```

[739.](https://www.acwing.com/problem/content/)



```cpp
```

[740.](https://www.acwing.com/problem/content/)



```cpp
```

[741.](https://www.acwing.com/problem/content/)



```cpp
```

[742.](https://www.acwing.com/problem/content/)



```cpp
```

[743.](https://www.acwing.com/problem/content/)



```cpp
```

[744.](https://www.acwing.com/problem/content/)



```cpp
```

[745.](https://www.acwing.com/problem/content/)



```cpp
```

[746.](https://www.acwing.com/problem/content/)



```cpp
```

[747.](https://www.acwing.com/problem/content/)



```cpp
```

[748.](https://www.acwing.com/problem/content/)



```cpp
```

[749.](https://www.acwing.com/problem/content/)



```cpp
```

[750.](https://www.acwing.com/problem/content/)



```cpp
```

[751.](https://www.acwing.com/problem/content/)



```cpp
```

[752.](https://www.acwing.com/problem/content/)



```cpp
```

[753.](https://www.acwing.com/problem/content/)



```cpp
```

[754.](https://www.acwing.com/problem/content/)



```cpp
```

[755.](https://www.acwing.com/problem/content/)



```cpp
```

[756.](https://www.acwing.com/problem/content/)



```cpp
```

[757.](https://www.acwing.com/problem/content/)



```cpp
```

[758.](https://www.acwing.com/problem/content/)



```cpp
```

[759.](https://www.acwing.com/problem/content/)



```cpp
```

[760.](https://www.acwing.com/problem/content/)



```cpp
```

[761.](https://www.acwing.com/problem/content/)



```cpp
```

[762.](https://www.acwing.com/problem/content/)



```cpp
```

[763.](https://www.acwing.com/problem/content/)



```cpp
```

[764.](https://www.acwing.com/problem/content/)



```cpp
```

[765.](https://www.acwing.com/problem/content/)



```cpp
```

[766.](https://www.acwing.com/problem/content/)



```cpp
```

[767.](https://www.acwing.com/problem/content/)



```cpp
```

[768.](https://www.acwing.com/problem/content/)



```cpp
```

[769.](https://www.acwing.com/problem/content/)



```cpp
```

[770.](https://www.acwing.com/problem/content/)



```cpp
```

[771.](https://www.acwing.com/problem/content/)



```cpp
```

[772.](https://www.acwing.com/problem/content/)



```cpp
```

[773.](https://www.acwing.com/problem/content/)



```cpp
```

[774.](https://www.acwing.com/problem/content/)



```cpp
```

[775.](https://www.acwing.com/problem/content/)



```cpp
```

[776.](https://www.acwing.com/problem/content/)



```cpp
```

[777.](https://www.acwing.com/problem/content/)



```cpp
```

[778.](https://www.acwing.com/problem/content/)



```cpp
```

[779.](https://www.acwing.com/problem/content/)



```cpp
```

[780.](https://www.acwing.com/problem/content/)



```cpp
```

[781.](https://www.acwing.com/problem/content/)



```cpp
```

[782.](https://www.acwing.com/problem/content/)



```cpp
```

[783.](https://www.acwing.com/problem/content/)



```cpp
```

[784.](https://www.acwing.com/problem/content/)



```cpp
```

[785. 快速排序](https://www.acwing.com/problem/content/787/)

```cpp
#include <iostream>

using namespace std;
const int N = 1e6 + 10;
int q[N];

void quicksort(int q[], int l, int r) {
    if (l >= r) return;
    int x = q[l + r >> 1];
    int i = l - 1, j = r + 1;
    while (i < j) {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i<j) swap(q[i],q[j]);
    }
    quicksort(q,l,j);
    quicksort(q,j+1,r);
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &q[i]);
    quicksort(q, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", q[i]);
    return 0;
}
```

[786.](https://www.acwing.com/problem/content/)



```cpp
```

[787. 归并排序](https://www.acwing.com/problem/content/789/)

```cpp
#include <iostream>

using namespace std;
const int N = 1e6 + 10;
int q[N], tmp[N];

void merge_sort(int q[], int l, int r) {
    if (l >= r) return;
    int mid = (l + r) >> 1;
    merge_sort(q,l, mid), merge_sort(q,mid + 1, r);
    int i = l, j = mid + 1, k = 0;
    while (i <= mid && j <= r) {
        if (q[i] <= q[j]) tmp[k++] = q[i++];
        else tmp[k++] = q[j++];
    }
    while (i <= mid) tmp[k++] = q[i++];
    while (j <= r) tmp[k++] = q[j++];
    for(i=l,j=0;i<=r;i++,j++) q[i]= tmp[j];
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d ", &q[i]);
    merge_sort(q, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d", q[i]);
    return 0;
}
```

[788.](https://www.acwing.com/problem/content/)



```cpp
```

[789. 数的范围](https://www.acwing.com/problem/content/791/)

```cpp
#include < iostream >

const int N = 10010;

int n, m;
int q[N];

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &q[i]);
    }
    while (m--) {
        int x;
        scanf("%d", &x);
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + r >> 1;
            if (q[mid] >= x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if (q[l] != x) {
            std::cout << "-1 -1" << std::endl;
        } else {
            std::cout << l << " ";
            int l = 0, r = n - 1;
            while (l < r) {
                int mid = l + r + 1 >> 1;
                if (q[mid] <= x) {
                    l = mid;
                } else {
                    r = mid - 1;
                }
            }
            std::cout << l << std::endl;
        }
    }
    return 0;
}
```

[790. 数的三次方根](https://www.acwing.com/problem/content/792/)

本题需要主要三次方的时候，当数字是0.001之类的小于1的数时，寻找范围需要扩大。

```cpp
#include <iostream>

using namespace std;

int main() {
    double x;
    scanf("%lf", &x);
    if (x < 0) {
        printf("-");
        x = -x;
    }
    double l = 0, r = x, mid;
    if (x<1) r=1;
    while (r - l >= 1e-8) {
        mid = (r + l) / 2;
        if (mid * mid * mid > x) r = mid;
        else l = mid;
    }
    printf("%lf", mid);
    return 0;
}
```

[791. 高精度加法](https://www.acwing.com/problem/content/793/)

这里的选择使用数组存储大整数，这里第0位存个位数，最高位放在数组最后面。这样当发生进位的时候，容易处理。

```cpp
#include <iostream>
#include <vector>

using namespace std;
const int N = 16 + 10;

vector<int> add(vector<int> &A, vector<int> &B) {
    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size() || i < B.size(); i++) {
        if (i < A.size()) t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }
    if (t) C.push_back(t);
    return C;
}

int main() {
    vector<int> A, B;
    string a, b;
    cin >> a >> b;
    for (int i = a.size() - 1; i >= 0; i--) A.push_back(a[i] - '0');
    for (int i = b.size() - 1; i >= 0; --i) B.push_back(b[i] - '0');
    auto c = add(A, B);
    for (int i = c.size() - 1; i >= 0; --i) printf("%d", c[i]);
    return 0;
}
```

[792. 高精度减法](https://www.acwing.com/problem/content/794/)

记得去掉结果中多余的0.

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> sub(vector<int> &A, vector<int> &B) {
    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i++) {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1;
        else t = 0;
    }
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

//A>=B
bool cmp(vector<int> &A, vector<int> &B) {
    if (A.size() != B.size()) return A.size() > B.size();
    else {
        for (int i = A.size() - 1; i >= 0; --i) {
            if (A[i] != B[i]) return A[i] > B[i];
        }
    }
    return true;
}

int main() {
    string a, b;
    cin >> a >> b;
    vector<int> A, B;
    for (int i = a.size() - 1; i >= 0; i--) A.push_back(a[i]-'0');
    for (int i = b.size() - 1; i >= 0; i--) B.push_back(b[i]-'0');
    if (cmp(A, B)) {
        auto C = sub(A, B);
        for (int i = C.size() - 1; i >= 0; i--) printf("%d", C[i]);
    } else {
        auto C = sub(B, A);
        printf("-");
        for (int i = C.size() - 1; i >= 0; i--) printf("%d", C[i]);
    }
    return 0;
}
```

[793. 高精度乘法](https://www.acwing.com/problem/content/795/)

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> mul(vector<int> &A, int B) {
    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size() || t; i++) {
        if (i < A.size()) t += A[i] * B;
        C.push_back(t % 10);
        t /= 10;
    }
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

int main() {
    string a;
    vector<int> A;
    int b;
    cin >> a >> b;
    for (int i = a.size() - 1; i >= 0; --i) A.push_back(a[i] - '0');
    auto C = mul(A, b);
    for (int i = C.size() - 1; i >= 0; i--) printf("%d", C[i]);
    return 0;
}
```

[794. 高精度除法](https://www.acwing.com/problem/content/796/)

除法这里需要注意，运算从高位开始处理。所以需要反过来进行处理。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> div(vector<int> &A, int b, int &r) {
    vector<int> C;
    for (int i = A.size() - 1; i >= 0; i--) {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

int main() {
    string a;
    int b;
    vector<int> A;
    cin >> a >> b;
    for (int i = a.size() - 1; i >= 0; i--) A.push_back(a[i] - '0');
    //r为余数
    int r = 0;
    auto C = div(A, b, r);
    for (int i = C.size() - 1; i >= 0; i--) printf("%d", C[i]);
    printf("\n%d", r);
    return 0;
}
```

[795. 前缀和](https://www.acwing.com/problem/content/797/)

本题使用的是一维前缀和。注意这里的s数组存放前缀和，相减的时候需要将左边界-1。s[0],a[0]处放0，以便后续操作。

```cpp
#include <iostream>

using namespace std;
const int N = 1e6 + 10;
int q[N];
int s[N];

int main() {
    int n, m;
    s[0] = 0;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &q[i]);
        s[i] = s[i - 1] + q[i];
    }
    while (m--) {
        int l, r;
        scanf("%d%d", &l, &r);
        printf("%d\n", s[r] - s[l - 1]);
    }
    return 0;
}
```

[796. 子矩阵的和](https://www.acwing.com/problem/content/798/)

本题依旧是前缀和，不过是二维前缀和，重点就两个公式。此处假设S为前缀和数组，q为相应的差分数组。

更新前缀和数组：$S[x-1,y]+S[x,y-1]-S[x-1,y-1]+q[x,y]$

计算前缀和之差：$S[x_2,y_2]-S[x_1-1,y_2]-S[x_2,y_1-1]+S[x_1-1,y_1-1]$

```cpp
#include <iostream>

using namespace std;
const int N = 1010;
int x[N][N], s[N][N];

int main() {
    int n, m, q;
    scanf("%d%d%d", &n, &m, &q);
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            scanf("%d", &x[i][j]);
            s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + x[i][j];
        }
    }
    int x1, y1, x2, y2;
    while (q--) {
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        printf("%d\n", s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]);
    }
    return 0;
}
```

[797. 差分](https://www.acwing.com/problem/content/799/)

```cpp
#include <iostream>

using namespace std;
const int N = 1e6 + 10;
// q数组为原数组,b数组为差分数组
int q[N], b[N];
void insert(int l,int r,int c){
    b[l]+=c;
    b[r+1]-=c;
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &q[i]);
        //step1 构造差分数组
        insert(i,i,q[i]);
    }
    //step2 更新差分数组信息
    int l,r,c;
    while (m--) {
        scanf("%d%d%d",&l,&r,&c);
        insert(l,r,c);
    }
    //step3 更新前缀和,需要注意这里是在差分数组的基础上进行前缀和的计算，所以都是+=操作
    //此处的b数组成为前缀和数组
    for(int i=1;i<=n;i++) {
        b[i]+=b[i-1];
        printf("%d ",b[i]);
    }
    return 0;
}
```

[798. 差分矩阵](https://www.acwing.com/problem/content/800/)

```cpp
#include <iostream>

using namespace std;
const int N = 1010;
int a[N][N], s[N][N];

//不同于一维差分数组，二维差分数组中[x1,y1]之后的正方形区域都会+c。
//因此需要将[x1,y2+1]和[x2+1,y1]之后的区域-c,还要给[x2+1,y2+1]+c
void insert(int x1, int y1, int x2, int y2, int c) {
    s[x1][y1] += c;
    s[x1][y2 + 1] -= c;
    s[x2 + 1][y1] -= c;
    s[x2 + 1][y2 + 1] += c;
}

int main() {
    int n, m, q;
    scanf("%d%d%d", &n, &m, &q);
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            scanf("%d", &a[i][j]);
            insert(i, j, i, j, a[i][j]);
        }
    }
    int x1, y1, x2, y2, c;
    while (q--) {
        scanf("%d%d%d%d%d", &x1, &y1, &x2, &y2, &c);
        insert(x1, y1, x2, y2, c);
    }
    //需要注意这里是在差分数组的基础上进行前缀和的计算，所以都是+=操作
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1];
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j)
            printf("%d ", s[i][j]);
        printf("\n");
    }
    return 0;

```

[799. 最长连续不重复子序列](https://www.acwing.com/problem/content/801/)

```cpp
#include <iostream>

using namespace std;
const int N = 1e6 + 10;
//数组q记录题目信息，数组s记录下标数字出现的次数
int q[N], s[N];

int main() {
    int n, res = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%d", &q[i]);
    //j在前，i在后
    //当s[q[i]]>1时说明有重复数字，此时，j向后移动至q[i]第一次出现的位置的后一个，此过程中将所有j经过的数字对应的s[q[j]]--
    for (int i = 0, j = 0; i < n; ++i) {
        ++s[q[i]];
        while (s[q[i]] > 1) --s[q[j++]];
        res = i - j + 1 > res ? i - j + 1 : res;
    }
    printf("%d", res);
    return 0;
}
```

[800.](https://www.acwing.com/problem/content/)



```cpp
```

#### 801~900

[801. 二进制中1的个数](https://www.acwing.com/problem/content/803/)

```cpp
#include <iostream>

using namespace std;
int lowbit(int x){
    return x&-x;
}
int main() {
    int n;
    scanf("%d", &n);
    while (n--) {
        int res=0,x;
        scanf("%d",&x);
        while (x){
            x-=lowbit(x);
            ++res;
        }
        printf("%d ",res);
    }
    return 0;
}
```

[802. 区间和](https://www.acwing.com/problem/content/804/)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int N = 3 * 1e5 + 10;
typedef pair<int, int> PAIR;
//存放插入与查询信息
vector<PAIR> add, query;
//存放计算区间和的差分数组和前缀和数组
int a[N], s[N];
//alls存放对应索引信息
vector<int> alls;

//unique的自己实现
vector<int> unique(vector<int> &A){
	int j=0;
	for(int i=0;i<A.size();i++){
        //要么是第一个数要么不重复
		if(!i||A[i]!=A[i-1]) A[j++]=A[i];
	}
    return A.begin()+j;
}

int find(int x) {
    int l = 0, r = alls.size() - 1;
    while (l < r) {
        int mid = l + r >> 1;
        if (alls[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return l;
}

int main() {
    int n, m, index, data, l, r;
    scanf("%d%d", &n, &m);
    //step1 将所有用到的位置索引存入alls容器中,将相应的插入信息与查询信息存入add和query中
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &index, &data);
        add.push_back({index, data});
        alls.push_back(index);
    }
    for (int i = 0; i < m; ++i) {
        scanf("%d%d", &l, &r);
        query.push_back({l, r});
        alls.push_back(l);
        alls.push_back(r);
    }
    //step2 索引位置去重,此时alls下标就是相应索引映射后的位置
    sort(alls.begin(), alls.end());
    alls.erase(unique(alls.begin(), alls.end()), alls.end());
    //step3 插入数据
    for (auto item: add) a[find(item.first)] += item.second;
    //step4 计算前缀和
    for (int i = 1; i <= alls.size(); ++i) s[i] += s[i - 1] + a[i];
    //step5 返回结果
    for (auto item :query) {
        printf("%d\n", s[find(item.second)] - s[find(item.first) - 1]);
    }
    return 0;
}
```

[803. 区间合并](https://www.acwing.com/problem/content/805/)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> PAIR;
vector<PAIR> all;

vector<PAIR> merge(vector<PAIR> &x) {
    vector<PAIR> res;
    sort(x.begin(), x.end());
    int st = -2e9, ed = -2e9;
    for (auto itor:x) {
        if (ed < itor.first) {
            if (st != -2e9)res.push_back({st, ed});
            st = itor.first;
            ed = itor.second;
        } else {
            ed = max(ed, itor.second);
        }

    }
    //将最后一组加入结果集，需要判断st!=-2e9避免传入空数组
    if (st != -2e9) res.push_back({st, ed});
    return res;
}

int main() {
    int n, l, r;
    scanf("%d", &n);
    while (n--) {
        scanf("%d%d", &l, &r);
        all.push_back({l, r});
    }
    printf("%d", merge(all).size());
    return 0;
}
```

[804.](https://www.acwing.com/problem/content/)



```cpp
```

[805.](https://www.acwing.com/problem/content/)



```cpp
```

[806.](https://www.acwing.com/problem/content/)



```cpp
```

[807.](https://www.acwing.com/problem/content/)



```cpp
```

[808.](https://www.acwing.com/problem/content/)



```cpp
```

[809.](https://www.acwing.com/problem/content/)



```cpp
```

[810.](https://www.acwing.com/problem/content/)



```cpp
```

[811.](https://www.acwing.com/problem/content/)



```cpp
```

[812.](https://www.acwing.com/problem/content/)



```cpp
```

[813.](https://www.acwing.com/problem/content/)



```cpp
```

[814.](https://www.acwing.com/problem/content/)



```cpp
```

[815.](https://www.acwing.com/problem/content/)



```cpp
```

[816.](https://www.acwing.com/problem/content/)



```cpp
```

[817.](https://www.acwing.com/problem/content/)



```cpp
```

[818.](https://www.acwing.com/problem/content/)



```cpp
```

[819.](https://www.acwing.com/problem/content/)



```cpp
```

[820.](https://www.acwing.com/problem/content/)



```cpp
```

[821.](https://www.acwing.com/problem/content/)



```cpp
```

[822.](https://www.acwing.com/problem/content/)



```cpp
```

[823.模拟栈](https://www.acwing.com/problem/content/830/)

```cpp
#include <iostream>
#include <cstring>

using namespace std;
const int N = 1e6 + 10;
int stk[N], top = -1;

void push(int x) {
    stk[++top] = x;
}

int pop() {
    return stk[top--];
}

const char *empty() {
    return top == -1 ? "YES" : "NO";
}

int query() {
    return stk[top];
}

int main() {
    int n;
    char op[6];
    scanf("%d", &n);
    while (n--) {
        int x;
        scanf("%s", &op);
        if (!strcmp(op, "push")) {
            scanf("%d", &x);
            push(x);
        }
        if (!strcmp(op, "pop")) pop();
        if (!strcmp(op, "empty")) printf("%s\n", empty());
        if (!strcmp(op, "query")) printf("%d\n", query());
    }
    return 0;
}
```

[824.](https://www.acwing.com/problem/content/)



```cpp
```

[825.](https://www.acwing.com/problem/content/)



```cpp
```

[826.单链表](https://www.acwing.com/problem/content/828/)

本题注意当删除头节点时，需要特判。

```cpp
#include <iostream>

using namespace std;
const int N = 1e6 + 10;
int e[N], ne[N];
int idx = 0, head = -1;

void insertFromHead(int x) {
    e[idx] = x;
    ne[idx] = head;
    head = idx++;
}

void insert(int k, int x) {
    e[idx] = x;
    ne[idx] = ne[k];
    ne[k] = idx++;
}

void pop(int k) {
    ne[k] = ne[ne[k]];
}

int main() {
    int m;
    char method;
    scanf("%d", &m);
    while (m--) {
        getchar();
        scanf("%c", &method);
        if (method == 'H') {
            int x;
            scanf("%d", &x);
            insertFromHead(x);
        }
        if (method == 'D') {
            int k;
            scanf("%d", &k);
            if (!k) head = ne[head];
            else pop(k - 1);
        }
        if (method == 'I') {
            int k, x;
            scanf("%d%d", &k, &x);
            insert(k - 1, x);
        }
    }
    for (int i = head; i != -1; i = ne[i]) printf("%d ", e[i]);
    return 0;
}
```

[827.双链表](https://www.acwing.com/problem/content/description/829/)

```cpp
#include <iostream>
#include <cstring>

using namespace std;
const int N = 1e6 + 10;
int l[N], r[N], e[N];
int idx;

void init() {
    //0代表起始端点，1代表结束端点
    //真实数字从idx==2开始存放
    idx = 2;
    l[1] = 0;
    r[0] = 1;
}

//此函数的逻辑是插入k的右侧节点
//若需要实现插入k的左侧节点只需传入l[k]即可
void add(int k, int v) {
    e[idx] = v;
    l[idx] = k;
    r[idx] = r[k];
    l[r[k]] = idx;
    r[k] = idx;
    ++idx;
}

void remove(int k) {
    r[l[k]] = r[k];
    l[r[k]] = l[k];
}


int main() {
    int n;
    init();
    scanf("%d", &n);
    while (n--) {
        char op[3];
        int x, y;
        scanf("%s", &op);
        if (!strcmp("L", op)) {
            scanf("%d", &x);
            add(0, x);
        }
        if (!strcmp("R", op)) {
            scanf("%d", &x);
            add(l[1], x);
        }
        if (!strcmp("D", op)) {
            scanf("%d", &x);
            remove(x + 1);
        }
        if (!strcmp("IL", op)) {
            scanf("%d%d", &x, &y);
            add(l[x + 1], y);
        }
        if (!strcmp("IR", op)) {
            scanf("%d%d", &x, &y);
            add(x + 1, y);
        }
    }
    for (int i = r[0]; i != 1; i = r[i]) printf("%d ", e[i]);
    return 0;
}
```

[828.](https://www.acwing.com/problem/content/)



```cpp
```

[829.模拟队列](https://www.acwing.com/problem/content/831/)

```cpp
#include <iostream>
#include <cstring>

using namespace std;
const int N = 1e6 + 10;
int e[N], head, tail;

void init() {
    head = 0;
    tail = -1;
}

void push(int x) {
    e[tail++] = x;
}

void pop() {
    ++head;
}

int query() {
    return e[head];
}

const char *empty() {
    return tail > head ? "NO" : "YES";
}

int main() {
    int n;
    scanf("%d", &n);
    char op[6];
    int x;
    while (n--) {
        scanf("%s", &op);
        if (!strcmp(op, "push")) {
            scanf("%d", &x);
            push(x);
        }
        if (!strcmp(op, "pop")) pop();
        if (!strcmp(op, "empty")) printf("%s\n", empty());
        if (!strcmp(op, "query")) printf("%d\n", query());
    }
    return 0;
}
```

[830.单调栈](https://www.acwing.com/problem/content/832/)

本题利用栈的性质

```cpp
#include <iostream>

using namespace std;
const int N = 1e5 + 10;
int stk[N], top = -1;

int main() {
    int n, x;
    scanf("%d", &n);
    while (n--) {
        scanf("%d", &x);
        while (top != -1 && stk[top] >= x) --top;
        if (top != -1) printf("%d ", stk[top]);
        else printf("-1 ");
        //注意，需要将当前数字压入栈中
        stk[++top] = x;
    }
    return 0;
}
```

[831.KMP字符串](https://www.acwing.com/problem/content/description/833/)

```cpp
// KMP算法
// 复杂度为O(m+n)
void build(const char *pattern) {
    int len = strlen(pattern);
    ne.resize(len + 1);
    for (int i = 0, j = ne[0] = -1; i < len; ne[++i] = ++j) {
        while (~j && pattern[j] != pattern[i]) j = ne[j];
    }
}

vector<int> match(const char *text, const char *pattern) {
    vector<int> res;
    int lenp = strlen(pattern), lent = strlen(text);
    build(pattern);
    for (int i = 0, j = 0; i < lent; ++i) {
        while (j > 0 && text[i] != pattern[j]) j = ne[j];
        if (text[i] == pattern[j]) ++j;
        if (j == lenp) res.push_back(i - lenp + 1), j = ne[j];
    }
    return res;
}
```

[832.](https://www.acwing.com/problem/content/)



```cpp
```

[833.](https://www.acwing.com/problem/content/)



```cpp
```

[834.](https://www.acwing.com/problem/content/)



```cpp
```

[835.](https://www.acwing.com/problem/content/)



```cpp
```

[836.](https://www.acwing.com/problem/content/)



```cpp
```

[837.](https://www.acwing.com/problem/content/)



```cpp
```

[838.](https://www.acwing.com/problem/content/)



```cpp
```

[839.](https://www.acwing.com/problem/content/)



```cpp
```

[840.](https://www.acwing.com/problem/content/)



```cpp
```

[841.](https://www.acwing.com/problem/content/)



```cpp
```

[842.](https://www.acwing.com/problem/content/)



```cpp
```

[843.](https://www.acwing.com/problem/content/)



```cpp
```

[844.](https://www.acwing.com/problem/content/)



```cpp
```

[845.](https://www.acwing.com/problem/content/)



```cpp
```

[846.](https://www.acwing.com/problem/content/)



```cpp
```

[847.](https://www.acwing.com/problem/content/)



```cpp
```

[848.](https://www.acwing.com/problem/content/)



```cpp
```

[849.](https://www.acwing.com/problem/content/)



```cpp
```

[850.](https://www.acwing.com/problem/content/)



```cpp
```

[851.](https://www.acwing.com/problem/content/)



```cpp
```

[852.](https://www.acwing.com/problem/content/)



```cpp
```

[853.](https://www.acwing.com/problem/content/)



```cpp
```

[854.](https://www.acwing.com/problem/content/)



```cpp
```

[855.](https://www.acwing.com/problem/content/)



```cpp
```

[856.](https://www.acwing.com/problem/content/)



```cpp
```

[857.](https://www.acwing.com/problem/content/)



```cpp
```

[858.](https://www.acwing.com/problem/content/)



```cpp
```

[859.](https://www.acwing.com/problem/content/)



```cpp
```

[860.](https://www.acwing.com/problem/content/)



```cpp
```

[861.](https://www.acwing.com/problem/content/)



```cpp
```

[862.](https://www.acwing.com/problem/content/)



```cpp
```

[863.](https://www.acwing.com/problem/content/)



```cpp
```

[864.](https://www.acwing.com/problem/content/)



```cpp
```

[865.](https://www.acwing.com/problem/content/)



```cpp
```

[866.](https://www.acwing.com/problem/content/)



```cpp
```

[867.](https://www.acwing.com/problem/content/)



```cpp
```

[868.](https://www.acwing.com/problem/content/)



```cpp
```

[869.](https://www.acwing.com/problem/content/)



```cpp
```

[870.](https://www.acwing.com/problem/content/)



```cpp
```

[871.](https://www.acwing.com/problem/content/)



```cpp
```

[872.](https://www.acwing.com/problem/content/)



```cpp
```

[873.](https://www.acwing.com/problem/content/)



```cpp
```

[874.](https://www.acwing.com/problem/content/)



```cpp
```

[875.](https://www.acwing.com/problem/content/)



```cpp
```

[876.](https://www.acwing.com/problem/content/)



```cpp
```

[877.](https://www.acwing.com/problem/content/)



```cpp
```

[878.](https://www.acwing.com/problem/content/)



```cpp
```

[879.](https://www.acwing.com/problem/content/)



```cpp
```

[880.](https://www.acwing.com/problem/content/)



```cpp
```

[881.](https://www.acwing.com/problem/content/)



```cpp
```

[882.](https://www.acwing.com/problem/content/)



```cpp
```

[883.](https://www.acwing.com/problem/content/)



```cpp
```

[884.](https://www.acwing.com/problem/content/)



```cpp
```

[885.](https://www.acwing.com/problem/content/)



```cpp
```

[886.](https://www.acwing.com/problem/content/)



```cpp
```

[887.](https://www.acwing.com/problem/content/)



```cpp
```

[888.](https://www.acwing.com/problem/content/)



```cpp
```

[889.](https://www.acwing.com/problem/content/)



```cpp
```

[890.](https://www.acwing.com/problem/content/)



```cpp
```

[891.](https://www.acwing.com/problem/content/)



```cpp
```

[892.](https://www.acwing.com/problem/content/)



```cpp
```

[893.](https://www.acwing.com/problem/content/)



```cpp
```

[894.](https://www.acwing.com/problem/content/)



```cpp
```

[895.](https://www.acwing.com/problem/content/)



```cpp
```

[896.](https://www.acwing.com/problem/content/)



```cpp
```

[897.](https://www.acwing.com/problem/content/)



```cpp
```

[898.](https://www.acwing.com/problem/content/)



```cpp
```

[899.](https://www.acwing.com/problem/content/)



```cpp
```

[900.](https://www.acwing.com/problem/content/)



```cpp
```

#### 901~1000

[901.](https://www.acwing.com/problem/content/)



```cpp
```

[902.](https://www.acwing.com/problem/content/)



```cpp
```

[903.](https://www.acwing.com/problem/content/)



```cpp
```

[904.](https://www.acwing.com/problem/content/)



```cpp
```

[905.](https://www.acwing.com/problem/content/)



```cpp
```

[906.](https://www.acwing.com/problem/content/)



```cpp
```

[907.](https://www.acwing.com/problem/content/)



```cpp
```

[908.](https://www.acwing.com/problem/content/)



```cpp
```

[909.](https://www.acwing.com/problem/content/)



```cpp
```

[910.](https://www.acwing.com/problem/content/)



```cpp
```

[911.](https://www.acwing.com/problem/content/)



```cpp
```

[912.](https://www.acwing.com/problem/content/)



```cpp
```

[913.](https://www.acwing.com/problem/content/)



```cpp
```

[914.](https://www.acwing.com/problem/content/)



```cpp
```

[915.](https://www.acwing.com/problem/content/)



```cpp
```

[916.](https://www.acwing.com/problem/content/)



```cpp
```

[917.](https://www.acwing.com/problem/content/)



```cpp
```

[918.](https://www.acwing.com/problem/content/)



```cpp
```

[919.](https://www.acwing.com/problem/content/)



```cpp
```

[920.](https://www.acwing.com/problem/content/)



```cpp
```

[921.](https://www.acwing.com/problem/content/)



```cpp
```

[922.](https://www.acwing.com/problem/content/)



```cpp
```

[923.](https://www.acwing.com/problem/content/)



```cpp
```

[924.](https://www.acwing.com/problem/content/)



```cpp
```

[925.](https://www.acwing.com/problem/content/)



```cpp
```

[926.](https://www.acwing.com/problem/content/)



```cpp
```

[927.](https://www.acwing.com/problem/content/)



```cpp
```

[928.](https://www.acwing.com/problem/content/)



```cpp
```

[929.](https://www.acwing.com/problem/content/)



```cpp
```

[930.](https://www.acwing.com/problem/content/)



```cpp
```

[931.](https://www.acwing.com/problem/content/)



```cpp
```

[932.](https://www.acwing.com/problem/content/)



```cpp
```

[933.](https://www.acwing.com/problem/content/)



```cpp
```

[934.](https://www.acwing.com/problem/content/)



```cpp
```

[935.](https://www.acwing.com/problem/content/)



```cpp
```

[936.](https://www.acwing.com/problem/content/)



```cpp
```

[937.](https://www.acwing.com/problem/content/)



```cpp
```

[938.](https://www.acwing.com/problem/content/)



```cpp
```

[939.](https://www.acwing.com/problem/content/)



```cpp
```

[940.](https://www.acwing.com/problem/content/)



```cpp
```

[941.](https://www.acwing.com/problem/content/)



```cpp
```

[942.](https://www.acwing.com/problem/content/)



```cpp
```

[943.](https://www.acwing.com/problem/content/)



```cpp
```

[944.](https://www.acwing.com/problem/content/)



```cpp
```

[945.](https://www.acwing.com/problem/content/)



```cpp
```

[946.](https://www.acwing.com/problem/content/)



```cpp
```

[947.](https://www.acwing.com/problem/content/)



```cpp
```

[948.](https://www.acwing.com/problem/content/)



```cpp
```

[949.](https://www.acwing.com/problem/content/)



```cpp
```

[950.](https://www.acwing.com/problem/content/)



```cpp
```

[951.](https://www.acwing.com/problem/content/)



```cpp
```

[952.](https://www.acwing.com/problem/content/)



```cpp
```

[953.](https://www.acwing.com/problem/content/)



```cpp
```

[954.](https://www.acwing.com/problem/content/)



```cpp
```

[955.](https://www.acwing.com/problem/content/)



```cpp
```

[956.](https://www.acwing.com/problem/content/)



```cpp
```

[957.](https://www.acwing.com/problem/content/)



```cpp
```

[958.](https://www.acwing.com/problem/content/)



```cpp
```

[959.](https://www.acwing.com/problem/content/)



```cpp
```

[960.](https://www.acwing.com/problem/content/)



```cpp
```

[961.](https://www.acwing.com/problem/content/)



```cpp
```

[962.](https://www.acwing.com/problem/content/)



```cpp
```

[963.](https://www.acwing.com/problem/content/)



```cpp
```

[964.](https://www.acwing.com/problem/content/)



```cpp
```

[965.](https://www.acwing.com/problem/content/)



```cpp
```

[966.](https://www.acwing.com/problem/content/)



```cpp
```

[967.](https://www.acwing.com/problem/content/)



```cpp
```

[968.](https://www.acwing.com/problem/content/)



```cpp
```

[969.](https://www.acwing.com/problem/content/)



```cpp
```

[970.](https://www.acwing.com/problem/content/)



```cpp
```

[971.](https://www.acwing.com/problem/content/)



```cpp
```

[972.](https://www.acwing.com/problem/content/)



```cpp
```

[973.](https://www.acwing.com/problem/content/)



```cpp
```

[974.](https://www.acwing.com/problem/content/)



```cpp
```

[975.](https://www.acwing.com/problem/content/)



```cpp
```

[976.](https://www.acwing.com/problem/content/)



```cpp
```

[977.](https://www.acwing.com/problem/content/)



```cpp
```

[978.](https://www.acwing.com/problem/content/)



```cpp
```

[979.](https://www.acwing.com/problem/content/)



```cpp
```

[980.](https://www.acwing.com/problem/content/)



```cpp
```

[981.](https://www.acwing.com/problem/content/)



```cpp
```

[982.](https://www.acwing.com/problem/content/)



```cpp
```

[983.](https://www.acwing.com/problem/content/)



```cpp
```

[984.](https://www.acwing.com/problem/content/)



```cpp
```

[985.](https://www.acwing.com/problem/content/)



```cpp
```

[986.](https://www.acwing.com/problem/content/)



```cpp
```

[987.](https://www.acwing.com/problem/content/)



```cpp
```

[988.](https://www.acwing.com/problem/content/)



```cpp
```

[989.](https://www.acwing.com/problem/content/)



```cpp
```

[990.](https://www.acwing.com/problem/content/)



```cpp
```

[991.](https://www.acwing.com/problem/content/)



```cpp
```

[992.](https://www.acwing.com/problem/content/)



```cpp
```

[993.](https://www.acwing.com/problem/content/)



```cpp
```

[994.](https://www.acwing.com/problem/content/)



```cpp
```

[995.](https://www.acwing.com/problem/content/)



```cpp
```

[996.](https://www.acwing.com/problem/content/)



```cpp
```

[997.](https://www.acwing.com/problem/content/)



```cpp
```

[998.](https://www.acwing.com/problem/content/)



```cpp
```

[999.](https://www.acwing.com/problem/content/)



```cpp
```

[1000.](https://www.acwing.com/problem/content/)



```cpp
```

## 1001~2000

### 1001~1500

#### 1001~1100

[1001.](https://www.acwing.com/problem/content/)



```cpp
```

[1002.](https://www.acwing.com/problem/content/)



```cpp
```

[1003.](https://www.acwing.com/problem/content/)



```cpp
```

[1004.](https://www.acwing.com/problem/content/)



```cpp
```

[1005.](https://www.acwing.com/problem/content/)



```cpp
```

[1006.](https://www.acwing.com/problem/content/)



```cpp
```

[1007.](https://www.acwing.com/problem/content/)



```cpp
```

[1008.](https://www.acwing.com/problem/content/)



```cpp
```

[1009.](https://www.acwing.com/problem/content/)



```cpp
```

[1010.](https://www.acwing.com/problem/content/)



```cpp
```

[1011.](https://www.acwing.com/problem/content/)



```cpp
```

[1012.](https://www.acwing.com/problem/content/)



```cpp
```

[1013.](https://www.acwing.com/problem/content/)



```cpp
```

[1014.](https://www.acwing.com/problem/content/)



```cpp
```

[1015.](https://www.acwing.com/problem/content/)



```cpp
```

[1016.](https://www.acwing.com/problem/content/)



```cpp
```

[1017.](https://www.acwing.com/problem/content/)



```cpp
```

[1018.](https://www.acwing.com/problem/content/)



```cpp
```

[1019.](https://www.acwing.com/problem/content/)



```cpp
```

[1020.](https://www.acwing.com/problem/content/)



```cpp
```

[1021.](https://www.acwing.com/problem/content/)



```cpp
```

[1022.](https://www.acwing.com/problem/content/)



```cpp
```

[1023.](https://www.acwing.com/problem/content/)



```cpp
```

[1024.](https://www.acwing.com/problem/content/)



```cpp
```

[1025.](https://www.acwing.com/problem/content/)



```cpp
```

[1026.](https://www.acwing.com/problem/content/)



```cpp
```

[1027.](https://www.acwing.com/problem/content/)



```cpp
```

[1028.](https://www.acwing.com/problem/content/)



```cpp
```

[1029.](https://www.acwing.com/problem/content/)



```cpp
```

[1030.](https://www.acwing.com/problem/content/)



```cpp
```

[1031.](https://www.acwing.com/problem/content/)



```cpp
```

[1032.](https://www.acwing.com/problem/content/)



```cpp
```

[1033.](https://www.acwing.com/problem/content/)



```cpp
```

[1034.](https://www.acwing.com/problem/content/)



```cpp
```

[1035.](https://www.acwing.com/problem/content/)



```cpp
```

[1036.](https://www.acwing.com/problem/content/)



```cpp
```

[1037.](https://www.acwing.com/problem/content/)



```cpp
```

[1038.](https://www.acwing.com/problem/content/)



```cpp
```

[1039.](https://www.acwing.com/problem/content/)



```cpp
```

[1040.](https://www.acwing.com/problem/content/)



```cpp
```

[1041.](https://www.acwing.com/problem/content/)



```cpp
```

[1042.](https://www.acwing.com/problem/content/)



```cpp
```

[1043.](https://www.acwing.com/problem/content/)



```cpp
```

[1044.](https://www.acwing.com/problem/content/)



```cpp
```

[1045.](https://www.acwing.com/problem/content/)



```cpp
```

[1046.](https://www.acwing.com/problem/content/)



```cpp
```

[1047.](https://www.acwing.com/problem/content/)



```cpp
```

[1048.](https://www.acwing.com/problem/content/)



```cpp
```

[1049.](https://www.acwing.com/problem/content/)



```cpp
```

[1050.](https://www.acwing.com/problem/content/)



```cpp
```

[1051.](https://www.acwing.com/problem/content/)



```cpp
```

[1052.](https://www.acwing.com/problem/content/)



```cpp
```

[1053.](https://www.acwing.com/problem/content/)



```cpp
```

[1054.](https://www.acwing.com/problem/content/)



```cpp
```

[1055.](https://www.acwing.com/problem/content/)



```cpp
```

[1056.](https://www.acwing.com/problem/content/)



```cpp
```

[1057.](https://www.acwing.com/problem/content/)



```cpp
```

[1058.](https://www.acwing.com/problem/content/)



```cpp
```

[1059.](https://www.acwing.com/problem/content/)



```cpp
```

[1060.](https://www.acwing.com/problem/content/)



```cpp
```

[1061.](https://www.acwing.com/problem/content/)



```cpp
```

[1062.](https://www.acwing.com/problem/content/)



```cpp
```

[1063.](https://www.acwing.com/problem/content/)



```cpp
```

[1064.](https://www.acwing.com/problem/content/)



```cpp
```

[1065.](https://www.acwing.com/problem/content/)



```cpp
```

[1066.](https://www.acwing.com/problem/content/)



```cpp
```

[1067.](https://www.acwing.com/problem/content/)



```cpp
```

[1068.](https://www.acwing.com/problem/content/)



```cpp
```

[1069.](https://www.acwing.com/problem/content/)



```cpp
```

[1070.](https://www.acwing.com/problem/content/)



```cpp
```

[1071.](https://www.acwing.com/problem/content/)



```cpp
```

[1072.](https://www.acwing.com/problem/content/)



```cpp
```

[1073.](https://www.acwing.com/problem/content/)



```cpp
```

[1074.](https://www.acwing.com/problem/content/)



```cpp
```

[1075.](https://www.acwing.com/problem/content/)



```cpp
```

[1076.](https://www.acwing.com/problem/content/)



```cpp
```

[1077.](https://www.acwing.com/problem/content/)



```cpp
```

[1078.](https://www.acwing.com/problem/content/)



```cpp
```

[1079.](https://www.acwing.com/problem/content/)



```cpp
```

[1080.](https://www.acwing.com/problem/content/)



```cpp
```

[1081.](https://www.acwing.com/problem/content/)



```cpp
```

[1082.](https://www.acwing.com/problem/content/)



```cpp
```

[1083.](https://www.acwing.com/problem/content/)



```cpp
```

[1084.](https://www.acwing.com/problem/content/)



```cpp
```

[1085.](https://www.acwing.com/problem/content/)



```cpp
```

[1086.](https://www.acwing.com/problem/content/)



```cpp
```

[1087.](https://www.acwing.com/problem/content/)



```cpp
```

[1088.](https://www.acwing.com/problem/content/)



```cpp
```

[1089.](https://www.acwing.com/problem/content/)



```cpp
```

[1090.](https://www.acwing.com/problem/content/)



```cpp
```

[1091.](https://www.acwing.com/problem/content/)



```cpp
```

[1092.](https://www.acwing.com/problem/content/)



```cpp
```

[1093.](https://www.acwing.com/problem/content/)



```cpp
```

[1094.](https://www.acwing.com/problem/content/)



```cpp
```

[1095.](https://www.acwing.com/problem/content/)



```cpp
```

[1096.](https://www.acwing.com/problem/content/)



```cpp
```

[1097.](https://www.acwing.com/problem/content/)



```cpp
```

[1098.](https://www.acwing.com/problem/content/)



```cpp
```

[1099.](https://www.acwing.com/problem/content/)



```cpp
```

[1100.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1101~1200

[1101.](https://www.acwing.com/problem/content/)



```cpp
```

[1102.](https://www.acwing.com/problem/content/)



```cpp
```

[1103.](https://www.acwing.com/problem/content/)



```cpp
```

[1104.](https://www.acwing.com/problem/content/)



```cpp
```

[1105.](https://www.acwing.com/problem/content/)



```cpp
```

[1106.](https://www.acwing.com/problem/content/)



```cpp
```

[1107.](https://www.acwing.com/problem/content/)



```cpp
```

[1108.](https://www.acwing.com/problem/content/)



```cpp
```

[1109.](https://www.acwing.com/problem/content/)



```cpp
```

[1110.](https://www.acwing.com/problem/content/)



```cpp
```

[1111.](https://www.acwing.com/problem/content/)



```cpp
```

[1112.](https://www.acwing.com/problem/content/)



```cpp
```

[1113.](https://www.acwing.com/problem/content/)



```cpp
```

[1114.](https://www.acwing.com/problem/content/)



```cpp
```

[1115.](https://www.acwing.com/problem/content/)



```cpp
```

[1116.](https://www.acwing.com/problem/content/)



```cpp
```

[1117.](https://www.acwing.com/problem/content/)



```cpp
```

[1118.](https://www.acwing.com/problem/content/)



```cpp
```

[1119.](https://www.acwing.com/problem/content/)



```cpp
```

[1120.](https://www.acwing.com/problem/content/)



```cpp
```

[1121.](https://www.acwing.com/problem/content/)



```cpp
```

[1122.](https://www.acwing.com/problem/content/)



```cpp
```

[1123.](https://www.acwing.com/problem/content/)



```cpp
```

[1124.](https://www.acwing.com/problem/content/)



```cpp
```

[1125.](https://www.acwing.com/problem/content/)



```cpp
```

[1126.](https://www.acwing.com/problem/content/)



```cpp
```

[1127.](https://www.acwing.com/problem/content/)



```cpp
```

[1128.](https://www.acwing.com/problem/content/)



```cpp
```

[1129.](https://www.acwing.com/problem/content/)



```cpp
```

[1130.](https://www.acwing.com/problem/content/)



```cpp
```

[1131.](https://www.acwing.com/problem/content/)



```cpp
```

[1132.](https://www.acwing.com/problem/content/)



```cpp
```

[1133.](https://www.acwing.com/problem/content/)



```cpp
```

[1134.](https://www.acwing.com/problem/content/)



```cpp
```

[1135.](https://www.acwing.com/problem/content/)



```cpp
```

[1136.](https://www.acwing.com/problem/content/)



```cpp
```

[1137.](https://www.acwing.com/problem/content/)



```cpp
```

[1138.](https://www.acwing.com/problem/content/)



```cpp
```

[1139.](https://www.acwing.com/problem/content/)



```cpp
```

[1140.](https://www.acwing.com/problem/content/)



```cpp
```

[1141.](https://www.acwing.com/problem/content/)



```cpp
```

[1142.](https://www.acwing.com/problem/content/)



```cpp
```

[1143.](https://www.acwing.com/problem/content/)



```cpp
```

[1144.](https://www.acwing.com/problem/content/)



```cpp
```

[1145.](https://www.acwing.com/problem/content/)



```cpp
```

[1146.](https://www.acwing.com/problem/content/)



```cpp
```

[1147.](https://www.acwing.com/problem/content/)



```cpp
```

[1148.](https://www.acwing.com/problem/content/)



```cpp
```

[1149.](https://www.acwing.com/problem/content/)



```cpp
```

[1150.](https://www.acwing.com/problem/content/)



```cpp
```

[1151.](https://www.acwing.com/problem/content/)



```cpp
```

[1152.](https://www.acwing.com/problem/content/)



```cpp
```

[1153.](https://www.acwing.com/problem/content/)



```cpp
```

[1154.](https://www.acwing.com/problem/content/)



```cpp
```

[1155.](https://www.acwing.com/problem/content/)



```cpp
```

[1156.](https://www.acwing.com/problem/content/)



```cpp
```

[1157.](https://www.acwing.com/problem/content/)



```cpp
```

[1158.](https://www.acwing.com/problem/content/)



```cpp
```

[1159.](https://www.acwing.com/problem/content/)



```cpp
```

[1160.](https://www.acwing.com/problem/content/)



```cpp
```

[1161.](https://www.acwing.com/problem/content/)



```cpp
```

[1162.](https://www.acwing.com/problem/content/)



```cpp
```

[1163.](https://www.acwing.com/problem/content/)



```cpp
```

[1164.](https://www.acwing.com/problem/content/)



```cpp
```

[1165.](https://www.acwing.com/problem/content/)



```cpp
```

[1166.](https://www.acwing.com/problem/content/)



```cpp
```

[1167.](https://www.acwing.com/problem/content/)



```cpp
```

[1168.](https://www.acwing.com/problem/content/)



```cpp
```

[1169.](https://www.acwing.com/problem/content/)



```cpp
```

[1170.](https://www.acwing.com/problem/content/)



```cpp
```

[1171.](https://www.acwing.com/problem/content/)



```cpp
```

[1172.](https://www.acwing.com/problem/content/)



```cpp
```

[1173.](https://www.acwing.com/problem/content/)



```cpp
```

[1174.](https://www.acwing.com/problem/content/)



```cpp
```

[1175.](https://www.acwing.com/problem/content/)



```cpp
```

[1176.](https://www.acwing.com/problem/content/)



```cpp
```

[1177.](https://www.acwing.com/problem/content/)



```cpp
```

[1178.](https://www.acwing.com/problem/content/)



```cpp
```

[1179.](https://www.acwing.com/problem/content/)



```cpp
```

[1180.](https://www.acwing.com/problem/content/)



```cpp
```

[1181.](https://www.acwing.com/problem/content/)



```cpp
```

[1182.](https://www.acwing.com/problem/content/)



```cpp
```

[1183.](https://www.acwing.com/problem/content/)



```cpp
```

[1184.](https://www.acwing.com/problem/content/)



```cpp
```

[1185.](https://www.acwing.com/problem/content/)



```cpp
```

[1186.](https://www.acwing.com/problem/content/)



```cpp
```

[1187.](https://www.acwing.com/problem/content/)



```cpp
```

[1188.](https://www.acwing.com/problem/content/)



```cpp
```

[1189.](https://www.acwing.com/problem/content/)



```cpp
```

[1190.](https://www.acwing.com/problem/content/)



```cpp
```

[1191.](https://www.acwing.com/problem/content/)



```cpp
```

[1192.](https://www.acwing.com/problem/content/)



```cpp
```

[1193.](https://www.acwing.com/problem/content/)



```cpp
```

[1194.](https://www.acwing.com/problem/content/)



```cpp
```

[1195.](https://www.acwing.com/problem/content/)



```cpp
```

[1196.](https://www.acwing.com/problem/content/)



```cpp
```

[1197.](https://www.acwing.com/problem/content/)



```cpp
```

[1198.](https://www.acwing.com/problem/content/)



```cpp
```

[1199.](https://www.acwing.com/problem/content/)



```cpp
```

[1200.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1201~1300

[1201.](https://www.acwing.com/problem/content/)



```cpp
```

[1202.](https://www.acwing.com/problem/content/)



```cpp
```

[1203.](https://www.acwing.com/problem/content/)



```cpp
```

[1204.](https://www.acwing.com/problem/content/)



```cpp
```

[1205.](https://www.acwing.com/problem/content/)



```cpp
```

[1206.](https://www.acwing.com/problem/content/)



```cpp
```

[1207.](https://www.acwing.com/problem/content/)



```cpp
```

[1208.](https://www.acwing.com/problem/content/)



```cpp
```

[1209.](https://www.acwing.com/problem/content/)



```cpp
```

[1210.](https://www.acwing.com/problem/content/)



```cpp
```

[1211.](https://www.acwing.com/problem/content/)



```cpp
```

[1212.](https://www.acwing.com/problem/content/)



```cpp
```

[1213.](https://www.acwing.com/problem/content/)



```cpp
```

[1214.](https://www.acwing.com/problem/content/)



```cpp
```

[1215.](https://www.acwing.com/problem/content/)



```cpp
```

[1216.](https://www.acwing.com/problem/content/)



```cpp
```

[1217.](https://www.acwing.com/problem/content/)



```cpp
```

[1218.](https://www.acwing.com/problem/content/)



```cpp
```

[1219.](https://www.acwing.com/problem/content/)



```cpp
```

[1220.](https://www.acwing.com/problem/content/)



```cpp
```

[1221.](https://www.acwing.com/problem/content/)



```cpp
```

[1222.](https://www.acwing.com/problem/content/)



```cpp
```

[1223.](https://www.acwing.com/problem/content/)



```cpp
```

[1224.](https://www.acwing.com/problem/content/)



```cpp
```

[1225.](https://www.acwing.com/problem/content/)



```cpp
```

[1226.](https://www.acwing.com/problem/content/)



```cpp
```

[1227.](https://www.acwing.com/problem/content/)



```cpp
```

[1228.](https://www.acwing.com/problem/content/)



```cpp
```

[1229.](https://www.acwing.com/problem/content/)



```cpp
```

[1230.](https://www.acwing.com/problem/content/)



```cpp
```

[1231.](https://www.acwing.com/problem/content/)



```cpp
```

[1232.](https://www.acwing.com/problem/content/)



```cpp
```

[1233.](https://www.acwing.com/problem/content/)



```cpp
```

[1234.](https://www.acwing.com/problem/content/)



```cpp
```

[1235.](https://www.acwing.com/problem/content/)



```cpp
```

[1236.](https://www.acwing.com/problem/content/)



```cpp
```

[1237.](https://www.acwing.com/problem/content/)



```cpp
```

[1238.](https://www.acwing.com/problem/content/)



```cpp
```

[1239.](https://www.acwing.com/problem/content/)



```cpp
```

[1240.](https://www.acwing.com/problem/content/)



```cpp
```

[1241.](https://www.acwing.com/problem/content/)



```cpp
```

[1242.](https://www.acwing.com/problem/content/)



```cpp
```

[1243.](https://www.acwing.com/problem/content/)



```cpp
```

[1244.](https://www.acwing.com/problem/content/)



```cpp
```

[1245.](https://www.acwing.com/problem/content/)



```cpp
```

[1246.](https://www.acwing.com/problem/content/)



```cpp
```

[1247.](https://www.acwing.com/problem/content/)



```cpp
```

[1248.](https://www.acwing.com/problem/content/)



```cpp
```

[1249.](https://www.acwing.com/problem/content/)



```cpp
```

[1250.](https://www.acwing.com/problem/content/)



```cpp
```

[1251.](https://www.acwing.com/problem/content/)



```cpp
```

[1252.](https://www.acwing.com/problem/content/)



```cpp
```

[1253.](https://www.acwing.com/problem/content/)



```cpp
```

[1254.](https://www.acwing.com/problem/content/)



```cpp
```

[1255.](https://www.acwing.com/problem/content/)



```cpp
```

[1256.](https://www.acwing.com/problem/content/)



```cpp
```

[1257.](https://www.acwing.com/problem/content/)



```cpp
```

[1258.](https://www.acwing.com/problem/content/)



```cpp
```

[1259.](https://www.acwing.com/problem/content/)



```cpp
```

[1260.](https://www.acwing.com/problem/content/)



```cpp
```

[1261.](https://www.acwing.com/problem/content/)



```cpp
```

[1262.](https://www.acwing.com/problem/content/)



```cpp
```

[1263.](https://www.acwing.com/problem/content/)



```cpp
```

[1264.](https://www.acwing.com/problem/content/)



```cpp
```

[1265.](https://www.acwing.com/problem/content/)



```cpp
```

[1266.](https://www.acwing.com/problem/content/)



```cpp
```

[1267.](https://www.acwing.com/problem/content/)



```cpp
```

[1268.](https://www.acwing.com/problem/content/)



```cpp
```

[1269.](https://www.acwing.com/problem/content/)



```cpp
```

[1270.](https://www.acwing.com/problem/content/)



```cpp
```

[1271.](https://www.acwing.com/problem/content/)



```cpp
```

[1272.](https://www.acwing.com/problem/content/)



```cpp
```

[1273.](https://www.acwing.com/problem/content/)



```cpp
```

[1274.](https://www.acwing.com/problem/content/)



```cpp
```

[1275.](https://www.acwing.com/problem/content/)



```cpp
```

[1276.](https://www.acwing.com/problem/content/)



```cpp
```

[1277.](https://www.acwing.com/problem/content/)



```cpp
```

[1278.](https://www.acwing.com/problem/content/)



```cpp
```

[1279.](https://www.acwing.com/problem/content/)



```cpp
```

[1280.](https://www.acwing.com/problem/content/)



```cpp
```

[1281.](https://www.acwing.com/problem/content/)



```cpp
```

[1282.](https://www.acwing.com/problem/content/)



```cpp
```

[1283.](https://www.acwing.com/problem/content/)



```cpp
```

[1284.](https://www.acwing.com/problem/content/)



```cpp
```

[1285.](https://www.acwing.com/problem/content/)



```cpp
```

[1286.](https://www.acwing.com/problem/content/)



```cpp
```

[1287.](https://www.acwing.com/problem/content/)



```cpp
```

[1288.](https://www.acwing.com/problem/content/)



```cpp
```

[1289.](https://www.acwing.com/problem/content/)



```cpp
```

[1290.](https://www.acwing.com/problem/content/)



```cpp
```

[1291.](https://www.acwing.com/problem/content/)



```cpp
```

[1292.](https://www.acwing.com/problem/content/)



```cpp
```

[1293.](https://www.acwing.com/problem/content/)



```cpp
```

[1294.](https://www.acwing.com/problem/content/)



```cpp
```

[1295.](https://www.acwing.com/problem/content/)



```cpp
```

[1296.](https://www.acwing.com/problem/content/)



```cpp
```

[1297.](https://www.acwing.com/problem/content/)



```cpp
```

[1298.](https://www.acwing.com/problem/content/)



```cpp
```

[1299.](https://www.acwing.com/problem/content/)



```cpp
```

[1300.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1301~1400

[1301.](https://www.acwing.com/problem/content/)



```cpp
```

[1302.](https://www.acwing.com/problem/content/)



```cpp
```

[1303.](https://www.acwing.com/problem/content/)



```cpp
```

[1304.](https://www.acwing.com/problem/content/)



```cpp
```

[1305.](https://www.acwing.com/problem/content/)



```cpp
```

[1306.](https://www.acwing.com/problem/content/)



```cpp
```

[1307.](https://www.acwing.com/problem/content/)



```cpp
```

[1308.](https://www.acwing.com/problem/content/)



```cpp
```

[1309.](https://www.acwing.com/problem/content/)



```cpp
```

[1310.](https://www.acwing.com/problem/content/)



```cpp
```

[1311.](https://www.acwing.com/problem/content/)



```cpp
```

[1312.](https://www.acwing.com/problem/content/)



```cpp
```

[1313.](https://www.acwing.com/problem/content/)



```cpp
```

[1314.](https://www.acwing.com/problem/content/)



```cpp
```

[1315.](https://www.acwing.com/problem/content/)



```cpp
```

[1316.](https://www.acwing.com/problem/content/)



```cpp
```

[1317.](https://www.acwing.com/problem/content/)



```cpp
```

[1318.](https://www.acwing.com/problem/content/)



```cpp
```

[1319.](https://www.acwing.com/problem/content/)



```cpp
```

[1320.](https://www.acwing.com/problem/content/)



```cpp
```

[1321.](https://www.acwing.com/problem/content/)



```cpp
```

[1322.](https://www.acwing.com/problem/content/)



```cpp
```

[1323.](https://www.acwing.com/problem/content/)



```cpp
```

[1324.](https://www.acwing.com/problem/content/)



```cpp
```

[1325.](https://www.acwing.com/problem/content/)



```cpp
```

[1326.](https://www.acwing.com/problem/content/)



```cpp
```

[1327.](https://www.acwing.com/problem/content/)



```cpp
```

[1328.](https://www.acwing.com/problem/content/)



```cpp
```

[1329.](https://www.acwing.com/problem/content/)



```cpp
```

[1330.](https://www.acwing.com/problem/content/)



```cpp
```

[1331.](https://www.acwing.com/problem/content/)



```cpp
```

[1332.](https://www.acwing.com/problem/content/)



```cpp
```

[1333.](https://www.acwing.com/problem/content/)



```cpp
```

[1334.](https://www.acwing.com/problem/content/)



```cpp
```

[1335.](https://www.acwing.com/problem/content/)



```cpp
```

[1336.](https://www.acwing.com/problem/content/)



```cpp
```

[1337.](https://www.acwing.com/problem/content/)



```cpp
```

[1338.](https://www.acwing.com/problem/content/)



```cpp
```

[1339.](https://www.acwing.com/problem/content/)



```cpp
```

[1340.](https://www.acwing.com/problem/content/)



```cpp
```

[1341.](https://www.acwing.com/problem/content/)



```cpp
```

[1342.](https://www.acwing.com/problem/content/)



```cpp
```

[1343.](https://www.acwing.com/problem/content/)



```cpp
```

[1344.](https://www.acwing.com/problem/content/)



```cpp
```

[1345.](https://www.acwing.com/problem/content/)



```cpp
```

[1346.](https://www.acwing.com/problem/content/)



```cpp
```

[1347.](https://www.acwing.com/problem/content/)



```cpp
```

[1348.](https://www.acwing.com/problem/content/)



```cpp
```

[1349.](https://www.acwing.com/problem/content/)



```cpp
```

[1350.](https://www.acwing.com/problem/content/)



```cpp
```

[1351.](https://www.acwing.com/problem/content/)



```cpp
```

[1352.](https://www.acwing.com/problem/content/)



```cpp
```

[1353.](https://www.acwing.com/problem/content/)



```cpp
```

[1354.](https://www.acwing.com/problem/content/)



```cpp
```

[1355.](https://www.acwing.com/problem/content/)



```cpp
```

[1356.](https://www.acwing.com/problem/content/)



```cpp
```

[1357.](https://www.acwing.com/problem/content/)



```cpp
```

[1358.](https://www.acwing.com/problem/content/)



```cpp
```

[1359.](https://www.acwing.com/problem/content/)



```cpp
```

[1360.](https://www.acwing.com/problem/content/)



```cpp
```

[1361.](https://www.acwing.com/problem/content/)



```cpp
```

[1362.](https://www.acwing.com/problem/content/)



```cpp
```

[1363.](https://www.acwing.com/problem/content/)



```cpp
```

[1364.](https://www.acwing.com/problem/content/)



```cpp
```

[1365.](https://www.acwing.com/problem/content/)



```cpp
```

[1366.](https://www.acwing.com/problem/content/)



```cpp
```

[1367.](https://www.acwing.com/problem/content/)



```cpp
```

[1368.](https://www.acwing.com/problem/content/)



```cpp
```

[1369.](https://www.acwing.com/problem/content/)



```cpp
```

[1370.](https://www.acwing.com/problem/content/)



```cpp
```

[1371.](https://www.acwing.com/problem/content/)



```cpp
```

[1372.](https://www.acwing.com/problem/content/)



```cpp
```

[1373.](https://www.acwing.com/problem/content/)



```cpp
```

[1374.](https://www.acwing.com/problem/content/)



```cpp
```

[1375.](https://www.acwing.com/problem/content/)



```cpp
```

[1376.](https://www.acwing.com/problem/content/)



```cpp
```

[1377.](https://www.acwing.com/problem/content/)



```cpp
```

[1378.](https://www.acwing.com/problem/content/)



```cpp
```

[1379.](https://www.acwing.com/problem/content/)



```cpp
```

[1380.](https://www.acwing.com/problem/content/)



```cpp
```

[1381. 阶乘](https://www.acwing.com/problem/content/1383/)

本题重点在于如何获取最后一个非零的数。通过分解质因数可知，这里计算出来的阶乘可以拆分为$n!=2^{\alpha-k}*5^{\beta-k}*10^k*C$ ,阶乘中的0就来源于这里的2和5之积，也就是k的数量。

```cpp
#include <iostream>
using namespace std;
int main(){
    int n;
    scanf("%d",&n);
    //这里的d2表示因数中2的个数，d5表示5的个数
    int res=1,d2=0,d5=0;
    for(int i=1;i<=n;i++){
        int x=i;
        while(x%2==0) x/=2,d2+=1;
        while(x%5==0) x/=5,d5+=1;
        //这里取余可以有效的减小数字的大小，对于结果没有影响
        res=res*x%10;
    }
    //将多扣除的2或者5乘回去
    int k=d2<d5?d2:d5;
    //这里取余可以有效的减小数字的大小，对于结果没有影响
    for(int i=0;i<d2-k;i++) res=res*2%10;
    for(int i=0;i<d5-k;i++) res=res*5%10;
    printf("%d",res%10);
    return 0;
}
```

[1382.](https://www.acwing.com/problem/content/)



```cpp
```

[1383.](https://www.acwing.com/problem/content/)



```cpp
```

[1384.](https://www.acwing.com/problem/content/)



```cpp
```

[1385.](https://www.acwing.com/problem/content/)



```cpp
```

[1386.](https://www.acwing.com/problem/content/)



```cpp
```

[1387.](https://www.acwing.com/problem/content/)



```cpp
```

[1388.](https://www.acwing.com/problem/content/)



```cpp
```

[1389.](https://www.acwing.com/problem/content/)



```cpp
```

[1390.](https://www.acwing.com/problem/content/)



```cpp
```

[1391.](https://www.acwing.com/problem/content/)



```cpp
```

[1392.](https://www.acwing.com/problem/content/)



```cpp
```

[1393.](https://www.acwing.com/problem/content/)



```cpp
```

[1394.](https://www.acwing.com/problem/content/)



```cpp
```

[1395.](https://www.acwing.com/problem/content/)



```cpp
```

[1396.](https://www.acwing.com/problem/content/)



```cpp
```

[1397.](https://www.acwing.com/problem/content/)



```cpp
```

[1398.](https://www.acwing.com/problem/content/)



```cpp
```

[1399.](https://www.acwing.com/problem/content/)



```cpp
```

[1400.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1401~1500

[1401.](https://www.acwing.com/problem/content/)



```cpp
```

[1402.](https://www.acwing.com/problem/content/)



```cpp
```

[1403.](https://www.acwing.com/problem/content/)



```cpp
```

[1404.](https://www.acwing.com/problem/content/)



```cpp
```

[1405.](https://www.acwing.com/problem/content/)



```cpp
```

[1406.](https://www.acwing.com/problem/content/)



```cpp
```

[1407.](https://www.acwing.com/problem/content/)



```cpp
```

[1408.](https://www.acwing.com/problem/content/)



```cpp
```

[1409.](https://www.acwing.com/problem/content/)



```cpp
```

[1410.](https://www.acwing.com/problem/content/)



```cpp
```

[1411.](https://www.acwing.com/problem/content/)



```cpp
```

[1412.](https://www.acwing.com/problem/content/)



```cpp
```

[1413.](https://www.acwing.com/problem/content/)



```cpp
```

[1414.](https://www.acwing.com/problem/content/)



```cpp
```

[1415.](https://www.acwing.com/problem/content/)



```cpp
```

[1416.](https://www.acwing.com/problem/content/)



```cpp
```

[1417.](https://www.acwing.com/problem/content/)



```cpp
```

[1418.](https://www.acwing.com/problem/content/)



```cpp
```

[1419.](https://www.acwing.com/problem/content/)



```cpp
```

[1420.](https://www.acwing.com/problem/content/)



```cpp
```

[1421.](https://www.acwing.com/problem/content/)



```cpp
```

[1422.](https://www.acwing.com/problem/content/)



```cpp
```

[1423.](https://www.acwing.com/problem/content/)



```cpp
```

[1424.](https://www.acwing.com/problem/content/)



```cpp
```

[1425.](https://www.acwing.com/problem/content/)



```cpp
```

[1426.](https://www.acwing.com/problem/content/)



```cpp
```

[1427.](https://www.acwing.com/problem/content/)



```cpp
```

[1428.](https://www.acwing.com/problem/content/)



```cpp
```

[1429.](https://www.acwing.com/problem/content/)



```cpp
```

[1430.](https://www.acwing.com/problem/content/)



```cpp
```

[1431.](https://www.acwing.com/problem/content/)



```cpp
```

[1432.](https://www.acwing.com/problem/content/)



```cpp
```

[1433.](https://www.acwing.com/problem/content/)



```cpp
```

[1434.](https://www.acwing.com/problem/content/)



```cpp
```

[1435.](https://www.acwing.com/problem/content/)



```cpp
```

[1436.](https://www.acwing.com/problem/content/)



```cpp
```

[1437.](https://www.acwing.com/problem/content/)



```cpp
```

[1438.](https://www.acwing.com/problem/content/)



```cpp
```

[1439.](https://www.acwing.com/problem/content/)



```cpp
```

[1440.](https://www.acwing.com/problem/content/)



```cpp
```

[1441.](https://www.acwing.com/problem/content/)



```cpp
```

[1442.](https://www.acwing.com/problem/content/)



```cpp
```

[1443.](https://www.acwing.com/problem/content/)



```cpp
```

[1444.](https://www.acwing.com/problem/content/)



```cpp
```

[1445.](https://www.acwing.com/problem/content/)



```cpp
```

[1446.](https://www.acwing.com/problem/content/)



```cpp
```

[1447.](https://www.acwing.com/problem/content/)



```cpp
```

[1448.](https://www.acwing.com/problem/content/)



```cpp
```

[1449.](https://www.acwing.com/problem/content/)



```cpp
```

[1450.](https://www.acwing.com/problem/content/)



```cpp
```

[1451.](https://www.acwing.com/problem/content/)



```cpp
```

[1452.](https://www.acwing.com/problem/content/)



```cpp
```

[1453.](https://www.acwing.com/problem/content/)



```cpp
```

[1454.](https://www.acwing.com/problem/content/)



```cpp
```

[1455.](https://www.acwing.com/problem/content/)



```cpp
```

[1456.](https://www.acwing.com/problem/content/)



```cpp
```

[1457.](https://www.acwing.com/problem/content/)



```cpp
```

[1458.](https://www.acwing.com/problem/content/)



```cpp
```

[1459.](https://www.acwing.com/problem/content/)



```cpp
```

[1460.](https://www.acwing.com/problem/content/)



```cpp
```

[1461.](https://www.acwing.com/problem/content/)



```cpp
```

[1462.](https://www.acwing.com/problem/content/)



```cpp
```

[1463.](https://www.acwing.com/problem/content/)



```cpp
```

[1464.](https://www.acwing.com/problem/content/)



```cpp
```

[1465.](https://www.acwing.com/problem/content/)



```cpp
```

[1466.](https://www.acwing.com/problem/content/)



```cpp
```

[1467.](https://www.acwing.com/problem/content/)



```cpp
```

[1468.](https://www.acwing.com/problem/content/)



```cpp
```

[1469.](https://www.acwing.com/problem/content/)



```cpp
```

[1470.](https://www.acwing.com/problem/content/)



```cpp
```

[1471.](https://www.acwing.com/problem/content/)



```cpp
```

[1472.](https://www.acwing.com/problem/content/)



```cpp
```

[1473.](https://www.acwing.com/problem/content/)



```cpp
```

[1474.](https://www.acwing.com/problem/content/)



```cpp
```

[1475.](https://www.acwing.com/problem/content/)



```cpp
```

[1476.](https://www.acwing.com/problem/content/)



```cpp
```

[1477.](https://www.acwing.com/problem/content/)



```cpp
```

[1478.](https://www.acwing.com/problem/content/)



```cpp
```

[1479.](https://www.acwing.com/problem/content/)



```cpp
```

[1480.](https://www.acwing.com/problem/content/)



```cpp
```

[1481.](https://www.acwing.com/problem/content/)



```cpp
```

[1482.](https://www.acwing.com/problem/content/)



```cpp
```

[1483.](https://www.acwing.com/problem/content/)



```cpp
```

[1484.](https://www.acwing.com/problem/content/)



```cpp
```

[1485.](https://www.acwing.com/problem/content/)



```cpp
```

[1486.](https://www.acwing.com/problem/content/)



```cpp
```

[1487.](https://www.acwing.com/problem/content/)



```cpp
```

[1488.](https://www.acwing.com/problem/content/)



```cpp
```

[1489.](https://www.acwing.com/problem/content/)



```cpp
```

[1490.](https://www.acwing.com/problem/content/)



```cpp
```

[1491.](https://www.acwing.com/problem/content/)



```cpp
```

[1492.](https://www.acwing.com/problem/content/)



```cpp
```

[1493.](https://www.acwing.com/problem/content/)



```cpp
```

[1494.](https://www.acwing.com/problem/content/)



```cpp
```

[1495.](https://www.acwing.com/problem/content/)



```cpp
```

[1496.](https://www.acwing.com/problem/content/)



```cpp
```

[1497.](https://www.acwing.com/problem/content/)



```cpp
```

[1498.](https://www.acwing.com/problem/content/)



```cpp
```

[1499.](https://www.acwing.com/problem/content/)



```cpp
```

[1500.](https://www.acwing.com/problem/content/)



```cpp
```

### 1501~2000

#### 1501~1600

[1501.](https://www.acwing.com/problem/content/)



```cpp
```

[1502.](https://www.acwing.com/problem/content/)



```cpp
```

[1503.](https://www.acwing.com/problem/content/)



```cpp
```

[1504.](https://www.acwing.com/problem/content/)



```cpp
```

[1505.](https://www.acwing.com/problem/content/)



```cpp
```

[1506.](https://www.acwing.com/problem/content/)



```cpp
```

[1507.](https://www.acwing.com/problem/content/)



```cpp
```

[1508.](https://www.acwing.com/problem/content/)



```cpp
```

[1509.](https://www.acwing.com/problem/content/)



```cpp
```

[1510.](https://www.acwing.com/problem/content/)



```cpp
```

[1511.](https://www.acwing.com/problem/content/)



```cpp
```

[1512.](https://www.acwing.com/problem/content/)



```cpp
```

[1513.](https://www.acwing.com/problem/content/)



```cpp
```

[1514.](https://www.acwing.com/problem/content/)



```cpp
```

[1515.](https://www.acwing.com/problem/content/)



```cpp
```

[1516.](https://www.acwing.com/problem/content/)



```cpp
```

[1517.](https://www.acwing.com/problem/content/)



```cpp
```

[1518.](https://www.acwing.com/problem/content/)



```cpp
```

[1519.](https://www.acwing.com/problem/content/)



```cpp
```

[1520.](https://www.acwing.com/problem/content/)



```cpp
```

[1521.](https://www.acwing.com/problem/content/)



```cpp
```

[1522.](https://www.acwing.com/problem/content/)



```cpp
```

[1523.](https://www.acwing.com/problem/content/)



```cpp
```

[1524.](https://www.acwing.com/problem/content/)



```cpp
```

[1525.](https://www.acwing.com/problem/content/)



```cpp
```

[1526.](https://www.acwing.com/problem/content/)



```cpp
```

[1527.](https://www.acwing.com/problem/content/)



```cpp
```

[1528.](https://www.acwing.com/problem/content/)



```cpp
```

[1529.](https://www.acwing.com/problem/content/)



```cpp
```

[1530.](https://www.acwing.com/problem/content/)



```cpp
```

[1531.](https://www.acwing.com/problem/content/)



```cpp
```

[1532.](https://www.acwing.com/problem/content/)



```cpp
```

[1533.](https://www.acwing.com/problem/content/)



```cpp
```

[1534.](https://www.acwing.com/problem/content/)



```cpp
```

[1535.](https://www.acwing.com/problem/content/)



```cpp
```

[1536.](https://www.acwing.com/problem/content/)



```cpp
```

[1537.](https://www.acwing.com/problem/content/)



```cpp
```

[1538.](https://www.acwing.com/problem/content/)



```cpp
```

[1539.](https://www.acwing.com/problem/content/)



```cpp
```

[1540.](https://www.acwing.com/problem/content/)



```cpp
```

[1541.](https://www.acwing.com/problem/content/)



```cpp
```

[1542.](https://www.acwing.com/problem/content/)



```cpp
```

[1543.](https://www.acwing.com/problem/content/)



```cpp
```

[1544.](https://www.acwing.com/problem/content/)



```cpp
```

[1545.](https://www.acwing.com/problem/content/)



```cpp
```

[1546.](https://www.acwing.com/problem/content/)



```cpp
```

[1547.](https://www.acwing.com/problem/content/)



```cpp
```

[1548.](https://www.acwing.com/problem/content/)



```cpp
```

[1549.](https://www.acwing.com/problem/content/)



```cpp
```

[1550.](https://www.acwing.com/problem/content/)



```cpp
```

[1551.](https://www.acwing.com/problem/content/)



```cpp
```

[1552.](https://www.acwing.com/problem/content/)



```cpp
```

[1553.](https://www.acwing.com/problem/content/)



```cpp
```

[1554.](https://www.acwing.com/problem/content/)



```cpp
```

[1555.](https://www.acwing.com/problem/content/)



```cpp
```

[1556.](https://www.acwing.com/problem/content/)



```cpp
```

[1557.](https://www.acwing.com/problem/content/)



```cpp
```

[1558.](https://www.acwing.com/problem/content/)



```cpp
```

[1559.](https://www.acwing.com/problem/content/)



```cpp
```

[1560.](https://www.acwing.com/problem/content/)



```cpp
```

[1561.](https://www.acwing.com/problem/content/)



```cpp
```

[1562.](https://www.acwing.com/problem/content/)



```cpp
```

[1563.](https://www.acwing.com/problem/content/)



```cpp
```

[1564.](https://www.acwing.com/problem/content/)



```cpp
```

[1565.](https://www.acwing.com/problem/content/)



```cpp
```

[1566.](https://www.acwing.com/problem/content/)



```cpp
```

[1567.](https://www.acwing.com/problem/content/)



```cpp
```

[1568.](https://www.acwing.com/problem/content/)



```cpp
```

[1569.](https://www.acwing.com/problem/content/)



```cpp
```

[1570.](https://www.acwing.com/problem/content/)



```cpp
```

[1571.](https://www.acwing.com/problem/content/)



```cpp
```

[1572.](https://www.acwing.com/problem/content/)



```cpp
```

[1573.](https://www.acwing.com/problem/content/)



```cpp
```

[1574.](https://www.acwing.com/problem/content/)



```cpp
```

[1575.](https://www.acwing.com/problem/content/)



```cpp
```

[1576.](https://www.acwing.com/problem/content/)



```cpp
```

[1577.](https://www.acwing.com/problem/content/)



```cpp
```

[1578.](https://www.acwing.com/problem/content/)



```cpp
```

[1579.](https://www.acwing.com/problem/content/)



```cpp
```

[1580.](https://www.acwing.com/problem/content/)



```cpp
```

[1581.](https://www.acwing.com/problem/content/)



```cpp
```

[1582.](https://www.acwing.com/problem/content/)



```cpp
```

[1583.](https://www.acwing.com/problem/content/)



```cpp
```

[1584.](https://www.acwing.com/problem/content/)



```cpp
```

[1585.](https://www.acwing.com/problem/content/)



```cpp
```

[1586.](https://www.acwing.com/problem/content/)



```cpp
```

[1587.](https://www.acwing.com/problem/content/)



```cpp
```

[1588.](https://www.acwing.com/problem/content/)



```cpp
```

[1589.](https://www.acwing.com/problem/content/)



```cpp
```

[1590.](https://www.acwing.com/problem/content/)



```cpp
```

[1591.](https://www.acwing.com/problem/content/)



```cpp
```

[1592.](https://www.acwing.com/problem/content/)



```cpp
```

[1593.](https://www.acwing.com/problem/content/)



```cpp
```

[1594.](https://www.acwing.com/problem/content/)



```cpp
```

[1595.](https://www.acwing.com/problem/content/)



```cpp
```

[1596.](https://www.acwing.com/problem/content/)



```cpp
```

[1597.](https://www.acwing.com/problem/content/)



```cpp
```

[1598.](https://www.acwing.com/problem/content/)



```cpp
```

[1599.](https://www.acwing.com/problem/content/)



```cpp
```

[1600.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1601~1700

[1601.](https://www.acwing.com/problem/content/)



```cpp
```

[1602.](https://www.acwing.com/problem/content/)



```cpp
```

[1603.](https://www.acwing.com/problem/content/)



```cpp
```

[1604.](https://www.acwing.com/problem/content/)



```cpp
```

[1605.](https://www.acwing.com/problem/content/)



```cpp
```

[1606.](https://www.acwing.com/problem/content/)



```cpp
```

[1607.](https://www.acwing.com/problem/content/)



```cpp
```

[1608.](https://www.acwing.com/problem/content/)



```cpp
```

[1609.](https://www.acwing.com/problem/content/)



```cpp
```

[1610.](https://www.acwing.com/problem/content/)



```cpp
```

[1611.](https://www.acwing.com/problem/content/)



```cpp
```

[1612.](https://www.acwing.com/problem/content/)



```cpp
```

[1613.](https://www.acwing.com/problem/content/)



```cpp
```

[1614.](https://www.acwing.com/problem/content/)



```cpp
```

[1615.](https://www.acwing.com/problem/content/)



```cpp
```

[1616.](https://www.acwing.com/problem/content/)



```cpp
```

[1617.](https://www.acwing.com/problem/content/)



```cpp
```

[1618.](https://www.acwing.com/problem/content/)



```cpp
```

[1619.](https://www.acwing.com/problem/content/)



```cpp
```

[1620.](https://www.acwing.com/problem/content/)



```cpp
```

[1621.](https://www.acwing.com/problem/content/)



```cpp
```

[1622.](https://www.acwing.com/problem/content/)



```cpp
```

[1623.](https://www.acwing.com/problem/content/)



```cpp
```

[1624.](https://www.acwing.com/problem/content/)



```cpp
```

[1625.](https://www.acwing.com/problem/content/)



```cpp
```

[1626.](https://www.acwing.com/problem/content/)



```cpp
```

[1627.](https://www.acwing.com/problem/content/)



```cpp
```

[1628.](https://www.acwing.com/problem/content/)



```cpp
```

[1629.](https://www.acwing.com/problem/content/)



```cpp
```

[1630.](https://www.acwing.com/problem/content/)



```cpp
```

[1631.](https://www.acwing.com/problem/content/)



```cpp
```

[1632.](https://www.acwing.com/problem/content/)



```cpp
```

[1633.](https://www.acwing.com/problem/content/)



```cpp
```

[1634.](https://www.acwing.com/problem/content/)



```cpp
```

[1635.](https://www.acwing.com/problem/content/)



```cpp
```

[1636.](https://www.acwing.com/problem/content/)



```cpp
```

[1637.](https://www.acwing.com/problem/content/)



```cpp
```

[1638.](https://www.acwing.com/problem/content/)



```cpp
```

[1639.](https://www.acwing.com/problem/content/)



```cpp
```

[1640.](https://www.acwing.com/problem/content/)



```cpp
```

[1641.](https://www.acwing.com/problem/content/)



```cpp
```

[1642.](https://www.acwing.com/problem/content/)



```cpp
```

[1643.](https://www.acwing.com/problem/content/)



```cpp
```

[1644.](https://www.acwing.com/problem/content/)



```cpp
```

[1645.](https://www.acwing.com/problem/content/)



```cpp
```

[1646.](https://www.acwing.com/problem/content/)



```cpp
```

[1647.](https://www.acwing.com/problem/content/)



```cpp
```

[1648.](https://www.acwing.com/problem/content/)



```cpp
```

[1649.](https://www.acwing.com/problem/content/)



```cpp
```

[1650.](https://www.acwing.com/problem/content/)



```cpp
```

[1651.](https://www.acwing.com/problem/content/)



```cpp
```

[1652.](https://www.acwing.com/problem/content/)



```cpp
```

[1653.](https://www.acwing.com/problem/content/)



```cpp
```

[1654.](https://www.acwing.com/problem/content/)



```cpp
```

[1655.](https://www.acwing.com/problem/content/)



```cpp
```

[1656.](https://www.acwing.com/problem/content/)



```cpp
```

[1657.](https://www.acwing.com/problem/content/)



```cpp
```

[1658.](https://www.acwing.com/problem/content/)



```cpp
```

[1659.](https://www.acwing.com/problem/content/)



```cpp
```

[1660.](https://www.acwing.com/problem/content/)



```cpp
```

[1661.](https://www.acwing.com/problem/content/)



```cpp
```

[1662.](https://www.acwing.com/problem/content/)



```cpp
```

[1663.](https://www.acwing.com/problem/content/)



```cpp
```

[1664.](https://www.acwing.com/problem/content/)



```cpp
```

[1665.](https://www.acwing.com/problem/content/)



```cpp
```

[1666.](https://www.acwing.com/problem/content/)



```cpp
```

[1667.](https://www.acwing.com/problem/content/)



```cpp
```

[1668.](https://www.acwing.com/problem/content/)



```cpp
```

[1669.](https://www.acwing.com/problem/content/)



```cpp
```

[1670.](https://www.acwing.com/problem/content/)



```cpp
```

[1671.](https://www.acwing.com/problem/content/)



```cpp
```

[1672.](https://www.acwing.com/problem/content/)



```cpp
```

[1673.](https://www.acwing.com/problem/content/)



```cpp
```

[1674.](https://www.acwing.com/problem/content/)



```cpp
```

[1675.](https://www.acwing.com/problem/content/)



```cpp
```

[1676.](https://www.acwing.com/problem/content/)



```cpp
```

[1677.](https://www.acwing.com/problem/content/)



```cpp
```

[1678.](https://www.acwing.com/problem/content/)



```cpp
```

[1679.](https://www.acwing.com/problem/content/)



```cpp
```

[1680.](https://www.acwing.com/problem/content/)



```cpp
```

[1681.](https://www.acwing.com/problem/content/)



```cpp
```

[1682.](https://www.acwing.com/problem/content/)



```cpp
```

[1683.](https://www.acwing.com/problem/content/)



```cpp
```

[1684.](https://www.acwing.com/problem/content/)



```cpp
```

[1685.](https://www.acwing.com/problem/content/)



```cpp
```

[1686.](https://www.acwing.com/problem/content/)



```cpp
```

[1687.](https://www.acwing.com/problem/content/)



```cpp
```

[1688.](https://www.acwing.com/problem/content/)



```cpp
```

[1689.](https://www.acwing.com/problem/content/)



```cpp
```

[1690.](https://www.acwing.com/problem/content/)



```cpp
```

[1691.](https://www.acwing.com/problem/content/)



```cpp
```

[1692.](https://www.acwing.com/problem/content/)



```cpp
```

[1693.](https://www.acwing.com/problem/content/)



```cpp
```

[1694.](https://www.acwing.com/problem/content/)



```cpp
```

[1695.](https://www.acwing.com/problem/content/)



```cpp
```

[1696.](https://www.acwing.com/problem/content/)



```cpp
```

[1697.](https://www.acwing.com/problem/content/)



```cpp
```

[1698.](https://www.acwing.com/problem/content/)



```cpp
```

[1699.](https://www.acwing.com/problem/content/)



```cpp
```

[1700.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1701~1800

[1701.](https://www.acwing.com/problem/content/)



```cpp
```

[1702.](https://www.acwing.com/problem/content/)



```cpp
```

[1703.](https://www.acwing.com/problem/content/)



```cpp
```

[1704.](https://www.acwing.com/problem/content/)



```cpp
```

[1705.](https://www.acwing.com/problem/content/)



```cpp
```

[1706.](https://www.acwing.com/problem/content/)



```cpp
```

[1707.](https://www.acwing.com/problem/content/)



```cpp
```

[1708.](https://www.acwing.com/problem/content/)



```cpp
```

[1709.](https://www.acwing.com/problem/content/)



```cpp
```

[1710.](https://www.acwing.com/problem/content/)



```cpp
```

[1711.](https://www.acwing.com/problem/content/)



```cpp
```

[1712.](https://www.acwing.com/problem/content/)



```cpp
```

[1713.](https://www.acwing.com/problem/content/)



```cpp
```

[1714.](https://www.acwing.com/problem/content/)



```cpp
```

[1715.](https://www.acwing.com/problem/content/)



```cpp
```

[1716.](https://www.acwing.com/problem/content/)



```cpp
```

[1717.](https://www.acwing.com/problem/content/)



```cpp
```

[1718.](https://www.acwing.com/problem/content/)



```cpp
```

[1719.](https://www.acwing.com/problem/content/)



```cpp
```

[1720.](https://www.acwing.com/problem/content/)



```cpp
```

[1721.](https://www.acwing.com/problem/content/)



```cpp
```

[1722.](https://www.acwing.com/problem/content/)



```cpp
```

[1723.](https://www.acwing.com/problem/content/)



```cpp
```

[1724.](https://www.acwing.com/problem/content/)



```cpp
```

[1725.](https://www.acwing.com/problem/content/)



```cpp
```

[1726.](https://www.acwing.com/problem/content/)



```cpp
```

[1727.](https://www.acwing.com/problem/content/)



```cpp
```

[1728.](https://www.acwing.com/problem/content/)



```cpp
```

[1729.](https://www.acwing.com/problem/content/)



```cpp
```

[1730.](https://www.acwing.com/problem/content/)



```cpp
```

[1731.](https://www.acwing.com/problem/content/)



```cpp
```

[1732.](https://www.acwing.com/problem/content/)



```cpp
```

[1733.](https://www.acwing.com/problem/content/)



```cpp
```

[1734.](https://www.acwing.com/problem/content/)



```cpp
```

[1735.](https://www.acwing.com/problem/content/)



```cpp
```

[1736.](https://www.acwing.com/problem/content/)



```cpp
```

[1737.](https://www.acwing.com/problem/content/)



```cpp
```

[1738.](https://www.acwing.com/problem/content/)



```cpp
```

[1739.](https://www.acwing.com/problem/content/)



```cpp
```

[1740.](https://www.acwing.com/problem/content/)



```cpp
```

[1741.](https://www.acwing.com/problem/content/)



```cpp
```

[1742.](https://www.acwing.com/problem/content/)



```cpp
```

[1743.](https://www.acwing.com/problem/content/)



```cpp
```

[1744.](https://www.acwing.com/problem/content/)



```cpp
```

[1745.](https://www.acwing.com/problem/content/)



```cpp
```

[1746.](https://www.acwing.com/problem/content/)



```cpp
```

[1747.](https://www.acwing.com/problem/content/)



```cpp
```

[1748.](https://www.acwing.com/problem/content/)



```cpp
```

[1749.](https://www.acwing.com/problem/content/)



```cpp
```

[1750.](https://www.acwing.com/problem/content/)



```cpp
```

[1751.](https://www.acwing.com/problem/content/)



```cpp
```

[1752.](https://www.acwing.com/problem/content/)



```cpp
```

[1753.](https://www.acwing.com/problem/content/)



```cpp
```

[1754.](https://www.acwing.com/problem/content/)



```cpp
```

[1755.](https://www.acwing.com/problem/content/)



```cpp
```

[1756.](https://www.acwing.com/problem/content/)



```cpp
```

[1757.](https://www.acwing.com/problem/content/)



```cpp
```

[1758.](https://www.acwing.com/problem/content/)



```cpp
```

[1759.](https://www.acwing.com/problem/content/)



```cpp
```

[1760.](https://www.acwing.com/problem/content/)



```cpp
```

[1761.](https://www.acwing.com/problem/content/)



```cpp
```

[1762.](https://www.acwing.com/problem/content/)



```cpp
```

[1763.](https://www.acwing.com/problem/content/)



```cpp
```

[1764.](https://www.acwing.com/problem/content/)



```cpp
```

[1765.](https://www.acwing.com/problem/content/)



```cpp
```

[1766.](https://www.acwing.com/problem/content/)



```cpp
```

[1767.](https://www.acwing.com/problem/content/)



```cpp
```

[1768.](https://www.acwing.com/problem/content/)



```cpp
```

[1769.](https://www.acwing.com/problem/content/)



```cpp
```

[1770.](https://www.acwing.com/problem/content/)



```cpp
```

[1771.](https://www.acwing.com/problem/content/)



```cpp
```

[1772.](https://www.acwing.com/problem/content/)



```cpp
```

[1773.](https://www.acwing.com/problem/content/)



```cpp
```

[1774.](https://www.acwing.com/problem/content/)



```cpp
```

[1775.](https://www.acwing.com/problem/content/)



```cpp
```

[1776.](https://www.acwing.com/problem/content/)



```cpp
```

[1777.](https://www.acwing.com/problem/content/)



```cpp
```

[1778.](https://www.acwing.com/problem/content/)



```cpp
```

[1779.](https://www.acwing.com/problem/content/)



```cpp
```

[1780.](https://www.acwing.com/problem/content/)



```cpp
```

[1781.](https://www.acwing.com/problem/content/)



```cpp
```

[1782.](https://www.acwing.com/problem/content/)



```cpp
```

[1783.](https://www.acwing.com/problem/content/)



```cpp
```

[1784.](https://www.acwing.com/problem/content/)



```cpp
```

[1785.](https://www.acwing.com/problem/content/)



```cpp
```

[1786.](https://www.acwing.com/problem/content/)



```cpp
```

[1787.](https://www.acwing.com/problem/content/)



```cpp
```

[1788.](https://www.acwing.com/problem/content/)



```cpp
```

[1789.](https://www.acwing.com/problem/content/)



```cpp
```

[1790.](https://www.acwing.com/problem/content/)



```cpp
```

[1791.](https://www.acwing.com/problem/content/)



```cpp
```

[1792.](https://www.acwing.com/problem/content/)



```cpp
```

[1793.](https://www.acwing.com/problem/content/)



```cpp
```

[1794.](https://www.acwing.com/problem/content/)



```cpp
```

[1795.](https://www.acwing.com/problem/content/)



```cpp
```

[1796.](https://www.acwing.com/problem/content/)



```cpp
```

[1797.](https://www.acwing.com/problem/content/)



```cpp
```

[1798.](https://www.acwing.com/problem/content/)



```cpp
```

[1799.](https://www.acwing.com/problem/content/)



```cpp
```

[1800.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1801~1900

[1801.](https://www.acwing.com/problem/content/)



```cpp
```

[1802.](https://www.acwing.com/problem/content/)



```cpp
```

[1803.](https://www.acwing.com/problem/content/)



```cpp
```

[1804.](https://www.acwing.com/problem/content/)



```cpp
```

[1805.](https://www.acwing.com/problem/content/)



```cpp
```

[1806.](https://www.acwing.com/problem/content/)



```cpp
```

[1807.](https://www.acwing.com/problem/content/)



```cpp
```

[1808.](https://www.acwing.com/problem/content/)



```cpp
```

[1809.](https://www.acwing.com/problem/content/)



```cpp
```

[1810.](https://www.acwing.com/problem/content/)



```cpp
```

[1811.](https://www.acwing.com/problem/content/)



```cpp
```

[1812.](https://www.acwing.com/problem/content/)



```cpp
```

[1813.](https://www.acwing.com/problem/content/)



```cpp
```

[1814.](https://www.acwing.com/problem/content/)



```cpp
```

[1815.](https://www.acwing.com/problem/content/)



```cpp
```

[1816.](https://www.acwing.com/problem/content/)



```cpp
```

[1817.](https://www.acwing.com/problem/content/)



```cpp
```

[1818.](https://www.acwing.com/problem/content/)



```cpp
```

[1819.](https://www.acwing.com/problem/content/)



```cpp
```

[1820.](https://www.acwing.com/problem/content/)



```cpp
```

[1821.](https://www.acwing.com/problem/content/)



```cpp
```

[1822.](https://www.acwing.com/problem/content/)



```cpp
```

[1823.](https://www.acwing.com/problem/content/)



```cpp
```

[1824.](https://www.acwing.com/problem/content/)



```cpp
```

[1825.](https://www.acwing.com/problem/content/)



```cpp
```

[1826.](https://www.acwing.com/problem/content/)



```cpp
```

[1827.](https://www.acwing.com/problem/content/)



```cpp
```

[1828.](https://www.acwing.com/problem/content/)



```cpp
```

[1829.](https://www.acwing.com/problem/content/)



```cpp
```

[1830.](https://www.acwing.com/problem/content/)



```cpp
```

[1831.](https://www.acwing.com/problem/content/)



```cpp
```

[1832.](https://www.acwing.com/problem/content/)



```cpp
```

[1833.](https://www.acwing.com/problem/content/)



```cpp
```

[1834.](https://www.acwing.com/problem/content/)



```cpp
```

[1835.](https://www.acwing.com/problem/content/)



```cpp
```

[1836.](https://www.acwing.com/problem/content/)



```cpp
```

[1837.](https://www.acwing.com/problem/content/)



```cpp
```

[1838.](https://www.acwing.com/problem/content/)



```cpp
```

[1839.](https://www.acwing.com/problem/content/)



```cpp
```

[1840.](https://www.acwing.com/problem/content/)



```cpp
```

[1841.](https://www.acwing.com/problem/content/)



```cpp
```

[1842.](https://www.acwing.com/problem/content/)



```cpp
```

[1843.](https://www.acwing.com/problem/content/)



```cpp
```

[1844.](https://www.acwing.com/problem/content/)



```cpp
```

[1845.](https://www.acwing.com/problem/content/)



```cpp
```

[1846.](https://www.acwing.com/problem/content/)



```cpp
```

[1847.](https://www.acwing.com/problem/content/)



```cpp
```

[1848.](https://www.acwing.com/problem/content/)



```cpp
```

[1849.](https://www.acwing.com/problem/content/)



```cpp
```

[1850.](https://www.acwing.com/problem/content/)



```cpp
```

[1851.](https://www.acwing.com/problem/content/)



```cpp
```

[1852.](https://www.acwing.com/problem/content/)



```cpp
```

[1853.](https://www.acwing.com/problem/content/)



```cpp
```

[1854.](https://www.acwing.com/problem/content/)



```cpp
```

[1855.](https://www.acwing.com/problem/content/)



```cpp
```

[1856.](https://www.acwing.com/problem/content/)



```cpp
```

[1857.](https://www.acwing.com/problem/content/)



```cpp
```

[1858.](https://www.acwing.com/problem/content/)



```cpp
```

[1859.](https://www.acwing.com/problem/content/)



```cpp
```

[1860.](https://www.acwing.com/problem/content/)



```cpp
```

[1861.](https://www.acwing.com/problem/content/)



```cpp
```

[1862.](https://www.acwing.com/problem/content/)



```cpp
```

[1863.](https://www.acwing.com/problem/content/)



```cpp
```

[1864.](https://www.acwing.com/problem/content/)



```cpp
```

[1865.](https://www.acwing.com/problem/content/)



```cpp
```

[1866.](https://www.acwing.com/problem/content/)



```cpp
```

[1867.](https://www.acwing.com/problem/content/)



```cpp
```

[1868.](https://www.acwing.com/problem/content/)



```cpp
```

[1869.](https://www.acwing.com/problem/content/)



```cpp
```

[1870.](https://www.acwing.com/problem/content/)



```cpp
```

[1871.](https://www.acwing.com/problem/content/)



```cpp
```

[1872.](https://www.acwing.com/problem/content/)



```cpp
```

[1873.](https://www.acwing.com/problem/content/)



```cpp
```

[1874.](https://www.acwing.com/problem/content/)



```cpp
```

[1875.](https://www.acwing.com/problem/content/)



```cpp
```

[1876.](https://www.acwing.com/problem/content/)



```cpp
```

[1877.](https://www.acwing.com/problem/content/)



```cpp
```

[1878.](https://www.acwing.com/problem/content/)



```cpp
```

[1879.](https://www.acwing.com/problem/content/)



```cpp
```

[1880.](https://www.acwing.com/problem/content/)



```cpp
```

[1881.](https://www.acwing.com/problem/content/)



```cpp
```

[1882.](https://www.acwing.com/problem/content/)



```cpp
```

[1883.](https://www.acwing.com/problem/content/)



```cpp
```

[1884.](https://www.acwing.com/problem/content/)



```cpp
```

[1885.](https://www.acwing.com/problem/content/)



```cpp
```

[1886.](https://www.acwing.com/problem/content/)



```cpp
```

[1887.](https://www.acwing.com/problem/content/)



```cpp
```

[1888.](https://www.acwing.com/problem/content/)



```cpp
```

[1889.](https://www.acwing.com/problem/content/)



```cpp
```

[1890.](https://www.acwing.com/problem/content/)



```cpp
```

[1891.](https://www.acwing.com/problem/content/)



```cpp
```

[1892.](https://www.acwing.com/problem/content/)



```cpp
```

[1893.](https://www.acwing.com/problem/content/)



```cpp
```

[1894.](https://www.acwing.com/problem/content/)



```cpp
```

[1895.](https://www.acwing.com/problem/content/)



```cpp
```

[1896.](https://www.acwing.com/problem/content/)



```cpp
```

[1897.](https://www.acwing.com/problem/content/)



```cpp
```

[1898.](https://www.acwing.com/problem/content/)



```cpp
```

[1899.](https://www.acwing.com/problem/content/)



```cpp
```

[1900.](https://www.acwing.com/problem/content/)



```cpp
```

#### 1901~2000

[1901.](https://www.acwing.com/problem/content/)



```cpp
```

[1902.](https://www.acwing.com/problem/content/)



```cpp
```

[1903.](https://www.acwing.com/problem/content/)



```cpp
```

[1904.](https://www.acwing.com/problem/content/)



```cpp
```

[1905.](https://www.acwing.com/problem/content/)



```cpp
```

[1906.](https://www.acwing.com/problem/content/)



```cpp
```

[1907.](https://www.acwing.com/problem/content/)



```cpp
```

[1908.](https://www.acwing.com/problem/content/)



```cpp
```

[1909.](https://www.acwing.com/problem/content/)



```cpp
```

[1910.](https://www.acwing.com/problem/content/)



```cpp
```

[1911.](https://www.acwing.com/problem/content/)



```cpp
```

[1912.](https://www.acwing.com/problem/content/)



```cpp
```

[1913.](https://www.acwing.com/problem/content/)



```cpp
```

[1914.](https://www.acwing.com/problem/content/)



```cpp
```

[1915.](https://www.acwing.com/problem/content/)



```cpp
```

[1916.](https://www.acwing.com/problem/content/)



```cpp
```

[1917.](https://www.acwing.com/problem/content/)



```cpp
```

[1918.](https://www.acwing.com/problem/content/)



```cpp
```

[1919.](https://www.acwing.com/problem/content/)



```cpp
```

[1920.](https://www.acwing.com/problem/content/)



```cpp
```

[1921.](https://www.acwing.com/problem/content/)



```cpp
```

[1922.](https://www.acwing.com/problem/content/)



```cpp
```

[1923.](https://www.acwing.com/problem/content/)



```cpp
```

[1924.](https://www.acwing.com/problem/content/)



```cpp
```

[1925.](https://www.acwing.com/problem/content/)



```cpp
```

[1926.](https://www.acwing.com/problem/content/)



```cpp
```

[1927.](https://www.acwing.com/problem/content/)



```cpp
```

[1928.](https://www.acwing.com/problem/content/)



```cpp
```

[1929.](https://www.acwing.com/problem/content/)



```cpp
```

[1930.](https://www.acwing.com/problem/content/)



```cpp
```

[1931.](https://www.acwing.com/problem/content/)



```cpp
```

[1932.](https://www.acwing.com/problem/content/)



```cpp
```

[1933.](https://www.acwing.com/problem/content/)



```cpp
```

[1934.](https://www.acwing.com/problem/content/)



```cpp
```

[1935.](https://www.acwing.com/problem/content/)



```cpp
```

[1936.](https://www.acwing.com/problem/content/)



```cpp
```

[1937.](https://www.acwing.com/problem/content/)



```cpp
```

[1938.](https://www.acwing.com/problem/content/)



```cpp
```

[1939.](https://www.acwing.com/problem/content/)



```cpp
```

[1940.](https://www.acwing.com/problem/content/)



```cpp
```

[1941.](https://www.acwing.com/problem/content/)



```cpp
```

[1942.](https://www.acwing.com/problem/content/)



```cpp
```

[1943.](https://www.acwing.com/problem/content/)



```cpp
```

[1944.](https://www.acwing.com/problem/content/)



```cpp
```

[1945.](https://www.acwing.com/problem/content/)



```cpp
```

[1946.](https://www.acwing.com/problem/content/)



```cpp
```

[1947.](https://www.acwing.com/problem/content/)



```cpp
```

[1948.](https://www.acwing.com/problem/content/)



```cpp
```

[1949.](https://www.acwing.com/problem/content/)



```cpp
```

[1950.](https://www.acwing.com/problem/content/)



```cpp
```

[1951.](https://www.acwing.com/problem/content/)



```cpp
```

[1952.](https://www.acwing.com/problem/content/)



```cpp
```

[1953.](https://www.acwing.com/problem/content/)



```cpp
```

[1954.](https://www.acwing.com/problem/content/)



```cpp
```

[1955.](https://www.acwing.com/problem/content/)



```cpp
```

[1956.](https://www.acwing.com/problem/content/)



```cpp
```

[1957.](https://www.acwing.com/problem/content/)



```cpp
```

[1958.](https://www.acwing.com/problem/content/)



```cpp
```

[1959.](https://www.acwing.com/problem/content/)



```cpp
```

[1960.](https://www.acwing.com/problem/content/)



```cpp
```

[1961.](https://www.acwing.com/problem/content/)



```cpp
```

[1962.](https://www.acwing.com/problem/content/)



```cpp
```

[1963.](https://www.acwing.com/problem/content/)



```cpp
```

[1964.](https://www.acwing.com/problem/content/)



```cpp
```

[1965.](https://www.acwing.com/problem/content/)



```cpp
```

[1966.](https://www.acwing.com/problem/content/)



```cpp
```

[1967.](https://www.acwing.com/problem/content/)



```cpp
```

[1968.](https://www.acwing.com/problem/content/)



```cpp
```

[1969.](https://www.acwing.com/problem/content/)



```cpp
```

[1970.](https://www.acwing.com/problem/content/)



```cpp
```

[1971.](https://www.acwing.com/problem/content/)



```cpp
```

[1972.](https://www.acwing.com/problem/content/)



```cpp
```

[1973.](https://www.acwing.com/problem/content/)



```cpp
```

[1974.](https://www.acwing.com/problem/content/)



```cpp
```

[1975.](https://www.acwing.com/problem/content/)



```cpp
```

[1976.](https://www.acwing.com/problem/content/)



```cpp
```

[1977.](https://www.acwing.com/problem/content/)



```cpp
```

[1978.](https://www.acwing.com/problem/content/)



```cpp
```

[1979.](https://www.acwing.com/problem/content/)



```cpp
```

[1980.](https://www.acwing.com/problem/content/)



```cpp
```

[1981.](https://www.acwing.com/problem/content/)



```cpp
```

[1982.](https://www.acwing.com/problem/content/)



```cpp
```

[1983.](https://www.acwing.com/problem/content/)



```cpp
```

[1984.](https://www.acwing.com/problem/content/)



```cpp
```

[1985.](https://www.acwing.com/problem/content/)



```cpp
```

[1986.](https://www.acwing.com/problem/content/)



```cpp
```

[1987.](https://www.acwing.com/problem/content/)



```cpp
```

[1988.](https://www.acwing.com/problem/content/)



```cpp
```

[1989.](https://www.acwing.com/problem/content/)



```cpp
```

[1990.](https://www.acwing.com/problem/content/)



```cpp
```

[1991.](https://www.acwing.com/problem/content/)



```cpp
```

[1992.](https://www.acwing.com/problem/content/)



```cpp
```

[1993.](https://www.acwing.com/problem/content/)



```cpp
```

[1994.](https://www.acwing.com/problem/content/)



```cpp
```

[1995.](https://www.acwing.com/problem/content/)



```cpp
```

[1996.](https://www.acwing.com/problem/content/)



```cpp
```

[1997.](https://www.acwing.com/problem/content/)



```cpp
```

[1998.](https://www.acwing.com/problem/content/)



```cpp
```

[1999.](https://www.acwing.com/problem/content/)



```cpp
```

[2000.](https://www.acwing.com/problem/content/)



```cpp
```

## 2001~3000

### 2001~2500

#### 2001~2100

[2001.](https://www.acwing.com/problem/content/)



```cpp
```

[2002.](https://www.acwing.com/problem/content/)



```cpp
```

[2003.](https://www.acwing.com/problem/content/)



```cpp
```

[2004.](https://www.acwing.com/problem/content/)



```cpp
```

[2005.](https://www.acwing.com/problem/content/)



```cpp
```

[2006.](https://www.acwing.com/problem/content/)



```cpp
```

[2007.](https://www.acwing.com/problem/content/)



```cpp
```

[2008.](https://www.acwing.com/problem/content/)



```cpp
```

[2009.](https://www.acwing.com/problem/content/)



```cpp
```

[2010.](https://www.acwing.com/problem/content/)



```cpp
```

[2011.](https://www.acwing.com/problem/content/)



```cpp
```

[2012.](https://www.acwing.com/problem/content/)



```cpp
```

[2013.](https://www.acwing.com/problem/content/)



```cpp
```

[2014.](https://www.acwing.com/problem/content/)



```cpp
```

[2015.](https://www.acwing.com/problem/content/)



```cpp
```

[2016.](https://www.acwing.com/problem/content/)



```cpp
```

[2017.](https://www.acwing.com/problem/content/)



```cpp
```

[2018.](https://www.acwing.com/problem/content/)



```cpp
```

[2019.](https://www.acwing.com/problem/content/)



```cpp
```

[2020.](https://www.acwing.com/problem/content/)



```cpp
```

[2021.](https://www.acwing.com/problem/content/)



```cpp
```

[2022.](https://www.acwing.com/problem/content/)



```cpp
```

[2023.](https://www.acwing.com/problem/content/)



```cpp
```

[2024.](https://www.acwing.com/problem/content/)



```cpp
```

[2025.](https://www.acwing.com/problem/content/)



```cpp
```

[2026.](https://www.acwing.com/problem/content/)



```cpp
```

[2027.](https://www.acwing.com/problem/content/)



```cpp
```

[2028.](https://www.acwing.com/problem/content/)



```cpp
```

[2029.](https://www.acwing.com/problem/content/)



```cpp
```

[2030.](https://www.acwing.com/problem/content/)



```cpp
```

[2031.](https://www.acwing.com/problem/content/)



```cpp
```

[2032.](https://www.acwing.com/problem/content/)



```cpp
```

[2033.](https://www.acwing.com/problem/content/)



```cpp
```

[2034.](https://www.acwing.com/problem/content/)



```cpp
```

[2035.](https://www.acwing.com/problem/content/)



```cpp
```

[2036.](https://www.acwing.com/problem/content/)



```cpp
```

[2037.](https://www.acwing.com/problem/content/)



```cpp
```

[2038.](https://www.acwing.com/problem/content/)



```cpp
```

[2039.](https://www.acwing.com/problem/content/)



```cpp
```

[2040.](https://www.acwing.com/problem/content/)



```cpp
```

[2041.](https://www.acwing.com/problem/content/)



```cpp
```

[2042.](https://www.acwing.com/problem/content/)



```cpp
```

[2043.](https://www.acwing.com/problem/content/)



```cpp
```

[2044.](https://www.acwing.com/problem/content/)



```cpp
```

[2045.](https://www.acwing.com/problem/content/)



```cpp
```

[2046.](https://www.acwing.com/problem/content/)



```cpp
```

[2047.](https://www.acwing.com/problem/content/)



```cpp
```

[2048.](https://www.acwing.com/problem/content/)



```cpp
```

[2049.](https://www.acwing.com/problem/content/)



```cpp
```

[2050.](https://www.acwing.com/problem/content/)



```cpp
```

[2051.](https://www.acwing.com/problem/content/)



```cpp
```

[2052.](https://www.acwing.com/problem/content/)



```cpp
```

[2053.](https://www.acwing.com/problem/content/)



```cpp
```

[2054.](https://www.acwing.com/problem/content/)



```cpp
```

[2055.](https://www.acwing.com/problem/content/)



```cpp
```

[2056.](https://www.acwing.com/problem/content/)



```cpp
```

[2057.](https://www.acwing.com/problem/content/)



```cpp
```

[2058.](https://www.acwing.com/problem/content/)



```cpp
```

[2059.](https://www.acwing.com/problem/content/)



```cpp
```

[2060.](https://www.acwing.com/problem/content/)



```cpp
```

[2061.](https://www.acwing.com/problem/content/)



```cpp
```

[2062.](https://www.acwing.com/problem/content/)



```cpp
```

[2063.](https://www.acwing.com/problem/content/)



```cpp
```

[2064.](https://www.acwing.com/problem/content/)



```cpp
```

[2065.](https://www.acwing.com/problem/content/)



```cpp
```

[2066.](https://www.acwing.com/problem/content/)



```cpp
```

[2067.](https://www.acwing.com/problem/content/)



```cpp
```

[2068.](https://www.acwing.com/problem/content/)



```cpp
```

[2069.](https://www.acwing.com/problem/content/)



```cpp
```

[2070.](https://www.acwing.com/problem/content/)



```cpp
```

[2071.](https://www.acwing.com/problem/content/)



```cpp
```

[2072.](https://www.acwing.com/problem/content/)



```cpp
```

[2073.](https://www.acwing.com/problem/content/)



```cpp
```

[2074.](https://www.acwing.com/problem/content/)



```cpp
```

[2075.](https://www.acwing.com/problem/content/)



```cpp
```

[2076.](https://www.acwing.com/problem/content/)



```cpp
```

[2077.](https://www.acwing.com/problem/content/)



```cpp
```

[2078.](https://www.acwing.com/problem/content/)



```cpp
```

[2079.](https://www.acwing.com/problem/content/)



```cpp
```

[2080.](https://www.acwing.com/problem/content/)



```cpp
```

[2081.](https://www.acwing.com/problem/content/)



```cpp
```

[2082.](https://www.acwing.com/problem/content/)



```cpp
```

[2083.](https://www.acwing.com/problem/content/)



```cpp
```

[2084.](https://www.acwing.com/problem/content/)



```cpp
```

[2085.](https://www.acwing.com/problem/content/)



```cpp
```

[2086.](https://www.acwing.com/problem/content/)



```cpp
```

[2087.](https://www.acwing.com/problem/content/)



```cpp
```

[2088.](https://www.acwing.com/problem/content/)



```cpp
```

[2089.](https://www.acwing.com/problem/content/)



```cpp
```

[2090.](https://www.acwing.com/problem/content/)



```cpp
```

[2091.](https://www.acwing.com/problem/content/)



```cpp
```

[2092.](https://www.acwing.com/problem/content/)



```cpp
```

[2093.](https://www.acwing.com/problem/content/)



```cpp
```

[2094.](https://www.acwing.com/problem/content/)



```cpp
```

[2095.](https://www.acwing.com/problem/content/)



```cpp
```

[2096.](https://www.acwing.com/problem/content/)



```cpp
```

[2097.](https://www.acwing.com/problem/content/)



```cpp
```

[2098.](https://www.acwing.com/problem/content/)



```cpp
```

[2099.](https://www.acwing.com/problem/content/)



```cpp
```

[2100.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2101~2200

[2101.](https://www.acwing.com/problem/content/)



```cpp
```

[2102.](https://www.acwing.com/problem/content/)



```cpp
```

[2103.](https://www.acwing.com/problem/content/)



```cpp
```

[2104.](https://www.acwing.com/problem/content/)



```cpp
```

[2105.](https://www.acwing.com/problem/content/)



```cpp
```

[2106.](https://www.acwing.com/problem/content/)



```cpp
```

[2107.](https://www.acwing.com/problem/content/)



```cpp
```

[2108.](https://www.acwing.com/problem/content/)



```cpp
```

[2109.](https://www.acwing.com/problem/content/)



```cpp
```

[2110.](https://www.acwing.com/problem/content/)



```cpp
```

[2111.](https://www.acwing.com/problem/content/)



```cpp
```

[2112.](https://www.acwing.com/problem/content/)



```cpp
```

[2113.](https://www.acwing.com/problem/content/)



```cpp
```

[2114.](https://www.acwing.com/problem/content/)



```cpp
```

[2115.](https://www.acwing.com/problem/content/)



```cpp
```

[2116.](https://www.acwing.com/problem/content/)



```cpp
```

[2117.](https://www.acwing.com/problem/content/)



```cpp
```

[2118.](https://www.acwing.com/problem/content/)



```cpp
```

[2119.](https://www.acwing.com/problem/content/)



```cpp
```

[2120.](https://www.acwing.com/problem/content/)



```cpp
```

[2121.](https://www.acwing.com/problem/content/)



```cpp
```

[2122.](https://www.acwing.com/problem/content/)



```cpp
```

[2123.](https://www.acwing.com/problem/content/)



```cpp
```

[2124.](https://www.acwing.com/problem/content/)



```cpp
```

[2125.](https://www.acwing.com/problem/content/)



```cpp
```

[2126.](https://www.acwing.com/problem/content/)



```cpp
```

[2127.](https://www.acwing.com/problem/content/)



```cpp
```

[2128.](https://www.acwing.com/problem/content/)



```cpp
```

[2129.](https://www.acwing.com/problem/content/)



```cpp
```

[2130.](https://www.acwing.com/problem/content/)



```cpp
```

[2131.](https://www.acwing.com/problem/content/)



```cpp
```

[2132.](https://www.acwing.com/problem/content/)



```cpp
```

[2133.](https://www.acwing.com/problem/content/)



```cpp
```

[2134.](https://www.acwing.com/problem/content/)



```cpp
```

[2135.](https://www.acwing.com/problem/content/)



```cpp
```

[2136.](https://www.acwing.com/problem/content/)



```cpp
```

[2137.](https://www.acwing.com/problem/content/)



```cpp
```

[2138.](https://www.acwing.com/problem/content/)



```cpp
```

[2139.](https://www.acwing.com/problem/content/)



```cpp
```

[2140.](https://www.acwing.com/problem/content/)



```cpp
```

[2141.](https://www.acwing.com/problem/content/)



```cpp
```

[2142.](https://www.acwing.com/problem/content/)



```cpp
```

[2143.](https://www.acwing.com/problem/content/)



```cpp
```

[2144.](https://www.acwing.com/problem/content/)



```cpp
```

[2145.](https://www.acwing.com/problem/content/)



```cpp
```

[2146.](https://www.acwing.com/problem/content/)



```cpp
```

[2147.](https://www.acwing.com/problem/content/)



```cpp
```

[2148.](https://www.acwing.com/problem/content/)



```cpp
```

[2149.](https://www.acwing.com/problem/content/)



```cpp
```

[2150.](https://www.acwing.com/problem/content/)



```cpp
```

[2151.](https://www.acwing.com/problem/content/)



```cpp
```

[2152.](https://www.acwing.com/problem/content/)



```cpp
```

[2153.](https://www.acwing.com/problem/content/)



```cpp
```

[2154.](https://www.acwing.com/problem/content/)



```cpp
```

[2155.](https://www.acwing.com/problem/content/)



```cpp
```

[2156.](https://www.acwing.com/problem/content/)



```cpp
```

[2157.](https://www.acwing.com/problem/content/)



```cpp
```

[2158.](https://www.acwing.com/problem/content/)



```cpp
```

[2159.](https://www.acwing.com/problem/content/)



```cpp
```

[2160.](https://www.acwing.com/problem/content/)



```cpp
```

[2161.](https://www.acwing.com/problem/content/)



```cpp
```

[2162.](https://www.acwing.com/problem/content/)



```cpp
```

[2163.](https://www.acwing.com/problem/content/)



```cpp
```

[2164.](https://www.acwing.com/problem/content/)



```cpp
```

[2165.](https://www.acwing.com/problem/content/)



```cpp
```

[2166.](https://www.acwing.com/problem/content/)



```cpp
```

[2167.](https://www.acwing.com/problem/content/)



```cpp
```

[2168.](https://www.acwing.com/problem/content/)



```cpp
```

[2169.](https://www.acwing.com/problem/content/)



```cpp
```

[2170.](https://www.acwing.com/problem/content/)



```cpp
```

[2171.](https://www.acwing.com/problem/content/)



```cpp
```

[2172.](https://www.acwing.com/problem/content/)



```cpp
```

[2173.](https://www.acwing.com/problem/content/)



```cpp
```

[2174.](https://www.acwing.com/problem/content/)



```cpp
```

[2175.](https://www.acwing.com/problem/content/)



```cpp
```

[2176.](https://www.acwing.com/problem/content/)



```cpp
```

[2177.](https://www.acwing.com/problem/content/)



```cpp
```

[2178.](https://www.acwing.com/problem/content/)



```cpp
```

[2179.](https://www.acwing.com/problem/content/)



```cpp
```

[2180.](https://www.acwing.com/problem/content/)



```cpp
```

[2181.](https://www.acwing.com/problem/content/)



```cpp
```

[2182.](https://www.acwing.com/problem/content/)



```cpp
```

[2183.](https://www.acwing.com/problem/content/)



```cpp
```

[2184.](https://www.acwing.com/problem/content/)



```cpp
```

[2185.](https://www.acwing.com/problem/content/)



```cpp
```

[2186.](https://www.acwing.com/problem/content/)



```cpp
```

[2187.](https://www.acwing.com/problem/content/)



```cpp
```

[2188.](https://www.acwing.com/problem/content/)



```cpp
```

[2189.](https://www.acwing.com/problem/content/)



```cpp
```

[2190.](https://www.acwing.com/problem/content/)



```cpp
```

[2191.](https://www.acwing.com/problem/content/)



```cpp
```

[2192.](https://www.acwing.com/problem/content/)



```cpp
```

[2193.](https://www.acwing.com/problem/content/)



```cpp
```

[2194.](https://www.acwing.com/problem/content/)



```cpp
```

[2195.](https://www.acwing.com/problem/content/)



```cpp
```

[2196.](https://www.acwing.com/problem/content/)



```cpp
```

[2197.](https://www.acwing.com/problem/content/)



```cpp
```

[2198.](https://www.acwing.com/problem/content/)



```cpp
```

[2199.](https://www.acwing.com/problem/content/)



```cpp
```

[2200.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2201~2300

[2201.](https://www.acwing.com/problem/content/)



```cpp
```

[2202.](https://www.acwing.com/problem/content/)



```cpp
```

[2203.](https://www.acwing.com/problem/content/)



```cpp
```

[2204.](https://www.acwing.com/problem/content/)



```cpp
```

[2205.](https://www.acwing.com/problem/content/)



```cpp
```

[2206.](https://www.acwing.com/problem/content/)



```cpp
```

[2207.](https://www.acwing.com/problem/content/)



```cpp
```

[2208.](https://www.acwing.com/problem/content/)



```cpp
```

[2209.](https://www.acwing.com/problem/content/)



```cpp
```

[2210.](https://www.acwing.com/problem/content/)



```cpp
```

[2211.](https://www.acwing.com/problem/content/)



```cpp
```

[2212.](https://www.acwing.com/problem/content/)



```cpp
```

[2213.](https://www.acwing.com/problem/content/)



```cpp
```

[2214.](https://www.acwing.com/problem/content/)



```cpp
```

[2215.](https://www.acwing.com/problem/content/)



```cpp
```

[2216.](https://www.acwing.com/problem/content/)



```cpp
```

[2217.](https://www.acwing.com/problem/content/)



```cpp
```

[2218.](https://www.acwing.com/problem/content/)



```cpp
```

[2219.](https://www.acwing.com/problem/content/)



```cpp
```

[2220.](https://www.acwing.com/problem/content/)



```cpp
```

[2221.](https://www.acwing.com/problem/content/)



```cpp
```

[2222.](https://www.acwing.com/problem/content/)



```cpp
```

[2223.](https://www.acwing.com/problem/content/)



```cpp
```

[2224.](https://www.acwing.com/problem/content/)



```cpp
```

[2225.](https://www.acwing.com/problem/content/)



```cpp
```

[2226.](https://www.acwing.com/problem/content/)



```cpp
```

[2227.](https://www.acwing.com/problem/content/)



```cpp
```

[2228.](https://www.acwing.com/problem/content/)



```cpp
```

[2229.](https://www.acwing.com/problem/content/)



```cpp
```

[2230.](https://www.acwing.com/problem/content/)



```cpp
```

[2231.](https://www.acwing.com/problem/content/)



```cpp
```

[2232.](https://www.acwing.com/problem/content/)



```cpp
```

[2233.](https://www.acwing.com/problem/content/)



```cpp
```

[2234.](https://www.acwing.com/problem/content/)



```cpp
```

[2235.](https://www.acwing.com/problem/content/)



```cpp
```

[2236.](https://www.acwing.com/problem/content/)



```cpp
```

[2237.](https://www.acwing.com/problem/content/)



```cpp
```

[2238.](https://www.acwing.com/problem/content/)



```cpp
```

[2239.](https://www.acwing.com/problem/content/)



```cpp
```

[2240.](https://www.acwing.com/problem/content/)



```cpp
```

[2241.](https://www.acwing.com/problem/content/)



```cpp
```

[2242.](https://www.acwing.com/problem/content/)



```cpp
```

[2243.](https://www.acwing.com/problem/content/)



```cpp
```

[2244.](https://www.acwing.com/problem/content/)



```cpp
```

[2245.](https://www.acwing.com/problem/content/)



```cpp
```

[2246.](https://www.acwing.com/problem/content/)



```cpp
```

[2247.](https://www.acwing.com/problem/content/)



```cpp
```

[2248.](https://www.acwing.com/problem/content/)



```cpp
```

[2249.](https://www.acwing.com/problem/content/)



```cpp
```

[2250.](https://www.acwing.com/problem/content/)



```cpp
```

[2251.](https://www.acwing.com/problem/content/)



```cpp
```

[2252.](https://www.acwing.com/problem/content/)



```cpp
```

[2253.](https://www.acwing.com/problem/content/)



```cpp
```

[2254.](https://www.acwing.com/problem/content/)



```cpp
```

[2255.](https://www.acwing.com/problem/content/)



```cpp
```

[2256.](https://www.acwing.com/problem/content/)



```cpp
```

[2257.](https://www.acwing.com/problem/content/)



```cpp
```

[2258.](https://www.acwing.com/problem/content/)



```cpp
```

[2259.](https://www.acwing.com/problem/content/)



```cpp
```

[2260.](https://www.acwing.com/problem/content/)



```cpp
```

[2261.](https://www.acwing.com/problem/content/)



```cpp
```

[2262.](https://www.acwing.com/problem/content/)



```cpp
```

[2263.](https://www.acwing.com/problem/content/)



```cpp
```

[2264.](https://www.acwing.com/problem/content/)



```cpp
```

[2265.](https://www.acwing.com/problem/content/)



```cpp
```

[2266.](https://www.acwing.com/problem/content/)



```cpp
```

[2267.](https://www.acwing.com/problem/content/)



```cpp
```

[2268.](https://www.acwing.com/problem/content/)



```cpp
```

[2269.](https://www.acwing.com/problem/content/)



```cpp
```

[2270.](https://www.acwing.com/problem/content/)



```cpp
```

[2271.](https://www.acwing.com/problem/content/)



```cpp
```

[2272.](https://www.acwing.com/problem/content/)



```cpp
```

[2273.](https://www.acwing.com/problem/content/)



```cpp
```

[2274.](https://www.acwing.com/problem/content/)



```cpp
```

[2275.](https://www.acwing.com/problem/content/)



```cpp
```

[2276.](https://www.acwing.com/problem/content/)



```cpp
```

[2277.](https://www.acwing.com/problem/content/)



```cpp
```

[2278.](https://www.acwing.com/problem/content/)



```cpp
```

[2279.](https://www.acwing.com/problem/content/)



```cpp
```

[2280.](https://www.acwing.com/problem/content/)



```cpp
```

[2281.](https://www.acwing.com/problem/content/)



```cpp
```

[2282.](https://www.acwing.com/problem/content/)



```cpp
```

[2283.](https://www.acwing.com/problem/content/)



```cpp
```

[2284.](https://www.acwing.com/problem/content/)



```cpp
```

[2285.](https://www.acwing.com/problem/content/)



```cpp
```

[2286.](https://www.acwing.com/problem/content/)



```cpp
```

[2287.](https://www.acwing.com/problem/content/)



```cpp
```

[2288.](https://www.acwing.com/problem/content/)



```cpp
```

[2289.](https://www.acwing.com/problem/content/)



```cpp
```

[2290.](https://www.acwing.com/problem/content/)



```cpp
```

[2291.](https://www.acwing.com/problem/content/)



```cpp
```

[2292.](https://www.acwing.com/problem/content/)



```cpp
```

[2293.](https://www.acwing.com/problem/content/)



```cpp
```

[2294.](https://www.acwing.com/problem/content/)



```cpp
```

[2295.](https://www.acwing.com/problem/content/)



```cpp
```

[2296.](https://www.acwing.com/problem/content/)



```cpp
```

[2297.](https://www.acwing.com/problem/content/)



```cpp
```

[2298.](https://www.acwing.com/problem/content/)



```cpp
```

[2299.](https://www.acwing.com/problem/content/)



```cpp
```

[2300.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2301~2400

[2301.](https://www.acwing.com/problem/content/)



```cpp
```

[2302.](https://www.acwing.com/problem/content/)



```cpp
```

[2303.](https://www.acwing.com/problem/content/)



```cpp
```

[2304.](https://www.acwing.com/problem/content/)



```cpp
```

[2305.](https://www.acwing.com/problem/content/)



```cpp
```

[2306.](https://www.acwing.com/problem/content/)



```cpp
```

[2307.](https://www.acwing.com/problem/content/)



```cpp
```

[2308.](https://www.acwing.com/problem/content/)



```cpp
```

[2309.](https://www.acwing.com/problem/content/)



```cpp
```

[2310.](https://www.acwing.com/problem/content/)



```cpp
```

[2311.](https://www.acwing.com/problem/content/)



```cpp
```

[2312.](https://www.acwing.com/problem/content/)



```cpp
```

[2313.](https://www.acwing.com/problem/content/)



```cpp
```

[2314.](https://www.acwing.com/problem/content/)



```cpp
```

[2315.](https://www.acwing.com/problem/content/)



```cpp
```

[2316.](https://www.acwing.com/problem/content/)



```cpp
```

[2317.](https://www.acwing.com/problem/content/)



```cpp
```

[2318.](https://www.acwing.com/problem/content/)



```cpp
```

[2319.](https://www.acwing.com/problem/content/)



```cpp
```

[2320.](https://www.acwing.com/problem/content/)



```cpp
```

[2321.](https://www.acwing.com/problem/content/)



```cpp
```

[2322.](https://www.acwing.com/problem/content/)



```cpp
```

[2323.](https://www.acwing.com/problem/content/)



```cpp
```

[2324.](https://www.acwing.com/problem/content/)



```cpp
```

[2325.](https://www.acwing.com/problem/content/)



```cpp
```

[2326.](https://www.acwing.com/problem/content/)



```cpp
```

[2327.](https://www.acwing.com/problem/content/)



```cpp
```

[2328.](https://www.acwing.com/problem/content/)



```cpp
```

[2329.](https://www.acwing.com/problem/content/)



```cpp
```

[2330.](https://www.acwing.com/problem/content/)



```cpp
```

[2331.](https://www.acwing.com/problem/content/)



```cpp
```

[2332.](https://www.acwing.com/problem/content/)



```cpp
```

[2333.](https://www.acwing.com/problem/content/)



```cpp
```

[2334.](https://www.acwing.com/problem/content/)



```cpp
```

[2335.](https://www.acwing.com/problem/content/)



```cpp
```

[2336.](https://www.acwing.com/problem/content/)



```cpp
```

[2337.](https://www.acwing.com/problem/content/)



```cpp
```

[2338.](https://www.acwing.com/problem/content/)



```cpp
```

[2339.](https://www.acwing.com/problem/content/)



```cpp
```

[2340.](https://www.acwing.com/problem/content/)



```cpp
```

[2341.](https://www.acwing.com/problem/content/)



```cpp
```

[2342.](https://www.acwing.com/problem/content/)



```cpp
```

[2343.](https://www.acwing.com/problem/content/)



```cpp
```

[2344.](https://www.acwing.com/problem/content/)



```cpp
```

[2345.](https://www.acwing.com/problem/content/)



```cpp
```

[2346.](https://www.acwing.com/problem/content/)



```cpp
```

[2347.](https://www.acwing.com/problem/content/)



```cpp
```

[2348.](https://www.acwing.com/problem/content/)



```cpp
```

[2349.](https://www.acwing.com/problem/content/)



```cpp
```

[2350.](https://www.acwing.com/problem/content/)



```cpp
```

[2351.](https://www.acwing.com/problem/content/)



```cpp
```

[2352.](https://www.acwing.com/problem/content/)



```cpp
```

[2353.](https://www.acwing.com/problem/content/)



```cpp
```

[2354.](https://www.acwing.com/problem/content/)



```cpp
```

[2355.](https://www.acwing.com/problem/content/)



```cpp
```

[2356.](https://www.acwing.com/problem/content/)



```cpp
```

[2357.](https://www.acwing.com/problem/content/)



```cpp
```

[2358.](https://www.acwing.com/problem/content/)



```cpp
```

[2359.](https://www.acwing.com/problem/content/)



```cpp
```

[2360.](https://www.acwing.com/problem/content/)



```cpp
```

[2361.](https://www.acwing.com/problem/content/)



```cpp
```

[2362.](https://www.acwing.com/problem/content/)



```cpp
```

[2363.](https://www.acwing.com/problem/content/)



```cpp
```

[2364.](https://www.acwing.com/problem/content/)



```cpp
```

[2365.](https://www.acwing.com/problem/content/)



```cpp
```

[2366.](https://www.acwing.com/problem/content/)



```cpp
```

[2367.](https://www.acwing.com/problem/content/)



```cpp
```

[2368.](https://www.acwing.com/problem/content/)



```cpp
```

[2369.](https://www.acwing.com/problem/content/)



```cpp
```

[2370.](https://www.acwing.com/problem/content/)



```cpp
```

[2371.](https://www.acwing.com/problem/content/)



```cpp
```

[2372.](https://www.acwing.com/problem/content/)



```cpp
```

[2373.](https://www.acwing.com/problem/content/)



```cpp
```

[2374.](https://www.acwing.com/problem/content/)



```cpp
```

[2375.](https://www.acwing.com/problem/content/)



```cpp
```

[2376.](https://www.acwing.com/problem/content/)



```cpp
```

[2377.](https://www.acwing.com/problem/content/)



```cpp
```

[2378.](https://www.acwing.com/problem/content/)



```cpp
```

[2379.](https://www.acwing.com/problem/content/)



```cpp
```

[2380.](https://www.acwing.com/problem/content/)



```cpp
```

[2381.](https://www.acwing.com/problem/content/)



```cpp
```

[2382.](https://www.acwing.com/problem/content/)



```cpp
```

[2383.](https://www.acwing.com/problem/content/)



```cpp
```

[2384.](https://www.acwing.com/problem/content/)



```cpp
```

[2385.](https://www.acwing.com/problem/content/)



```cpp
```

[2386.](https://www.acwing.com/problem/content/)



```cpp
```

[2387.](https://www.acwing.com/problem/content/)



```cpp
```

[2388.](https://www.acwing.com/problem/content/)



```cpp
```

[2389.](https://www.acwing.com/problem/content/)



```cpp
```

[2390.](https://www.acwing.com/problem/content/)



```cpp
```

[2391.](https://www.acwing.com/problem/content/)



```cpp
```

[2392.](https://www.acwing.com/problem/content/)



```cpp
```

[2393.](https://www.acwing.com/problem/content/)



```cpp
```

[2394.](https://www.acwing.com/problem/content/)



```cpp
```

[2395.](https://www.acwing.com/problem/content/)



```cpp
```

[2396.](https://www.acwing.com/problem/content/)



```cpp
```

[2397.](https://www.acwing.com/problem/content/)



```cpp
```

[2398.](https://www.acwing.com/problem/content/)



```cpp
```

[2399.](https://www.acwing.com/problem/content/)



```cpp
```

[2400.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2401~2500

[2401.](https://www.acwing.com/problem/content/)



```cpp
```

[2402.](https://www.acwing.com/problem/content/)



```cpp
```

[2403.](https://www.acwing.com/problem/content/)



```cpp
```

[2404.](https://www.acwing.com/problem/content/)



```cpp
```

[2405.](https://www.acwing.com/problem/content/)



```cpp
```

[2406.](https://www.acwing.com/problem/content/)



```cpp
```

[2407.](https://www.acwing.com/problem/content/)



```cpp
```

[2408.](https://www.acwing.com/problem/content/)



```cpp
```

[2409.](https://www.acwing.com/problem/content/)



```cpp
```

[2410.](https://www.acwing.com/problem/content/)



```cpp
```

[2411.](https://www.acwing.com/problem/content/)



```cpp
```

[2412.](https://www.acwing.com/problem/content/)



```cpp
```

[2413.](https://www.acwing.com/problem/content/)



```cpp
```

[2414.](https://www.acwing.com/problem/content/)



```cpp
```

[2415.](https://www.acwing.com/problem/content/)



```cpp
```

[2416.](https://www.acwing.com/problem/content/)



```cpp
```

[2417.](https://www.acwing.com/problem/content/)



```cpp
```

[2418.](https://www.acwing.com/problem/content/)



```cpp
```

[2419.](https://www.acwing.com/problem/content/)



```cpp
```

[2420.](https://www.acwing.com/problem/content/)



```cpp
```

[2421.](https://www.acwing.com/problem/content/)



```cpp
```

[2422.](https://www.acwing.com/problem/content/)



```cpp
```

[2423.](https://www.acwing.com/problem/content/)



```cpp
```

[2424.](https://www.acwing.com/problem/content/)



```cpp
```

[2425.](https://www.acwing.com/problem/content/)



```cpp
```

[2426.](https://www.acwing.com/problem/content/)



```cpp
```

[2427.](https://www.acwing.com/problem/content/)



```cpp
```

[2428.](https://www.acwing.com/problem/content/)



```cpp
```

[2429.](https://www.acwing.com/problem/content/)



```cpp
```

[2430.](https://www.acwing.com/problem/content/)



```cpp
```

[2431.](https://www.acwing.com/problem/content/)



```cpp
```

[2432.](https://www.acwing.com/problem/content/)



```cpp
```

[2433.](https://www.acwing.com/problem/content/)



```cpp
```

[2434.](https://www.acwing.com/problem/content/)



```cpp
```

[2435.](https://www.acwing.com/problem/content/)



```cpp
```

[2436.](https://www.acwing.com/problem/content/)



```cpp
```

[2437.](https://www.acwing.com/problem/content/)



```cpp
```

[2438.](https://www.acwing.com/problem/content/)



```cpp
```

[2439.](https://www.acwing.com/problem/content/)



```cpp
```

[2440.](https://www.acwing.com/problem/content/)



```cpp
```

[2441.](https://www.acwing.com/problem/content/)



```cpp
```

[2442.](https://www.acwing.com/problem/content/)



```cpp
```

[2443.](https://www.acwing.com/problem/content/)



```cpp
```

[2444.](https://www.acwing.com/problem/content/)



```cpp
```

[2445.](https://www.acwing.com/problem/content/)



```cpp
```

[2446.](https://www.acwing.com/problem/content/)



```cpp
```

[2447.](https://www.acwing.com/problem/content/)



```cpp
```

[2448.](https://www.acwing.com/problem/content/)



```cpp
```

[2449.](https://www.acwing.com/problem/content/)



```cpp
```

[2450.](https://www.acwing.com/problem/content/)



```cpp
```

[2451.](https://www.acwing.com/problem/content/)



```cpp
```

[2452.](https://www.acwing.com/problem/content/)



```cpp
```

[2453.](https://www.acwing.com/problem/content/)



```cpp
```

[2454.](https://www.acwing.com/problem/content/)



```cpp
```

[2455.](https://www.acwing.com/problem/content/)



```cpp
```

[2456.](https://www.acwing.com/problem/content/)



```cpp
```

[2457.](https://www.acwing.com/problem/content/)



```cpp
```

[2458.](https://www.acwing.com/problem/content/)



```cpp
```

[2459.](https://www.acwing.com/problem/content/)



```cpp
```

[2460.](https://www.acwing.com/problem/content/)



```cpp
```

[2461.](https://www.acwing.com/problem/content/)



```cpp
```

[2462.](https://www.acwing.com/problem/content/)



```cpp
```

[2463.](https://www.acwing.com/problem/content/)



```cpp
```

[2464.](https://www.acwing.com/problem/content/)



```cpp
```

[2465.](https://www.acwing.com/problem/content/)



```cpp
```

[2466.](https://www.acwing.com/problem/content/)



```cpp
```

[2467.](https://www.acwing.com/problem/content/)



```cpp
```

[2468.](https://www.acwing.com/problem/content/)



```cpp
```

[2469.](https://www.acwing.com/problem/content/)



```cpp
```

[2470.](https://www.acwing.com/problem/content/)



```cpp
```

[2471.](https://www.acwing.com/problem/content/)



```cpp
```

[2472.](https://www.acwing.com/problem/content/)



```cpp
```

[2473.](https://www.acwing.com/problem/content/)



```cpp
```

[2474.](https://www.acwing.com/problem/content/)



```cpp
```

[2475.](https://www.acwing.com/problem/content/)



```cpp
```

[2476.](https://www.acwing.com/problem/content/)



```cpp
```

[2477.](https://www.acwing.com/problem/content/)



```cpp
```

[2478.](https://www.acwing.com/problem/content/)



```cpp
```

[2479.](https://www.acwing.com/problem/content/)



```cpp
```

[2480.](https://www.acwing.com/problem/content/)



```cpp
```

[2481.](https://www.acwing.com/problem/content/)



```cpp
```

[2482.](https://www.acwing.com/problem/content/)



```cpp
```

[2483.](https://www.acwing.com/problem/content/)



```cpp
```

[2484.](https://www.acwing.com/problem/content/)



```cpp
```

[2485.](https://www.acwing.com/problem/content/)



```cpp
```

[2486.](https://www.acwing.com/problem/content/)



```cpp
```

[2487.](https://www.acwing.com/problem/content/)



```cpp
```

[2488.](https://www.acwing.com/problem/content/)



```cpp
```

[2489.](https://www.acwing.com/problem/content/)



```cpp
```

[2490.](https://www.acwing.com/problem/content/)



```cpp
```

[2491.](https://www.acwing.com/problem/content/)



```cpp
```

[2492.](https://www.acwing.com/problem/content/)



```cpp
```

[2493.](https://www.acwing.com/problem/content/)



```cpp
```

[2494.](https://www.acwing.com/problem/content/)



```cpp
```

[2495.](https://www.acwing.com/problem/content/)



```cpp
```

[2496.](https://www.acwing.com/problem/content/)



```cpp
```

[2497.](https://www.acwing.com/problem/content/)



```cpp
```

[2498.](https://www.acwing.com/problem/content/)



```cpp
```

[2499.](https://www.acwing.com/problem/content/)



```cpp
```

[2500.](https://www.acwing.com/problem/content/)



```cpp
```

### 2501~3000

#### 2501~2600

[2501.](https://www.acwing.com/problem/content/)



```cpp
```

[2502.](https://www.acwing.com/problem/content/)



```cpp
```

[2503.](https://www.acwing.com/problem/content/)



```cpp
```

[2504.](https://www.acwing.com/problem/content/)



```cpp
```

[2505.](https://www.acwing.com/problem/content/)



```cpp
```

[2506.](https://www.acwing.com/problem/content/)



```cpp
```

[2507.](https://www.acwing.com/problem/content/)



```cpp
```

[2508.](https://www.acwing.com/problem/content/)



```cpp
```

[2509.](https://www.acwing.com/problem/content/)



```cpp
```

[2510.](https://www.acwing.com/problem/content/)



```cpp
```

[2511.](https://www.acwing.com/problem/content/)



```cpp
```

[2512.](https://www.acwing.com/problem/content/)



```cpp
```

[2513.](https://www.acwing.com/problem/content/)



```cpp
```

[2514.](https://www.acwing.com/problem/content/)



```cpp
```

[2515.](https://www.acwing.com/problem/content/)



```cpp
```

[2516.](https://www.acwing.com/problem/content/)



```cpp
```

[2517.](https://www.acwing.com/problem/content/)



```cpp
```

[2518.](https://www.acwing.com/problem/content/)



```cpp
```

[2519.](https://www.acwing.com/problem/content/)



```cpp
```

[2520.](https://www.acwing.com/problem/content/)



```cpp
```

[2521.](https://www.acwing.com/problem/content/)



```cpp
```

[2522.](https://www.acwing.com/problem/content/)



```cpp
```

[2523.](https://www.acwing.com/problem/content/)



```cpp
```

[2524.](https://www.acwing.com/problem/content/)



```cpp
```

[2525.](https://www.acwing.com/problem/content/)



```cpp
```

[2526.](https://www.acwing.com/problem/content/)



```cpp
```

[2527.](https://www.acwing.com/problem/content/)



```cpp
```

[2528.](https://www.acwing.com/problem/content/)



```cpp
```

[2529.](https://www.acwing.com/problem/content/)



```cpp
```

[2530.](https://www.acwing.com/problem/content/)



```cpp
```

[2531.](https://www.acwing.com/problem/content/)



```cpp
```

[2532.](https://www.acwing.com/problem/content/)



```cpp
```

[2533.](https://www.acwing.com/problem/content/)



```cpp
```

[2534.](https://www.acwing.com/problem/content/)



```cpp
```

[2535.](https://www.acwing.com/problem/content/)



```cpp
```

[2536.](https://www.acwing.com/problem/content/)



```cpp
```

[2537.](https://www.acwing.com/problem/content/)



```cpp
```

[2538.](https://www.acwing.com/problem/content/)



```cpp
```

[2539.](https://www.acwing.com/problem/content/)



```cpp
```

[2540.](https://www.acwing.com/problem/content/)



```cpp
```

[2541.](https://www.acwing.com/problem/content/)



```cpp
```

[2542.](https://www.acwing.com/problem/content/)



```cpp
```

[2543.](https://www.acwing.com/problem/content/)



```cpp
```

[2544.](https://www.acwing.com/problem/content/)



```cpp
```

[2545.](https://www.acwing.com/problem/content/)



```cpp
```

[2546.](https://www.acwing.com/problem/content/)



```cpp
```

[2547.](https://www.acwing.com/problem/content/)



```cpp
```

[2548.](https://www.acwing.com/problem/content/)



```cpp
```

[2549.](https://www.acwing.com/problem/content/)



```cpp
```

[2550.](https://www.acwing.com/problem/content/)



```cpp
```

[2551.](https://www.acwing.com/problem/content/)



```cpp
```

[2552.](https://www.acwing.com/problem/content/)



```cpp
```

[2553.](https://www.acwing.com/problem/content/)



```cpp
```

[2554.](https://www.acwing.com/problem/content/)



```cpp
```

[2555.](https://www.acwing.com/problem/content/)



```cpp
```

[2556.](https://www.acwing.com/problem/content/)



```cpp
```

[2557.](https://www.acwing.com/problem/content/)



```cpp
```

[2558.](https://www.acwing.com/problem/content/)



```cpp
```

[2559.](https://www.acwing.com/problem/content/)



```cpp
```

[2560.](https://www.acwing.com/problem/content/)



```cpp
```

[2561.](https://www.acwing.com/problem/content/)



```cpp
```

[2562.](https://www.acwing.com/problem/content/)



```cpp
```

[2563.](https://www.acwing.com/problem/content/)



```cpp
```

[2564.](https://www.acwing.com/problem/content/)



```cpp
```

[2565.](https://www.acwing.com/problem/content/)



```cpp
```

[2566.](https://www.acwing.com/problem/content/)



```cpp
```

[2567.](https://www.acwing.com/problem/content/)



```cpp
```

[2568.](https://www.acwing.com/problem/content/)



```cpp
```

[2569.](https://www.acwing.com/problem/content/)



```cpp
```

[2570.](https://www.acwing.com/problem/content/)



```cpp
```

[2571.](https://www.acwing.com/problem/content/)



```cpp
```

[2572.](https://www.acwing.com/problem/content/)



```cpp
```

[2573.](https://www.acwing.com/problem/content/)



```cpp
```

[2574.](https://www.acwing.com/problem/content/)



```cpp
```

[2575.](https://www.acwing.com/problem/content/)



```cpp
```

[2576.](https://www.acwing.com/problem/content/)



```cpp
```

[2577.](https://www.acwing.com/problem/content/)



```cpp
```

[2578.](https://www.acwing.com/problem/content/)



```cpp
```

[2579.](https://www.acwing.com/problem/content/)



```cpp
```

[2580.](https://www.acwing.com/problem/content/)



```cpp
```

[2581.](https://www.acwing.com/problem/content/)



```cpp
```

[2582.](https://www.acwing.com/problem/content/)



```cpp
```

[2583.](https://www.acwing.com/problem/content/)



```cpp
```

[2584.](https://www.acwing.com/problem/content/)



```cpp
```

[2585.](https://www.acwing.com/problem/content/)



```cpp
```

[2586.](https://www.acwing.com/problem/content/)



```cpp
```

[2587.](https://www.acwing.com/problem/content/)



```cpp
```

[2588.](https://www.acwing.com/problem/content/)



```cpp
```

[2589.](https://www.acwing.com/problem/content/)



```cpp
```

[2590.](https://www.acwing.com/problem/content/)



```cpp
```

[2591.](https://www.acwing.com/problem/content/)



```cpp
```

[2592.](https://www.acwing.com/problem/content/)



```cpp
```

[2593.](https://www.acwing.com/problem/content/)



```cpp
```

[2594.](https://www.acwing.com/problem/content/)



```cpp
```

[2595.](https://www.acwing.com/problem/content/)



```cpp
```

[2596.](https://www.acwing.com/problem/content/)



```cpp
```

[2597.](https://www.acwing.com/problem/content/)



```cpp
```

[2598.](https://www.acwing.com/problem/content/)



```cpp
```

[2599.](https://www.acwing.com/problem/content/)



```cpp
```

[2600.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2601~2700

[2601.](https://www.acwing.com/problem/content/)



```cpp
```

[2602.](https://www.acwing.com/problem/content/)



```cpp
```

[2603.](https://www.acwing.com/problem/content/)



```cpp
```

[2604.](https://www.acwing.com/problem/content/)



```cpp
```

[2605.](https://www.acwing.com/problem/content/)



```cpp
```

[2606.](https://www.acwing.com/problem/content/)



```cpp
```

[2607.](https://www.acwing.com/problem/content/)



```cpp
```

[2608.](https://www.acwing.com/problem/content/)



```cpp
```

[2609.](https://www.acwing.com/problem/content/)



```cpp
```

[2610.](https://www.acwing.com/problem/content/)



```cpp
```

[2611.](https://www.acwing.com/problem/content/)



```cpp
```

[2612.](https://www.acwing.com/problem/content/)



```cpp
```

[2613.](https://www.acwing.com/problem/content/)



```cpp
```

[2614.](https://www.acwing.com/problem/content/)



```cpp
```

[2615.](https://www.acwing.com/problem/content/)



```cpp
```

[2616.](https://www.acwing.com/problem/content/)



```cpp
```

[2617.](https://www.acwing.com/problem/content/)



```cpp
```

[2618.](https://www.acwing.com/problem/content/)



```cpp
```

[2619.](https://www.acwing.com/problem/content/)



```cpp
```

[2620.](https://www.acwing.com/problem/content/)



```cpp
```

[2621.](https://www.acwing.com/problem/content/)



```cpp
```

[2622.](https://www.acwing.com/problem/content/)



```cpp
```

[2623.](https://www.acwing.com/problem/content/)



```cpp
```

[2624.](https://www.acwing.com/problem/content/)



```cpp
```

[2625.](https://www.acwing.com/problem/content/)



```cpp
```

[2626.](https://www.acwing.com/problem/content/)



```cpp
```

[2627.](https://www.acwing.com/problem/content/)



```cpp
```

[2628.](https://www.acwing.com/problem/content/)



```cpp
```

[2629.](https://www.acwing.com/problem/content/)



```cpp
```

[2630.](https://www.acwing.com/problem/content/)



```cpp
```

[2631.](https://www.acwing.com/problem/content/)



```cpp
```

[2632.](https://www.acwing.com/problem/content/)



```cpp
```

[2633.](https://www.acwing.com/problem/content/)



```cpp
```

[2634.](https://www.acwing.com/problem/content/)



```cpp
```

[2635.](https://www.acwing.com/problem/content/)



```cpp
```

[2636.](https://www.acwing.com/problem/content/)



```cpp
```

[2637.](https://www.acwing.com/problem/content/)



```cpp
```

[2638.](https://www.acwing.com/problem/content/)



```cpp
```

[2639.](https://www.acwing.com/problem/content/)



```cpp
```

[2640.](https://www.acwing.com/problem/content/)



```cpp
```

[2641.](https://www.acwing.com/problem/content/)



```cpp
```

[2642.](https://www.acwing.com/problem/content/)



```cpp
```

[2643.](https://www.acwing.com/problem/content/)



```cpp
```

[2644.](https://www.acwing.com/problem/content/)



```cpp
```

[2645.](https://www.acwing.com/problem/content/)



```cpp
```

[2646.](https://www.acwing.com/problem/content/)



```cpp
```

[2647.](https://www.acwing.com/problem/content/)



```cpp
```

[2648.](https://www.acwing.com/problem/content/)



```cpp
```

[2649.](https://www.acwing.com/problem/content/)



```cpp
```

[2650.](https://www.acwing.com/problem/content/)



```cpp
```

[2651.](https://www.acwing.com/problem/content/)



```cpp
```

[2652.](https://www.acwing.com/problem/content/)



```cpp
```

[2653.](https://www.acwing.com/problem/content/)



```cpp
```

[2654.](https://www.acwing.com/problem/content/)



```cpp
```

[2655.](https://www.acwing.com/problem/content/)



```cpp
```

[2656.](https://www.acwing.com/problem/content/)



```cpp
```

[2657.](https://www.acwing.com/problem/content/)



```cpp
```

[2658.](https://www.acwing.com/problem/content/)



```cpp
```

[2659.](https://www.acwing.com/problem/content/)



```cpp
```

[2660.](https://www.acwing.com/problem/content/)



```cpp
```

[2661.](https://www.acwing.com/problem/content/)



```cpp
```

[2662.](https://www.acwing.com/problem/content/)



```cpp
```

[2663.](https://www.acwing.com/problem/content/)



```cpp
```

[2664.](https://www.acwing.com/problem/content/)



```cpp
```

[2665.](https://www.acwing.com/problem/content/)



```cpp
```

[2666.](https://www.acwing.com/problem/content/)



```cpp
```

[2667.](https://www.acwing.com/problem/content/)



```cpp
```

[2668.](https://www.acwing.com/problem/content/)



```cpp
```

[2669.](https://www.acwing.com/problem/content/)



```cpp
```

[2670.](https://www.acwing.com/problem/content/)



```cpp
```

[2671.](https://www.acwing.com/problem/content/)



```cpp
```

[2672.](https://www.acwing.com/problem/content/)



```cpp
```

[2673.](https://www.acwing.com/problem/content/)



```cpp
```

[2674.](https://www.acwing.com/problem/content/)



```cpp
```

[2675.](https://www.acwing.com/problem/content/)



```cpp
```

[2676.](https://www.acwing.com/problem/content/)



```cpp
```

[2677.](https://www.acwing.com/problem/content/)



```cpp
```

[2678.](https://www.acwing.com/problem/content/)



```cpp
```

[2679.](https://www.acwing.com/problem/content/)



```cpp
```

[2680.](https://www.acwing.com/problem/content/)



```cpp
```

[2681.](https://www.acwing.com/problem/content/)



```cpp
```

[2682.](https://www.acwing.com/problem/content/)



```cpp
```

[2683.](https://www.acwing.com/problem/content/)



```cpp
```

[2684.](https://www.acwing.com/problem/content/)



```cpp
```

[2685.](https://www.acwing.com/problem/content/)



```cpp
```

[2686.](https://www.acwing.com/problem/content/)



```cpp
```

[2687.](https://www.acwing.com/problem/content/)



```cpp
```

[2688.](https://www.acwing.com/problem/content/)



```cpp
```

[2689.](https://www.acwing.com/problem/content/)



```cpp
```

[2690.](https://www.acwing.com/problem/content/)



```cpp
```

[2691.](https://www.acwing.com/problem/content/)



```cpp
```

[2692.](https://www.acwing.com/problem/content/)



```cpp
```

[2693.](https://www.acwing.com/problem/content/)



```cpp
```

[2694.](https://www.acwing.com/problem/content/)



```cpp
```

[2695.](https://www.acwing.com/problem/content/)



```cpp
```

[2696.](https://www.acwing.com/problem/content/)



```cpp
```

[2697.](https://www.acwing.com/problem/content/)



```cpp
```

[2698.](https://www.acwing.com/problem/content/)



```cpp
```

[2699.](https://www.acwing.com/problem/content/)



```cpp
```

[2700.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2701~2800

[2701.](https://www.acwing.com/problem/content/)



```cpp
```

[2702.](https://www.acwing.com/problem/content/)



```cpp
```

[2703.](https://www.acwing.com/problem/content/)



```cpp
```

[2704.](https://www.acwing.com/problem/content/)



```cpp
```

[2705.](https://www.acwing.com/problem/content/)



```cpp
```

[2706.](https://www.acwing.com/problem/content/)



```cpp
```

[2707.](https://www.acwing.com/problem/content/)



```cpp
```

[2708.](https://www.acwing.com/problem/content/)



```cpp
```

[2709.](https://www.acwing.com/problem/content/)



```cpp
```

[2710.](https://www.acwing.com/problem/content/)



```cpp
```

[2711.](https://www.acwing.com/problem/content/)



```cpp
```

[2712.](https://www.acwing.com/problem/content/)



```cpp
```

[2713.](https://www.acwing.com/problem/content/)



```cpp
```

[2714.](https://www.acwing.com/problem/content/)



```cpp
```

[2715.](https://www.acwing.com/problem/content/)



```cpp
```

[2716.](https://www.acwing.com/problem/content/)



```cpp
```

[2717.](https://www.acwing.com/problem/content/)



```cpp
```

[2718.](https://www.acwing.com/problem/content/)



```cpp
```

[2719.](https://www.acwing.com/problem/content/)



```cpp
```

[2720.](https://www.acwing.com/problem/content/)



```cpp
```

[2721.](https://www.acwing.com/problem/content/)



```cpp
```

[2722.](https://www.acwing.com/problem/content/)



```cpp
```

[2723.](https://www.acwing.com/problem/content/)



```cpp
```

[2724.](https://www.acwing.com/problem/content/)



```cpp
```

[2725.](https://www.acwing.com/problem/content/)



```cpp
```

[2726.](https://www.acwing.com/problem/content/)



```cpp
```

[2727.](https://www.acwing.com/problem/content/)



```cpp
```

[2728.](https://www.acwing.com/problem/content/)



```cpp
```

[2729.](https://www.acwing.com/problem/content/)



```cpp
```

[2730.](https://www.acwing.com/problem/content/)



```cpp
```

[2731.](https://www.acwing.com/problem/content/)



```cpp
```

[2732.](https://www.acwing.com/problem/content/)



```cpp
```

[2733.](https://www.acwing.com/problem/content/)



```cpp
```

[2734.](https://www.acwing.com/problem/content/)



```cpp
```

[2735.](https://www.acwing.com/problem/content/)



```cpp
```

[2736.](https://www.acwing.com/problem/content/)



```cpp
```

[2737.](https://www.acwing.com/problem/content/)



```cpp
```

[2738.](https://www.acwing.com/problem/content/)



```cpp
```

[2739.](https://www.acwing.com/problem/content/)



```cpp
```

[2740.](https://www.acwing.com/problem/content/)



```cpp
```

[2741.](https://www.acwing.com/problem/content/)



```cpp
```

[2742.](https://www.acwing.com/problem/content/)



```cpp
```

[2743.](https://www.acwing.com/problem/content/)



```cpp
```

[2744.](https://www.acwing.com/problem/content/)



```cpp
```

[2745.](https://www.acwing.com/problem/content/)



```cpp
```

[2746.](https://www.acwing.com/problem/content/)



```cpp
```

[2747.](https://www.acwing.com/problem/content/)



```cpp
```

[2748.](https://www.acwing.com/problem/content/)



```cpp
```

[2749.](https://www.acwing.com/problem/content/)



```cpp
```

[2750.](https://www.acwing.com/problem/content/)



```cpp
```

[2751.](https://www.acwing.com/problem/content/)



```cpp
```

[2752.](https://www.acwing.com/problem/content/)



```cpp
```

[2753.](https://www.acwing.com/problem/content/)



```cpp
```

[2754.](https://www.acwing.com/problem/content/)



```cpp
```

[2755.](https://www.acwing.com/problem/content/)



```cpp
```

[2756.](https://www.acwing.com/problem/content/)



```cpp
```

[2757.](https://www.acwing.com/problem/content/)



```cpp
```

[2758.](https://www.acwing.com/problem/content/)



```cpp
```

[2759.](https://www.acwing.com/problem/content/)



```cpp
```

[2760.](https://www.acwing.com/problem/content/)



```cpp
```

[2761.](https://www.acwing.com/problem/content/)



```cpp
```

[2762.](https://www.acwing.com/problem/content/)



```cpp
```

[2763.](https://www.acwing.com/problem/content/)



```cpp
```

[2764.](https://www.acwing.com/problem/content/)



```cpp
```

[2765.](https://www.acwing.com/problem/content/)



```cpp
```

[2766.](https://www.acwing.com/problem/content/)



```cpp
```

[2767.](https://www.acwing.com/problem/content/)



```cpp
```

[2768.](https://www.acwing.com/problem/content/)



```cpp
```

[2769.](https://www.acwing.com/problem/content/)



```cpp
```

[2770.](https://www.acwing.com/problem/content/)



```cpp
```

[2771.](https://www.acwing.com/problem/content/)



```cpp
```

[2772.](https://www.acwing.com/problem/content/)



```cpp
```

[2773.](https://www.acwing.com/problem/content/)



```cpp
```

[2774.](https://www.acwing.com/problem/content/)



```cpp
```

[2775.](https://www.acwing.com/problem/content/)



```cpp
```

[2776.](https://www.acwing.com/problem/content/)



```cpp
```

[2777.](https://www.acwing.com/problem/content/)



```cpp
```

[2778.](https://www.acwing.com/problem/content/)



```cpp
```

[2779.](https://www.acwing.com/problem/content/)



```cpp
```

[2780.](https://www.acwing.com/problem/content/)



```cpp
```

[2781.](https://www.acwing.com/problem/content/)



```cpp
```

[2782.](https://www.acwing.com/problem/content/)



```cpp
```

[2783.](https://www.acwing.com/problem/content/)



```cpp
```

[2784.](https://www.acwing.com/problem/content/)



```cpp
```

[2785.](https://www.acwing.com/problem/content/)



```cpp
```

[2786.](https://www.acwing.com/problem/content/)



```cpp
```

[2787.](https://www.acwing.com/problem/content/)



```cpp
```

[2788.](https://www.acwing.com/problem/content/)



```cpp
```

[2789.](https://www.acwing.com/problem/content/)



```cpp
```

[2790.](https://www.acwing.com/problem/content/)



```cpp
```

[2791.](https://www.acwing.com/problem/content/)



```cpp
```

[2792.](https://www.acwing.com/problem/content/)



```cpp
```

[2793.](https://www.acwing.com/problem/content/)



```cpp
```

[2794.](https://www.acwing.com/problem/content/)



```cpp
```

[2795.](https://www.acwing.com/problem/content/)



```cpp
```

[2796.](https://www.acwing.com/problem/content/)



```cpp
```

[2797.](https://www.acwing.com/problem/content/)



```cpp
```

[2798.](https://www.acwing.com/problem/content/)



```cpp
```

[2799.](https://www.acwing.com/problem/content/)



```cpp
```

[2800.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2801~2900

[2801.](https://www.acwing.com/problem/content/)



```cpp
```

[2802.](https://www.acwing.com/problem/content/)



```cpp
```

[2803.](https://www.acwing.com/problem/content/)



```cpp
```

[2804.](https://www.acwing.com/problem/content/)



```cpp
```

[2805.](https://www.acwing.com/problem/content/)



```cpp
```

[2806.](https://www.acwing.com/problem/content/)



```cpp
```

[2807.](https://www.acwing.com/problem/content/)



```cpp
```

[2808.](https://www.acwing.com/problem/content/)



```cpp
```

[2809.](https://www.acwing.com/problem/content/)



```cpp
```

[2810.](https://www.acwing.com/problem/content/)



```cpp
```

[2811.](https://www.acwing.com/problem/content/)



```cpp
```

[2812.](https://www.acwing.com/problem/content/)



```cpp
```

[2813.](https://www.acwing.com/problem/content/)



```cpp
```

[2814.](https://www.acwing.com/problem/content/)



```cpp
```

[2815.](https://www.acwing.com/problem/content/)



```cpp
```

[2816.](https://www.acwing.com/problem/content/)



```cpp
```

[2817.](https://www.acwing.com/problem/content/)



```cpp
```

[2818.](https://www.acwing.com/problem/content/)



```cpp
```

[2819.](https://www.acwing.com/problem/content/)



```cpp
```

[2820.](https://www.acwing.com/problem/content/)



```cpp
```

[2821.](https://www.acwing.com/problem/content/)



```cpp
```

[2822.](https://www.acwing.com/problem/content/)



```cpp
```

[2823.](https://www.acwing.com/problem/content/)



```cpp
```

[2824.](https://www.acwing.com/problem/content/)



```cpp
```

[2825.](https://www.acwing.com/problem/content/)



```cpp
```

[2826.](https://www.acwing.com/problem/content/)



```cpp
```

[2827.](https://www.acwing.com/problem/content/)



```cpp
```

[2828.](https://www.acwing.com/problem/content/)



```cpp
```

[2829.](https://www.acwing.com/problem/content/)



```cpp
```

[2830.](https://www.acwing.com/problem/content/)



```cpp
```

[2831.](https://www.acwing.com/problem/content/)



```cpp
```

[2832.](https://www.acwing.com/problem/content/)



```cpp
```

[2833.](https://www.acwing.com/problem/content/)



```cpp
```

[2834.](https://www.acwing.com/problem/content/)



```cpp
```

[2835.](https://www.acwing.com/problem/content/)



```cpp
```

[2836.](https://www.acwing.com/problem/content/)



```cpp
```

[2837.](https://www.acwing.com/problem/content/)



```cpp
```

[2838.](https://www.acwing.com/problem/content/)



```cpp
```

[2839.](https://www.acwing.com/problem/content/)



```cpp
```

[2840.](https://www.acwing.com/problem/content/)



```cpp
```

[2841.](https://www.acwing.com/problem/content/)



```cpp
```

[2842.](https://www.acwing.com/problem/content/)



```cpp
```

[2843.](https://www.acwing.com/problem/content/)



```cpp
```

[2844.](https://www.acwing.com/problem/content/)



```cpp
```

[2845.](https://www.acwing.com/problem/content/)



```cpp
```

[2846.](https://www.acwing.com/problem/content/)



```cpp
```

[2847.](https://www.acwing.com/problem/content/)



```cpp
```

[2848.](https://www.acwing.com/problem/content/)



```cpp
```

[2849.](https://www.acwing.com/problem/content/)



```cpp
```

[2850.](https://www.acwing.com/problem/content/)



```cpp
```

[2851.](https://www.acwing.com/problem/content/)



```cpp
```

[2852.](https://www.acwing.com/problem/content/)



```cpp
```

[2853.](https://www.acwing.com/problem/content/)



```cpp
```

[2854.](https://www.acwing.com/problem/content/)



```cpp
```

[2855.](https://www.acwing.com/problem/content/)



```cpp
```

[2856.](https://www.acwing.com/problem/content/)



```cpp
```

[2857.](https://www.acwing.com/problem/content/)



```cpp
```

[2858.](https://www.acwing.com/problem/content/)



```cpp
```

[2859.](https://www.acwing.com/problem/content/)



```cpp
```

[2860.](https://www.acwing.com/problem/content/)



```cpp
```

[2861.](https://www.acwing.com/problem/content/)



```cpp
```

[2862.](https://www.acwing.com/problem/content/)



```cpp
```

[2863.](https://www.acwing.com/problem/content/)



```cpp
```

[2864.](https://www.acwing.com/problem/content/)



```cpp
```

[2865.](https://www.acwing.com/problem/content/)



```cpp
```

[2866.](https://www.acwing.com/problem/content/)



```cpp
```

[2867.](https://www.acwing.com/problem/content/)



```cpp
```

[2868.](https://www.acwing.com/problem/content/)



```cpp
```

[2869.](https://www.acwing.com/problem/content/)



```cpp
```

[2870.](https://www.acwing.com/problem/content/)



```cpp
```

[2871.](https://www.acwing.com/problem/content/)



```cpp
```

[2872.](https://www.acwing.com/problem/content/)



```cpp
```

[2873.](https://www.acwing.com/problem/content/)



```cpp
```

[2874.](https://www.acwing.com/problem/content/)



```cpp
```

[2875.](https://www.acwing.com/problem/content/)



```cpp
```

[2876.](https://www.acwing.com/problem/content/)



```cpp
```

[2877.](https://www.acwing.com/problem/content/)



```cpp
```

[2878.](https://www.acwing.com/problem/content/)



```cpp
```

[2879.](https://www.acwing.com/problem/content/)



```cpp
```

[2880.](https://www.acwing.com/problem/content/)



```cpp
```

[2881.](https://www.acwing.com/problem/content/)



```cpp
```

[2882.](https://www.acwing.com/problem/content/)



```cpp
```

[2883.](https://www.acwing.com/problem/content/)



```cpp
```

[2884.](https://www.acwing.com/problem/content/)



```cpp
```

[2885.](https://www.acwing.com/problem/content/)



```cpp
```

[2886.](https://www.acwing.com/problem/content/)



```cpp
```

[2887.](https://www.acwing.com/problem/content/)



```cpp
```

[2888.](https://www.acwing.com/problem/content/)



```cpp
```

[2889.](https://www.acwing.com/problem/content/)



```cpp
```

[2890.](https://www.acwing.com/problem/content/)



```cpp
```

[2891.](https://www.acwing.com/problem/content/)



```cpp
```

[2892.](https://www.acwing.com/problem/content/)



```cpp
```

[2893.](https://www.acwing.com/problem/content/)



```cpp
```

[2894.](https://www.acwing.com/problem/content/)



```cpp
```

[2895.](https://www.acwing.com/problem/content/)



```cpp
```

[2896.](https://www.acwing.com/problem/content/)



```cpp
```

[2897.](https://www.acwing.com/problem/content/)



```cpp
```

[2898.](https://www.acwing.com/problem/content/)



```cpp
```

[2899.](https://www.acwing.com/problem/content/)



```cpp
```

[2900.](https://www.acwing.com/problem/content/)



```cpp
```

#### 2901~3000

[2901.](https://www.acwing.com/problem/content/)



```cpp
```

[2902.](https://www.acwing.com/problem/content/)



```cpp
```

[2903.](https://www.acwing.com/problem/content/)



```cpp
```

[2904.](https://www.acwing.com/problem/content/)



```cpp
```

[2905.](https://www.acwing.com/problem/content/)



```cpp
```

[2906.](https://www.acwing.com/problem/content/)



```cpp
```

[2907.](https://www.acwing.com/problem/content/)



```cpp
```

[2908.](https://www.acwing.com/problem/content/)



```cpp
```

[2909.](https://www.acwing.com/problem/content/)



```cpp
```

[2910.](https://www.acwing.com/problem/content/)



```cpp
```

[2911.](https://www.acwing.com/problem/content/)



```cpp
```

[2912.](https://www.acwing.com/problem/content/)



```cpp
```

[2913.](https://www.acwing.com/problem/content/)



```cpp
```

[2914.](https://www.acwing.com/problem/content/)



```cpp
```

[2915.](https://www.acwing.com/problem/content/)



```cpp
```

[2916.](https://www.acwing.com/problem/content/)



```cpp
```

[2917.](https://www.acwing.com/problem/content/)



```cpp
```

[2918.](https://www.acwing.com/problem/content/)



```cpp
```

[2919.](https://www.acwing.com/problem/content/)



```cpp
```

[2920.](https://www.acwing.com/problem/content/)



```cpp
```

[2921.](https://www.acwing.com/problem/content/)



```cpp
```

[2922.](https://www.acwing.com/problem/content/)



```cpp
```

[2923.](https://www.acwing.com/problem/content/)



```cpp
```

[2924.](https://www.acwing.com/problem/content/)



```cpp
```

[2925.](https://www.acwing.com/problem/content/)



```cpp
```

[2926.](https://www.acwing.com/problem/content/)



```cpp
```

[2927.](https://www.acwing.com/problem/content/)



```cpp
```

[2928.](https://www.acwing.com/problem/content/)



```cpp
```

[2929.](https://www.acwing.com/problem/content/)



```cpp
```

[2930.](https://www.acwing.com/problem/content/)



```cpp
```

[2931.](https://www.acwing.com/problem/content/)



```cpp
```

[2932.](https://www.acwing.com/problem/content/)



```cpp
```

[2933.](https://www.acwing.com/problem/content/)



```cpp
```

[2934.](https://www.acwing.com/problem/content/)



```cpp
```

[2935.](https://www.acwing.com/problem/content/)



```cpp
```

[2936.](https://www.acwing.com/problem/content/)



```cpp
```

[2937.](https://www.acwing.com/problem/content/)



```cpp
```

[2938.](https://www.acwing.com/problem/content/)



```cpp
```

[2939.](https://www.acwing.com/problem/content/)



```cpp
```

[2940.](https://www.acwing.com/problem/content/)



```cpp
```

[2941.](https://www.acwing.com/problem/content/)



```cpp
```

[2942.](https://www.acwing.com/problem/content/)



```cpp
```

[2943.](https://www.acwing.com/problem/content/)



```cpp
```

[2944.](https://www.acwing.com/problem/content/)



```cpp
```

[2945.](https://www.acwing.com/problem/content/)



```cpp
```

[2946.](https://www.acwing.com/problem/content/)



```cpp
```

[2947.](https://www.acwing.com/problem/content/)



```cpp
```

[2948.](https://www.acwing.com/problem/content/)



```cpp
```

[2949.](https://www.acwing.com/problem/content/)



```cpp
```

[2950.](https://www.acwing.com/problem/content/)



```cpp
```

[2951.](https://www.acwing.com/problem/content/)



```cpp
```

[2952.](https://www.acwing.com/problem/content/)



```cpp
```

[2953.](https://www.acwing.com/problem/content/)



```cpp
```

[2954.](https://www.acwing.com/problem/content/)



```cpp
```

[2955.](https://www.acwing.com/problem/content/)



```cpp
```

[2956.](https://www.acwing.com/problem/content/)



```cpp
```

[2957.](https://www.acwing.com/problem/content/)



```cpp
```

[2958.](https://www.acwing.com/problem/content/)



```cpp
```

[2959.](https://www.acwing.com/problem/content/)



```cpp
```

[2960.](https://www.acwing.com/problem/content/)



```cpp
```

[2961.](https://www.acwing.com/problem/content/)



```cpp
```

[2962.](https://www.acwing.com/problem/content/)



```cpp
```

[2963.](https://www.acwing.com/problem/content/)



```cpp
```

[2964.](https://www.acwing.com/problem/content/)



```cpp
```

[2965.](https://www.acwing.com/problem/content/)



```cpp
```

[2966.](https://www.acwing.com/problem/content/)



```cpp
```

[2967.](https://www.acwing.com/problem/content/)



```cpp
```

[2968.](https://www.acwing.com/problem/content/)



```cpp
```

[2969.](https://www.acwing.com/problem/content/)



```cpp
```

[2970.](https://www.acwing.com/problem/content/)



```cpp
```

[2971.](https://www.acwing.com/problem/content/)



```cpp
```

[2972.](https://www.acwing.com/problem/content/)



```cpp
```

[2973.](https://www.acwing.com/problem/content/)



```cpp
```

[2974.](https://www.acwing.com/problem/content/)



```cpp
```

[2975.](https://www.acwing.com/problem/content/)



```cpp
```

[2976.](https://www.acwing.com/problem/content/)



```cpp
```

[2977.](https://www.acwing.com/problem/content/)



```cpp
```

[2978.](https://www.acwing.com/problem/content/)



```cpp
```

[2979.](https://www.acwing.com/problem/content/)



```cpp
```

[2980.](https://www.acwing.com/problem/content/)



```cpp
```

[2981.](https://www.acwing.com/problem/content/)



```cpp
```

[2982.](https://www.acwing.com/problem/content/)



```cpp
```

[2983.](https://www.acwing.com/problem/content/)



```cpp
```

[2984.](https://www.acwing.com/problem/content/)



```cpp
```

[2985.](https://www.acwing.com/problem/content/)



```cpp
```

[2986.](https://www.acwing.com/problem/content/)



```cpp
```

[2987.](https://www.acwing.com/problem/content/)



```cpp
```

[2988.](https://www.acwing.com/problem/content/)



```cpp
```

[2989.](https://www.acwing.com/problem/content/)



```cpp
```

[2990.](https://www.acwing.com/problem/content/)



```cpp
```

[2991.](https://www.acwing.com/problem/content/)



```cpp
```

[2992.](https://www.acwing.com/problem/content/)



```cpp
```

[2993.](https://www.acwing.com/problem/content/)



```cpp
```

[2994.](https://www.acwing.com/problem/content/)



```cpp
```

[2995.](https://www.acwing.com/problem/content/)



```cpp
```

[2996.](https://www.acwing.com/problem/content/)



```cpp
```

[2997.](https://www.acwing.com/problem/content/)



```cpp
```

[2998.](https://www.acwing.com/problem/content/)



```cpp
```

[2999.](https://www.acwing.com/problem/content/)



```cpp
```

[3000.](https://www.acwing.com/problem/content/)



```cpp
```

## 3001~4000

### 3001~3500

#### 3001~3100

[3001.](https://www.acwing.com/problem/content/)



```cpp
```

[3002.](https://www.acwing.com/problem/content/)



```cpp
```

[3003.](https://www.acwing.com/problem/content/)



```cpp
```

[3004.](https://www.acwing.com/problem/content/)



```cpp
```

[3005.](https://www.acwing.com/problem/content/)



```cpp
```

[3006.](https://www.acwing.com/problem/content/)



```cpp
```

[3007.](https://www.acwing.com/problem/content/)



```cpp
```

[3008.](https://www.acwing.com/problem/content/)



```cpp
```

[3009.](https://www.acwing.com/problem/content/)



```cpp
```

[3010.](https://www.acwing.com/problem/content/)



```cpp
```

[3011.](https://www.acwing.com/problem/content/)



```cpp
```

[3012.](https://www.acwing.com/problem/content/)



```cpp
```

[3013.](https://www.acwing.com/problem/content/)



```cpp
```

[3014.](https://www.acwing.com/problem/content/)



```cpp
```

[3015.](https://www.acwing.com/problem/content/)



```cpp
```

[3016.](https://www.acwing.com/problem/content/)



```cpp
```

[3017.](https://www.acwing.com/problem/content/)



```cpp
```

[3018.](https://www.acwing.com/problem/content/)



```cpp
```

[3019.](https://www.acwing.com/problem/content/)



```cpp
```

[3020.](https://www.acwing.com/problem/content/)



```cpp
```

[3021.](https://www.acwing.com/problem/content/)



```cpp
```

[3022.](https://www.acwing.com/problem/content/)



```cpp
```

[3023.](https://www.acwing.com/problem/content/)



```cpp
```

[3024.](https://www.acwing.com/problem/content/)



```cpp
```

[3025.](https://www.acwing.com/problem/content/)



```cpp
```

[3026.](https://www.acwing.com/problem/content/)



```cpp
```

[3027.](https://www.acwing.com/problem/content/)



```cpp
```

[3028.](https://www.acwing.com/problem/content/)



```cpp
```

[3029.](https://www.acwing.com/problem/content/)



```cpp
```

[3030.](https://www.acwing.com/problem/content/)



```cpp
```

[3031.](https://www.acwing.com/problem/content/)



```cpp
```

[3032.](https://www.acwing.com/problem/content/)



```cpp
```

[3033.](https://www.acwing.com/problem/content/)



```cpp
```

[3034.](https://www.acwing.com/problem/content/)



```cpp
```

[3035.](https://www.acwing.com/problem/content/)



```cpp
```

[3036.](https://www.acwing.com/problem/content/)



```cpp
```

[3037.](https://www.acwing.com/problem/content/)



```cpp
```

[3038.](https://www.acwing.com/problem/content/)



```cpp
```

[3039.](https://www.acwing.com/problem/content/)



```cpp
```

[3040.](https://www.acwing.com/problem/content/)



```cpp
```

[3041.](https://www.acwing.com/problem/content/)



```cpp
```

[3042.](https://www.acwing.com/problem/content/)



```cpp
```

[3043.](https://www.acwing.com/problem/content/)



```cpp
```

[3044.](https://www.acwing.com/problem/content/)



```cpp
```

[3045.](https://www.acwing.com/problem/content/)



```cpp
```

[3046.](https://www.acwing.com/problem/content/)



```cpp
```

[3047.](https://www.acwing.com/problem/content/)



```cpp
```

[3048.](https://www.acwing.com/problem/content/)



```cpp
```

[3049.](https://www.acwing.com/problem/content/)



```cpp
```

[3050.](https://www.acwing.com/problem/content/)



```cpp
```

[3051.](https://www.acwing.com/problem/content/)



```cpp
```

[3052.](https://www.acwing.com/problem/content/)



```cpp
```

[3053.](https://www.acwing.com/problem/content/)



```cpp
```

[3054.](https://www.acwing.com/problem/content/)



```cpp
```

[3055.](https://www.acwing.com/problem/content/)



```cpp
```

[3056.](https://www.acwing.com/problem/content/)



```cpp
```

[3057.](https://www.acwing.com/problem/content/)



```cpp
```

[3058.](https://www.acwing.com/problem/content/)



```cpp
```

[3059.](https://www.acwing.com/problem/content/)



```cpp
```

[3060.](https://www.acwing.com/problem/content/)



```cpp
```

[3061.](https://www.acwing.com/problem/content/)



```cpp
```

[3062.](https://www.acwing.com/problem/content/)



```cpp
```

[3063.](https://www.acwing.com/problem/content/)



```cpp
```

[3064.](https://www.acwing.com/problem/content/)



```cpp
```

[3065.](https://www.acwing.com/problem/content/)



```cpp
```

[3066.](https://www.acwing.com/problem/content/)



```cpp
```

[3067.](https://www.acwing.com/problem/content/)



```cpp
```

[3068.](https://www.acwing.com/problem/content/)



```cpp
```

[3069.](https://www.acwing.com/problem/content/)



```cpp
```

[3070.](https://www.acwing.com/problem/content/)



```cpp
```

[3071.](https://www.acwing.com/problem/content/)



```cpp
```

[3072.](https://www.acwing.com/problem/content/)



```cpp
```

[3073.](https://www.acwing.com/problem/content/)



```cpp
```

[3074.](https://www.acwing.com/problem/content/)



```cpp
```

[3075.](https://www.acwing.com/problem/content/)



```cpp
```

[3076.](https://www.acwing.com/problem/content/)



```cpp
```

[3077.](https://www.acwing.com/problem/content/)



```cpp
```

[3078.](https://www.acwing.com/problem/content/)



```cpp
```

[3079.](https://www.acwing.com/problem/content/)



```cpp
```

[3080.](https://www.acwing.com/problem/content/)



```cpp
```

[3081.](https://www.acwing.com/problem/content/)



```cpp
```

[3082.](https://www.acwing.com/problem/content/)



```cpp
```

[3083.](https://www.acwing.com/problem/content/)



```cpp
```

[3084.](https://www.acwing.com/problem/content/)



```cpp
```

[3085.](https://www.acwing.com/problem/content/)



```cpp
```

[3086.](https://www.acwing.com/problem/content/)



```cpp
```

[3087.](https://www.acwing.com/problem/content/)



```cpp
```

[3088.](https://www.acwing.com/problem/content/)



```cpp
```

[3089.](https://www.acwing.com/problem/content/)



```cpp
```

[3090.](https://www.acwing.com/problem/content/)



```cpp
```

[3091.](https://www.acwing.com/problem/content/)



```cpp
```

[3092.](https://www.acwing.com/problem/content/)



```cpp
```

[3093.](https://www.acwing.com/problem/content/)



```cpp
```

[3094.](https://www.acwing.com/problem/content/)



```cpp
```

[3095.](https://www.acwing.com/problem/content/)



```cpp
```

[3096.](https://www.acwing.com/problem/content/)



```cpp
```

[3097.](https://www.acwing.com/problem/content/)



```cpp
```

[3098.](https://www.acwing.com/problem/content/)



```cpp
```

[3099.](https://www.acwing.com/problem/content/)



```cpp
```

[3100.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3101~3200

[3101.](https://www.acwing.com/problem/content/)



```cpp
```

[3102.](https://www.acwing.com/problem/content/)



```cpp
```

[3103.](https://www.acwing.com/problem/content/)



```cpp
```

[3104.](https://www.acwing.com/problem/content/)



```cpp
```

[3105.](https://www.acwing.com/problem/content/)



```cpp
```

[3106.](https://www.acwing.com/problem/content/)



```cpp
```

[3107.](https://www.acwing.com/problem/content/)



```cpp
```

[3108.](https://www.acwing.com/problem/content/)



```cpp
```

[3109.](https://www.acwing.com/problem/content/)



```cpp
```

[3110.](https://www.acwing.com/problem/content/)



```cpp
```

[3111.](https://www.acwing.com/problem/content/)



```cpp
```

[3112.](https://www.acwing.com/problem/content/)



```cpp
```

[3113.](https://www.acwing.com/problem/content/)



```cpp
```

[3114.](https://www.acwing.com/problem/content/)



```cpp
```

[3115.](https://www.acwing.com/problem/content/)



```cpp
```

[3116.](https://www.acwing.com/problem/content/)



```cpp
```

[3117.](https://www.acwing.com/problem/content/)



```cpp
```

[3118.](https://www.acwing.com/problem/content/)



```cpp
```

[3119.](https://www.acwing.com/problem/content/)



```cpp
```

[3120.](https://www.acwing.com/problem/content/)



```cpp
```

[3121.](https://www.acwing.com/problem/content/)



```cpp
```

[3122.](https://www.acwing.com/problem/content/)



```cpp
```

[3123.](https://www.acwing.com/problem/content/)



```cpp
```

[3124.](https://www.acwing.com/problem/content/)



```cpp
```

[3125.](https://www.acwing.com/problem/content/)



```cpp
```

[3126.](https://www.acwing.com/problem/content/)



```cpp
```

[3127.](https://www.acwing.com/problem/content/)



```cpp
```

[3128.](https://www.acwing.com/problem/content/)



```cpp
```

[3129.](https://www.acwing.com/problem/content/)



```cpp
```

[3130.](https://www.acwing.com/problem/content/)



```cpp
```

[3131.](https://www.acwing.com/problem/content/)



```cpp
```

[3132.](https://www.acwing.com/problem/content/)



```cpp
```

[3133.](https://www.acwing.com/problem/content/)



```cpp
```

[3134.](https://www.acwing.com/problem/content/)



```cpp
```

[3135.](https://www.acwing.com/problem/content/)



```cpp
```

[3136.](https://www.acwing.com/problem/content/)



```cpp
```

[3137.](https://www.acwing.com/problem/content/)



```cpp
```

[3138.](https://www.acwing.com/problem/content/)



```cpp
```

[3139.](https://www.acwing.com/problem/content/)



```cpp
```

[3140.](https://www.acwing.com/problem/content/)



```cpp
```

[3141.](https://www.acwing.com/problem/content/)



```cpp
```

[3142.](https://www.acwing.com/problem/content/)



```cpp
```

[3143.](https://www.acwing.com/problem/content/)



```cpp
```

[3144.](https://www.acwing.com/problem/content/)



```cpp
```

[3145.](https://www.acwing.com/problem/content/)



```cpp
```

[3146.](https://www.acwing.com/problem/content/)



```cpp
```

[3147.](https://www.acwing.com/problem/content/)



```cpp
```

[3148.](https://www.acwing.com/problem/content/)



```cpp
```

[3149.](https://www.acwing.com/problem/content/)



```cpp
```

[3150.](https://www.acwing.com/problem/content/)



```cpp
```

[3151.](https://www.acwing.com/problem/content/)



```cpp
```

[3152.](https://www.acwing.com/problem/content/)



```cpp
```

[3153.](https://www.acwing.com/problem/content/)



```cpp
```

[3154.](https://www.acwing.com/problem/content/)



```cpp
```

[3155.](https://www.acwing.com/problem/content/)



```cpp
```

[3156.](https://www.acwing.com/problem/content/)



```cpp
```

[3157.](https://www.acwing.com/problem/content/)



```cpp
```

[3158.](https://www.acwing.com/problem/content/)



```cpp
```

[3159.](https://www.acwing.com/problem/content/)



```cpp
```

[3160.](https://www.acwing.com/problem/content/)



```cpp
```

[3161.](https://www.acwing.com/problem/content/)



```cpp
```

[3162.](https://www.acwing.com/problem/content/)



```cpp
```

[3163.](https://www.acwing.com/problem/content/)



```cpp
```

[3164.](https://www.acwing.com/problem/content/)



```cpp
```

[3165.](https://www.acwing.com/problem/content/)



```cpp
```

[3166.](https://www.acwing.com/problem/content/)



```cpp
```

[3167.](https://www.acwing.com/problem/content/)



```cpp
```

[3168.](https://www.acwing.com/problem/content/)



```cpp
```

[3169.](https://www.acwing.com/problem/content/)



```cpp
```

[3170.](https://www.acwing.com/problem/content/)



```cpp
```

[3171.](https://www.acwing.com/problem/content/)



```cpp
```

[3172.](https://www.acwing.com/problem/content/)



```cpp
```

[3173.](https://www.acwing.com/problem/content/)



```cpp
```

[3174.](https://www.acwing.com/problem/content/)



```cpp
```

[3175.](https://www.acwing.com/problem/content/)



```cpp
```

[3176.](https://www.acwing.com/problem/content/)



```cpp
```

[3177.](https://www.acwing.com/problem/content/)



```cpp
```

[3178.](https://www.acwing.com/problem/content/)



```cpp
```

[3179.](https://www.acwing.com/problem/content/)



```cpp
```

[3180.](https://www.acwing.com/problem/content/)



```cpp
```

[3181.](https://www.acwing.com/problem/content/)



```cpp
```

[3182.](https://www.acwing.com/problem/content/)



```cpp
```

[3183.](https://www.acwing.com/problem/content/)



```cpp
```

[3184.](https://www.acwing.com/problem/content/)



```cpp
```

[3185.](https://www.acwing.com/problem/content/)



```cpp
```

[3186.](https://www.acwing.com/problem/content/)



```cpp
```

[3187.](https://www.acwing.com/problem/content/)



```cpp
```

[3188.](https://www.acwing.com/problem/content/)



```cpp
```

[3189.](https://www.acwing.com/problem/content/)



```cpp
```

[3190.](https://www.acwing.com/problem/content/)



```cpp
```

[3191.](https://www.acwing.com/problem/content/)



```cpp
```

[3192. 出现次数最多的数](https://www.acwing.com/problem/content/3195/)

```cpp
#include <iostream>

using namespace std;
const int N = 10000 + 10;
int q[N];

int main() {
    int n, num, min = 0;
    scanf("%d", &n);
    while (n--) {
        scanf("%d", &num);
        q[num] += 1;
    }
    for (int i = 0; i < N; i++) {
        if (q[min] < q[i]) min = i;
    }
    printf("%d", min);
    return 0;
}
```

[3193.](https://www.acwing.com/problem/content/)



```cpp
```

[3194.](https://www.acwing.com/problem/content/)



```cpp
```

[3195.](https://www.acwing.com/problem/content/)



```cpp
```

[3196.](https://www.acwing.com/problem/content/)



```cpp
```

[3197.](https://www.acwing.com/problem/content/)



```cpp
```

[3198.](https://www.acwing.com/problem/content/)



```cpp
```

[3199.](https://www.acwing.com/problem/content/)



```cpp
```

[3200.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3201~3300

[3201.](https://www.acwing.com/problem/content/)



```cpp
```

[3202.](https://www.acwing.com/problem/content/)



```cpp
```

[3203.](https://www.acwing.com/problem/content/)



```cpp
```

[3204.](https://www.acwing.com/problem/content/)



```cpp
```

[3205.](https://www.acwing.com/problem/content/)



```cpp
```

[3206.](https://www.acwing.com/problem/content/)



```cpp
```

[3207.](https://www.acwing.com/problem/content/)



```cpp
```

[3208.](https://www.acwing.com/problem/content/)



```cpp
```

[3209.](https://www.acwing.com/problem/content/)



```cpp
```

[3210.](https://www.acwing.com/problem/content/)



```cpp
```

[3211.](https://www.acwing.com/problem/content/)



```cpp
```

[3212.](https://www.acwing.com/problem/content/)



```cpp
```

[3213.](https://www.acwing.com/problem/content/)



```cpp
```

[3214.](https://www.acwing.com/problem/content/)



```cpp
```

[3215.](https://www.acwing.com/problem/content/)



```cpp
```

[3216.](https://www.acwing.com/problem/content/)



```cpp
```

[3217.](https://www.acwing.com/problem/content/)



```cpp
```

[3218.](https://www.acwing.com/problem/content/)



```cpp
```

[3219.](https://www.acwing.com/problem/content/)



```cpp
```

[3220.](https://www.acwing.com/problem/content/)



```cpp
```

[3221.](https://www.acwing.com/problem/content/)



```cpp
```

[3222.](https://www.acwing.com/problem/content/)



```cpp
```

[3223.](https://www.acwing.com/problem/content/)



```cpp
```

[3224.](https://www.acwing.com/problem/content/)



```cpp
```

[3225.](https://www.acwing.com/problem/content/)



```cpp
```

[3226.](https://www.acwing.com/problem/content/)



```cpp
```

[3227.](https://www.acwing.com/problem/content/)



```cpp
```

[3228.](https://www.acwing.com/problem/content/)



```cpp
```

[3229.](https://www.acwing.com/problem/content/)



```cpp
```

[3230.](https://www.acwing.com/problem/content/)



```cpp
```

[3231.](https://www.acwing.com/problem/content/)



```cpp
```

[3232.](https://www.acwing.com/problem/content/)



```cpp
```

[3233.](https://www.acwing.com/problem/content/)



```cpp
```

[3234.](https://www.acwing.com/problem/content/)



```cpp
```

[3235.](https://www.acwing.com/problem/content/)



```cpp
```

[3236.](https://www.acwing.com/problem/content/)



```cpp
```

[3237.](https://www.acwing.com/problem/content/)



```cpp
```

[3238.](https://www.acwing.com/problem/content/)



```cpp
```

[3239.](https://www.acwing.com/problem/content/)



```cpp
```

[3240.](https://www.acwing.com/problem/content/)



```cpp
```

[3241.](https://www.acwing.com/problem/content/)



```cpp
```

[3242.](https://www.acwing.com/problem/content/)



```cpp
```

[3243.](https://www.acwing.com/problem/content/)



```cpp
```

[3244.](https://www.acwing.com/problem/content/)



```cpp
```

[3245.](https://www.acwing.com/problem/content/)



```cpp
```

[3246.](https://www.acwing.com/problem/content/)



```cpp
```

[3247.](https://www.acwing.com/problem/content/)



```cpp
```

[3248.](https://www.acwing.com/problem/content/)



```cpp
```

[3249.](https://www.acwing.com/problem/content/)



```cpp
```

[3250.](https://www.acwing.com/problem/content/)



```cpp
```

[3251.](https://www.acwing.com/problem/content/)



```cpp
```

[3252.](https://www.acwing.com/problem/content/)



```cpp
```

[3253.](https://www.acwing.com/problem/content/)



```cpp
```

[3254.](https://www.acwing.com/problem/content/)



```cpp
```

[3255.](https://www.acwing.com/problem/content/)



```cpp
```

[3256.](https://www.acwing.com/problem/content/)



```cpp
```

[3257.](https://www.acwing.com/problem/content/)



```cpp
```

[3258.](https://www.acwing.com/problem/content/)



```cpp
```

[3259.](https://www.acwing.com/problem/content/)



```cpp
```

[3260.](https://www.acwing.com/problem/content/)



```cpp
```

[3261.](https://www.acwing.com/problem/content/)



```cpp
```

[3262.](https://www.acwing.com/problem/content/)



```cpp
```

[3263.](https://www.acwing.com/problem/content/)



```cpp
```

[3264.](https://www.acwing.com/problem/content/)



```cpp
```

[3265.](https://www.acwing.com/problem/content/)



```cpp
```

[3266.](https://www.acwing.com/problem/content/)



```cpp
```

[3267.](https://www.acwing.com/problem/content/)



```cpp
```

[3268.](https://www.acwing.com/problem/content/)



```cpp
```

[3269.](https://www.acwing.com/problem/content/)



```cpp
```

[3270.](https://www.acwing.com/problem/content/)



```cpp
```

[3271.](https://www.acwing.com/problem/content/)



```cpp
```

[3272.](https://www.acwing.com/problem/content/)



```cpp
```

[3273.](https://www.acwing.com/problem/content/)



```cpp
```

[3274.](https://www.acwing.com/problem/content/)



```cpp
```

[3275.](https://www.acwing.com/problem/content/)



```cpp
```

[3276.](https://www.acwing.com/problem/content/)



```cpp
```

[3277.](https://www.acwing.com/problem/content/)



```cpp
```

[3278.](https://www.acwing.com/problem/content/)



```cpp
```

[3279.](https://www.acwing.com/problem/content/)



```cpp
```

[3280.](https://www.acwing.com/problem/content/)



```cpp
```

[3281.](https://www.acwing.com/problem/content/)



```cpp
```

[3282.](https://www.acwing.com/problem/content/)



```cpp
```

[3283.](https://www.acwing.com/problem/content/)



```cpp
```

[3284.](https://www.acwing.com/problem/content/)



```cpp
```

[3285.](https://www.acwing.com/problem/content/)



```cpp
```

[3286.](https://www.acwing.com/problem/content/)



```cpp
```

[3287.](https://www.acwing.com/problem/content/)



```cpp
```

[3288.](https://www.acwing.com/problem/content/)



```cpp
```

[3289.](https://www.acwing.com/problem/content/)



```cpp
```

[3290.](https://www.acwing.com/problem/content/)



```cpp
```

[3291.](https://www.acwing.com/problem/content/)



```cpp
```

[3292.](https://www.acwing.com/problem/content/)



```cpp
```

[3293.](https://www.acwing.com/problem/content/)



```cpp
```

[3294.](https://www.acwing.com/problem/content/)



```cpp
```

[3295.](https://www.acwing.com/problem/content/)



```cpp
```

[3296.](https://www.acwing.com/problem/content/)



```cpp
```

[3297.](https://www.acwing.com/problem/content/)



```cpp
```

[3298.](https://www.acwing.com/problem/content/)



```cpp
```

[3299.](https://www.acwing.com/problem/content/)



```cpp
```

[3300.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3301~3400

[3301.](https://www.acwing.com/problem/content/)



```cpp
```

[3302.](https://www.acwing.com/problem/content/)



```cpp
```

[3303.](https://www.acwing.com/problem/content/)



```cpp
```

[3304.](https://www.acwing.com/problem/content/)



```cpp
```

[3305.](https://www.acwing.com/problem/content/)



```cpp
```

[3306.](https://www.acwing.com/problem/content/)



```cpp
```

[3307.](https://www.acwing.com/problem/content/)



```cpp
```

[3308.](https://www.acwing.com/problem/content/)



```cpp
```

[3309.](https://www.acwing.com/problem/content/)



```cpp
```

[3310.](https://www.acwing.com/problem/content/)



```cpp
```

[3311.](https://www.acwing.com/problem/content/)



```cpp
```

[3312.](https://www.acwing.com/problem/content/)



```cpp
```

[3313.](https://www.acwing.com/problem/content/)



```cpp
```

[3314.](https://www.acwing.com/problem/content/)



```cpp
```

[3315.](https://www.acwing.com/problem/content/)



```cpp
```

[3316.](https://www.acwing.com/problem/content/)



```cpp
```

[3317.](https://www.acwing.com/problem/content/)



```cpp
```

[3318.](https://www.acwing.com/problem/content/)



```cpp
```

[3319.](https://www.acwing.com/problem/content/)



```cpp
```

[3320.](https://www.acwing.com/problem/content/)



```cpp
```

[3321.](https://www.acwing.com/problem/content/)



```cpp
```

[3322.](https://www.acwing.com/problem/content/)



```cpp
```

[3323.](https://www.acwing.com/problem/content/)



```cpp
```

[3324.](https://www.acwing.com/problem/content/)



```cpp
```

[3325.](https://www.acwing.com/problem/content/)



```cpp
```

[3326.](https://www.acwing.com/problem/content/)



```cpp
```

[3327.](https://www.acwing.com/problem/content/)



```cpp
```

[3328.](https://www.acwing.com/problem/content/)



```cpp
```

[3329.](https://www.acwing.com/problem/content/)



```cpp
```

[3330.](https://www.acwing.com/problem/content/)



```cpp
```

[3331.](https://www.acwing.com/problem/content/)



```cpp
```

[3332.](https://www.acwing.com/problem/content/)



```cpp
```

[3333.](https://www.acwing.com/problem/content/)



```cpp
```

[3334.](https://www.acwing.com/problem/content/)



```cpp
```

[3335.](https://www.acwing.com/problem/content/)



```cpp
```

[3336.](https://www.acwing.com/problem/content/)



```cpp
```

[3337.](https://www.acwing.com/problem/content/)



```cpp
```

[3338.](https://www.acwing.com/problem/content/)



```cpp
```

[3339.](https://www.acwing.com/problem/content/)



```cpp
```

[3340.](https://www.acwing.com/problem/content/)



```cpp
```

[3341.](https://www.acwing.com/problem/content/)



```cpp
```

[3342.](https://www.acwing.com/problem/content/)



```cpp
```

[3343.](https://www.acwing.com/problem/content/)



```cpp
```

[3344.](https://www.acwing.com/problem/content/)



```cpp
```

[3345.](https://www.acwing.com/problem/content/)



```cpp
```

[3346.](https://www.acwing.com/problem/content/)



```cpp
```

[3347.](https://www.acwing.com/problem/content/)



```cpp
```

[3348.](https://www.acwing.com/problem/content/)



```cpp
```

[3349.](https://www.acwing.com/problem/content/)



```cpp
```

[3350.](https://www.acwing.com/problem/content/)



```cpp
```

[3351.](https://www.acwing.com/problem/content/)



```cpp
```

[3352.](https://www.acwing.com/problem/content/)



```cpp
```

[3353.](https://www.acwing.com/problem/content/)



```cpp
```

[3354.](https://www.acwing.com/problem/content/)



```cpp
```

[3355.](https://www.acwing.com/problem/content/)



```cpp
```

[3356.](https://www.acwing.com/problem/content/)



```cpp
```

[3357.](https://www.acwing.com/problem/content/)



```cpp
```

[3358.](https://www.acwing.com/problem/content/)



```cpp
```

[3359.](https://www.acwing.com/problem/content/)



```cpp
```

[3360.](https://www.acwing.com/problem/content/)



```cpp
```

[3361.](https://www.acwing.com/problem/content/)



```cpp
```

[3362.](https://www.acwing.com/problem/content/)



```cpp
```

[3363.](https://www.acwing.com/problem/content/)



```cpp
```

[3364.](https://www.acwing.com/problem/content/)



```cpp
```

[3365.](https://www.acwing.com/problem/content/)



```cpp
```

[3366.](https://www.acwing.com/problem/content/)



```cpp
```

[3367.](https://www.acwing.com/problem/content/)



```cpp
```

[3368.](https://www.acwing.com/problem/content/)



```cpp
```

[3369.](https://www.acwing.com/problem/content/)



```cpp
```

[3370.](https://www.acwing.com/problem/content/)



```cpp
```

[3371.](https://www.acwing.com/problem/content/)



```cpp
```

[3372.](https://www.acwing.com/problem/content/)



```cpp
```

[3373.](https://www.acwing.com/problem/content/)



```cpp
```

[3374.](https://www.acwing.com/problem/content/)



```cpp
```

[3375.](https://www.acwing.com/problem/content/)



```cpp
```

[3376.](https://www.acwing.com/problem/content/)



```cpp
```

[3377.](https://www.acwing.com/problem/content/)



```cpp
```

[3378.](https://www.acwing.com/problem/content/)



```cpp
```

[3379.](https://www.acwing.com/problem/content/)



```cpp
```

[3380.](https://www.acwing.com/problem/content/)



```cpp
```

[3381.](https://www.acwing.com/problem/content/)



```cpp
```

[3382.](https://www.acwing.com/problem/content/)



```cpp
```

[3383.](https://www.acwing.com/problem/content/)



```cpp
```

[3384.](https://www.acwing.com/problem/content/)



```cpp
```

[3385.](https://www.acwing.com/problem/content/)



```cpp
```

[3386.](https://www.acwing.com/problem/content/)



```cpp
```

[3387.](https://www.acwing.com/problem/content/)



```cpp
```

[3388.](https://www.acwing.com/problem/content/)



```cpp
```

[3389.](https://www.acwing.com/problem/content/)



```cpp
```

[3390.](https://www.acwing.com/problem/content/)



```cpp
```

[3391.](https://www.acwing.com/problem/content/)



```cpp
```

[3392.](https://www.acwing.com/problem/content/)



```cpp
```

[3393.](https://www.acwing.com/problem/content/)



```cpp
```

[3394.](https://www.acwing.com/problem/content/)



```cpp
```

[3395.](https://www.acwing.com/problem/content/)



```cpp
```

[3396.](https://www.acwing.com/problem/content/)



```cpp
```

[3397.](https://www.acwing.com/problem/content/)



```cpp
```

[3398.](https://www.acwing.com/problem/content/)



```cpp
```

[3399.](https://www.acwing.com/problem/content/)



```cpp
```

[3400.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3401~3500

[3401.](https://www.acwing.com/problem/content/)



```cpp
```

[3402.](https://www.acwing.com/problem/content/)



```cpp
```

[3403.](https://www.acwing.com/problem/content/)



```cpp
```

[3404.](https://www.acwing.com/problem/content/)



```cpp
```

[3405.](https://www.acwing.com/problem/content/)



```cpp
```

[3406.](https://www.acwing.com/problem/content/)



```cpp
```

[3407.](https://www.acwing.com/problem/content/)



```cpp
```

[3408.](https://www.acwing.com/problem/content/)



```cpp
```

[3409.](https://www.acwing.com/problem/content/)



```cpp
```

[3410.](https://www.acwing.com/problem/content/)



```cpp
```

[3411.](https://www.acwing.com/problem/content/)



```cpp
```

[3412.](https://www.acwing.com/problem/content/)



```cpp
```

[3413.](https://www.acwing.com/problem/content/)



```cpp
```

[3414.](https://www.acwing.com/problem/content/)



```cpp
```

[3415.](https://www.acwing.com/problem/content/)



```cpp
```

[3416.](https://www.acwing.com/problem/content/)



```cpp
```

[3417.](https://www.acwing.com/problem/content/)



```cpp
```

[3418.](https://www.acwing.com/problem/content/)



```cpp
```

[3419.](https://www.acwing.com/problem/content/)



```cpp
```

[3420.](https://www.acwing.com/problem/content/)



```cpp
```

[3421.](https://www.acwing.com/problem/content/)



```cpp
```

[3422.](https://www.acwing.com/problem/content/)



```cpp
```

[3423.](https://www.acwing.com/problem/content/)



```cpp
```

[3424.](https://www.acwing.com/problem/content/)



```cpp
```

[3425.](https://www.acwing.com/problem/content/)



```cpp
```

[3426.](https://www.acwing.com/problem/content/)



```cpp
```

[3427.](https://www.acwing.com/problem/content/)



```cpp
```

[3428.](https://www.acwing.com/problem/content/)



```cpp
```

[3429.](https://www.acwing.com/problem/content/)



```cpp
```

[3430.](https://www.acwing.com/problem/content/)



```cpp
```

[3431.](https://www.acwing.com/problem/content/)



```cpp
```

[3432.](https://www.acwing.com/problem/content/)



```cpp
```

[3433.](https://www.acwing.com/problem/content/)



```cpp
```

[3434.](https://www.acwing.com/problem/content/)



```cpp
```

[3435.](https://www.acwing.com/problem/content/)



```cpp
```

[3436.](https://www.acwing.com/problem/content/)



```cpp
```

[3437.](https://www.acwing.com/problem/content/)



```cpp
```

[3438.](https://www.acwing.com/problem/content/)



```cpp
```

[3439.](https://www.acwing.com/problem/content/)



```cpp
```

[3440.](https://www.acwing.com/problem/content/)



```cpp
```

[3441.](https://www.acwing.com/problem/content/)



```cpp
```

[3442.](https://www.acwing.com/problem/content/)



```cpp
```

[3443.](https://www.acwing.com/problem/content/)



```cpp
```

[3444.](https://www.acwing.com/problem/content/)



```cpp
```

[3445.](https://www.acwing.com/problem/content/)



```cpp
```

[3446.](https://www.acwing.com/problem/content/)



```cpp
```

[3447.](https://www.acwing.com/problem/content/)



```cpp
```

[3448.](https://www.acwing.com/problem/content/)



```cpp
```

[3449.](https://www.acwing.com/problem/content/)



```cpp
```

[3450.](https://www.acwing.com/problem/content/)



```cpp
```

[3451.](https://www.acwing.com/problem/content/)



```cpp
```

[3452.](https://www.acwing.com/problem/content/)



```cpp
```

[3453.](https://www.acwing.com/problem/content/)



```cpp
```

[3454.](https://www.acwing.com/problem/content/)



```cpp
```

[3455.](https://www.acwing.com/problem/content/)



```cpp
```

[3456.](https://www.acwing.com/problem/content/)



```cpp
```

[3457.](https://www.acwing.com/problem/content/)



```cpp
```

[3458.](https://www.acwing.com/problem/content/)



```cpp
```

[3459.](https://www.acwing.com/problem/content/)



```cpp
```

[3460.](https://www.acwing.com/problem/content/)



```cpp
```

[3461.](https://www.acwing.com/problem/content/)



```cpp
```

[3462.](https://www.acwing.com/problem/content/)



```cpp
```

[3463.](https://www.acwing.com/problem/content/)



```cpp
```

[3464.](https://www.acwing.com/problem/content/)



```cpp
```

[3465.](https://www.acwing.com/problem/content/)



```cpp
```

[3466.](https://www.acwing.com/problem/content/)



```cpp
```

[3467.](https://www.acwing.com/problem/content/)



```cpp
```

[3468.](https://www.acwing.com/problem/content/)



```cpp
```

[3469.](https://www.acwing.com/problem/content/)



```cpp
```

[3470.](https://www.acwing.com/problem/content/)



```cpp
```

[3471.](https://www.acwing.com/problem/content/)



```cpp
```

[3472.](https://www.acwing.com/problem/content/)



```cpp
```

[3473.](https://www.acwing.com/problem/content/)



```cpp
```

[3474.](https://www.acwing.com/problem/content/)



```cpp
```

[3475.](https://www.acwing.com/problem/content/)



```cpp
```

[3476.](https://www.acwing.com/problem/content/)



```cpp
```

[3477.](https://www.acwing.com/problem/content/)



```cpp
```

[3478.](https://www.acwing.com/problem/content/)



```cpp
```

[3479.](https://www.acwing.com/problem/content/)



```cpp
```

[3480.](https://www.acwing.com/problem/content/)



```cpp
```

[3481.](https://www.acwing.com/problem/content/)



```cpp
```

[3482.](https://www.acwing.com/problem/content/)



```cpp
```

[3483.](https://www.acwing.com/problem/content/)



```cpp
```

[3484.](https://www.acwing.com/problem/content/)



```cpp
```

[3485.](https://www.acwing.com/problem/content/)



```cpp
```

[3486.](https://www.acwing.com/problem/content/)



```cpp
```

[3487.](https://www.acwing.com/problem/content/)



```cpp
```

[3488.](https://www.acwing.com/problem/content/)



```cpp
```

[3489.](https://www.acwing.com/problem/content/)



```cpp
```

[3490.](https://www.acwing.com/problem/content/)



```cpp
```

[3491.](https://www.acwing.com/problem/content/)



```cpp
```

[3492.](https://www.acwing.com/problem/content/)



```cpp
```

[3493.](https://www.acwing.com/problem/content/)



```cpp
```

[3494.](https://www.acwing.com/problem/content/)



```cpp
```

[3495.](https://www.acwing.com/problem/content/)



```cpp
```

[3496.](https://www.acwing.com/problem/content/)



```cpp
```

[3497.](https://www.acwing.com/problem/content/)



```cpp
```

[3498.](https://www.acwing.com/problem/content/)



```cpp
```

[3499.](https://www.acwing.com/problem/content/)



```cpp
```

[3500.](https://www.acwing.com/problem/content/)



```cpp
```

### 3501~4000

#### 3501~3600

[3501.](https://www.acwing.com/problem/content/)



```cpp
```

[3502.](https://www.acwing.com/problem/content/)



```cpp
```

[3503.](https://www.acwing.com/problem/content/)



```cpp
```

[3504.](https://www.acwing.com/problem/content/)



```cpp
```

[3505.](https://www.acwing.com/problem/content/)



```cpp
```

[3506.](https://www.acwing.com/problem/content/)



```cpp
```

[3507.](https://www.acwing.com/problem/content/)



```cpp
```

[3508.](https://www.acwing.com/problem/content/)



```cpp
```

[3509.](https://www.acwing.com/problem/content/)



```cpp
```

[3510.](https://www.acwing.com/problem/content/)



```cpp
```

[3511.](https://www.acwing.com/problem/content/)



```cpp
```

[3512.](https://www.acwing.com/problem/content/)



```cpp
```

[3513.](https://www.acwing.com/problem/content/)



```cpp
```

[3514.](https://www.acwing.com/problem/content/)



```cpp
```

[3515.](https://www.acwing.com/problem/content/)



```cpp
```

[3516.](https://www.acwing.com/problem/content/)



```cpp
```

[3517.](https://www.acwing.com/problem/content/)



```cpp
```

[3518.](https://www.acwing.com/problem/content/)



```cpp
```

[3519.](https://www.acwing.com/problem/content/)



```cpp
```

[3520.](https://www.acwing.com/problem/content/)



```cpp
```

[3521.](https://www.acwing.com/problem/content/)



```cpp
```

[3522.](https://www.acwing.com/problem/content/)



```cpp
```

[3523.](https://www.acwing.com/problem/content/)



```cpp
```

[3524.](https://www.acwing.com/problem/content/)



```cpp
```

[3525.](https://www.acwing.com/problem/content/)



```cpp
```

[3526.](https://www.acwing.com/problem/content/)



```cpp
```

[3527.](https://www.acwing.com/problem/content/)



```cpp
```

[3528.](https://www.acwing.com/problem/content/)



```cpp
```

[3529.](https://www.acwing.com/problem/content/)



```cpp
```

[3530.](https://www.acwing.com/problem/content/)



```cpp
```

[3531.](https://www.acwing.com/problem/content/)



```cpp
```

[3532.](https://www.acwing.com/problem/content/)



```cpp
```

[3533.](https://www.acwing.com/problem/content/)



```cpp
```

[3534.](https://www.acwing.com/problem/content/)



```cpp
```

[3535.](https://www.acwing.com/problem/content/)



```cpp
```

[3536.](https://www.acwing.com/problem/content/)



```cpp
```

[3537.](https://www.acwing.com/problem/content/)



```cpp
```

[3538.](https://www.acwing.com/problem/content/)



```cpp
```

[3539.](https://www.acwing.com/problem/content/)



```cpp
```

[3540.](https://www.acwing.com/problem/content/)



```cpp
```

[3541.](https://www.acwing.com/problem/content/)



```cpp
```

[3542.](https://www.acwing.com/problem/content/)



```cpp
```

[3543.](https://www.acwing.com/problem/content/)



```cpp
```

[3544.](https://www.acwing.com/problem/content/)



```cpp
```

[3545.](https://www.acwing.com/problem/content/)



```cpp
```

[3546.](https://www.acwing.com/problem/content/)



```cpp
```

[3547.](https://www.acwing.com/problem/content/)



```cpp
```

[3548.](https://www.acwing.com/problem/content/)



```cpp
```

[3549.](https://www.acwing.com/problem/content/)



```cpp
```

[3550.](https://www.acwing.com/problem/content/)



```cpp
```

[3551.](https://www.acwing.com/problem/content/)



```cpp
```

[3552.](https://www.acwing.com/problem/content/)



```cpp
```

[3553.](https://www.acwing.com/problem/content/)



```cpp
```

[3554.](https://www.acwing.com/problem/content/)



```cpp
```

[3555.](https://www.acwing.com/problem/content/)



```cpp
```

[3556.](https://www.acwing.com/problem/content/)



```cpp
```

[3557.](https://www.acwing.com/problem/content/)



```cpp
```

[3558.](https://www.acwing.com/problem/content/)



```cpp
```

[3559.](https://www.acwing.com/problem/content/)



```cpp
```

[3560.](https://www.acwing.com/problem/content/)



```cpp
```

[3561.](https://www.acwing.com/problem/content/)



```cpp
```

[3562.](https://www.acwing.com/problem/content/)



```cpp
```

[3563.](https://www.acwing.com/problem/content/)



```cpp
```

[3564.](https://www.acwing.com/problem/content/)



```cpp
```

[3565.](https://www.acwing.com/problem/content/)



```cpp
```

[3566.](https://www.acwing.com/problem/content/)



```cpp
```

[3567.](https://www.acwing.com/problem/content/)



```cpp
```

[3568.](https://www.acwing.com/problem/content/)



```cpp
```

[3569.](https://www.acwing.com/problem/content/)



```cpp
```

[3570.](https://www.acwing.com/problem/content/)



```cpp
```

[3571.](https://www.acwing.com/problem/content/)



```cpp
```

[3572.](https://www.acwing.com/problem/content/)



```cpp
```

[3573.](https://www.acwing.com/problem/content/)



```cpp
```

[3574.](https://www.acwing.com/problem/content/)



```cpp
```

[3575.](https://www.acwing.com/problem/content/)



```cpp
```

[3576.](https://www.acwing.com/problem/content/)



```cpp
```

[3577.](https://www.acwing.com/problem/content/)



```cpp
```

[3578.](https://www.acwing.com/problem/content/)



```cpp
```

[3579.](https://www.acwing.com/problem/content/)



```cpp
```

[3580.](https://www.acwing.com/problem/content/)



```cpp
```

[3581.](https://www.acwing.com/problem/content/)



```cpp
```

[3582.](https://www.acwing.com/problem/content/)



```cpp
```

[3583.](https://www.acwing.com/problem/content/)



```cpp
```

[3584.](https://www.acwing.com/problem/content/)



```cpp
```

[3585.](https://www.acwing.com/problem/content/)



```cpp
```

[3586.](https://www.acwing.com/problem/content/)



```cpp
```

[3587.](https://www.acwing.com/problem/content/)



```cpp
```

[3588.](https://www.acwing.com/problem/content/)



```cpp
```

[3589.](https://www.acwing.com/problem/content/)



```cpp
```

[3590.](https://www.acwing.com/problem/content/)



```cpp
```

[3591.](https://www.acwing.com/problem/content/)



```cpp
```

[3592.](https://www.acwing.com/problem/content/)



```cpp
```

[3593.](https://www.acwing.com/problem/content/)



```cpp
```

[3594.](https://www.acwing.com/problem/content/)



```cpp
```

[3595.](https://www.acwing.com/problem/content/)



```cpp
```

[3596.](https://www.acwing.com/problem/content/)



```cpp
```

[3597.](https://www.acwing.com/problem/content/)



```cpp
```

[3598.](https://www.acwing.com/problem/content/)



```cpp
```

[3599.](https://www.acwing.com/problem/content/)



```cpp
```

[3600.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3601~3700

[3601.](https://www.acwing.com/problem/content/)



```cpp
```

[3602.](https://www.acwing.com/problem/content/)



```cpp
```

[3603.](https://www.acwing.com/problem/content/)



```cpp
```

[3604.](https://www.acwing.com/problem/content/)



```cpp
```

[3605.](https://www.acwing.com/problem/content/)



```cpp
```

[3606.](https://www.acwing.com/problem/content/)



```cpp
```

[3607.](https://www.acwing.com/problem/content/)



```cpp
```

[3608.](https://www.acwing.com/problem/content/)



```cpp
```

[3609.](https://www.acwing.com/problem/content/)



```cpp
```

[3610.](https://www.acwing.com/problem/content/)



```cpp
```

[3611.](https://www.acwing.com/problem/content/)



```cpp
```

[3612.](https://www.acwing.com/problem/content/)



```cpp
```

[3613.](https://www.acwing.com/problem/content/)



```cpp
```

[3614.](https://www.acwing.com/problem/content/)



```cpp
```

[3615.](https://www.acwing.com/problem/content/)



```cpp
```

[3616.](https://www.acwing.com/problem/content/)



```cpp
```

[3617.](https://www.acwing.com/problem/content/)



```cpp
```

[3618.](https://www.acwing.com/problem/content/)



```cpp
```

[3619.](https://www.acwing.com/problem/content/)



```cpp
```

[3620.](https://www.acwing.com/problem/content/)



```cpp
```

[3621.](https://www.acwing.com/problem/content/)



```cpp
```

[3622.](https://www.acwing.com/problem/content/)



```cpp
```

[3623.](https://www.acwing.com/problem/content/)



```cpp
```

[3624.](https://www.acwing.com/problem/content/)



```cpp
```

[3625.](https://www.acwing.com/problem/content/)



```cpp
```

[3626.](https://www.acwing.com/problem/content/)



```cpp
```

[3627.](https://www.acwing.com/problem/content/)



```cpp
```

[3628.](https://www.acwing.com/problem/content/)



```cpp
```

[3629.](https://www.acwing.com/problem/content/)



```cpp
```

[3630.](https://www.acwing.com/problem/content/)



```cpp
```

[3631.](https://www.acwing.com/problem/content/)



```cpp
```

[3632.](https://www.acwing.com/problem/content/)



```cpp
```

[3633.](https://www.acwing.com/problem/content/)



```cpp
```

[3634.](https://www.acwing.com/problem/content/)



```cpp
```

[3635.](https://www.acwing.com/problem/content/)



```cpp
```

[3636.](https://www.acwing.com/problem/content/)



```cpp
```

[3637.](https://www.acwing.com/problem/content/)



```cpp
```

[3638.](https://www.acwing.com/problem/content/)



```cpp
```

[3639.](https://www.acwing.com/problem/content/)



```cpp
```

[3640.](https://www.acwing.com/problem/content/)



```cpp
```

[3641.](https://www.acwing.com/problem/content/)



```cpp
```

[3642.](https://www.acwing.com/problem/content/)



```cpp
```

[3643.](https://www.acwing.com/problem/content/)



```cpp
```

[3644.](https://www.acwing.com/problem/content/)



```cpp
```

[3645.](https://www.acwing.com/problem/content/)



```cpp
```

[3646.](https://www.acwing.com/problem/content/)



```cpp
```

[3647.](https://www.acwing.com/problem/content/)



```cpp
```

[3648.](https://www.acwing.com/problem/content/)



```cpp
```

[3649.](https://www.acwing.com/problem/content/)



```cpp
```

[3650.](https://www.acwing.com/problem/content/)



```cpp
```

[3651.](https://www.acwing.com/problem/content/)



```cpp
```

[3652.](https://www.acwing.com/problem/content/)



```cpp
```

[3653.](https://www.acwing.com/problem/content/)



```cpp
```

[3654.](https://www.acwing.com/problem/content/)



```cpp
```

[3655.](https://www.acwing.com/problem/content/)



```cpp
```

[3656.](https://www.acwing.com/problem/content/)



```cpp
```

[3657.](https://www.acwing.com/problem/content/)



```cpp
```

[3658.](https://www.acwing.com/problem/content/)



```cpp
```

[3659.](https://www.acwing.com/problem/content/)



```cpp
```

[3660.](https://www.acwing.com/problem/content/)



```cpp
```

[3661.](https://www.acwing.com/problem/content/)



```cpp
```

[3662.](https://www.acwing.com/problem/content/)



```cpp
```

[3663.](https://www.acwing.com/problem/content/)



```cpp
```

[3664.](https://www.acwing.com/problem/content/)



```cpp
```

[3665.](https://www.acwing.com/problem/content/)



```cpp
```

[3666.](https://www.acwing.com/problem/content/)



```cpp
```

[3667.](https://www.acwing.com/problem/content/)



```cpp
```

[3668.](https://www.acwing.com/problem/content/)



```cpp
```

[3669.](https://www.acwing.com/problem/content/)



```cpp
```

[3670.](https://www.acwing.com/problem/content/)



```cpp
```

[3671.](https://www.acwing.com/problem/content/)



```cpp
```

[3672.](https://www.acwing.com/problem/content/)



```cpp
```

[3673.](https://www.acwing.com/problem/content/)



```cpp
```

[3674.](https://www.acwing.com/problem/content/)



```cpp
```

[3675.](https://www.acwing.com/problem/content/)



```cpp
```

[3676.](https://www.acwing.com/problem/content/)



```cpp
```

[3677.](https://www.acwing.com/problem/content/)



```cpp
```

[3678.](https://www.acwing.com/problem/content/)



```cpp
```

[3679.](https://www.acwing.com/problem/content/)



```cpp
```

[3680.](https://www.acwing.com/problem/content/)



```cpp
```

[3681.](https://www.acwing.com/problem/content/)



```cpp
```

[3682.](https://www.acwing.com/problem/content/)



```cpp
```

[3683.](https://www.acwing.com/problem/content/)



```cpp
```

[3684.](https://www.acwing.com/problem/content/)



```cpp
```

[3685.](https://www.acwing.com/problem/content/)



```cpp
```

[3686.](https://www.acwing.com/problem/content/)



```cpp
```

[3687.](https://www.acwing.com/problem/content/)



```cpp
```

[3688.](https://www.acwing.com/problem/content/)



```cpp
```

[3689.](https://www.acwing.com/problem/content/)



```cpp
```

[3690.](https://www.acwing.com/problem/content/)



```cpp
```

[3691.](https://www.acwing.com/problem/content/)



```cpp
```

[3692.](https://www.acwing.com/problem/content/)



```cpp
```

[3693.](https://www.acwing.com/problem/content/)



```cpp
```

[3694.](https://www.acwing.com/problem/content/)



```cpp
```

[3695.](https://www.acwing.com/problem/content/)



```cpp
```

[3696.](https://www.acwing.com/problem/content/)



```cpp
```

[3697.](https://www.acwing.com/problem/content/)



```cpp
```

[3698.](https://www.acwing.com/problem/content/)



```cpp
```

[3699.](https://www.acwing.com/problem/content/)



```cpp
```

[3700.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3701~3800

[3701.](https://www.acwing.com/problem/content/)



```cpp
```

[3702.](https://www.acwing.com/problem/content/)



```cpp
```

[3703.](https://www.acwing.com/problem/content/)



```cpp
```

[3704.](https://www.acwing.com/problem/content/)



```cpp
```

[3705.](https://www.acwing.com/problem/content/)



```cpp
```

[3706.](https://www.acwing.com/problem/content/)



```cpp
```

[3707.](https://www.acwing.com/problem/content/)



```cpp
```

[3708.](https://www.acwing.com/problem/content/)



```cpp
```

[3709.](https://www.acwing.com/problem/content/)



```cpp
```

[3710.](https://www.acwing.com/problem/content/)



```cpp
```

[3711.](https://www.acwing.com/problem/content/)



```cpp
```

[3712.](https://www.acwing.com/problem/content/)



```cpp
```

[3713.](https://www.acwing.com/problem/content/)



```cpp
```

[3714.](https://www.acwing.com/problem/content/)



```cpp
```

[3715.](https://www.acwing.com/problem/content/)



```cpp
```

[3716.](https://www.acwing.com/problem/content/)



```cpp
```

[3717.](https://www.acwing.com/problem/content/)



```cpp
```

[3718.](https://www.acwing.com/problem/content/)



```cpp
```

[3719.](https://www.acwing.com/problem/content/)



```cpp
```

[3720.](https://www.acwing.com/problem/content/)



```cpp
```

[3721.](https://www.acwing.com/problem/content/)



```cpp
```

[3722.](https://www.acwing.com/problem/content/)



```cpp
```

[3723.](https://www.acwing.com/problem/content/)



```cpp
```

[3724.](https://www.acwing.com/problem/content/)



```cpp
```

[3725.](https://www.acwing.com/problem/content/)



```cpp
```

[3726.](https://www.acwing.com/problem/content/)



```cpp
```

[3727.](https://www.acwing.com/problem/content/)



```cpp
```

[3728.](https://www.acwing.com/problem/content/)



```cpp
```

[3729.](https://www.acwing.com/problem/content/)



```cpp
```

[3730.](https://www.acwing.com/problem/content/)



```cpp
```

[3731.](https://www.acwing.com/problem/content/)



```cpp
```

[3732.](https://www.acwing.com/problem/content/)



```cpp
```

[3733.](https://www.acwing.com/problem/content/)



```cpp
```

[3734.](https://www.acwing.com/problem/content/)



```cpp
```

[3735.](https://www.acwing.com/problem/content/)



```cpp
```

[3736.](https://www.acwing.com/problem/content/)



```cpp
```

[3737.](https://www.acwing.com/problem/content/)



```cpp
```

[3738.](https://www.acwing.com/problem/content/)



```cpp
```

[3739.](https://www.acwing.com/problem/content/)



```cpp
```

[3740.](https://www.acwing.com/problem/content/)



```cpp
```

[3741.](https://www.acwing.com/problem/content/)



```cpp
```

[3742.](https://www.acwing.com/problem/content/)



```cpp
```

[3743.](https://www.acwing.com/problem/content/)



```cpp
```

[3744.](https://www.acwing.com/problem/content/)



```cpp
```

[3745.](https://www.acwing.com/problem/content/)



```cpp
```

[3746.](https://www.acwing.com/problem/content/)



```cpp
```

[3747.](https://www.acwing.com/problem/content/)



```cpp
```

[3748.](https://www.acwing.com/problem/content/)



```cpp
```

[3749.](https://www.acwing.com/problem/content/)



```cpp
```

[3750.](https://www.acwing.com/problem/content/)



```cpp
```

[3751.](https://www.acwing.com/problem/content/)



```cpp
```

[3752.](https://www.acwing.com/problem/content/)



```cpp
```

[3753.](https://www.acwing.com/problem/content/)



```cpp
```

[3754.](https://www.acwing.com/problem/content/)



```cpp
```

[3755.](https://www.acwing.com/problem/content/)



```cpp
```

[3756.](https://www.acwing.com/problem/content/)



```cpp
```

[3757.](https://www.acwing.com/problem/content/)



```cpp
```

[3758.](https://www.acwing.com/problem/content/)



```cpp
```

[3759.](https://www.acwing.com/problem/content/)



```cpp
```

[3760.](https://www.acwing.com/problem/content/)



```cpp
```

[3761.](https://www.acwing.com/problem/content/)



```cpp
```

[3762.](https://www.acwing.com/problem/content/)



```cpp
```

[3763.](https://www.acwing.com/problem/content/)



```cpp
```

[3764.](https://www.acwing.com/problem/content/)



```cpp
```

[3765.](https://www.acwing.com/problem/content/)



```cpp
```

[3766.](https://www.acwing.com/problem/content/)



```cpp
```

[3767.](https://www.acwing.com/problem/content/)



```cpp
```

[3768.](https://www.acwing.com/problem/content/)



```cpp
```

[3769.](https://www.acwing.com/problem/content/)



```cpp
```

[3770.](https://www.acwing.com/problem/content/)



```cpp
```

[3771.](https://www.acwing.com/problem/content/)



```cpp
```

[3772.](https://www.acwing.com/problem/content/)



```cpp
```

[3773.](https://www.acwing.com/problem/content/)



```cpp
```

[3774.](https://www.acwing.com/problem/content/)



```cpp
```

[3775.](https://www.acwing.com/problem/content/)



```cpp
```

[3776.](https://www.acwing.com/problem/content/)



```cpp
```

[3777.](https://www.acwing.com/problem/content/)



```cpp
```

[3778.](https://www.acwing.com/problem/content/)



```cpp
```

[3779.](https://www.acwing.com/problem/content/)



```cpp
```

[3780.](https://www.acwing.com/problem/content/)



```cpp
```

[3781.](https://www.acwing.com/problem/content/)



```cpp
```

[3782.](https://www.acwing.com/problem/content/)



```cpp
```

[3783.](https://www.acwing.com/problem/content/)



```cpp
```

[3784.](https://www.acwing.com/problem/content/)



```cpp
```

[3785.](https://www.acwing.com/problem/content/)



```cpp
```

[3786.](https://www.acwing.com/problem/content/)



```cpp
```

[3787.](https://www.acwing.com/problem/content/)



```cpp
```

[3788.](https://www.acwing.com/problem/content/)



```cpp
```

[3789.](https://www.acwing.com/problem/content/)



```cpp
```

[3790.](https://www.acwing.com/problem/content/)



```cpp
```

[3791.](https://www.acwing.com/problem/content/)



```cpp
```

[3792.](https://www.acwing.com/problem/content/)



```cpp
```

[3793.](https://www.acwing.com/problem/content/)



```cpp
```

[3794.](https://www.acwing.com/problem/content/)



```cpp
```

[3795.](https://www.acwing.com/problem/content/)



```cpp
```

[3796.](https://www.acwing.com/problem/content/)



```cpp
```

[3797.](https://www.acwing.com/problem/content/)



```cpp
```

[3798.](https://www.acwing.com/problem/content/)



```cpp
```

[3799.](https://www.acwing.com/problem/content/)



```cpp
```

[3800.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3801~3900

[3801.](https://www.acwing.com/problem/content/)



```cpp
```

[3802.](https://www.acwing.com/problem/content/)



```cpp
```

[3803.](https://www.acwing.com/problem/content/)



```cpp
```

[3804.](https://www.acwing.com/problem/content/)



```cpp
```

[3805.](https://www.acwing.com/problem/content/)



```cpp
```

[3806.](https://www.acwing.com/problem/content/)



```cpp
```

[3807.](https://www.acwing.com/problem/content/)



```cpp
```

[3808.](https://www.acwing.com/problem/content/)



```cpp
```

[3809.](https://www.acwing.com/problem/content/)



```cpp
```

[3810.](https://www.acwing.com/problem/content/)



```cpp
```

[3811.](https://www.acwing.com/problem/content/)



```cpp
```

[3812.](https://www.acwing.com/problem/content/)



```cpp
```

[3813.](https://www.acwing.com/problem/content/)



```cpp
```

[3814.](https://www.acwing.com/problem/content/)



```cpp
```

[3815.](https://www.acwing.com/problem/content/)



```cpp
```

[3816.](https://www.acwing.com/problem/content/)



```cpp
```

[3817.](https://www.acwing.com/problem/content/)



```cpp
```

[3818.](https://www.acwing.com/problem/content/)



```cpp
```

[3819.](https://www.acwing.com/problem/content/)



```cpp
```

[3820.](https://www.acwing.com/problem/content/)



```cpp
```

[3821.](https://www.acwing.com/problem/content/)



```cpp
```

[3822.](https://www.acwing.com/problem/content/)



```cpp
```

[3823.](https://www.acwing.com/problem/content/)



```cpp
```

[3824.](https://www.acwing.com/problem/content/)



```cpp
```

[3825.](https://www.acwing.com/problem/content/)



```cpp
```

[3826.](https://www.acwing.com/problem/content/)



```cpp
```

[3827.](https://www.acwing.com/problem/content/)



```cpp
```

[3828.](https://www.acwing.com/problem/content/)



```cpp
```

[3829.](https://www.acwing.com/problem/content/)



```cpp
```

[3830.](https://www.acwing.com/problem/content/)



```cpp
```

[3831.](https://www.acwing.com/problem/content/)



```cpp
```

[3832.](https://www.acwing.com/problem/content/)



```cpp
```

[3833.](https://www.acwing.com/problem/content/)



```cpp
```

[3834.](https://www.acwing.com/problem/content/)



```cpp
```

[3835.](https://www.acwing.com/problem/content/)



```cpp
```

[3836.](https://www.acwing.com/problem/content/)



```cpp
```

[3837.](https://www.acwing.com/problem/content/)



```cpp
```

[3838.](https://www.acwing.com/problem/content/)



```cpp
```

[3839.](https://www.acwing.com/problem/content/)



```cpp
```

[3840.](https://www.acwing.com/problem/content/)



```cpp
```

[3841.](https://www.acwing.com/problem/content/)



```cpp
```

[3842.](https://www.acwing.com/problem/content/)



```cpp
```

[3843.](https://www.acwing.com/problem/content/)



```cpp
```

[3844.](https://www.acwing.com/problem/content/)



```cpp
```

[3845.](https://www.acwing.com/problem/content/)



```cpp
```

[3846.](https://www.acwing.com/problem/content/)



```cpp
```

[3847.](https://www.acwing.com/problem/content/)



```cpp
```

[3848.](https://www.acwing.com/problem/content/)



```cpp
```

[3849.](https://www.acwing.com/problem/content/)



```cpp
```

[3850.](https://www.acwing.com/problem/content/)



```cpp
```

[3851.](https://www.acwing.com/problem/content/)



```cpp
```

[3852.](https://www.acwing.com/problem/content/)



```cpp
```

[3853.](https://www.acwing.com/problem/content/)



```cpp
```

[3854.](https://www.acwing.com/problem/content/)



```cpp
```

[3855.](https://www.acwing.com/problem/content/)



```cpp
```

[3856.](https://www.acwing.com/problem/content/)



```cpp
```

[3857.](https://www.acwing.com/problem/content/)



```cpp
```

[3858.](https://www.acwing.com/problem/content/)



```cpp
```

[3859.](https://www.acwing.com/problem/content/)



```cpp
```

[3860.](https://www.acwing.com/problem/content/)



```cpp
```

[3861.](https://www.acwing.com/problem/content/)



```cpp
```

[3862.](https://www.acwing.com/problem/content/)



```cpp
```

[3863.](https://www.acwing.com/problem/content/)



```cpp
```

[3864.](https://www.acwing.com/problem/content/)



```cpp
```

[3865.](https://www.acwing.com/problem/content/)



```cpp
```

[3866.](https://www.acwing.com/problem/content/)



```cpp
```

[3867.](https://www.acwing.com/problem/content/)



```cpp
```

[3868.](https://www.acwing.com/problem/content/)



```cpp
```

[3869.](https://www.acwing.com/problem/content/)



```cpp
```

[3870.](https://www.acwing.com/problem/content/)



```cpp
```

[3871.](https://www.acwing.com/problem/content/)



```cpp
```

[3872.](https://www.acwing.com/problem/content/)



```cpp
```

[3873.](https://www.acwing.com/problem/content/)



```cpp
```

[3874.](https://www.acwing.com/problem/content/)



```cpp
```

[3875.](https://www.acwing.com/problem/content/)



```cpp
```

[3876.](https://www.acwing.com/problem/content/)



```cpp
```

[3877.](https://www.acwing.com/problem/content/)



```cpp
```

[3878.](https://www.acwing.com/problem/content/)



```cpp
```

[3879.](https://www.acwing.com/problem/content/)



```cpp
```

[3880.](https://www.acwing.com/problem/content/)



```cpp
```

[3881.](https://www.acwing.com/problem/content/)



```cpp
```

[3882.](https://www.acwing.com/problem/content/)



```cpp
```

[3883.](https://www.acwing.com/problem/content/)



```cpp
```

[3884.](https://www.acwing.com/problem/content/)



```cpp
```

[3885.](https://www.acwing.com/problem/content/)



```cpp
```

[3886.](https://www.acwing.com/problem/content/)



```cpp
```

[3887.](https://www.acwing.com/problem/content/)



```cpp
```

[3888.](https://www.acwing.com/problem/content/)



```cpp
```

[3889.](https://www.acwing.com/problem/content/)



```cpp
```

[3890.](https://www.acwing.com/problem/content/)



```cpp
```

[3891.](https://www.acwing.com/problem/content/)



```cpp
```

[3892.](https://www.acwing.com/problem/content/)



```cpp
```

[3893.](https://www.acwing.com/problem/content/)



```cpp
```

[3894.](https://www.acwing.com/problem/content/)



```cpp
```

[3895.](https://www.acwing.com/problem/content/)



```cpp
```

[3896.](https://www.acwing.com/problem/content/)



```cpp
```

[3897.](https://www.acwing.com/problem/content/)



```cpp
```

[3898.](https://www.acwing.com/problem/content/)



```cpp
```

[3899.](https://www.acwing.com/problem/content/)



```cpp
```

[3900.](https://www.acwing.com/problem/content/)



```cpp
```

#### 3901~4000

[3901.](https://www.acwing.com/problem/content/)



```cpp
```

[3902.](https://www.acwing.com/problem/content/)



```cpp
```

[3903.](https://www.acwing.com/problem/content/)



```cpp
```

[3904.](https://www.acwing.com/problem/content/)



```cpp
```

[3905.](https://www.acwing.com/problem/content/)



```cpp
```

[3906.](https://www.acwing.com/problem/content/)



```cpp
```

[3907.](https://www.acwing.com/problem/content/)



```cpp
```

[3908.](https://www.acwing.com/problem/content/)



```cpp
```

[3909.](https://www.acwing.com/problem/content/)



```cpp
```

[3910.](https://www.acwing.com/problem/content/)



```cpp
```

[3911.](https://www.acwing.com/problem/content/)



```cpp
```

[3912.](https://www.acwing.com/problem/content/)



```cpp
```

[3913.](https://www.acwing.com/problem/content/)



```cpp
```

[3914.](https://www.acwing.com/problem/content/)



```cpp
```

[3915.](https://www.acwing.com/problem/content/)



```cpp
```

[3916.](https://www.acwing.com/problem/content/)



```cpp
```

[3917.](https://www.acwing.com/problem/content/)



```cpp
```

[3918.](https://www.acwing.com/problem/content/)



```cpp
```

[3919.](https://www.acwing.com/problem/content/)



```cpp
```

[3920.](https://www.acwing.com/problem/content/)



```cpp
```

[3921.](https://www.acwing.com/problem/content/)



```cpp
```

[3922.](https://www.acwing.com/problem/content/)



```cpp
```

[3923.](https://www.acwing.com/problem/content/)



```cpp
```

[3924.](https://www.acwing.com/problem/content/)



```cpp
```

[3925.](https://www.acwing.com/problem/content/)



```cpp
```

[3926.](https://www.acwing.com/problem/content/)



```cpp
```

[3927.](https://www.acwing.com/problem/content/)



```cpp
```

[3928.](https://www.acwing.com/problem/content/)



```cpp
```

[3929.](https://www.acwing.com/problem/content/)



```cpp
```

[3930.](https://www.acwing.com/problem/content/)



```cpp
```

[3931.](https://www.acwing.com/problem/content/)



```cpp
```

[3932.](https://www.acwing.com/problem/content/)



```cpp
```

[3933.](https://www.acwing.com/problem/content/)



```cpp
```

[3934.](https://www.acwing.com/problem/content/)



```cpp
```

[3935.](https://www.acwing.com/problem/content/)



```cpp
```

[3936.](https://www.acwing.com/problem/content/)



```cpp
```

[3937.](https://www.acwing.com/problem/content/)



```cpp
```

[3938.](https://www.acwing.com/problem/content/)



```cpp
```

[3939.](https://www.acwing.com/problem/content/)



```cpp
```

[3940.](https://www.acwing.com/problem/content/)



```cpp
```

[3941.](https://www.acwing.com/problem/content/)



```cpp
```

[3942.](https://www.acwing.com/problem/content/)



```cpp
```

[3943.](https://www.acwing.com/problem/content/)



```cpp
```

[3944.](https://www.acwing.com/problem/content/)



```cpp
```

[3945.](https://www.acwing.com/problem/content/)



```cpp
```

[3946.](https://www.acwing.com/problem/content/)



```cpp
```

[3947.](https://www.acwing.com/problem/content/)



```cpp
```

[3948.](https://www.acwing.com/problem/content/)



```cpp
```

[3949.](https://www.acwing.com/problem/content/)



```cpp
```

[3950.](https://www.acwing.com/problem/content/)



```cpp
```

[3951.](https://www.acwing.com/problem/content/)



```cpp
```

[3952.](https://www.acwing.com/problem/content/)



```cpp
```

[3953.](https://www.acwing.com/problem/content/)



```cpp
```

[3954.](https://www.acwing.com/problem/content/)



```cpp
```

[3955.](https://www.acwing.com/problem/content/)



```cpp
```

[3956.](https://www.acwing.com/problem/content/)



```cpp
```

[3957.](https://www.acwing.com/problem/content/)



```cpp
```

[3958.](https://www.acwing.com/problem/content/)



```cpp
```

[3959.](https://www.acwing.com/problem/content/)



```cpp
```

[3960.](https://www.acwing.com/problem/content/)



```cpp
```

[3961.](https://www.acwing.com/problem/content/)



```cpp
```

[3962.](https://www.acwing.com/problem/content/)



```cpp
```

[3963.](https://www.acwing.com/problem/content/)



```cpp
```

[3964.](https://www.acwing.com/problem/content/)



```cpp
```

[3965.](https://www.acwing.com/problem/content/)



```cpp
```

[3966.](https://www.acwing.com/problem/content/)



```cpp
```

[3967.](https://www.acwing.com/problem/content/)



```cpp
```

[3968.](https://www.acwing.com/problem/content/)



```cpp
```

[3969.](https://www.acwing.com/problem/content/)



```cpp
```

[3970.](https://www.acwing.com/problem/content/)



```cpp
```

[3971.](https://www.acwing.com/problem/content/)



```cpp
```

[3972.](https://www.acwing.com/problem/content/)



```cpp
```

[3973.](https://www.acwing.com/problem/content/)



```cpp
```

[3974.](https://www.acwing.com/problem/content/)



```cpp
```

[3975.](https://www.acwing.com/problem/content/)



```cpp
```

[3976.](https://www.acwing.com/problem/content/)



```cpp
```

[3977.](https://www.acwing.com/problem/content/)



```cpp
```

[3978.](https://www.acwing.com/problem/content/)



```cpp
```

[3979.](https://www.acwing.com/problem/content/)



```cpp
```

[3980.](https://www.acwing.com/problem/content/)



```cpp
```

[3981.](https://www.acwing.com/problem/content/)



```cpp
```

[3982.](https://www.acwing.com/problem/content/)



```cpp
```

[3983.](https://www.acwing.com/problem/content/)



```cpp
```

[3984.](https://www.acwing.com/problem/content/)



```cpp
```

[3985.](https://www.acwing.com/problem/content/)



```cpp
```

[3986.](https://www.acwing.com/problem/content/)



```cpp
```

[3987.](https://www.acwing.com/problem/content/)



```cpp
```

[3988.](https://www.acwing.com/problem/content/)



```cpp
```

[3989.](https://www.acwing.com/problem/content/)



```cpp
```

[3990.](https://www.acwing.com/problem/content/)



```cpp
```

[3991.](https://www.acwing.com/problem/content/)



```cpp
```

[3992.](https://www.acwing.com/problem/content/)



```cpp
```

[3993.](https://www.acwing.com/problem/content/)



```cpp
```

[3994.](https://www.acwing.com/problem/content/)



```cpp
```

[3995.](https://www.acwing.com/problem/content/)



```cpp
```

[3996.](https://www.acwing.com/problem/content/)



```cpp
```

[3997.](https://www.acwing.com/problem/content/)



```cpp
```

[3998.](https://www.acwing.com/problem/content/)



```cpp
```

[3999.](https://www.acwing.com/problem/content/)



```cpp
```

