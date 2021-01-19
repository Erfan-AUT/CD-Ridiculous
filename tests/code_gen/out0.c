int n1, n2, n3, T0, T1, T2, T3, T4, T5, T6, T7, T8, T9;
int main()
{
    T0 = 20 - 10;
    T1 = T0 / 2;
    n1 = T1;
    T3 = n1 / T2;
    n2 = T3;
    T4 = n1 * n2;
    T5 = T4 - 10;
    n3 = T5;
    printf("%d", n1);
    printf("%d", n2);
    printf("%d", n3);
    T6 = n2 * n2;
    T7 = T6 * n2;
    if (n1 <= 2)
        goto L1;
    if (2 >= n2)
        goto L1;
    if (n2 >= n1)
        goto L1;
    if (n1 > n1)
        goto L1;
    if (n1 > T7)
        goto L1;
    while (n2)
    {
        T8 = n3 + 1;
        n3 = T8;
        T9 = n2 - 1;
        n2 = T9;
    }
L1:
    if (n2 >= 3)
        goto L0;
    n2 = 80;
L0:
    printf("%d", n1);
    printf("%d", n2);
    printf("%d", n3);
}