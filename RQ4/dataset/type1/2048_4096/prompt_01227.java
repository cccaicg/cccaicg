/**
 * 去除特殊字符或将所有中文标号替换为英文标号
 * 
 * @param str
 * @return
 */
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public static String stringFilter(String str) 
{
    str = str.replaceAll("【", "[").replaceAll("】", "]")
            .replaceAll("！", "!").replaceAll("：", ":");// ��换中文标号
    String regEx = "[『』]"; // ��除��特��字符
    Pattern p = Pattern.compile(regEx);
    Matcher m = p.matcher(str);
    return m.replaceAll("").trim();
}   