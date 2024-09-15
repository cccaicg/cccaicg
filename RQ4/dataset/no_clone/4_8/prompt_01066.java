/**
 * Get the text up but not including the specified character or the
 * end of line, whichever comes first.
 * @param  d A delimiter character.
 * @return   A string.
 */
public String nextTo(char d) throws JSONException 
{
    int start = this.pos;
    int end = this.text.indexOf(d, this.pos);
    if (end == -1)
    {
        end = this.text.length();
    }
    this.pos = end + 1;
    return this.text.substring(start, end);
}   