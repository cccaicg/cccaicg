/**
 * Default Constructor
 */
public HttpRequest() 
{
    this.method = "GET";
    this.url = "/";
    this.headers = new HashMap<>();
    this.body = "";
}   