/**
 * 构建错误信息.(ErrorInfo)
 */
public ErrorInfo getErrorInfo(HttpServletRequest request, Throwable error) 
{
    ErrorInfo info = new ErrorInfo();
    info.setUrl(request.getRequestURL().toString());
    info.setMessage(error.getMessage());
    info.setStackTrace(getStackTrace(error));
    return info;
}   