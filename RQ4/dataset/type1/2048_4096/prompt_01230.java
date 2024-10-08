/**
 * 半角转换为全角
 * 
 * @param input
 * @return
 */
public static String toDBC(String input) 
{
    char[] c = input.toCharArray();
    for (int i = 0; i < c.length; i++)
    {
        if (c[i] == 12288)
        {
            c[i] = (char) 32;
            continue;
        }
        if (c[i] > 65280 && c[i] < 65375)
            c[i] = (char) (c[i] - 65248);
    }
    return new String(c);
}   