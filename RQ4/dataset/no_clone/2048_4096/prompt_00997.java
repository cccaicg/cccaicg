/**
 * @return
 */

public List<String> scanForURLs() 
{
    List<String> urls = new ArrayList<String>();
    String url = null;
    while (scanner.hasNextLine())
    {
        url = scanner.nextLine();
        urls.add(url);
    }
    return urls;
}   