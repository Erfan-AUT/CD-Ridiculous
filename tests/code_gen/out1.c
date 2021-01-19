int T0, T1;
int main()
{
    if (x1 != 1)
        goto L0;
    y = 1;
L0:
    if (x1 != 2)
        goto L1;
    y = 2;
L1:
    if (x1 != 3)
        goto L2;
    T0 = y + 1;
    T1 = T0 + 0;
    y = array[T1];
L2:
}