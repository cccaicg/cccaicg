/**
 * Tokenizes a {@code CharSequence} into a list of Strings.
 *
 * @param input text to be tokenized
 * @return a list of tokens as String objects
 */
public List<String> tokenizeToStrings(CharSequence input) 
{
    List<String> tokens = new ArrayList<String>();
    Tokenizer tokenizer = new Tokenizer(input);
    while (tokenizer.hasNext())
    {
        tokens.add(tokenizer.next());
    }
    return tokens;
}   