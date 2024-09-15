/**
 * 比较两个字符串（大小写敏感）。
 *
 * <pre>
 *
 *    StringUtil.equals(null, null)   = true
 *    StringUtil.equals(null, &quot;abc&quot;)  = false
 *    StringUtil.equals(&quot;abc&quot;, null)  = false
 *    StringUtil.equals(&quot;abc&quot;, &quot;abc&quot;) = true
 *    StringUtil.equals(&quot;abc&quot;, &quot;ABC&quot;) = false
 *
 * </pre>
 *
 * @param str1
 *                要比较的字符串1
 * @param str2
 *                要比较的字符串2
 *
 * @return 如果两个字符串相同，或者都是 <code>null</code> ，则返回 <code>true</code>
 */
public static boolean equals(String str1, String str2) 
{
    if (str1 == null)
    {
        return str2 == null;
    }

    return str1.equals(str2);
}   