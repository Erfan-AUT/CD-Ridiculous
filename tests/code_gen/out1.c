int T0, i, j, T1, T2, T3;
int main()
{
    T0 = 10 + 0;
    j = 0;
    i = 0;
L0:
    if (i >= 10)
        goto L1;
    T2 = i + 0;
    T3 = T2 + 0;
    array[T3] = i;
    T1 = i + 1;
    i = T1;
    goto L0;
L1:
}