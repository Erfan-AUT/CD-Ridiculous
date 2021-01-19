int T0, T1, T2, T3, T4, T5;
int main()
{
    T0 = i + 0;
    T1 = i + 1;
    T2 = T1 + 0;
    T3 = i + 2;
    T4 = T3 + 0;
    T0 = i + 0;
    T1 = i + 1;
    T2 = T1 + 0;
    T3 = i + 2;
    T4 = T3 + 0;
    if (array[T0] > array[T4])
        goto L0;
    if (array[T2] > array[T4])
        goto L0;
L0:
}