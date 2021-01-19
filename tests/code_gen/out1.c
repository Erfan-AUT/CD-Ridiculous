int T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10;
int main()
{
    j = 0;
    T0 = i + 0;
    T1 = i + 1;
    T2 = T1 + 0;
    T3 = i + 2;
    T4 = T3 + 0;
    T5 = i + 0;
    T6 = i + 1;
    T7 = T6 + 0;
    T8 = i + 2;
    T9 = T8 + 0;
    if (array[T0] > array[T4])
        goto L0;
    if (array[T2] > array[T4])
        goto L0;
L0:
    if (array[T5] < array[T9])
        goto L1;
    if (array[T7] < array[T9])
        goto L1;
    j = 1;
L1:
}