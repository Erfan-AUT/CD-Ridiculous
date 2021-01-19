int T0, i, j, T1;
int main()
{
    T0 = 10 + 0;
    j = 0;
    i = 0;
    T1 = 0;
L0:
    if (T1 < 1)
        goto L1;
    i = array[T1];
    printf("%d", i);
    T1 = T1 + 1;
    goto L0;
L1:
}