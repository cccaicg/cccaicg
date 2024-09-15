/** Handles loading text from our resources, including interpreting <b> and <i> tags. */
public static CharSequence getText(Resources res, int id, Object... formatArgs) 
{
    String text = res.getString(id);
    if (formatArgs.length > 0)
    {
        text = String.format(text, formatArgs);
    }
    return Html.fromHtml(text);
}   