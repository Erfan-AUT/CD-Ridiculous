#include <stdio.h>
int array[(int)1e6];
int b1, b2, b3, b4, p1, i, T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10;
int main()
{
    b3 = 0;
    if (6 >= 2)
        goto L1;
    if (33 != 33)
        goto L1;
    b3 = 1;
L1:
    b2 = 0;
    if (3 >= 5)
        goto L0;
    if (5 >= 7)
        goto L0;
    if (7 >= 9)
        goto L0;
    if (9 <= b1)
        goto L0;
    if (b1 <= -1)
        goto L0;
    b2 = 1;
L0:
    i = 0;
    b1 = 0;
    printf("%d", b4);
    b4 = 0;
    b4 = 1;
L7:
    if (0)
        goto L6;
    if (1)
        goto L6;
    b4 = 1;
L6:
    if (b1 == 0)
        goto L9;
    T2 = i + 1;
    i = T2;
L9:
    printf("%d", i);
    i = 0;
    if (b2 == 0)
        goto L10;
    T3 = i + 35;
    i = T3;
L10:
    T4 = i + 33;
    i = T4;
    printf("%d", i);
    i = 0;
L11:
    if (== 0)
        goto L12;
    T6 = i + 1;
    i = T6;
    goto L11;
L12:
    printf("%d", i);
    i = 0;
    if (i != 0)
        goto L13;
    T7 = i + 37;
    i = T7;
L13:
    if (i != 1)
        goto L14;
    T8 = i + 32;
    i = T8;
L14:
    printf("%d", i);
    i = 0;
    p1 = 33;
L15:
    if (p1 > 78)
        goto L16;
    T10 = i + 2;
    i = T10;
    T9 = p1 + 1;
    p1 = T9;
    goto L15;
L16:
    printf("%d", i);
    return 0;
}