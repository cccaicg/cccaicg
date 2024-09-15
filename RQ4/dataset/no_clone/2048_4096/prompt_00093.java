// special hack to workaround Java module system
private void breakCage(String... args) 
{
    if (args.length == 0)
    {
        System.out.println("No arguments provided");
        return;
    }

    System.out.println("Arguments:");
    for (String arg : args)
    {
        System.out.println(arg);
    }
}   