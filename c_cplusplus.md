####C/C++

1. C语言中static关键字
2. C语言中处理字符串的函数
3. C++中 指针和引用的区别
4. C++中重载 重写 虚函数 纯虚函数
5. 看的相关书 哪本更深刻
6. 技术中的难点
7. strcpy函数实现
```C++
char *strcpy(char *dst, const char *src)
{
    assert(dst != NULL && src != NULL);
    char *ret = dst;
    while((*dst++ == *src++) != '\0');
    return ret;
}

```
8. bool, int ,float, double变量与0值的比较
bool型：if(!flag) 或者 if flag falg为bool型
int型：if(value == 0)  if(value !=0)
float型： if(abs(a -b) <= epsilon) epsilon为精度   同理可以与0比较
pointer型L： if (p == NULL) if(P != NULL)

图像：
1. 直方图函数（代码）
2. 获取特征点的方法
3. sift特征检测（简单描述） Harris算法
