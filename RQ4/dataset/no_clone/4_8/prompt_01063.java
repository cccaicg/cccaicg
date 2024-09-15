/**
 * Returns the next XML meta token. This is used for skipping over <!...>
 * and <?...?> structures.
 * @return Syntax characters (<code>< > / = ! ?</code>) are returned as
 *  Character, and strings and names are returned as Boolean. We don't care
 *  what the values actually are.
 * @throws JSONException If a string is not properly closed or if the XML
 *  is badly structured.
 */
public Object nextMeta() throws JSONException 
{
    char c;
    do
    {
        c = next();
        if (c == 0)
        {
            throw syntaxError("Unexpected EOF");
        }
    }
    while (c != '<' && c != '>' && c != '!' && c != '?' && c != '/');
    switch (c)
    {
        case '<':
            return '<';
        case '>':
            return '>';
        case '!':
            return !nextMeta();
        case '?':
            return nextXML();
        case '/':
            return '/';
    }
    return nextString(c);
}   