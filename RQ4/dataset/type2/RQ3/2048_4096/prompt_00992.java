/**
 * @param protocol
 * @return
 */
public static AbsTransport getTransport(String protocol) 
{
    if (protocol.equalsIgnoreCase("udp"))
    {
        return new UdpTransport();
    }
    else if (protocol.equalsIgnoreCase("tcp"))
    {
        return new TcpTransport();
    }
    else
    {
        throw new IllegalArgumentException("Invalid protocol: " + protocol);
    }
}   