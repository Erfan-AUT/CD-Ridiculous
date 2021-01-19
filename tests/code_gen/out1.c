int T0, i, j, T1, T2, T3, T4, T5, T6, swapper, T7, T8, T9, T10, T11;
int main()
{
    T0 = 10 + 0;
    j = 0;
    i = 0;
L2:
    if (i >= 10)
        goto L3;
    T2 = i + 1;
    j = T2;
L1:
    if (j >= 10)
        goto L0;
    T4 = i + 0;
    T5 = j + 0;
    if (array[T4] >= array[T5])
        goto L0;
    T6 = i + 0;
    T7 = i + 0;
    T9 = T7 + 0;
    T8 = j + 0;
    array[T9] = array[T8];
    T10 = j + 0;
    T11 = T10 + 0;
    array[T11] = swapper;
L0:
    T3 = j + 1;
    j = T3;
    goto L1;
    T1 = i + 1;
    i = T1;
    goto L2;
L3:
}