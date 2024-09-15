/**
 * 显示文章内容，转换markdown为html
 *
 * @param value
 * @return
 */
public static String article(String value) 
{
    if (null == value)
    {
        return "";
    }
    String html = MarkdownUtils.markdownToHtmlExtensions(value);
    return html;
}   